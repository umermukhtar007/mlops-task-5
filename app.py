from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path="/static", static_folder="static")
app.config['MONGO_URI'] = 'mongodb://root:root@my-db:27017/userDB?authSource=admin'
mongo = PyMongo(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    mongo.db.users.insert_one(data)
    return jsonify({'message': 'info saved'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
