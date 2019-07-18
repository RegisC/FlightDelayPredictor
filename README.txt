Initialisation de Heroku 
------------------------

Exporter la liste des paquetages requis :
pip freeze > requirements.txt

Supprimer les entrées suivantes :
mkl-fft
mkl-random

heroku login
heroku git:remote -a rc-flight-delays
git add .
git commit -m "Message"
git push heroku master

Pour afficher les messages émis sur le serveur
----------------------------------------------

heroku logs -t

Exécution locale
----------------

conda activate flightdelay_env

RunFlask.bat
ou
ipython FlightDelayPredictor.py
ou 
waitress-serve --port=5000  app:instance

