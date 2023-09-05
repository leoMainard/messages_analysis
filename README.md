# messages_analysis

**Problème 2 :** Vous devez analyser les messages postés sur les réseaux sociaux (Tweeter, Facebook , Tik tok ,
Instagram, etc...) dans le but de répondre à des questions formulées en langage naturel . 

## Les scénarios

### 1 - ChatGPT-3

Utilisation de l’API fourni par OpenAI, pour utiliser chatGpt. Nous fournissons le message avec une consigne pour guider gpt, afin qu’il réponde correctement.

### 2 - **Utilisation d'API de médias sociaux**

Nous pouvons utiliser les API officielles de plateformes telles que Twitter, Facebook, Instagram, TikTok, etc., pour extraire des messages et des commentaires.

- Comment cela fonctionne :
    1. On s’inscrit en tant que développeur sur les plateformes sociales et on obtient des clés d'API.
    2. On utilise des bibliothèques Python comme Tweepy pour Twitter, Facebook SDK pour Facebook, et des modules personnalisés pour d'autres plateformes.
    3. On utilise l'API pour extraire les messages pertinents en fonction des mots-clés ou des hashtags.
    4. On analyse les messages et leurs commentaires à l'aide de bibliothèques NLP (traitement du langage naturel) telles que spaCy ou NLTK.
    5. Répondez aux questions en fonction de l'analyse effectuée.
- Avantages : Utilisation de données en temps réel, accès direct aux données des réseaux sociaux.
- Inconvénients : Les limites de l'API, la nécessité de gérer les autorisations d'accès.

### 3 - **Web Scraping**

- Scénario : Vous pouvez scraper les données à partir des pages publiques des réseaux sociaux à l'aide de techniques de web scraping.
- Comment cela fonctionne :
    1. Utilisez des bibliothèques Python comme Beautiful Soup ou Scrapy pour extraire les messages et les commentaires des pages publiques.
    2. Stockez les données extraites dans une base de données ou un fichier.
    3. Analysez les données en utilisant des outils de traitement du langage naturel.
    4. Répondez aux questions en fonction des analyses.
- Avantages : Accès à un large éventail de données, pas besoin d'autorisations d'API.
- Inconvénients : Les politiques de scraping peuvent changer, nécessité de respecter les droits d'auteur et la vie privée.

Pour les deux derniers scénarios, nous pouvons construire notre jeux de données, récupérer de nombreuses questions, avec les réponses. Regrouper les questions qui se ressemble ainsi que la réponse qui revient le plus souvent. Ensuite, lorsqu’on pose une question, on affecte un score à la question qui ressemble le plus à la notre, et on affiche la réponse qui lui correspond.


---
Quelle analyse ?

Analyse de sentiments ?

Rétention d’informations dans une base