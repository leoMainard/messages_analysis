# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    # decide sentiment as positive, negative, and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")
    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")
    else:
        print("Neutral")

    print("Sentiment_dict :",sentiment_dict)

# Driver code
if __name__ == "__main__":
    print("\n1st statement :")
    sentence = "Octoparse is the best web-scraping tool for \ students."
    # function calling
    sentiment_scores(sentence)
    print("\n2nd Statement :")
    sentence = "I am busy and my schedule is hectic"
    sentiment_scores(sentence)
    print("\n3rd Statement :")
    sentence = "I am feeling sad and lonely today."
    sentiment_scores(sentence)

    print("\nTest sur phrase française : ")
    texte = "PLK, versatile mais certaines collabs ne sont pas à la hauteur. Choisir avec plus de discernement."
    sentiment_scores(texte)

    print("\nTest sur phrase française : ")
    texte = "PLK c'est trop nul, je n'aime pas du tout."
    sentiment_scores(texte)




# texte = "PLK, versatile mais certaines collabs ne sont pas à la hauteur. Choisir avec plus de discernement."
# texte2 = "plk versatile certaines collabs hauteur choisir plus discernement"

# sentiment = test_analyse_sentiment(texte)

# print(sentiment)