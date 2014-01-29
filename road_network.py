""" Downloads road network from Vegdata.no for Norwegian counties (hard coded for Vestfold for now). See http://vegnett.vegdata.no/ for information and license for use of the data. """

# ScriptRunner said these could be useful. I use some of them already.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


def run_script(iface):
	places = ['07']
	#categories = ['E', 'R', 'F', 'K', 'P', 'S']
	categories = ['E', 'R']
	url = 'http://vegnett.vegdata.no/nvdb/api/vegnett/'
    
	for cat in categories:
		for place in places:
			get = url+place+'.json?kategori='+cat
			print ("* Downloading layer: "+get)
			layer = QgsVectorLayer (get, 'road_network-'+place+"-"+cat, "ogr")
			QgsMapLayerRegistry.instance().addMapLayer(layer)