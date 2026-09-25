
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
    <style>
        body {
            background-color: #e8f5e9;
            font-family: Arial;
            text-align: center;
            padding: 50px;
        }

        h1 {
            color: #2e7d32;
            font-size: 40px;
        }

        p {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            font-size: 18px;
            line-height: 1.6;
        }

        button {
            background-color: #43a047;
            color: white;
            border: none;
            padding: 15px 25px;
            margin: 10px;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background-color: #2e7d32;
        }
    </style>

    <h1>🌍 İklim değişikliği nedir?</h1>

    <p>
    İklim değişikliği, uzun vadeli hava durumu desenlerindeki değişiklikleri ifade eder.
    Bu değişiklikler, doğal süreçler ve insan faaliyetleri nedeniyle meydana gelebilir.
    İklim değişikliği, sıcaklık artışları, deniz seviyesindeki yükselmeler,
    aşırı hava olayları ve ekosistemlerdeki bozulmalar gibi çeşitli etkilerle
    kendini gösterebilir.
    </p>

    <a href="/iklim-degisikligi-neyapabiliriz">
        <button>🌱 Ne yapabiliriz?</button>
    </a>

    <a href="/iklim-degisikligi-endiselenmelimiyiz">
        <button>🌡️ Endişelenmeli miyiz?</button>
    </a>
    '''

app.run(debug=True)

