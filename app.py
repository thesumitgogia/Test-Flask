from os import name
from flask import Flask, render_template, request
import pymongo
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['name']
        
        client = pymongo.MongoClient("mongodb+srv://sumit123:sumit123@cluster0.8x1lw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client['s']
        col = db['c']
        dt = {'h': 's'}
        col.insert_one(dt)
        print(title)

    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True,host='127.1.1.1', port='8000')