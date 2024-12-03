import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.pipeline import Pipeline
import nltk
from nltk.corpus import stopwords
import string
import re

# Download NLTK stopwords
nltk.download('stopwords')

# Load Dataset
# Assuming 'spam.csv' dataset is available
# Columns: 'v1' (label), 'v2' (email text)
data = pd.read_csv('spam.csv', encoding='latin-1')
data = data[['v1', 'v2']].rename(columns={'v1': 'label', 'v2': 'text'})

# Map labels to binary values (ham = 0, spam = 1)
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Text Preprocessing Function
def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Apply preprocessing
data['text'] = data['text'].apply(preprocess_text)

# Features and Labels
X = data['text']
y = data['label']

# Split into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build a Pipeline
pipeline = Pipeline([
    ('vectorizer', CountVectorizer(stop_words='english')),  # Bag-of-Words
    ('tfidf', TfidfTransformer()),                         # TF-IDF Transformation
    ('classifier', MultinomialNB())                        # Multinomial Naive Bayes
])

# Train the Model
pipeline.fit(X_train, y_train)

# Make Predictions
y_pred = pipeline.predict(X_test)

# Evaluation
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nAccuracy:", accuracy_score(y_test, y_pred))
