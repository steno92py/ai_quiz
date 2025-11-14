# Quiz AI in Python

Un'applicazione web Flask completa per quiz su Intelligenza Artificiale in Python, con sistema di registrazione/login utenti, classifica globale e widget meteo integrato.

## Funzionalità

- **Sistema di Autenticazione**: Registrazione e login utenti con password hashate
- **Quiz Interattivo**: Domande su AI, Machine Learning, Deep Learning e librerie Python
- **Sistema di Punteggio**: Guadagna punti per ogni risposta corretta
- **Classifica Globale**: Compete con altri giocatori
- **Widget Meteo**: Previsioni a 5 giorni per qualsiasi città (fetch lato browser)
 - **Persistenza Meteo**: L’ultima ricerca meteo resta visibile tornando alla Home
- **Interfaccia Responsive**: Design moderno con Bootstrap 5

## Requisiti

- Python 3.8+
- Flask 3.0+
- SQLite (incluso con Python)
- Servizio Open-Meteo per previsioni (nessuna chiave API richiesta)

## Installazione

1. **Clona o scarica il progetto**

2. **Crea un ambiente virtuale**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```

3. **Installa le dipendenze**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura le variabili d'ambiente**:

   Crea un file `.env` nella directory principale:
   ```
   SECRET_KEY=la-tua-chiave-segreta-molto-sicura
   ```

Nota: per il meteo ora si usa [Open‑Meteo](https://open-meteo.com/), che non richiede chiave API. Le chiamate sono effettuate dal browser, compatibile con PythonAnywhere free.

## Esecuzione in Locale

Per eseguire l'applicazione in modalità sviluppo:

```bash
python run.py
```

Il server troverà **automaticamente una porta disponibile** (a partire dalla 5001) ed eviterà conflitti. L'URL sarà mostrato chiaramente nel terminale:

```
============================================================
Server Flask in esecuzione!
============================================================
URL: http://127.0.0.1:5001
URL rete locale: http://0.0.0.0:5001
============================================================
```

**Nota**: La porta viene selezionata dinamicamente, quindi potrebbe essere 5001, 5002, 5003, ecc. a seconda della disponibilità.

## Inizializzazione del Database

Al primo avvio, l'applicazione creerà automaticamente il database SQLite (`app.db`) con le tabelle necessarie.

### Popolare il Database con Domande di Esempio

Per aggiungere domande al quiz, puoi usare la shell Flask:

```bash
flask shell
```

Poi esegui:

```python
from app.extensions import db
from app.models import Question

# Esempio di domanda
q = Question(
    text="Quale libreria Python è principalmente usata per il calcolo numerico?",
    option_a="requests",
    option_b="NumPy",
    option_c="Flask",
    option_d="BeautifulSoup",
    correct_option="b",
    topic="ai_python",
    difficulty="easy"
)

db.session.add(q)
db.session.commit()
```

Oppure crea uno script Python per aggiungere multiple domande in batch.

## Struttura del Progetto

```
ai_quiz_site/
├── app/
│   ├── __init__.py          # App factory
│   ├── extensions.py        # Estensioni Flask
│   ├── models.py            # Modelli database
│   ├── main/                # Blueprint principale
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── auth/                # Blueprint autenticazione
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── quiz/                # Blueprint quiz
│   │   ├── __init__.py
│   │   └── routes.py
│   └── services/            # Servizi esterni
│       ├── __init__.py
│       └── weather.py
├── templates/               # Template Jinja2
├── static/                  # File statici (CSS, JS)
├── config.py               # Configurazione
├── wsgi.py                 # Entry point per WSGI
├── requirements.txt        # Dipendenze Python
└── README.md              # Questo file
```

## Deployment su PythonAnywhere

1. **Carica i file** su PythonAnywhere tramite Git o upload diretto

2. **Crea un virtual environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```

3. **Configura il WSGI file** nella Web tab:
   - Punta al file `wsgi.py`
   - Assicurati che il path sia corretto

4. **Imposta le variabili d'ambiente**:
   - Nella Web tab, vai alla sezione "Environment variables"
   - Aggiungi `SECRET_KEY`

5. **Inizializza il database**:
   ```bash
   python
   from app import create_app
   from app.extensions import db
   from config import ProdConfig

   app = create_app(ProdConfig)
   with app.app_context():
       db.create_all()
   ```

6. **Riavvia l'app** dalla Web tab

## Configurazione

L'applicazione supporta due configurazioni:

- **DevConfig**: Per sviluppo locale (debug attivo)
- **ProdConfig**: Per produzione (debug disattivo, sicurezza rafforzata)

Modifica `config.py` per personalizzare le impostazioni.

## Sicurezza

- Le password sono hashate usando Werkzeug
- CSRF protection tramite Flask-WTF (opzionale, da implementare)
- Session security con Flask-Login
- In produzione, usa sempre HTTPS

## Personalizzazione

### Aggiungere Nuove Domande

Crea uno script per popolare il database o usa la shell Flask come mostrato sopra.

### Modificare il Punteggio

Modifica `POINTS_PER_CORRECT_ANSWER` in `config.py` (default: 10 punti).

### Cambiare il Design

Modifica i template in `templates/` e gli stili in `static/css/style.css`.

## Troubleshooting

### Meteo non visualizzato
- Verifica il nome della città e riprova (usa la grafia corretta)
- Controlla la connessione del browser (le chiamate sono lato client)
- Consulta lo stato dei servizi Open‑Meteo se il problema persiste

### Note su cache meteo
- Lato server è presente una cache per il client Python (non utilizzata quando il fetch è lato browser).
- Il browser può comunque mantenere l’ultima ricerca localmente (localStorage) per ripristinarla al ritorno in Home.

### Errore database
- Elimina `app.db` e riavvia l'app per ricreare il database
- Verifica i permessi di scrittura nella directory

### Login non funziona
- Verifica che `SECRET_KEY` sia impostata
- Controlla che i dati inseriti siano corretti
- Assicurati che l'utente sia registrato nel database

## Licenza

Progetto educativo sviluppato per KODLAND.

## Sviluppatore

**Stefano Nocco**

---

Per domande o supporto, contatta lo sviluppatore.
