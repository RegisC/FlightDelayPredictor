Initialisation de Heroku 
------------------------

Exporter la liste des paquetages requis :
pip freeze > requirements.txt

Supprimer les entrées suivantes :
mkl-fft
mkl-random
mkl-service

heroku login
heroku git:remote -a rc-flight-delays
git add .
git commit -m "Message"
git push heroku master


Pour afficher les messages émis sur le serveur
----------------------------------------------

heroku logs -t


Adresse du serveur web
----------------------

https://rc-flight-delays.herokuapp.com/predict


Exécution locale
----------------

conda activate flightdelay_env

RunFlask.bat
ou
ipython FlightDelayPredictor.py
ou 
waitress-serve --port=5000  app:instance


Conversion de l'arbre en format png
-----------------------------------

dot -Tpng tree.dot -o tree.png


Variables explicatives
----------------------

Régression linéaire simple
['MONTH', 'DAY_OF_WEEK', 'CRS_ELAPSED_TIME', 'CRS_DEP_HOUR', 'CRS_ARR_HOUR', 'car_AS', 'car_B6', 'car_DL', 'car_EV', 'car_F9', 'car_HA', 'car_NK', 'car_OO', 'car_UA', 'car_VX', 'car_WN']

Régression linéaire avec variables catégorielles
['CRS_ELAPSED_TIME', 'car_AS', 'car_B6', 'car_DL', 'car_EV', 'car_F9', 'car_HA', 'car_NK', 'car_OO', 'car_UA', 'car_VX', 'car_WN', 'd_2', 'd_3', 'd_4', 'd_5', 'd_6', 'd_7', 'm_2', 'm_3', 'm_4', 'm_5', 'm_6', 'm_7', 'm_8', 'm_9', 'm_10', 'm_11', 'm_12', 'dep_1', 'dep_2', 'dep_3', 'dep_4', 'dep_5', 'dep_6', 'dep_7', 'dep_8', 'dep_9', 'dep_10', 'dep_11', 'dep_12', 'dep_13', 'dep_14', 'dep_15', 'dep_16', 'dep_17', 'dep_18', 'dep_19', 'dep_20', 'dep_21', 'dep_22', 'dep_23']

Régression linéaire avec infos T-1
['CRS_ELAPSED_TIME', 'CARRIER_DELAY', 'ORIGIN_DELAY', 'car_AS', 'car_B6', 'car_DL', 'car_EV', 'car_F9', 'car_HA', 'car_NK', 'car_OO', 'car_UA', 'car_VX', 'car_WN', 'd_2', 'd_3', 'd_4', 'd_5', 'd_6', 'd_7', 'm_2', 'm_3', 'm_4', 'm_5', 'm_6', 'm_7', 'm_8', 'm_9', 'm_10', 'm_11', 'm_12', 'dep_1', 'dep_2', 'dep_3', 'dep_4', 'dep_5', 'dep_6', 'dep_7', 'dep_8', 'dep_9', 'dep_10', 'dep_11', 'dep_12', 'dep_13', 'dep_14', 'dep_15', 'dep_16', 'dep_17', 'dep_18', 'dep_19', 'dep_20', 'dep_21', 'dep_22', 'dep_23']

Idem + heure d'arrivée
['CRS_ELAPSED_TIME', 'CARRIER_DELAY', 'ORIGIN_DELAY', 'car_AS', 'car_B6', 'car_DL', 'car_EV', 'car_F9', 'car_HA', 'car_NK', 'car_OO', 'car_UA', 'car_VX', 'car_WN', 'd_2', 'd_3', 'd_4', 'd_5', 'd_6', 'd_7', 'm_2', 'm_3', 'm_4', 'm_5', 'm_6', 'm_7', 'm_8', 'm_9', 'm_10', 'm_11', 'm_12', 'dep_1', 'dep_2', 'dep_3', 'dep_4', 'dep_5', 'dep_6', 'dep_7', 'dep_8', 'dep_9', 'dep_10', 'dep_11', 'dep_12', 'dep_13', 'dep_14', 'dep_15', 'dep_16', 'dep_17', 'dep_18', 'dep_19', 'dep_20', 'dep_21', 'dep_22', 'dep_23', 'arr_1', 'arr_2', 'arr_3', 'arr_4', 'arr_5', 'arr_6', 'arr_7', 'arr_8', 'arr_9', 'arr_10', 'arr_11', 'arr_12', 'arr_13', 'arr_14', 'arr_15', 'arr_16', 'arr_17', 'arr_18', 'arr_19', 'arr_20', 'arr_21', 'arr_22', 'arr_23']

Idem + exclusion des valeurs extrêmes

Arbre de régression
['CRS_ELAPSED_TIME', 'CARRIER_DELAY', 'ORIGIN_DELAY', 'car_AS', 'car_B6', 'car_DL', 'car_EV', 'car_F9', 'car_HA', 'car_NK', 'car_OO', 'car_UA', 'car_VX', 'car_WN', 'd_2', 'd_3', 'd_4', 'd_5', 'd_6', 'd_7', 'm_2', 'm_3', 'm_4', 'm_5', 'm_6', 'm_7', 'm_8', 'm_9', 'm_10', 'm_11', 'm_12', 'dep_1', 'dep_2', 'dep_3', 'dep_4', 'dep_5', 'dep_6', 'dep_7', 'dep_8', 'dep_9', 'dep_10', 'dep_11', 'dep_12', 'dep_13', 'dep_14', 'dep_15', 'dep_16', 'dep_17', 'dep_18', 'dep_19', 'dep_20', 'dep_21', 'dep_22', 'dep_23']

GBR (variables catégorielles, infos T-1, sans heure d'arrivée)
['CRS_ELAPSED_TIME', 'CARRIER_DELAY', 'ORIGIN_DELAY', 'car_AS', 'car_B6', 'car_DL', 'car_EV', 'car_F9', 'car_HA', 'car_NK', 'car_OO', 'car_UA', 'car_VX', 'car_WN', 'd_2', 'd_3', 'd_4', 'd_5', 'd_6', 'd_7', 'm_2', 'm_3', 'm_4', 'm_5', 'm_6', 'm_7', 'm_8', 'm_9', 'm_10', 'm_11', 'm_12', 'dep_1', 'dep_2', 'dep_3', 'dep_4', 'dep_5', 'dep_6', 'dep_7', 'dep_8', 'dep_9', 'dep_10', 'dep_11', 'dep_12', 'dep_13', 'dep_14', 'dep_15', 'dep_16', 'dep_17', 'dep_18', 'dep_19', 'dep_20', 'dep_21', 'dep_22', 'dep_23']

GBR avec retard connu
['DEP_DELAY', 'CRS_ELAPSED_TIME', 'CARRIER_DELAY', 'ORIGIN_DELAY', 'car_AS', 'car_B6', 'car_DL', 'car_EV', 'car_F9', 'car_HA', 'car_NK', 'car_OO', 'car_UA', 'car_VX', 'car_WN', 'd_2', 'd_3', 'd_4', 'd_5', 'd_6', 'd_7', 'm_2', 'm_3', 'm_4', 'm_5', 'm_6', 'm_7', 'm_8', 'm_9', 'm_10', 'm_11', 'm_12', 'dep_1', 'dep_2', 'dep_3', 'dep_4', 'dep_5', 'dep_6', 'dep_7', 'dep_8', 'dep_9', 'dep_10', 'dep_11', 'dep_12', 'dep_13', 'dep_14', 'dep_15', 'dep_16', 'dep_17', 'dep_18', 'dep_19', 'dep_20', 'dep_21', 'dep_22', 'dep_23']

Régression polynômiale (variables catégorielles, infos T-1, vacances, sans heure d'arrivée)
['CRS_ELAPSED_TIME', 'NEXT_HOL', 'PREV_HOL', 'CARRIER_DELAY', 'ORIGIN_DELAY', 'car_AS', 'car_B6', 'car_DL', 'car_EV', 'car_F9', 'car_HA', 'car_NK', 'car_OO', 'car_UA', 'car_VX', 'car_WN', 'd_2', 'd_3', 'd_4', 'd_5', 'd_6', 'd_7', 'm_2', 'm_3', 'm_4', 'm_5', 'm_6', 'm_7', 'm_8', 'm_9', 'm_10', 'm_11', 'm_12', 'dep_1', 'dep_2', 'dep_3', 'dep_4', 'dep_5', 'dep_6', 'dep_7', 'dep_8', 'dep_9', 'dep_10', 'dep_11', 'dep_12', 'dep_13', 'dep_14', 'dep_15', 'dep_16', 'dep_17', 'dep_18', 'dep_19', 'dep_20', 'dep_21', 'dep_22', 'dep_23']

Régression KNN
['CRS_ELAPSED_TIME', 'NEXT_HOL', 'PREV_HOL', 'CARRIER_DELAY', 'ORIGIN_DELAY', 'car_AS', 'car_B6', 'car_DL', 'car_EV', 'car_F9', 'car_HA', 'car_NK', 'car_OO', 'car_UA', 'car_VX', 'car_WN', 'd_2', 'd_3', 'd_4', 'd_5', 'd_6', 'd_7', 'm_2', 'm_3', 'm_4', 'm_5', 'm_6', 'm_7', 'm_8', 'm_9', 'm_10', 'm_11', 'm_12', 'dep_1', 'dep_2', 'dep_3', 'dep_4', 'dep_5', 'dep_6', 'dep_7', 'dep_8', 'dep_9', 'dep_10', 'dep_11', 'dep_12', 'dep_13', 'dep_14', 'dep_15', 'dep_16', 'dep_17', 'dep_18', 'dep_19', 'dep_20', 'dep_21', 'dep_22', 'dep_23']


