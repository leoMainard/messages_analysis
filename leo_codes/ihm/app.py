from flask import Flask, render_template, flash, request, jsonify
from test import histogramme, camembert, nuage_mots, sentiments
import json
import random

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = '123456789'
app.config['JSON_AS_ASCII'] = False  # Utilisez UTF-8 pour les réponses JSON

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        recherche = request.form.get('search')
        sentiment, precision, nb_messages, data_histo, data_cam, data_nuage, message_erreur = sentiments(recherche)

        if message_erreur:
            flash('Aucun résultat trouvé pour cette recherche.', category='error')
            
        return render_template('index.html', liste_histo = data_histo, liste_cam = data_cam, liste_nuage = data_nuage,
                               nombre_mots = nb_messages, precision_sentiment = precision, sentiment_trouve = sentiment, recherche_valeur = recherche)

    return render_template('index.html', liste_histo = [], liste_cam = [], liste_nuage = [],
                               nombre_mots = 0, precision_sentiment = 0, sentiment_trouve = 'None')

@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    data_histo = histogramme()
    return jsonify(data_histo)

if __name__ == '__main__':
    app.run(debug=True)
