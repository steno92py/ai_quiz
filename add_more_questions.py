"""Script to add 50 additional AI/Python quiz questions to the database.

Run this script to populate the database with more advanced questions.
"""

from app import create_app
from app.extensions import db
from app.models import Question
from config import DevConfig


def add_new_questions():
    """Add 50 new quiz questions about AI in Python."""

    questions = [
        {
            "text": "Quale libreria Python è più comunemente usata per il machine learning 'classico' (alberi, regressioni, SVM, ecc.)?",
            "option_a": "NumPy",
            "option_b": "Flask",
            "option_c": "scikit-learn",
            "option_d": "Selenium",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "Quale libreria Python è più usata per creare e addestrare reti neurali profonde?",
            "option_a": "Matplotlib",
            "option_b": "PyTorch",
            "option_c": "Requests",
            "option_d": "BeautifulSoup",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In un tipico flusso di lavoro di machine learning in Python, qual è il primo passo?",
            "option_a": "Addestrare il modello",
            "option_b": "Deployare il modello in produzione",
            "option_c": "Caricare e pulire i dati",
            "option_d": "Calcolare la matrice di confusione",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "Quale oggetto di scikit-learn viene usato per dividere i dati in train e test?",
            "option_a": "train_test_split",
            "option_b": "split_data",
            "option_c": "random_split",
            "option_d": "data_partition",
            "correct_option": "a",
            "difficulty": "easy"
        },
        {
            "text": "In scikit-learn, quale metodo viene usato per addestrare un modello?",
            "option_a": "run()",
            "option_b": "fit()",
            "option_c": "train()",
            "option_d": "learn()",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In scikit-learn, quale metodo viene usato per effettuare predizioni con un modello già addestrato?",
            "option_a": "predict()",
            "option_b": "forecast()",
            "option_c": "run()",
            "option_d": "classify()",
            "correct_option": "a",
            "difficulty": "easy"
        },
        {
            "text": "Quale libreria Python è più indicata per la manipolazione di tabelle di dati (dataset tipo CSV)?",
            "option_a": "NumPy",
            "option_b": "Pandas",
            "option_c": "Matplotlib",
            "option_d": "Pillow",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "Quale formato di dati è più comunemente usato per salvare dataset tabellari che poi vengono letti con pandas?",
            "option_a": ".exe",
            "option_b": ".csv",
            "option_c": ".png",
            "option_d": ".mp3",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In pandas, quale metodo si usa per leggere un file CSV?",
            "option_a": "pd.load_csv()",
            "option_b": "pd.read_csv()",
            "option_c": "pd.csv()",
            "option_d": "pd.import_csv()",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In NumPy, come si chiama l'oggetto principale che rappresenta array multidimensionali?",
            "option_a": "ndarray",
            "option_b": "DataFrame",
            "option_c": "Series",
            "option_d": "Matrix",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "In scikit-learn, che tipo di oggetto è tipicamente un modello (es. LogisticRegression)?",
            "option_a": "Una funzione globale",
            "option_b": "Una classe con metodi fit e predict",
            "option_c": "Un modulo Python",
            "option_d": "Un file di configurazione",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale funzione di scikit-learn è usata per valutare modelli con validazione incrociata?",
            "option_a": "cross_val_score",
            "option_b": "validate_model",
            "option_c": "kfold_score",
            "option_d": "cv_evaluate",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "In un problema di classificazione binaria, quale metrica è più adatta quando le classi sono sbilanciate?",
            "option_a": "Accuracy",
            "option_b": "Precision",
            "option_c": "Recall",
            "option_d": "AUC-ROC",
            "correct_option": "d",
            "difficulty": "hard"
        },
        {
            "text": "Quale classe di scikit-learn è adatta a un problema di regressione lineare semplice?",
            "option_a": "LogisticRegression",
            "option_b": "LinearRegression",
            "option_c": "KMeans",
            "option_d": "DecisionTreeClassifier",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "Quale classe di scikit-learn è usata per il clustering non supervisionato?",
            "option_a": "RandomForestClassifier",
            "option_b": "KMeans",
            "option_c": "SVC",
            "option_d": "GaussianNB",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In un dataset di machine learning, come si chiamano le colonne che rappresentano le variabili predittive?",
            "option_a": "Target",
            "option_b": "Features",
            "option_c": "Labels",
            "option_d": "Outcomes",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In Python, quale modulo viene spesso usato per gestire la serializzazione (salvataggio) di oggetti, ad esempio modelli addestrati?",
            "option_a": "pickle",
            "option_b": "json",
            "option_c": "csv",
            "option_d": "os",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "In scikit-learn, quale oggetto permette di concatenare più trasformazioni e un modello finale?",
            "option_a": "Pipeline",
            "option_b": "Flow",
            "option_c": "Chain",
            "option_d": "Sequence",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "Quale tecnica riduce il rischio di overfitting decidendo in anticipo l'architettura o la complessità del modello?",
            "option_a": "Data augmentation",
            "option_b": "Regularizzazione",
            "option_c": "Feature scaling",
            "option_d": "Cross-validation",
            "correct_option": "b",
            "difficulty": "hard"
        },
        {
            "text": "In un modello di regressione lineare, cosa rappresenta il termine di bias (intercetta)?",
            "option_a": "La pendenza della retta",
            "option_b": "Il rumore sui dati",
            "option_c": "Il valore di output quando tutte le feature sono zero",
            "option_d": "Il numero di campioni",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "Quale framework Python è più spesso associato a modelli di deep learning eseguiti su GPU?",
            "option_a": "Flask",
            "option_b": "Django",
            "option_c": "PyTorch",
            "option_d": "OpenCV",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "In PyTorch, quale classe rappresenta i dati multidimensionali con gradiente?",
            "option_a": "Tensor",
            "option_b": "Array",
            "option_c": "DataFrame",
            "option_d": "Matrix",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "In PyTorch, quale modulo contiene gli strati (layers) standard come Linear, Conv2d, ecc.?",
            "option_a": "torch.layers",
            "option_b": "torch.nn",
            "option_c": "torch.core",
            "option_d": "torch.model",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In PyTorch, quale oggetto si usa tipicamente per iterare sui dati in mini-batch?",
            "option_a": "DataLoader",
            "option_b": "BatchIterator",
            "option_c": "MiniBatch",
            "option_d": "DatasetLoader",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "In un tipico ciclo di addestramento PyTorch, quale ordine è corretto?",
            "option_a": "loss.backward(), optimizer.zero_grad(), optimizer.step()",
            "option_b": "optimizer.step(), loss.backward(), optimizer.zero_grad()",
            "option_c": "optimizer.zero_grad(), loss.backward(), optimizer.step()",
            "option_d": "loss.backward(), optimizer.step(), optimizer.zero_grad()",
            "correct_option": "c",
            "difficulty": "hard"
        },
        {
            "text": "Per il NLP in Python, quale libreria è specializzata in modelli transformer pre-addestrati (BERT, GPT, ecc.)?",
            "option_a": "scikit-learn",
            "option_b": "spaCy",
            "option_c": "NLTK",
            "option_d": "Transformers (Hugging Face)",
            "correct_option": "d",
            "difficulty": "medium"
        },
        {
            "text": "In scikit-learn, quale classe è usata per convertire testo in una rappresentazione numerica 'bag-of-words'?",
            "option_a": "LabelEncoder",
            "option_b": "CountVectorizer",
            "option_c": "StandardScaler",
            "option_d": "PCA",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In un modello di classificazione, cosa rappresenta la 'confusion matrix'?",
            "option_a": "Una lista dei parametri del modello",
            "option_b": "Una tabella che mostra veri positivi, falsi positivi, veri negativi, falsi negativi",
            "option_c": "Una tabella con l'accuratezza per ogni classe",
            "option_d": "Una matrice di correlazione fra le feature",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale tecnica di pre-processing è spesso necessaria per modelli di ML sensibili alla scala delle feature (es. KNN, SVM)?",
            "option_a": "One-hot encoding",
            "option_b": "Feature scaling (standardizzazione/normalizzazione)",
            "option_c": "Imputazione dei valori mancanti",
            "option_d": "PCA",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In scikit-learn, quale classe usi per standardizzare le feature (media 0, varianza 1)?",
            "option_a": "MinMaxScaler",
            "option_b": "StandardScaler",
            "option_c": "Normalizer",
            "option_d": "RobustScaler",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Qual è la funzione di attivazione più tradizionale usata nei percettroni multistrato prima dell'avvento di ReLU?",
            "option_a": "Softmax",
            "option_b": "Sigmoid",
            "option_c": "Linear",
            "option_d": "Identity",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Qual è un effetto tipico dell'overfitting?",
            "option_a": "Alte performance su train, basse su test",
            "option_b": "Basse performance su train, alte su test",
            "option_c": "Alte performance su entrambe le parti",
            "option_d": "Basse performance su entrambe le parti",
            "correct_option": "a",
            "difficulty": "easy"
        },
        {
            "text": "In un problema di classificazione multiclasse, quale funzione di perdita è comunemente usata nelle reti neurali?",
            "option_a": "Mean Squared Error",
            "option_b": "Binary Cross-Entropy",
            "option_c": "Categorical Cross-Entropy",
            "option_d": "Hinge Loss",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "Quale tecnica riduce il rischio di overfitting disattivando casualmente neuroni durante l'addestramento?",
            "option_a": "Batch Normalization",
            "option_b": "Dropout",
            "option_c": "Early Stopping",
            "option_d": "Data Augmentation",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In un dataset per image classification, quale libreria Python è spesso usata per trasformare e caricare immagini (insieme a PyTorch)?",
            "option_a": "Pillow (PIL)",
            "option_b": "Requests",
            "option_c": "Selenium",
            "option_d": "argparse",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "In scikit-learn, quale parametro controlla la profondità massima di un DecisionTreeClassifier?",
            "option_a": "max_depth",
            "option_b": "depth",
            "option_c": "tree_depth",
            "option_d": "max_level",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "Quale è un vantaggio principale dei Random Forest rispetto a un singolo albero decisionale?",
            "option_a": "Sono più veloci da addestrare",
            "option_b": "Non richiedono dati di training",
            "option_c": "Generalizzano meglio grazie alla media su molti alberi",
            "option_d": "Non possono fare overfitting",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "Quale tecnica di ricerca iperparametri esplora combinazioni predefinite di parametri?",
            "option_a": "Random Search",
            "option_b": "Grid Search",
            "option_c": "Bayesian Optimization",
            "option_d": "Genetic Algorithm",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale oggetto scikit-learn usi per fare Grid Search con cross-validation?",
            "option_a": "GridSearchCV",
            "option_b": "GridValidator",
            "option_c": "ParamSearch",
            "option_d": "HyperGrid",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "In un modello di regressione, quale metrica misura l'errore quadratico medio?",
            "option_a": "MAE",
            "option_b": "RMSE",
            "option_c": "MSE",
            "option_d": "R²",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "In Python, quale libreria è spesso usata per salvare modelli di scikit-learn in formato binario più efficiente di pickle?",
            "option_a": "joblib",
            "option_b": "json",
            "option_c": "csv",
            "option_d": "sqlite3",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "Quale è un modo comune di esporre un modello di AI in produzione utilizzando Python?",
            "option_a": "Integrarlo in un file .txt",
            "option_b": "Esportarlo come immagine .png",
            "option_c": "Esporlo tramite una API REST (es. Flask/FastAPI)",
            "option_d": "Convertirlo in script Bash",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "In scikit-learn, quale metodo puoi usare per ottenere la probabilità delle classi (se il modello lo supporta)?",
            "option_a": "predict_proba()",
            "option_b": "predict_prob()",
            "option_c": "class_prob()",
            "option_d": "proba()",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "Quale tipo di problema risolve un modello di regressione logistica?",
            "option_a": "Regressione di valori continui",
            "option_b": "Clustering non supervisionato",
            "option_c": "Classificazione (tipicamente binaria)",
            "option_d": "Riduzione della dimensionalità",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "In un modello di rete neurale per classificazione, cosa rappresenta in genere il livello di output con attivazione Softmax?",
            "option_a": "La probabilità di ciascuna classe",
            "option_b": "La somma dei pesi",
            "option_c": "Il tasso di apprendimento",
            "option_d": "La funzione di perdita",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "Quale parametro in un algoritmo di gradient descent controlla la dimensione dei passi dell'aggiornamento dei pesi?",
            "option_a": "Numero di epoche",
            "option_b": "Learning rate",
            "option_c": "Batch size",
            "option_d": "Momentum",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In Python, quale costrutto viene spesso usato per assicurare il rilascio di risorse (file, sessioni, ecc.)?",
            "option_a": "try-finally",
            "option_b": "if-else",
            "option_c": "for",
            "option_d": "while",
            "correct_option": "a",
            "difficulty": "easy"
        },
        {
            "text": "Nel pre-processing di testi, cosa fa il tokenization?",
            "option_a": "Converte numeri in stringhe",
            "option_b": "Divide il testo in unità più piccole (parole, subword, caratteri)",
            "option_c": "Rimuove i valori nulli dal dataset",
            "option_d": "Ordina le frasi alfabeticamente",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In un dataset, perché è importante gestire i valori mancanti prima di addestrare un modello?",
            "option_a": "Per ridurre la dimensione del file",
            "option_b": "Per rendere i grafici più belli",
            "option_c": "Per evitare errori o bias nel modello",
            "option_d": "Per aumentare automaticamente l'accuratezza",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "Qual è uno scopo tipico della riduzione di dimensionalità (es. con PCA) in un contesto di AI in Python?",
            "option_a": "Aumentare il numero di feature",
            "option_b": "Ridurre il rumore e velocizzare l'addestramento",
            "option_c": "Convertire variabili categoriche in numeriche",
            "option_d": "Mescolare casualmente i dati",
            "correct_option": "b",
            "difficulty": "medium"
        }
    ]

    # Add all questions to the database
    added_count = 0
    for q_data in questions:
        question = Question(
            text=q_data["text"],
            option_a=q_data["option_a"],
            option_b=q_data["option_b"],
            option_c=q_data["option_c"],
            option_d=q_data["option_d"],
            correct_option=q_data["correct_option"],
            topic="ai_python",
            difficulty=q_data["difficulty"]
        )
        db.session.add(question)
        added_count += 1

    db.session.commit()
    print(f"Aggiunte {added_count} nuove domande al database!")


if __name__ == '__main__':
    app = create_app(DevConfig)

    with app.app_context():
        # Show current count
        existing_count = Question.query.filter_by(topic='ai_python').count()
        print(f"Domande attuali nel database: {existing_count}")

        response = input("Vuoi aggiungere 50 nuove domande? (s/n): ")
        if response.lower() != 's':
            print("Operazione annullata.")
            exit(0)

        # Add the questions
        add_new_questions()

        # Show new total
        new_total = Question.query.filter_by(topic='ai_python').count()
        print(f"\nDatabase popolato con successo!")
        print(f"Totale domande nel database: {new_total}")
