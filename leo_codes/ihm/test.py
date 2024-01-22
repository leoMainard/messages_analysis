import random
from textblob import TextBlob
import pymongo
import re
from collections import Counter

def mongoDB_connexion():
    connex = pymongo.MongoClient("mongodb://usertest:passusertest33@10.8.2.5:27017/?authMechanism=DEFAULT&authSource=test_db")
    db = connex.test_db
    return db

def sentiments(recherche):
    db = mongoDB_connexion()

    # Création d'une expression régulière insensible à la casse
    regex = re.compile(re.escape(recherche), re.IGNORECASE)
    resultats = db.TDL_sentiments.find({"Nom_du_rappeur": regex})
    
    total_messages = 0
    message_erreur = False
    sentiments_count = {}
    mots = [] 
    precision = 0    
    histo = []
    cam = []
    nuage = []
    sentiment = 'None'

    for document in resultats:
        total_messages += 1

        message = document.get('message_nettoye')
        mots.extend(re.findall(r'\b\w+\b', message.lower()))  # extraire les mots et les convertir en minuscule

        sentiment = document.get('sentiment')
        if sentiment in sentiments_count:
            sentiments_count[sentiment] += 1
        else:
            sentiments_count[sentiment] = 1
    
    # Vérification si aucun résultat
    if total_messages == 0:
        message_erreur =  True
        return sentiment, precision, total_messages, histo, cam, nuage, message_erreur
            
    # Sentiment le plus présent
    sentiment = max(sentiments_count, key=sentiments_count.get)

    # Précision
    precision = round(sentiments_count[sentiment] / total_messages * 100)


    # Compter la fréquence de chaque mot
    frequence_mots = Counter(mots)

    # Sélectionner les 30 mots les plus fréquents
    mots_frequents = frequence_mots.most_common(30)

    
    # Analyser le sentiment de chaque mot
    for mot, freq in mots_frequents:
        sentiment_temp = TextBlob(mot).sentiment.polarity

        if sentiment_temp > 0.5:
            sentiment_label = "Très positif"
        elif sentiment_temp > 0.2:
            sentiment_label = "Positif"
        elif sentiment_temp < -0.5:
            sentiment_label = "Très négatif"
        elif sentiment_temp < -0.2:
            sentiment_label = "Négatif"
        else:
            sentiment_label = "Neutre"

        nuage.append({"x": mot, "value": freq, "category": sentiment_label})


    histo = [
        list(sentiments_count.keys()),
        list(sentiments_count.values()),
        ['rgb(255, 99, 132)', 'rgb(75, 192, 192)', 'rgb(255, 205, 86)', 'rgb(201, 203, 207)', 'rgb(54, 162, 235)']
    ]

    cam = [
        list(sentiments_count.keys()),
        list(sentiments_count.values()),
        ['rgb(255, 99, 132)', 'rgb(75, 192, 192)', 'rgb(255, 205, 86)', 'rgb(201, 203, 207)', 'rgb(54, 162, 235)']
    ]

    return sentiment, precision, total_messages, histo, cam, nuage, message_erreur



def histogramme():
    histo = [
        ['Heureux', 'Mitige', 'Triste', 'Enthousiaste', 'Stresse'],
        [random.randint(0, 20) for _ in range(5)],
        ['rgb(255, 99, 132)','rgb(75, 192, 192)','rgb(255, 205, 86)','rgb(201, 203, 207)','rgb(54, 162, 235)']
    ]

    return histo

def camembert():
    cam = [
        ['Heureux', 'Mitige', 'Triste', 'Enthousiaste', 'Stresse'],
        [random.randint(0, 100) for _ in range(5)],
        ['rgb(255, 99, 132)','rgb(75, 192, 192)','rgb(255, 205, 86)','rgb(201, 203, 207)','rgb(54, 162, 235)']
    ]

    return cam

def nuage_mots():
    data = []
    sentiment = ['Heureux', 'Mitige', 'Triste', 'Enthousiaste', 'Stresse']
    mots_neymar = [
    'football','but','joueur','attaquant','Brésil','Paris Saint-Germain','PSG',
    'Ligue 1','Barcelone','Neymar Jr','Ney','Brésilien','samba','coup franc',
    'talent','dribble','magicien','équipe nationale','championnat',
    'idole','fans','fête','Barça','Santos','Milan',
    'Santos FC','Neymarzete','Superstar','records'
    ]

    for i in range (200):
        mot_aleatoire = random.choice(mots_neymar)
        value = random.randint(0, 1000)
        sentiment_aleatoire = random.choice(sentiment)

        data.append( {"x": mot_aleatoire, "value": value, "category": sentiment_aleatoire})

    return data
