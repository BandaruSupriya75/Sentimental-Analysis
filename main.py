import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK resources (run only once)
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis on a given text
def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Example usage
text = "I love this product! It's amazing."
sentiment = analyze_sentiment(text)
print(sentiment)  # Output: Positive
