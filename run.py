"""Development server entry point.

Run this script to start the Flask development server locally.
"""

import socket
import webbrowser
import threading
import time
import logging
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from the project .env BEFORE importing app/config
# Use an explicit path so it works regardless of current working directory
_DOTENV_PATH = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=_DOTENV_PATH)

from app import create_app
from config import DevConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def find_free_port(start_port: int = 5001, max_attempts: int = 10) -> int:
    """Find a free port starting from start_port.

    Args:
        start_port: Port number to start searching from.
        max_attempts: Maximum number of ports to try.

    Returns:
        Available port number.

    Raises:
        RuntimeError: If no free port is found.
    """
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue

    raise RuntimeError(f'Nessuna porta disponibile trovata tra {start_port} e {start_port + max_attempts - 1}')


def open_browser(url: str, delay: float = 1.5) -> None:
    """Open browser after a delay to allow server to start.

    Args:
        url: URL to open in the browser.
        delay: Delay in seconds before opening browser.
    """
    time.sleep(delay)
    webbrowser.open(url)


app = create_app(DevConfig)

if __name__ == '__main__':
    import os

    try:
        # Find port only in the first process, store it, and reuse in reloader
        if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
            # First run: find port and store it
            port = find_free_port()
            os.environ['APP_PORT'] = str(port)

            print(f'\n{"="*60}')
            print(f'Server Flask in esecuzione!')
            print(f'{"="*60}')
            print(f'URL: http://127.0.0.1:{port}')
            print(f'URL rete locale: http://0.0.0.0:{port}')
            print(f'{"="*60}\n')
        else:
            # Reloader: reuse the stored port
            port = int(os.environ.get('APP_PORT', '5001'))
            url = f'http://127.0.0.1:{port}'

            print(f'\n{"="*60}')
            print(f'Server Flask in esecuzione!')
            print(f'{"="*60}')
            print(f'URL: {url}')
            print(f'URL rete locale: http://0.0.0.0:{port}')
            print(f'{"="*60}')
            print(f'Apertura del browser in corso...\n')

            # Open browser only once in the reloader process
            threading.Thread(target=open_browser, args=(url,), daemon=True).start()

        app.run(debug=True, host='0.0.0.0', port=port, use_reloader=True)
    except RuntimeError as e:
        print(f'Errore: {e}')
        print('Prova a chiudere altri programmi che usano le porte o riavvia il computer.')
