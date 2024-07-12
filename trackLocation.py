import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium
from flask import Flask, render_template

"""Starts a Flask Web Application"""

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return 'home.html'


@app.route("/about")
def about():
    return 'about.html'


@app.route("/location")
def location():
    return 'location.html'


key = "ad6e7ced7e414f06b0d2351b9ab15c77" #Geocoder API Key needs to paste here "your key" 
number = input("please enter your number: ")
new_number = phonenumbers.parse(number)
location = geocoder.description_for_number(new_number, "en")
print(location)

service_name = carrier.name_for_number(new_number,"en")
print(service_name)

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

my_map = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat, lng], popup= location).add_to(my_map)

my_map.save("location.html")

print("location tracking completed")

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)