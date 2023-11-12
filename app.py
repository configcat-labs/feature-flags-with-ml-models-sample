import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle

def train_classifier(model_type):
    # Load the training data
    df = pd.read_json('./models/{0}/classification_data.json'.format(model_type))
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['intent'], random_state=0)

    # Train the model
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(X_train)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    model = LinearSVC(dual="auto").fit(X_train_tfidf, y_train)

    # Save the vectorizer 
    vec_file = './models/{0}/vectorizer.pickle'.format(model_type)
    pickle.dump(count_vect, open(vec_file, 'wb'))

    # Save the model
    mod_file = './models/{0}/classifier.model'.format(model_type)
    pickle.dump(model, open(mod_file, 'wb'))

    # Print training complete to the terminal
    print("Training completed for {0} model".format(model_type))
    

def classify_text(text, model_type):
    # Load the vectorizer
    vec_file = './models/{0}/vectorizer.pickle'.format(model_type)
    count_vect = pickle.load(open(vec_file, 'rb'))

    # Load the model
    mod_file = './models/{0}/classifier.model'.format(model_type)
    model = pickle.load(open(mod_file, 'rb'))

    # Classify the text
    text_counts = count_vect.transform([text])
    predicted = model.predict(text_counts)
    scores = model.decision_function(text_counts)

    result = {
        'model': model_type,
        'intent': predicted[0],
        'confidence': max(scores[0]),
        'text': text
    }

    return result
