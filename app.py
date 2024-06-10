import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv # type: ignore
import requests

load_dotenv() 

api_key = os.getenv("apiKey")

app = Flask(__name__)
#Raw route for debugging
@app.route("/raw")
def raw():
    search_query = "GOOG"
    url = f"https://newsapi.org/v2/everything?q={search_query}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data 

@app.route("/")
def hello():
    # Get search query from request object
    search_query = request.args.get("search_query")  # Access using 'args' for GET requests

    # If search query exists, update API request URL
    if search_query:
        url = f"https://newsapi.org/v2/everything?q={search_query}&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()
        # print(data)
    else:
        # Handle case where no search query is provided
        data = None  # Or set a default message

    return render_template("index.html", news_data=data, search_query=search_query)




