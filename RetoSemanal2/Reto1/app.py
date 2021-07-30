from flask import Flask

app=Flask(__name__)

dep={
    "ok":True,
    "content":['Amazonas', 'Ancash', 'Apurimac', 'Arequipa', 'Ayacucho', 'Cajamarca', 'Callao', 'Cusco', 'Huancavelica', 'Huanuco', 'Ica', 'Junín', 'La Libertad', 'Lambayeque', 'Lima', 'Loreto', 'Madre de Dios', 'Moquegua', 'Pasco', 'Piura', 'Puno',' San Martín', 'Tacna', 'Tumbes', 'Ucayali'],
    "message":"Enviado"
}

@app.route('/')
def departamentos():
    departamentos=dep.get("content")
    return f'Los departamentos del Perú son {departamentos}'

if __name__ == '__main__':
    app.run()