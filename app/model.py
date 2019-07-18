import app.forms
import numpy as np
import pandas as pd
import pickle
import sklearn.linear_model

class Model:	
	def __init__(self, form):
		print("Nouveau modèle instancié")
		self.dep_date = form.dep_date.data
		self.dep_time = form.dep_time.data
		self.airline = form.airline.data	
		d = form.flight_duration.data
		self.flight_duration = 	d.minute + d.hour * 60
		self.flight_departed = form.flight_departed.data
		self.dep_delay = form.dep_delay.data
		print(f"Départ le {self.dep_date} à {self.dep_time} sur {self.airline},"
			  f"temps de vol {self.flight_duration} minutes," 
			  f"décollé : {self.flight_departed},"
			  f"délai au décollage {self.dep_delay} minutes.")
		self.load()
	
	def load(self):
		MODEL_FILE = 'regression_model.sav'
		self.model = pickle.load(open(MODEL_FILE, 'rb'))
		print("Coefficients du modèle de régression :")
		print(self.model.coef_)
		
	def predict(self):
		delay = self.model.predict(self.get_input_vector())[0]
		print(f"Retard prédit : {delay:0.4f} minute(s).")
		self.delay = int(delay)

	def get_input_vector(self):
		df = self.get_empty_df()
		df.loc[0, 'CRS_ELAPSED_TIME'] = self.flight_duration
		df.loc[0, 'CARRIER_DELAY'] = 3.45137
		df.loc[0, 'ORIGIN_DELAY'] = 6.41685
		# Compagnie 
		col = 'car_' + self.airline
		if col in df.columns:
			df.loc[0, col] = 1 
		# Jour de la semaine
		col = 'd_' + str(self.dep_date.weekday() + 1)
		if col in df.columns:
			df.loc[0, col] = 1 
		# Mois
		col = 'm_' + str(self.dep_date.month)
		if col in df.columns:
			df.loc[0, col] = 1 		
		# Heure de départ
		col = 'dep_' + str(self.dep_time.hour)
		if col in df.columns:
			df.loc[0, col] = 1 				
		# print(df.iloc[0,:])
		X = df.values
		# print("Taille de X :", X.shape)
		return X
		
	def get_empty_df(self):
		d = {
			'CRS_ELAPSED_TIME': { 0: 0 },
			'CARRIER_DELAY': { 0: 0 },
			'ORIGIN_DELAY': { 0: 0 },
			'car_AS': { 0: 0 },
			'car_B6': { 0: 0 },
			'car_DL': { 0: 0 },
			'car_EV': { 0: 0 },
			'car_F9': { 0: 0 },
			'car_HA': { 0: 0 },
			'car_NK': { 0: 0 },
			'car_OO': { 0: 0 },
			'car_UA': { 0: 0 },
			'car_VX': { 0: 0 },
			'car_WN': { 0: 0 },
			'd_2': { 0: 0 },
			'd_3': { 0: 0 },
			'd_4': { 0: 0 },
			'd_5': { 0: 0 },
			'd_6': { 0: 0 },
			'd_7': { 0: 0 },
			'm_2': { 0: 0 },
			'm_3': { 0: 0 },
			'm_4': { 0: 0 },
			'm_5': { 0: 0 },
			'm_6': { 0: 0 },
			'm_7': { 0: 0 },
			'm_8': { 0: 0 },
			'm_9': { 0: 0 },
			'm_10': { 0: 0 },
			'm_11': { 0: 0 },
			'm_12': { 0: 0 },
			'dep_1': { 0: 0 },
			'dep_2': { 0: 0 },
			'dep_3': { 0: 0 },
			'dep_4': { 0: 0 },
			'dep_5': { 0: 0 },
			'dep_6': { 0: 0 },
			'dep_7': { 0: 0 },
			'dep_8': { 0: 0 },
			'dep_9': { 0: 0 },
			'dep_10': { 0: 0 },
			'dep_11': { 0: 0 },
			'dep_12': { 0: 0 },
			'dep_13': { 0: 0 },
			'dep_14': { 0: 0 },
			'dep_15': { 0: 0 },
			'dep_16': { 0: 0 },
			'dep_17': { 0: 0 },
			'dep_18': { 0: 0 },
			'dep_19': { 0: 0 },
			'dep_20': { 0: 0 },
			'dep_21': { 0: 0 },
			'dep_22': { 0: 0 },
			'dep_23': { 0: 0 }
		}
		return pd.DataFrame(d)

