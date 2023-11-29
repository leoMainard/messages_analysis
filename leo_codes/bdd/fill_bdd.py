import pymongo
import pandas as pd
import time

# ----------------------------- Fonction
def mongoDB_connexion():
    # connex = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    connex = pymongo.MongoClient("mongodb://usertest:passusertest33@10.8.2.5:27017/?authMechanism=DEFAULT&authSource=test_db")
    db = connex.test_db
    return db

def delete_bdd_values(db):
    db.TDL_bdd.delete_many({})
    print("Valeurs de la base de données 'TDL_bdd' supprimées.")

def add_values_bdd(bdd_source, bdd_destination, time_sleep):
    print("Pour le moment, cette fonction s'arrête après l'ajout de 300 lignes.")
    print("Supprimer 'compte' pour tout ajouter.\n")

    i = 1
    if bdd_destination.count_documents({ 'index': 1 }, limit = 1) != 0:
        i = int(bdd_destination.find_one(sort=[('index', pymongo.DESCENDING)])['index'])
        i = i+1
    nb_ajout = 1

    compte = 0 # Supprimer

    for line in bdd_source.find():

        if compte == 3:break # Supprimer

        insert = {
            'message' : line['message']
            ,'Nom_du_rappeur' : line['Nom_du_rappeur']
            ,'date_message': line['date_message']
            ,'index' : i
        }

        bdd_destination.insert_one(insert) # insertion de la ligne dans la base de données

        i += 1

        nb_ajout += 1
        if (nb_ajout % 100) == 0:
            # Patienter 30 secondes puis poursuivre
            print("Ajout de 100 nouveaux messages dans la base de données.")

            compte += 1 # Supprimer

            time.sleep(time_sleep)

import json
import random
# ----------------------------- Code
if __name__ == '__main__':
    db = mongoDB_connexion()
    # delete_bdd_values(db)

    add_values_bdd(db.TDL_source, db.TDL_bdd,1)

    