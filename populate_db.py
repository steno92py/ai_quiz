"""Script to populate the database with sample AI/Python quiz questions.

Run this script after initializing the database to add sample questions.
"""

from app import create_app
from app.extensions import db
from app.models import Question
from config import DevConfig


def populate_questions():
    """Add sample quiz questions about AI in Python."""

    questions = [
        {
            "text": "Quale libreria Python è principalmente usata per il calcolo numerico e array multidimensionali?",
            "option_a": "requests",
            "option_b": "NumPy",
            "option_c": "Flask",
            "option_d": "BeautifulSoup",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "Quale libreria Python è ampiamente utilizzata per il deep learning e le reti neurali?",
            "option_a": "Matplotlib",
            "option_b": "pandas",
            "option_c": "PyTorch",
            "option_d": "Seaborn",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "Cosa significa 'overfitting' nel machine learning?",
            "option_a": "Il modello è troppo semplice",
            "option_b": "Il modello memorizza i dati di training e non generalizza bene",
            "option_c": "Il dataset è troppo piccolo",
            "option_d": "Il modello ha troppo pochi parametri",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale funzione di scikit-learn si usa per dividere i dati in training e test set?",
            "option_a": "split_data()",
            "option_b": "divide_dataset()",
            "option_c": "train_test_split()",
            "option_d": "separate_data()",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "Quale libreria Python è specializzata per la manipolazione e analisi di dati strutturati?",
            "option_a": "NumPy",
            "option_b": "pandas",
            "option_c": "SciPy",
            "option_d": "Keras",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "Cosa rappresenta un 'epoch' nel training di una rete neurale?",
            "option_a": "Una singola predizione",
            "option_b": "Un passaggio completo attraverso l'intero dataset di training",
            "option_c": "Il numero di layer nella rete",
            "option_d": "La velocità di apprendimento",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale metodo è usato per prevenire l'overfitting nelle reti neurali?",
            "option_a": "Aumentare il learning rate",
            "option_b": "Dropout",
            "option_c": "Rimuovere layer nascosti",
            "option_d": "Usare solo una epoca",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale framework di deep learning è sviluppato da Google?",
            "option_a": "PyTorch",
            "option_b": "Caffe",
            "option_c": "TensorFlow",
            "option_d": "Theano",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "Cosa fa la funzione 'fit()' in scikit-learn?",
            "option_a": "Valuta il modello",
            "option_b": "Addestra il modello sui dati",
            "option_c": "Pulisce i dati",
            "option_d": "Visualizza i risultati",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "Quale funzione di attivazione è comunemente usata negli output layer per classificazione binaria?",
            "option_a": "ReLU",
            "option_b": "Sigmoid",
            "option_c": "Tanh",
            "option_d": "Linear",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Cos'è il 'gradient descent'?",
            "option_a": "Un tipo di rete neurale",
            "option_b": "Un algoritmo di ottimizzazione per minimizzare la loss function",
            "option_c": "Una tecnica di data augmentation",
            "option_d": "Un metodo di cross-validation",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale libreria Python viene usata per creare visualizzazioni di dati?",
            "option_a": "NumPy",
            "option_b": "scikit-learn",
            "option_c": "Matplotlib",
            "option_d": "TensorFlow",
            "correct_option": "c",
            "difficulty": "easy"
        },
        {
            "text": "Cosa significa CNN nel deep learning?",
            "option_a": "Central Neural Network",
            "option_b": "Convolutional Neural Network",
            "option_c": "Complex Number Network",
            "option_d": "Continuous Neural Network",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "Quale metrica è appropriata per valutare un modello di classificazione binaria sbilanciato?",
            "option_a": "Accuracy",
            "option_b": "F1-Score",
            "option_c": "Mean Squared Error",
            "option_d": "R-squared",
            "correct_option": "b",
            "difficulty": "hard"
        },
        {
            "text": "Quale tecnica è usata per normalizzare i dati prima del training?",
            "option_a": "One-Hot Encoding",
            "option_b": "Feature Scaling",
            "option_c": "Data Augmentation",
            "option_d": "Dropout",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Cos'è il 'learning rate' nel machine learning?",
            "option_a": "La velocità del processore",
            "option_b": "Il passo con cui i pesi vengono aggiornati durante l'ottimizzazione",
            "option_c": "Il numero di epochs",
            "option_d": "La dimensione del batch",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale algoritmo è comunemente usato per problemi di regressione?",
            "option_a": "K-Means",
            "option_b": "Linear Regression",
            "option_c": "Decision Tree Classification",
            "option_d": "PCA",
            "correct_option": "b",
            "difficulty": "easy"
        },
        {
            "text": "Cosa rappresenta la 'loss function' nel training di un modello?",
            "option_a": "Il numero di errori",
            "option_b": "Una misura di quanto le predizioni differiscono dai valori reali",
            "option_c": "Il tempo di training",
            "option_d": "La complessità del modello",
            "correct_option": "b",
            "difficulty": "medium"
        },
        {
            "text": "Quale tecnica è usata per ridurre la dimensionalità dei dati?",
            "option_a": "K-Means",
            "option_b": "Random Forest",
            "option_c": "PCA (Principal Component Analysis)",
            "option_d": "Gradient Boosting",
            "correct_option": "c",
            "difficulty": "medium"
        },
        {
            "text": "Cosa sono gli 'hyperparameters' in un modello di machine learning?",
            "option_a": "I pesi della rete neurale",
            "option_b": "Parametri impostati prima del training che controllano il processo di apprendimento",
            "option_c": "I dati di input",
            "option_d": "Gli errori del modello",
            "correct_option": "b",
            "difficulty": "hard"
        }
    ]

    # Add all questions to the database
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

    db.session.commit()
    print(f"Aggiunte {len(questions)} domande al database!")


if __name__ == '__main__':
    app = create_app(DevConfig)

    with app.app_context():
        # Check if questions already exist
        existing_count = Question.query.filter_by(topic='ai_python').count()

        if existing_count > 0:
            print(f"Il database contiene già {existing_count} domande.")
            response = input("Vuoi aggiungere altre domande? (s/n): ")
            if response.lower() != 's':
                print("Operazione annullata.")
                exit(0)

        # Populate the database
        populate_questions()
        print("\nDatabase popolato con successo!")
        print(f"Totale domande nel database: {Question.query.filter_by(topic='ai_python').count()}")
