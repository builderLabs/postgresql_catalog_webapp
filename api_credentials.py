#!/usr/bin/python

import json




# --- Google API credentials ----------------------------------------

googleCredPath = 'api_cred/client_secrets.json'


# --- Facebook API credentials --------------------------------------



# --- init credentials ----------------------------------------------

appCred = dict()
appCred['Google'] = dict()
appCred['Google']['client_id'] =  json.loads(open(googleCredPath, 'r').read())['web']['client_id']
appCred['Google']['appName'] = "Sample Catalog Project"

