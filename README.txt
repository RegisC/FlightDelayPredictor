Initialisation de Heroku 
------------------------

heroku git:remote -a rc-flight-delays


Exécution locale
----------------

conda activate flightdelay_env

RunFlask.bat
ou
ipython FlightDelayPredictor.py
ou 
waitress-serve --port=5000  app:instance

Mise à jour des fichiers sur Heroku
-----------------------------------

Exporter la liste des paquetages requis :
conda list --export > requirements.txt

