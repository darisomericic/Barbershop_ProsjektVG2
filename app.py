from flask import Flask
from flask_cors import CORS # importerer cors for å tillate kobling fra andre domener 
from dotenv import load_dotenv # importerer dotenv for å lese det som står i .env filen og for å gjøre det tigjengelig i Python
import os # importeres for å hente ting skrevet i .env filen
import requests # dette importeres for at API-kall skal fungere
import mariadb # importeres for å kunne snakke med DB
import mariadb # iporteres for å kunne snakke med DB

load_dotenv() # laster alt som står i .env filer

app = Flask(__name__)
CORS(app) # tillater tilkobling fra andre domener 


def db_connection(): # funskjonen for å koble til DB
        return mariadb.connect( # kobler på DB ved å bruke .env info 
           host=os.getenv('DB_HOST'), # host 
           user=os.getenv('DB_USER'), # bruker
           password=os.getenv('DB_PASS'), # passord
           database=os.getenv('DB_NAME'), # database navn
           port=int(os.getenv("DB_PORT", 3306)) # port, hvis det ikke står i .env filen så bruker den 3306 som er standard for mariadb
        )
        
        
        
        
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)