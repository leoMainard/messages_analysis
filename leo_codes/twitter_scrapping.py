import requests
from bs4 import BeautifulSoup

def get_tweets(keyword):
  """
  Scrapper les tweets pour un mot-clé donné.

  Args:
    keyword: Le mot-clé à rechercher.

  Returns:
    Une liste de tweets.
  """

  # Obtenir la page de résultats de recherche pour le mot-clé.
  url = "https://twitter.com/search?q={}".format(keyword)
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  # Extraire les tweets de la page.
  tweets = soup.find_all("div", class_="js-tweet-container")

  # Renvoyer la liste des tweets.
  return tweets


def main():
  # Rechercher les tweets pour le mot-clé "python".
  tweets = get_tweets("python")

  # Afficher les tweets.
  for tweet in tweets:
    print(tweet)


if __name__ == "__main__":
  main()