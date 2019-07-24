import datetime
import flask_wtf
import wtforms as wtf
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Optional
from wtforms import BooleanField, IntegerField
from wtforms_components import TimeField

class NoValSelectField(wtf.SelectField):
	"""Cette classe désactive la validation, qui ne fonctionnait pas."""
	def pre_validate(self, form):
		pass 

class FlightDetailsForm(flask_wtf.FlaskForm):	
	airlines = [
		'AA', 'AS', 'B6', 'DL', 'F9', 'HA', 'NK', 'EV', 'OO', 'UA', 'VX', 'WN'
	]	
	airports = [
		'ABE', 'ABI', 'ABQ', 'ABR', 'ABY', 'ACK', 'ACT', 'ACV', 'ACY', 'ADK',
		'ADQ', 'AEX', 'AGS', 'AKN', 'ALB', 'AMA', 'ANC', 'APN', 'ASE', 'ATL',
		'ATW', 'AUS', 'AVL', 'AVP', 'AZO', 'BDL', 'BET', 'BFL', 'BGM', 'BGR',
		'BHM', 'BIL', 'BIS', 'BJI', 'BLI', 'BMI', 'BNA', 'BOI', 'BOS', 'BPT',
		'BQK', 'BQN', 'BRD', 'BRO', 'BRW', 'BTM', 'BTR', 'BTV', 'BUF', 'BUR',
		'BWI', 'BZN', 'CAE', 'CAK', 'CDC', 'CDV', 'CHA', 'CHO', 'CHS', 'CID',
		'CIU', 'CLE', 'CLL', 'CLT', 'CMH', 'CMX', 'COD', 'COS', 'CPR', 'CRP',
		'CRW', 'CSG', 'CVG', 'CWA', 'DAB', 'DAL', 'DAY', 'DCA', 'DEN', 'DFW',
		'DHN', 'DLG', 'DLH', 'DRO', 'DSM', 'DTW', 'DVL', 'EAU', 'ECP', 'EFD',
		'EGE', 'EKO', 'ELM', 'ELP', 'ERI', 'ESC', 'EUG', 'EVV', 'EWN', 'EWR',
		'EYW', 'FAI', 'FAR', 'FAT', 'FAY', 'FCA', 'FLG', 'FLL', 'FNT', 'FSD',
		'FSM', 'FWA', 'GCC', 'GCK', 'GEG', 'GFK', 'GGG', 'GJT', 'GNV', 'GPT',
		'GRB', 'GRI', 'GRK', 'GRR', 'GSO', 'GSP', 'GST', 'GTF', 'GTR', 'GUC',
		'GUM', 'HDN', 'HIB', 'HLN', 'HNL', 'HOB', 'HOU', 'HPN', 'HRL', 'HSV',
		'HYA', 'HYS', 'IAD', 'IAG', 'IAH', 'ICT', 'IDA', 'ILM', 'IMT', 'IND',
		'INL', 'ISN', 'ISP', 'ITH', 'ITO', 'JAC', 'JAN', 'JAX', 'JFK', 'JLN',
		'JMS', 'JNU', 'KOA', 'KTN', 'LAN', 'LAR', 'LAS', 'LAW', 'LAX', 'LBB',
		'LBE', 'LCH', 'LEX', 'LFT', 'LGA', 'LGB', 'LIH', 'LIT', 'LNK', 'LRD',
		'LSE', 'LWS', 'MAF', 'MBS', 'MCI', 'MCO', 'MDT', 'MDW', 'MEI', 'MEM',
		'MFE', 'MFR', 'MGM', 'MHK', 'MHT', 'MIA', 'MKE', 'MKG', 'MLB', 'MLI',
		'MLU', 'MMH', 'MOB', 'MOT', 'MQT', 'MRY', 'MSN', 'MSO', 'MSP', 'MSY',
		'MTJ', 'MVY', 'MYR', 'OAJ', 'OAK', 'OGG', 'OKC', 'OMA', 'OME', 'ONT',
		'ORD', 'ORF', 'ORH', 'OTH', 'OTZ', 'PAH', 'PBG', 'PBI', 'PDX', 'PGD',
		'PHF', 'PHL', 'PHX', 'PIA', 'PIB', 'PIH', 'PIT', 'PLN', 'PNS', 'PPG',
		'PSC', 'PSE', 'PSG', 'PSP', 'PVD', 'PWM', 'RAP', 'RDD', 'RDM', 'RDU',
		'RHI', 'RIC', 'RKS', 'RNO', 'ROA', 'ROC', 'ROW', 'RST', 'RSW', 'SAF',
		'SAN', 'SAT', 'SAV', 'SBA', 'SBN', 'SBP', 'SCC', 'SCE', 'SDF', 'SEA',
		'SFO', 'SGF', 'SGU', 'SHV', 'SIT', 'SJC', 'SJT', 'SJU', 'SLC', 'SMF',
		'SMX', 'SNA', 'SPI', 'SPN', 'SPS', 'SRQ', 'STL', 'STT', 'STX', 'SUN',
		'SWF', 'SYR', 'TLH', 'TPA', 'TRI', 'TTN', 'TUL', 'TUS', 'TVC', 'TWF',
		'TXK', 'TYR', 'TYS', 'UST', 'VLD', 'VPS', 'WRG', 'WYS', 'XNA', 'YAK', 
		'YUM'
	]
	choices = list(zip(airlines, airlines))
	airline = wtf.SelectField('Compagnie aérienne', choices=choices)
	choices = list(zip(airports, airports))
	dep_airport = wtf.SelectField('Aéroport de départ', choices=choices)
	dep_date = DateField("Date (locale) de départ du vol", 
							 validators=[DataRequired()], format='%Y-%m-%d',
							 default=datetime.datetime.today)	
	dep_time = TimeField("Heure (locale) de départ du vol", 
							 validators=[DataRequired()])								 
	flight_duration = TimeField('Durée annoncée du vol', 
								validators=[DataRequired()])
	#flight_departed = BooleanField('Avion déjà en vol')
	dep_delay = IntegerField('Retard au décollage, si connu (minutes)',
							 validators=[Optional(strip_whitespace=True)])
	submit = wtf.SubmitField("Prédire l'heure d'arrivée")
	
	def reset_choices(self):
		# Pourquoi ceci est-il nécessaire ?
		self.airline.choices = zip(self.airlines, self.airlines)
		self.dep_airport.choices = zip(self.airports, self.airports)
