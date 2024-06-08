from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import requests
load_dotenv() 

url = "https://newsapi.org/v2/everything?q=AAPL&apiKey=ace4a856372147739d32a3a7cf3f004e"

response = requests.get(url)
data = response.json()

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")
    # return data





