from fill_bdd import mongoDB_connexion, delete_old_values, delete_bdd_values
import re
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')

def clean_text(text):
    # Supprimer les smileys
    text = re.sub(r':\)', '', text)
    text = re.sub(r':\(', '', text)
    # Supprimer la ponctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Convertir en minuscules
    text = text.lower()
    # Supprimer les stopwords
    stop_words = set(stopwords.words('french'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]

    return ' '.join(filtered_text)

def anlayse_sentiment(texte):
    polarite = TextBlob(texte,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment[0]

    if polarite > 0.5:
        sentiment = "Admiré"
    elif polarite > 0.2:
        sentiment = "Célèbre"
    elif polarite < -0.5:
        sentiment = "Discrédité"
    elif polarite < -0.2:
        sentiment = "Controversé"
    else:
        sentiment = "Reconnue"

    return sentiment


def add_values_sentiments(bdd_source, bdd_destination):
    # Récupérer les index de la destination
    destination_ids = {doc['_id'] for doc in bdd_destination.find({}, {'_id': 1})}

    # Trouver les documents dans la source qui ne sont pas dans la destination
    new_documents = bdd_source.find({'_id': {'$nin': list(destination_ids)}})

    x = 0

    for line in new_documents:
        x+=1

        msg = clean_text(line['message'])

        sentiment = anlayse_sentiment(msg)

        insert = {
            '_id': line['_id']
            ,'message' : line['message']
            ,'Nom_du_rappeur' : line['Nom_du_rappeur']
            ,'date_message': line['date_message']
            ,'message_nettoye' : msg
            ,'sentiment' : sentiment
        }

        bdd_destination.insert_one(insert) # insertion de la ligne dans la base de données

    print("Nombre de documents trouvés :",x)


if __name__ == '__main__':
    print("---- Action sur la base TDL_sentiments : ")
    # ------------------------------------------------ Connexion à la base de données
    db = mongoDB_connexion()

    # ------------------------------------------------ Ajout de valeurs dans la base de données
    add_values_sentiments(db.TDL_bdd, db.TDL_sentiments)

    # ------------------------------------------------ Suppression de valeurs dans la base de données
    # delete_old_values(db.TDL_sentiments,"10/12/2023") # datetime.now()
    # delete_bdd_values(db.TDL_sentiments)