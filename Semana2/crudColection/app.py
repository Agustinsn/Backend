from flask import Flask

from flask import request
#instanciar flask __name___ por que no hay nombre
app= Flask(__name__)
#user es un diccionario y cada usuario tambien es un diccionario
users={
    'u01':{
        "first_name":'Ted',
        "last_name":'Thompson'
    },
    'u02':{
        "first_name":'Cleo',
        "last_name":'Sosa'
    }
}

@app.route('/')
def index():
    return 'hello word'

@app.route('/users')
def get_users():
    return users

#get user usando queryparams
# /user?id=u01
@app.route('/user')
def get_user():
    id=request.args.get('id')
    return users[id]


@app.route('/new_user', methods=['POST'])
def create_user():
    data=request.json
    users[data['id']]={
        "first_name":data['first_name'],
        "last_name":data['last_name']
    }
    return 'Ok', 201
#Se pasara el user por queryparams
#y los datos a actualizar mediante json
#metodo update para no modificar datos que no se requieren
@app.route('/update_user',methods=['PUT'])
def update_user():
    user=request.args.get('id')
    data=request.json
    users[user].update(data)
    return 'Ok'

@app.route('/delete_user',methods=['DELETE'])
def delete_user():
    id=request.args.get('id')
    users.pop(id)
    return 'Ok',203

