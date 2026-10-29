from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde cualquier origen a todos los endpoints

@app.route('/getmyinfo')
def getMyInfo():
    value = {
        "name":"user name",
        "lastname":"user lastname",
        "socialMedia":{
            "facebook":"fb.com",
            "instagram":"instagram.com",
            "twitter":"x.com",
            "linkedin":"linkedin.com",
            "github":"github.com"
        },
        "author":"name autor"
    }
    return jsonify(value)

if __name__ == '__main__':
    app.run(debug=True)