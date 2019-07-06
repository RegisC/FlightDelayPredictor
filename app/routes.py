import flask
from app import instance
import app.forms
import app.model

print('Chargement du module routes.py')

@instance.route('/')
def main():
	# Page d'accueil définie dans main.html
	return(flask.render_template('main.html')) 

@instance.route('/predict', methods=['GET', 'POST'])
def show_form():
	# Formulaire de description du vol
	form = app.forms.FlightDetailsForm()
	if form.validate_on_submit():
		print("Valeurs validées")
		model = app.model.Model(form)
		model.predict()
		return flask.render_template('results.html', 
									 title='Résultat', 
									 model=model)
	else:
		print("Départ :", form.dep_datetime.data)
		print("Erreur de validation")
	return flask.render_template('predict.html', 
								 title='Paramètres du vol',
								 form=form)

@instance.route('/results')
def show_results():
	# Affichage des résultats
	return(flask.render_template('results.html')) 
	