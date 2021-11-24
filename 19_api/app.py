# Yea! -- Andrew Juang, Eliza Knapp, Yuqing Wu
# SoftDev
# K19 -- A RESTful Journey Skyward
# 2021-11-23

from flask import Flask, render_template
#import requests
import urllib
import json

app = Flask(__name__)

# get api key
f = open("key_nasa.txt")
API_KEY = f.read().strip()

@app.route("/")
def main():

    # api with urllib
    r = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + API_KEY)

    JSON = r.read()
    print(JSON)

    URL = json.loads(JSON)['url']
    print("URL:" + URL)



    # -- Another way to do api with requests --
    #print("API_KEY: " + API_KEY + "\n")
    #r = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + API_KEY)

    #print("JSON:")
    #print(r.json())

    #URL = r.json()['url']
    #print("\nURL: " + URL)


    return render_template('main.html',pic=URL)

if __name__ == "__main__":
    app.debug = True
    app.run()
