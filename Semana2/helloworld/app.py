from flask import Flask
from flask import request

app= Flask(__name__)

@app.route('/name_post', methods=['POST'])
def name_post():
    json= request.json
    name=json['first_name']
    return f"hello {name}"

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/name')
def hello_name():
    first_name=request.args.get('/first_name')
    last_name=request.args.get('/last_name')
    return f"hello {first_name} {last_name}"

if __name__ == '__main__':
    app.run()