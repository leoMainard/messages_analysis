import pymongo
import time
from datetime import datetime

# ----------------------------- Fonction
def mongoDB_connexion():
    connex = pymongo.MongoClient("mongodb://usertest:passusertest33@10.8.2.5:27017/?authMechanism=DEFAULT&authSource=test_db")
    db = connex.test_db
    return db

def add_values_bdd(bdd_source, bdd_destination, nb_lignes_ajouter=100):

    # ---------------------- Récupération de x lignes aléatoires à ajouter
    pipeline = [
        {"$sample": {"size": nb_lignes_ajouter}}
    ]
    
    resultats = list(bdd_source.aggregate(pipeline))
    
    # ---------------------- Ajout des lignes dans la base de données
    for line in resultats:

        insert = {
            'message' : line['message']
            ,'Nom_du_rappeur' : line['Nom_du_rappeur']
            ,'date_message': line['date_message']
        }

        bdd_destination.insert_one(insert) # insertion de la ligne dans la base de données

    print(f">>> Ajout de {nb_lignes_ajouter} lignes à la base.")
    
def delete_old_values(base, date):
    nb_supprime = 0 
    date1 = datetime.strptime(date, "%d/%m/%Y")

    for line in base.find():
        date_message = datetime.strptime(line['date_message'], "%d/%m/%Y")

        difference = date1 - date_message
        
        if difference.days > 7:
            base.delete_one({"_id": line["_id"]})
            nb_supprime += 1

    print(difference.days)
    print(f">>> Suppression de {nb_supprime} lignes.")

def delete_bdd_values(base):
    base.delete_many({})
    print(">>> Valeurs de la base de données supprimées.")


# ----------------------------- Code
if __name__ == '__main__':
    print("---- Action sur la base TDL_bdd : ")
    # ------------------------------------------------ Connexion à la base de données
    db = mongoDB_connexion()

    # ------------------------------------------------ Ajout de valeurs dans la base de données
    for i in range(30):
        add_values_bdd(db.TDL_source, db.TDL_bdd)
        time.sleep(0.1)

    # ------------------------------------------------ Suppression de valeurs dans la base de données
    # delete_old_values(db.TDL_bdd,"10/12/2023") # datetime.now()
    # delete_bdd_values(db.TDL_bdd)


    