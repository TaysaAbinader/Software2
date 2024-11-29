from flask import Flask
import json
from DatabaseConnection import connection
import mysql.connector

app = Flask(__name__)

def get_airport_info(icao):
    try:
        cursor = connection.cursor()
        sql = f"SELECT name, municipality FROM airport WHERE airport.ident = '{icao}';"
        cursor.execute(sql)
        airport = cursor.fetchone()
        cursor.close()
        return airport
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None


@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    airport_info = get_airport_info(icao.upper())
    if airport_info:
        print(airport_info)
        response = {
            "ICAO": icao.upper(),
            "Name": airport_info[0],
            "Location": airport_info[1]
        }
        return json.dumps(response)

    return json.dumps({"message": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
