from flask import Flask, render_template, request
import json
from urllib.request import urlopen, Request

from psycopg2 import sql

import connection

app = Flask(__name__)


def api(page):
    webURL = Request("https://swapi.co/api/planets?page=" + str(page), headers={'User-Agent': 'Mozilla/5.0'})  # This will return a string containing the data in JSON format
    data = urlopen(webURL).read()
    response_data = json.loads(data.decode('utf-8'))  # parse the JSON and convert it into a dict
    print(response_data['results'])
    return response_data['results']


@app.route('/')
@app.route('/')
def root():
    if request.args.get('[age'):
        page = int(request.args.get('page'))
    else:
        page = 1

    results = getPlanets(page)
    print(execute_query("SELECT * from users"))
    return render_template("index.html", results=results, page = page)


@app.route('/residents', methods=["POST"])
def residents():
    planet_residents = []
    planet_id = request.form.get("index")
    planet = getPlanet(planet_id)
    print(planet)
    for resident in planet["residents"]:
        print("res: " + resident)
        planet_residents.append(get_api_url(resident))
    # print(residents)
    return render_template("residents.html", residents=planet_residents, planet=planet["name"])

def getPlanet(id):
    webURL = Request("https://swapi.co/api/planets/" + str(id), headers={
        'User-Agent': 'Mozilla/5.0'})  # This will return a string containing the data in JSON format
    data = urlopen(webURL).read()
    response_data = json.loads(data.decode('utf-8'))  # parse the JSON and convert it into a dict
    # print(response_data)
    return response_data


def get_api_url(url):
    print("url: " + url)
    webURL = Request(url, headers={'User-Agent': 'Mozilla/5.0'})  # This will return a string containing the data in JSON format
    data = urlopen(webURL).read()
    response_data = json.loads(data.decode('utf-8'))  # parse the JSON and convert it into a dict
    # print(response_data)
    return response_data


def getPlanets(page):
    plantes = api(page)
    # print(len(plantes))
    return plantes


@connection.connection_handler
def execute_query(cursor, query):
    if query.startswith("SELECT"):
        cursor.execute(
            sql.SQL(query)
        )
        result = cursor.fetchall()

    else:
        result = cursor.execute(query)
    return result


if __name__ == '__main__':
    app.run()
