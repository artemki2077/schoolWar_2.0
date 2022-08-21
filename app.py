from flask import Flask, request, jsonify
import datetime as dt


app = Flask(__name__)


@app.route('/')
def main():
    return "Spynder, лох"



if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)