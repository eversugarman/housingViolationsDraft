from flask import Flask, render_template, request
from violations import get_full_data
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index ():
    return render_template("index.html")
headers = {
  'X-App-Token': 'cKxtMsywux5IuCCh7aixGChhT'
}
params = {
  'boro' : 'BROOKLYN',
  'streetname' : 'AVENUE *',
  'housenumber' : '1215'
  #I'd like these to be edited based on what the user inputs on the buttons from index.html's violations form

}

response = request.get('https://data.cityofnewyork.us/resource/wvxf-dwi5.json', headers=headers, params=params)
print("Got code:",response.status_code)
print(response.text)
data = response.json()
for violation in data:

    print(violation)


@app.route ("/violations")
def get_violations():
    Street_Name = request.args.get("streetname")
    Boro_Name = request.args.get("boro")
    House_Number= request.args.get("housenumber")
    place_data = get_violations(House_Number, Street_Name, Boro_Name)
    return render_template(
        "violations.html",
        title = place_data["name"],
        status = place_data["response"][violation]
       )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

