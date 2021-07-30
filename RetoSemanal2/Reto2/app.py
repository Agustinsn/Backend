from flask import Flask, request

app=Flask(__name__)

usuarios={

}

@app.route('/ingresar',methods=['POST'])
def ingresar():
    datos=request.form
    usuarios[datos['id']]={
        "nombre":datos['nombre'],
        "edad":datos['edad'],
    }
    return 'Datos ingresados', 201

@app.route('/mostrarTodos', methods=['GET'])
def mostrar_todos():
    return f'Los usuarios ingresados son: {usuarios}'

@app.route('/mostar')
def mostrar():
    id=request.args.get('id')
    usuario=usuarios[id]
    return f'El usuario es:{usuario}'