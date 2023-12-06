from flask import Flask, render_template, request
from violations import get_full_data
from waitress import serve

import requests

app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index ():
    return render_template("index.html")
headers = {
  'X-App-Token': 'cKxtMsywux5IuCCh7aixGChhT'
}





@app.route ("/violations")
def test():
    Street_Name = request.args.get("streetname")
    Boro_Name = request.args.get("boro")
    House_Number= request.args.get("housenumber")
    # place_data = get_violations(House_Number, Street_Name, Boro_Name)

    params = {
      'boro' : 'BROOKLYN',
      'streetname' : 'AVENUE *',
      'housenumber' : '1215',
      # "$limit" : 50000,
      #I'd like these to be edited based on what the user inputs on the buttons from index.html's violations form

    }



    # let's figure out what info was provided by the user
    if Street_Name.strip() == "":
        # no street name / remove it from the params
        del params['streetname']
    else:
        # street name, add it to the params,
        # TODO: logic here to normalize the street name so it works better
        Street_Name = Street_Name.upper()
        params['streetname'] = Street_Name.strip()

    if House_Number.strip() == "":
        # no street name / remove it from the params
        del params['housenumber']
    else:
        # street name, add it to the params,
        # TODO: logic here to normalize 
        params['housenumber'] = House_Number.strip()
        
    if Boro_Name.strip() == "":
        # no street name / remove it from the params
        del params['boro']
    else:
        # street name, add it to the params,
        # TODO: logic here to normalize 
        params['boro'] = Boro_Name.strip()
        
    
    # lets fire off the request with the search data we have now
    response = requests.get('https://data.cityofnewyork.us/resource/wvxf-dwi5.json', headers=headers, params=params)
    # for debugging only:
    # print(params)
    # print("Got code:",response.status_code)
    # print(response.text)
    data = response.json()


    

    

    return render_template(
        "violations.html",
        Street_Name = Street_Name,
        House_Number = House_Number,
        Boro_Name = Boro_Name,
        data=data
       )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

