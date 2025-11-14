"""Weather service for fetching 5-day forecast data.

This module uses Open-Meteo APIs via the `openmeteo-requests` client with
`requests-cache` and `retry-requests` for resilient, cached calls. It performs
geocoding to resolve a city name into coordinates and then retrieves hourly
temperature data, aggregating it into day/night averages for the next 5 days.

All timestamps are aligned to the local timezone of the resolved location and
days prior to “today” (local) are filtered out, so the first entry is always
today when data is available.
"""

import logging
import requests
from datetime import datetime
from typing import Optional, List, Dict
from pathlib import Path

import openmeteo_requests
import requests_cache
from retry_requests import retry

logger = logging.getLogger(__name__)

# Prepare a cached + retrying session for all HTTP calls
_CACHE_DIR = (Path(__file__).resolve().parents[2] / ".openmeteo_cache")
try:
    _CACHE_DIR.mkdir(parents=True, exist_ok=True)
    _cache_session = requests_cache.CachedSession(
        str(_CACHE_DIR / "weather_cache"), expire_after=3600
    )
except Exception:
    # Fallback to non-cached session if filesystem is not writable
    _cache_session = requests.Session()

_retry_session = retry(_cache_session, retries=3, backoff_factor=0.3)
_openmeteo = openmeteo_requests.Client(session=_retry_session)


# Italian weekday names
ITALIAN_WEEKDAYS = [
    'Lunedì',    # Monday
    'Martedì',   # Tuesday
    'Mercoledì', # Wednesday
    'Giovedì',   # Thursday
    'Venerdì',   # Friday
    'Sabato',    # Saturday
    'Domenica'   # Sunday
]


def get_five_day_forecast(city_name: str) -> Optional[List[Dict]]:
    """Fetch 5-day weather forecast (day/night averages) for a city.

    Uses Open-Meteo Geocoding API to resolve the city, then fetches hourly
    temperatures from Open-Meteo Forecast API and aggregates into day/night
    averages for the next 5 days.

    Args:
        city_name: Name of the city to get forecast for.

    Returns:
        List of 5 dictionaries containing daily forecast data, or None if error.
        Each dictionary contains:
            - date: date object
            - weekday: Italian weekday name
            - temp_day: Daytime temperature in Celsius (average 06:00-17:59)
            - temp_night: Nighttime temperature in Celsius (average 18:00-05:59)

    Raises:
        ValueError: If city is invalid or not found.
        requests.RequestException: If an API request fails.
    """
    if not city_name or not city_name.strip():
        logger.error(f'Nome città non valido: {city_name}')
        raise ValueError('Nome città non valido.')

    city = city_name.strip()
    geocode_url = 'https://geocoding-api.open-meteo.com/v1/search'
    forecast_url = 'https://api.open-meteo.com/v1/forecast'

    try:
        # 1) Geocoding: city -> (lat, lon)
        geo_params = {
            'name': city,
            'count': 1,
            'language': 'it',
            'format': 'json'
        }
        logger.info(f'Geocoding Open-Meteo: {geocode_url}?name={city}&count=1&language=it&format=json')
        g_res = _retry_session.get(geocode_url, params=geo_params, timeout=10)
        logger.info(f'Geocoding status: {g_res.status_code}')
        g_res.raise_for_status()
        g_data = g_res.json()

        results = g_data.get('results') or []
        if not results:
            raise ValueError(f'Città "{city_name}" non trovata.')

        first = results[0]
        lat = first.get('latitude')
        lon = first.get('longitude')
        resolved_name = first.get('name')
        country = first.get('country')
        logger.info(f'Risolta città: {resolved_name}, {country} -> lat={lat}, lon={lon}')

        # 2) Forecast: hourly temperature
        params = {
            'latitude': lat,
            'longitude': lon,
            'hourly': 'temperature_2m',
            'forecast_days': 5,
            'timezone': 'auto'
        }
        logger.info(
            f'Chiamata Open-Meteo Forecast (client): lat={lat}, lon={lon}, hourly=temperature_2m, days=5'
        )

        # Use the Open-Meteo client (supports batching; we use single request)
        responses = _openmeteo.weather_api(forecast_url, params=params)
        if not responses:
            logger.error('Risposta Open-Meteo vuota')
            return None
        response = responses[0]

        hourly = response.Hourly()
        # Build timestamps from start, end, interval
        start_ts = int(hourly.Time())  # epoch seconds (UTC base)
        end_ts = int(hourly.TimeEnd())
        interval = int(hourly.Interval()) or 3600

        # Get local timezone offset in seconds if available
        try:
            offset_fn = getattr(response, 'UtcOffsetSeconds', None)
            utc_offset_seconds = int(offset_fn()) if callable(offset_fn) else 0
        except Exception:
            utc_offset_seconds = 0

        temps = hourly.Variables(0).ValuesAsNumpy()
        if temps is None:
            logger.error('Dati orari non disponibili')
            return None

        count = int((end_ts - start_ts) / interval)
        count = min(count, len(temps))

        # Group by date with day/night temps
        daily_forecasts: Dict[datetime.date, Dict] = {}
        for i in range(count):
            ts = start_ts + i * interval
            # Convert to local time using offset provided by the API
            dt = datetime.utcfromtimestamp(ts + utc_offset_seconds)
            d = dt.date()
            hour = dt.hour

            if d not in daily_forecasts:
                daily_forecasts[d] = {
                    'date': d,
                    'temp_day': None,
                    'temp_night': None,
                    'day_temps': [],
                    'night_temps': []
                }

            t = float(temps[i])
            if 6 <= hour < 18:
                daily_forecasts[d]['day_temps'].append(t)
            else:
                daily_forecasts[d]['night_temps'].append(t)

        # Filter out past days relative to local date, then prepare first 5 days
        today_local = datetime.utcfromtimestamp(int(datetime.utcnow().timestamp()) + utc_offset_seconds).date()
        valid_days = [d for d in sorted(daily_forecasts.keys()) if d >= today_local]

        # Prepare results for first 5 days
        results: List[Dict] = []
        for d in valid_days[:5]:
            day_data = daily_forecasts[d]
            day_temps = day_data['day_temps']
            night_temps = day_data['night_temps']

            temp_day = round(sum(day_temps) / len(day_temps), 1) if day_temps else None
            temp_night = round(sum(night_temps) / len(night_temps), 1) if night_temps else None

            weekday_name = ITALIAN_WEEKDAYS[d.weekday()]
            results.append({
                'date': d,
                'weekday': weekday_name,
                'temp_day': temp_day,
                'temp_night': temp_night
            })

        return results

    except requests.exceptions.HTTPError as e:
        status = getattr(e.response, 'status_code', 'unknown')
        text = getattr(e.response, 'text', '')
        logger.error(f'Errore HTTP {status}: {text}')
        if status == 404:
            raise ValueError(f'Città "{city_name}" non trovata.')
        raise requests.RequestException(f'Errore HTTP: {status}')

    except requests.exceptions.RequestException as e:
        logger.error(f'Errore di connessione API: {str(e)}')
        raise requests.RequestException(f"Errore di connessione all'API meteo: {str(e)}")

    except Exception as e:
        logger.error(f'Errore imprevisto: {str(e)}')
        raise Exception(f'Errore imprevisto durante il recupero dei dati meteo: {str(e)}')
