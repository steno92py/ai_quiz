"""Script to add questions 51-100 to the database.

Run this script to populate the database with more AI/Python questions.
"""

from app import create_app
from app.extensions import db
from app.models import Question
from config import DevConfig


def add_questions_51_100():
    """Add questions 51-100 about AI in Python."""

    questions = [
        {
            "text": "In scikit-learn, quale classe useresti per un modello K-Nearest Neighbors di classificazione?",
            "option_a": "KNeighborsClassifier",
            "option_b": "KNNModel",
            "option_c": "NearestNeighborsClassifier",
            "option_d": "KNNClassifier",
            "correct_option": "a",
            "difficulty": "easy"
        },
        {
            "text": "In scikit-learn, quale classe useresti per un modello K-Nearest Neighbors di regressione?",
            "option_a": "KNeighborsRegressor",
            "option_b": "KNNRegressor",
            "option_c": "NearestRegressor",
            "option_d": "KNeighborsModel",
            "correct_option": "a",
            "difficulty": "easy"
        },
        {
            "text": "Quale funzione di NumPy viene usata per creare un array di zeri?",
            "option_a": "np.zeros()",
            "option_b": "np.zero()",
            "option_c": "np.empty()",
            "option_d": "np.null()",
            "correct_option": "a",
            "difficulty": "easy"
        },
        {
            "text": "Quale funzione di NumPy viene spesso usata per generare numeri casuali tra 0 e 1 per inizializzare pesi?",
            "option_a": "np.rand()",
            "option_b": "np.random.rand()",
            "option_c": "np.random.random_int()",
            "option_d": "np.random.uniform_int()",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In un dataset pandas, come si chiama il tipo di oggetto che rappresenta una colonna?",
            "option_a": "Row",
            "option_b": "Series",
            "option_c": "Column",
            "option_d": "Vector",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In scikit-learn, quale classe useresti per una SVM di classificazione?",
            "option_a": "SVR",
            "option_b": "SVC",
            "option_c": "SVMClassifier",
            "option_d": "SupportVector",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In scikit-learn, quale classe useresti per una SVM di regressione?",
            "option_a": "SVR",
            "option_b": "SVC",
            "option_c": "SVRegression",
            "option_d": "LinearSVRClassifier",
            "correct_option": "a",
            "difficulty": "easy"
        },
        {
            "text": "Quale funzione scikit-learn usi per generare una matrice di confusione?",
            "option_a": "confusion()",
            "option_b": "confusion_matrix()",
            "option_c": "classification_matrix()",
            "option_d": "error_matrix()",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In un problema di classificazione, quale metodo di scikit-learn puoi usare per ottenere un report completo con precision, recall e f1-score?",
            "option_a": "classification_report()",
            "option_b": "metrics_report()",
            "option_c": "score_report()",
            "option_d": "model_report()",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "Quale tipo di problema è tipicamente risolto da KMeans?",
            "option_a": "Classificazione supervisionata",
            "option_b": "Regressione",
            "option_c": "Clustering non supervisionato",
            "option_d": "Riduzione di dimensionalità",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "In Python, quale keyword viene usata per definire una funzione che calcola una loss personalizzata?",
            "option_a": "func",
            "option_b": "def",
            "option_c": "lambda solo",
            "option_d": "loss",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In scikit-learn, cosa rappresenta il parametro n_estimators in RandomForestClassifier?",
            "option_a": "Numero massimo di feature",
            "option_b": "Numero di alberi nella foresta",
            "option_c": "Numero massimo di foglie",
            "option_d": "Numero di iterazioni di training",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In scikit-learn, quale parametro di LogisticRegression controlla la forza della regolarizzazione L2?",
            "option_a": "alpha",
            "option_b": "lambda_",
            "option_c": "C",
            "option_d": "reg",
            "correct_option": "c",
            "difficulty": "hard"
        },
        {
            "text": "Quale è un tipico problema quando le feature hanno scale molto diverse?",
            "option_a": "Overfitting automatico",
            "option_b": "Il modello ignora le feature con valori piccoli",
            "option_c": "Algoritmi basati su distanza possono dare risultati distorti",
            "option_d": "Il modello non converge mai",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "Quale funzione di NumPy calcola la media di un array?",
            "option_a": "np.avg()",
            "option_b": "np.mean()",
            "option_c": "np.middle()",
            "option_d": "np.average_value()",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In pandas, quale metodo usi per rimuovere righe con valori NaN?",
            "option_a": "drop_nan()",
            "option_b": "remove_nan()",
            "option_c": "dropna()",
            "option_d": "cleanna()",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "Nel contesto di AI in Python, a cosa serve OneHotEncoder di scikit-learn?",
            "option_a": "A normalizzare numericamente le feature",
            "option_b": "A codificare variabili categoriche in vettori binari",
            "option_c": "A ridurre la dimensionalità",
            "option_d": "A scalare i target",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale tecnica riduce la dimensionalità preservando il più possibile la varianza dei dati?",
            "option_a": "PCA",
            "option_b": "KMeans",
            "option_c": "StandardScaler",
            "option_d": "LabelEncoder",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "In scikit-learn, quale classe è usata per problemi di Naive Bayes gaussiano?",
            "option_a": "MultinomialNB",
            "option_b": "BernoulliNB",
            "option_c": "GaussianNB",
            "option_d": "NaiveBayesGaussian",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "Quale libreria Python viene usata principalmente per la visualizzazione di grafici 2D (es. per analisi dati AI)?",
            "option_a": "Matplotlib",
            "option_b": "Requests",
            "option_c": "Pillow",
            "option_d": "Flask",
            "correct_option": "a",
            "difficulty": "easy"
        },
        {
            "text": "In Matplotlib, quale funzione viene usata tipicamente per tracciare un grafico a linee semplice?",
            "option_a": "plot_line()",
            "option_b": "line()",
            "option_c": "plot()",
            "option_d": "draw()",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "In un loop di training di un modello di AI in Python, cosa rappresenta tipicamente una 'epoch'?",
            "option_a": "L'addestramento su un singolo batch",
            "option_b": "L'addestramento su tutto il dataset una volta",
            "option_c": "Il numero di feature usate",
            "option_d": "Il numero di neuroni nel modello",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In PyTorch, quale oggetto contiene i parametri di un modello e aggiorna i pesi usando la loss?",
            "option_a": "torch.loss",
            "option_b": "torch.updater",
            "option_c": "optimizer",
            "option_d": "grad_manager",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "Qual è lo scopo del metodo model.eval() in PyTorch?",
            "option_a": "Abilitare dropout",
            "option_b": "Mettere il modello in modalità inferenza (no dropout, no batchnorm training)",
            "option_c": "Resettare i pesi",
            "option_d": "Salvare il modello su file",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Qual è lo scopo del metodo model.train() in PyTorch?",
            "option_a": "Mettere il modello in modalità inferenza",
            "option_b": "Mettere il modello in modalità addestramento (abilita dropout, ecc.)",
            "option_c": "Salvare il modello",
            "option_d": "Azzerare i gradienti",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In PyTorch, quale funzione è comunemente usata per salvare un modello su disco?",
            "option_a": "torch.save()",
            "option_b": "torch.export()",
            "option_c": "torch.store()",
            "option_d": "torch.model_save()",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "Nel NLP con Python, cosa fa lo 'stemming'?",
            "option_a": "Traduce il testo in un'altra lingua",
            "option_b": "Riduce le parole alle loro radici (spesso in modo grossolano)",
            "option_c": "Conta la frequenza delle parole",
            "option_d": "Ordina alfabeticamente le frasi",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Nel contesto di dataset testuali, cosa sono le 'stopwords'?",
            "option_a": "Parole con significato molto tecnico",
            "option_b": "Parole che indicano fine frase",
            "option_c": "Parole molto frequenti e poco informative (es. 'il', 'e', 'di')",
            "option_d": "Parole proibite nel testo",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "In scikit-learn, quale classe useresti per fare una regressione logistica multiclasse?",
            "option_a": "LogisticRegression con multi_class='multinomial'",
            "option_b": "MultiLogistic",
            "option_c": "SoftmaxRegression",
            "option_d": "MultiClassLogisticRegressor",
            "correct_option": "a",
            "difficulty": "hard"
        },
        {
            "text": "Qual è lo scopo di random_state in molte funzioni di scikit-learn?",
            "option_a": "Aumentare la velocità di esecuzione",
            "option_b": "Gestire la memoria",
            "option_c": "Rendere i risultati riproducibili fissando il seed del generatore casuale",
            "option_d": "Ridurre il numero di feature",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "In un dataset di immagini, cosa fa la 'data augmentation'?",
            "option_a": "Riduce il numero di immagini",
            "option_b": "Aggiunge etichette extra",
            "option_c": "Genera nuove immagini modificate (rotazioni, zoom, ecc.) per migliorare la generalizzazione",
            "option_d": "Elimina il rumore dalle immagini",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "In un modello di rete neurale, cosa indica l'iperparametro 'batch size'?",
            "option_a": "Numero di neuroni nel primo strato",
            "option_b": "Numero di feature totali",
            "option_c": "Numero di campioni usati per ogni aggiornamento dei pesi",
            "option_d": "Numero di epoche totali",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "Qual è un sintomo tipico di 'underfitting'?",
            "option_a": "Il modello va bene su train ma male su test",
            "option_b": "Il modello va male sia su train che su test",
            "option_c": "Il modello va male su train ma bene su test",
            "option_d": "Il modello ha una accuracy del 100%",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In Python, quale libreria viene spesso usata per caricare file .json contenenti configurazioni di modelli o pipeline?",
            "option_a": "pickle",
            "option_b": "yaml",
            "option_c": "json",
            "option_d": "configparser",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "In scikit-learn, quale oggetto si usa per codificare target categorici come numeri interi?",
            "option_a": "LabelBinarizer",
            "option_b": "LabelEncoder",
            "option_c": "OneHotEncoder",
            "option_d": "OrdinalEncoder",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Per un problema di ranking in un motore di ricerca, quale tipo di modello di AI in Python potresti usare?",
            "option_a": "Modello di regressione o apprendimento a ranking",
            "option_b": "Solo KMeans",
            "option_c": "Solo DBSCAN",
            "option_d": "Solo PCA",
            "correct_option": "a",
            "difficulty": "hard"
        },
        {
            "text": "Per integrare un modello di AI in un'applicazione web Python, quale framework è spesso usato per creare API REST leggere?",
            "option_a": "Django Admin",
            "option_b": "Flask o FastAPI",
            "option_c": "Selenium",
            "option_d": "Tkinter",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "Quale criterio di split viene usato comunemente nei Decision Tree per classificazione?",
            "option_a": "MSE",
            "option_b": "Entropia o Gini",
            "option_c": "MAE",
            "option_d": "R²",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In scikit-learn, quale classe useresti per creare una foresta casuale di regressione?",
            "option_a": "RandomForestClassifier",
            "option_b": "RandomForestRegressor",
            "option_c": "RandomRegressorForest",
            "option_d": "ForestRegressor",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In un ambiente di produzione, perché è importante serializzare anche i trasformatori (scalers, encoder) oltre al modello?",
            "option_a": "Per ridurre la dimensione del file finale",
            "option_b": "Per poter applicare ai dati di input le stesse trasformazioni usate in training",
            "option_c": "Per evitare di installare scikit-learn",
            "option_d": "Per aumentare la velocità di training",
            "correct_option": "b",
            "difficulty": "hard"
        },
        {
            "text": "Quale libreria Python è spesso usata per monitorare esperimenti di ML (log di metriche, iperparametri, ecc.)?",
            "option_a": "mlflow",
            "option_b": "pytest",
            "option_c": "pylint",
            "option_d": "pip",
            "correct_option": "a",
            "difficulty": "medium"
        },
        {
            "text": "In un sistema di raccomandazione implementato in Python, quale tipo di modello potresti utilizzare?",
            "option_a": "Solo KMeans",
            "option_b": "Modelli di collaborative filtering o matrix factorization",
            "option_c": "Solo regressione lineare",
            "option_d": "Solo modelli di clustering gerarchico",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In PyTorch, cosa fa loss.backward()?",
            "option_a": "Aggiorna direttamente i pesi",
            "option_b": "Calcola i gradienti dei pesi rispetto alla loss",
            "option_c": "Resetta i gradienti",
            "option_d": "Salva la loss su file",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In un contesto di AI in Python, cosa si intende per 'feature engineering'?",
            "option_a": "Aggiunta di più GPU al server",
            "option_b": "Progettazione e trasformazione delle variabili di input per migliorare le performance del modello",
            "option_c": "Aumento del numero di epoche",
            "option_d": "Cambiare il tipo di modello da regressione a classificazione",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale è un vantaggio dell'uso di Pipeline in scikit-learn?",
            "option_a": "Riduce automaticamente l'overfitting",
            "option_b": "Permette di concatenare trasformazioni e modello, evitando errori di ordine e facilitando il deployment",
            "option_c": "Rimuove automaticamente i valori mancanti",
            "option_d": "Sceglie automaticamente il modello migliore",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In Python, quale costrutto useresti per misurare il tempo di esecuzione di un blocco di codice in modo semplice?",
            "option_a": "time.time() prima e dopo",
            "option_b": "len()",
            "option_c": "range()",
            "option_d": "sleep()",
            "correct_option": "a",
            "difficulty": "easy"
        },
        {
            "text": "Nel clustering con KMeans, cosa rappresenta il parametro n_clusters?",
            "option_a": "Numero massimo di iterazioni",
            "option_b": "Numero di centroidi/gruppi da trovare",
            "option_c": "Numero di feature",
            "option_d": "Numero di campioni nel dataset",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "In un modello di rete neurale, cosa fa la funzione di attivazione ReLU?",
            "option_a": "Restituisce sempre 0",
            "option_b": "Restituisce il valore di input senza modifiche",
            "option_c": "Restituisce max(0, x)",
            "option_d": "Restituisce min(0, x)",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "Quale tecnica di regolarizzazione aggiunge un termine proporzionale al quadrato dei pesi nella funzione di perdita?",
            "option_a": "L1",
            "option_b": "L2",
            "option_c": "Dropout",
            "option_d": "Early stopping",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "In scikit-learn, quale classe useresti per eseguire una regressione lineare con regolarizzazione L1?",
            "option_a": "Ridge",
            "option_b": "Lasso",
            "option_c": "ElasticNet",
            "option_d": "LinearRegression",
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

        response = input("Vuoi aggiungere altre 50 domande (51-100)? (s/n): ")
        if response.lower() != 's':
            print("Operazione annullata.")
            exit(0)

        # Add the questions
        add_questions_51_100()

        # Show new total
        new_total = Question.query.filter_by(topic='ai_python').count()
        print(f"\nDatabase popolato con successo!")
        print(f"Totale domande nel database: {new_total}")
