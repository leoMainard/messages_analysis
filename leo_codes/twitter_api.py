# Import
import configparser
import tweepy

# Lecture du fichier config
config = configparser.ConfigParser()
config.read('config.ini')

# Récupération des clés
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']


# Authentification
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Récupération de l'id de quelqu'un à partir de son pseudonyme
print(" --- Récupération des informations de quelqu'un à partir de son @.")
screen_name = "MiaandeOel"
arobase = api.get_user(screen_name=screen_name)
print("@                   :",screen_name)
print("User id             :", arobase.id)
print("User name           :", arobase.name)
print("Description         :", arobase.description)
print("Compte créé le      :", arobase.created_at.strftime("%d/%m/%Y"))
print("Nombre de followers :", arobase.followers_count, "\n")



# Récupération des tweets de la timeline
tweets = api.user_timeline(screen_name=screen_name)
tweets

# Impossible à réaliser. Demande une augmentation de version, moyennant paiement.