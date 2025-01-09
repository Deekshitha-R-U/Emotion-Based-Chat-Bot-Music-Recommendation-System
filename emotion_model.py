from textblob import TextBlob

def get_emotion(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.5:
        return "happy"
    elif polarity > 0:
        return "neutral"
    elif polarity < 0:
        return "sad"
    else:
        return "neutral"
