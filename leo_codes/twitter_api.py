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