from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
def get_full_data(boro="BROOKLYN", streetname = "AVENUE N", housenumber = 1215):
    response = requests.get('https://data.cityofnewyork.us/resource/wvxf-dwi5.json$select=violation,streetname,boro,housenumber&$limit=10000')
    #tried to build querie with soda as instructed in documentation, attempting to limit how much data is coming in but I don't think its working https://dev.socrata.com/docs/queries/ 

headers = {
  'X-App-Token': 'cKxtMsywux5IuCCh7aixGChhT'
}

