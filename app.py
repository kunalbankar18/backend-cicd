from flask import Flask,jsonify
from data import get_data

app= Flask(__name__)

@app.route('/')
def helloWorld():

    return 'Hello World'

@app.route('/api')
def api():

    data = get_data()

    data={
        'data':data
    }

    return jsonify(data)

if __name__=='__main__':

    app.run(port=5000,host='0.0.0.0',debug=True )