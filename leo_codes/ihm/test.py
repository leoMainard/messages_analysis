import random
import json

def histogramme():
    histo = [
        ['Heureux', 'Mitige', 'Triste', 'Enthousiaste', 'Stresse'],
        [random.randint(0, 20) for _ in range(5)],
        ['rgb(255, 99, 132)','rgb(75, 192, 192)','rgb(255, 205, 86)','rgb(201, 203, 207)','rgb(54, 162, 235)']
    ]

    return histo
    # # Spécifiez le nom du fichier TXT dans lequel vous souhaitez enregistrer la liste
    # nom_fichier = './leo_codes/ihm/files/histo.txt'

    # # Enregistrez la liste dans le fichier TXT
    # with open(nom_fichier, 'w') as fichier:
    #     json.dump(histo, fichier)

    # print(f"La liste a été enregistrée dans le fichier {nom_fichier}.")


def camembert():
    cam = [
        ['Heureux', 'Mitige', 'Triste', 'Enthousiaste', 'Stresse'],
        [random.randint(0, 100) for _ in range(5)],
        ['rgb(255, 99, 132)','rgb(75, 192, 192)','rgb(255, 205, 86)','rgb(201, 203, 207)','rgb(54, 162, 235)']
    ]

    return cam
    # # Spécifiez le nom du fichier TXT dans lequel vous souhaitez enregistrer la liste
    # nom_fichier = './leo_codes/ihm/files/camembert.txt'

    # # Enregistrez la liste dans le fichier TXT
    # with open(nom_fichier, 'w') as fichier:
    #     json.dump(cam, fichier)

    # print(f"La liste a été enregistrée dans le fichier {nom_fichier}.")


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
    # # Spécifiez le nom du fichier TXT dans lequel vous souhaitez enregistrer la liste
    # nom_fichier = './leo_codes/ihm/files/nuage.txt'

    # # Enregistrez la liste dans le fichier TXT
    # with open(nom_fichier, 'w') as fichier:
    #     json.dump(data, fichier)

    # print(f"La liste a été enregistrée dans le fichier {nom_fichier}.")

# if __name__ == "__main__":
#     histogramme()
#     camembert()
#     nuage_mots()
