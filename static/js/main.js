// Custom JavaScript for AI Quiz Site
// Add your custom JavaScript code here

document.addEventListener('DOMContentLoaded', function () {
  console.log('AI Quiz Site loaded successfully!');

  const form = document.getElementById('weather-form');
  const input = document.getElementById('city-input');
  const alertBox = document.getElementById('weather-alert');
  const resultsBox = document.getElementById('weather-results');
  const cityEl = document.getElementById('weather-city');
  const tableBody = document.querySelector('#weather-table tbody');

  // Load last search from localStorage
  try {
    const saved = JSON.parse(localStorage.getItem('weather:last'));
    if (saved && saved.city && Array.isArray(saved.forecast)) {
      input.value = saved.city;
      renderForecast(saved.city, saved.forecast);
    }
  } catch (_) {
    // ignore parse errors
  }

  form?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const city = (input?.value || '').trim();
    if (!city) {
      showAlert('Per favore, inserisci il nome di una città.', 'warning');
      return;
    }

    try {
      hideAlert();
      const forecast = await fetchForecast(city);
      if (!forecast || !forecast.length) {
        showAlert(`Nessun dato meteo trovato per "${city}". Verifica il nome della città.`, 'danger');
        return;
      }
      renderForecast(city, forecast);
      persistForecast(city, forecast);
    } catch (err) {
      console.error(err);
      showAlert(`Errore durante il recupero dei dati meteo: ${err.message || err}`, 'danger');
    }
  });

  function showAlert(message, level = 'info') {
    if (!alertBox) return;
    alertBox.className = `alert alert-${level}`;
    alertBox.textContent = message;
    alertBox.classList.remove('d-none');
  }

  function hideAlert() {
    if (!alertBox) return;
    alertBox.classList.add('d-none');
    alertBox.textContent = '';
  }

  function renderForecast(city, forecast) {
    if (!resultsBox || !tableBody || !cityEl) return;
    cityEl.textContent = city;
    tableBody.innerHTML = '';
    for (const day of forecast) {
      const tr = document.createElement('tr');
      const dateTd = document.createElement('td');
      dateTd.textContent = formatDate(day.date);
      const weekTd = document.createElement('td');
      weekTd.innerHTML = `<strong>${day.weekday}</strong>`;
      const dayTd = document.createElement('td');
      dayTd.textContent = (day.temp_day ?? 'N/D') + (day.temp_day != null ? '°C' : '');
      const nightTd = document.createElement('td');
      nightTd.textContent = (day.temp_night ?? 'N/D') + (day.temp_night != null ? '°C' : '');
      tr.append(dateTd, weekTd, dayTd, nightTd);
      tableBody.appendChild(tr);
    }
    resultsBox.classList.remove('d-none');
  }

  function persistForecast(city, forecast) {
    try {
      localStorage.setItem('weather:last', JSON.stringify({ city, forecast }));
    } catch (_) {
      // ignore quota or serialization errors
    }
  }

  async function fetchForecast(city) {
    // 1) Geocoding
    const geoUrl = new URL('https://geocoding-api.open-meteo.com/v1/search');
    geoUrl.searchParams.set('name', city);
    geoUrl.searchParams.set('count', '1');
    geoUrl.searchParams.set('language', 'it');
    geoUrl.searchParams.set('format', 'json');

    const gRes = await fetch(geoUrl.toString(), { cache: 'no-store' });
    if (!gRes.ok) throw new Error(`Geocoding fallito (${gRes.status})`);
    const gData = await gRes.json();
    const place = (gData.results || [])[0];
    if (!place) throw new Error(`Città "${city}" non trovata.`);

    const { latitude: lat, longitude: lon } = place;

    // 2) Forecast hourly temps (local timezone of location)
    const fUrl = new URL('https://api.open-meteo.com/v1/forecast');
    fUrl.searchParams.set('latitude', String(lat));
    fUrl.searchParams.set('longitude', String(lon));
    fUrl.searchParams.set('hourly', 'temperature_2m');
    fUrl.searchParams.set('forecast_days', '5');
    fUrl.searchParams.set('timezone', 'auto');

    const fRes = await fetch(fUrl.toString(), { cache: 'no-store' });
    if (!fRes.ok) throw new Error(`Forecast fallito (${fRes.status})`);
    const fData = await fRes.json();

    const times = (fData.hourly && fData.hourly.time) || [];
    const temps = (fData.hourly && fData.hourly.temperature_2m) || [];
    if (!times.length || times.length !== temps.length) return [];

    // Aggregate by local date string in the response (YYYY-MM-DD)
    const daily = new Map();
    for (let i = 0; i < times.length; i++) {
      const t = times[i];
      const temp = Number(temps[i]);
      const dateStr = t.slice(0, 10); // YYYY-MM-DD
      const hour = Number(t.slice(11, 13));
      if (!daily.has(dateStr)) {
        daily.set(dateStr, { day: [], night: [] });
      }
      if (hour >= 6 && hour < 18) daily.get(dateStr).day.push(temp);
      else daily.get(dateStr).night.push(temp);
    }

    // Build results for up to 5 days in order of appearance
    const weekdaysIt = ['Lunedì','Martedì','Mercoledì','Giovedì','Venerdì','Sabato','Domenica'];
    const results = [];
    for (const [dateStr, vals] of daily.entries()) {
      if (results.length >= 5) break;
      const d = new Date(dateStr + 'T00:00:00'); // interpreted as local browser time; only weekday label needed
      const weekday = weekdaysIt[(d.getDay() + 6) % 7]; // convert Sun(0)->6
      const avg = (arr) => (arr.length ? Math.round((arr.reduce((a,b)=>a+b,0)/arr.length) * 10)/10 : null);
      results.push({
        date: dateStr,
        weekday,
        temp_day: avg(vals.day),
        temp_night: avg(vals.night)
      });
    }

    return results;
  }

  function formatDate(dateStr) {
    // dateStr is YYYY-MM-DD
    try {
      const [y, m, d] = dateStr.split('-').map(Number);
      return `${String(d).padStart(2,'0')}/${String(m).padStart(2,'0')}/${y}`;
    } catch (_) {
      return dateStr;
    }
  }
});
