from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

superheroes = [
  {
    "createdAt": "2024-05-25T12:53:50.473Z",
    "name": "Super Man",
    "avatar": "https://www.cinemascomics.com/wp-content/uploads/2021/06/Superman.jpg",
    "power": "Super fuerza",
    "height": 1.89,
    "id": "1"
  },
  {
    "createdAt": "2024-05-25T18:57:16.232Z",
    "name": "Flash",
    "avatar": "https://img.posterstore.com/zoom/wb0143-8theflash-running50x70.jpg",
    "power": "Velocidad",
    "height": 1.76,
    "id": "2"
  },
  {
    "createdAt": "2024-05-25T10:08:56.081Z",
    "name": "Linterna verde",
    "avatar": "https://docpastor.com/wp-content/uploads/2016/09/75anosde_Green_Lantern.jpg",
    "power": "Manipulación espacio-tiempo",
    "height": 1.92,
    "id": "3"
  },
  {
    "createdAt": "2024-05-25T04:51:29.914Z",
    "name": "Spider Man",
    "avatar": "https://m.media-amazon.com/images/M/MV5BMmQ1NzBlYmItNmZkZi00OTZkLTg5YTEtNTI5YjczZjk3Yjc1XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg",
    "power": "Super fuerza",
    "height": 1.79,
    "id": "4"
  },
  {
    "createdAt": "2024-05-25T01:56:32.002Z",
    "name": "Capitan America",
    "avatar": "https://i.pinimg.com/736x/5d/13/58/5d1358223ae9cf7e8f1121cacac3b167.jpg",
    "power": "Super fuerza",
    "height": 1.82,
    "id": "5"
  },
  {
    "createdAt": "2024-05-24T22:47:49.807Z",
    "name": "Iroman",
    "avatar": "https://i.pinimg.com/236x/fb/ca/c5/fbcac59762f94785d0969b8edaacaf49.jpg",
    "power": "Robotica",
    "height": 1.81,
    "id": "6"
  },
  {
    "createdAt": "2024-05-25T13:32:10.352Z",
    "name": "Vision",
    "avatar": "https://i.pinimg.com/originals/6c/4a/0f/6c4a0f2a1a79c731d20ca8fad369f71e.png",
    "power": "Psiquicos",
    "height": 1.78,
    "id": "7"
  },
  {
    "createdAt": "2024-05-25T15:55:05.714Z",
    "name": "thor",
    "avatar": "https://i.pinimg.com/236x/a0/89/dd/a089ddc424309d43a14a1ee50af42dbe.jpg",
    "power": "Dios",
    "height": 1.93,
    "id": "8"
  },
  {
    "createdAt": "2024-05-25T16:34:17.483Z",
    "name": "Rockect",
    "avatar": "https://tooys.mx/media/catalog/product/cache/39c7ff5a74bd9fa282a021db605b774d/r/o/rocket-and-cosmo_marvel_00.jpg",
    "power": "Super inteligencia",
    "height": 0.57,
    "id": "9"
  },
  {
    "createdAt": "2024-05-25T12:33:27.424Z",
    "name": "Cosmo",
    "avatar": "https://tooys.mx/media/catalog/product/cache/39c7ff5a74bd9fa282a021db605b774d/r/o/rocket-and-cosmo_marvel_00.jpg",
    "power": "Super Perro",
    "height": 0.56,
    "id": "10"
  }
]

# Ruta para obtener todos los superhéroes
@app.route('/superheroes', methods=['GET'])
def get_superheroes():
    response = jsonify(superheroes)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Ruta para obtener un superhéroe por ID
@app.route('/superheroes/<id>', methods=['GET'])
def get_superhero(id):
    superhero = next((sh for sh in superheroes if sh['id'] == id), None)
    if superhero is None:
        return jsonify({"error": "Superhéroe no encontrado"}), 404
    return jsonify(superhero), 200

# Ruta para crear un nuevo superhéroe
@app.route('/superheroes', methods=['POST'])
def create_superheroe():
    new_heroe = request.json
    new_heroe["id"] = max(heroe["id"] for heroe in superheroes)
    superheroes.append(new_heroe)
    response = jsonify(new_heroe)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 201

# Ruta para actualizar un superhéroe existente
@app.route('/superheroes/edit', methods=['POST'])
def edit_superhero():
    data = request.json
    createdAt = data.get('createdAt')
    id = data.get('id')
    name = data.get('name')
    power = data.get('power')
    height = data.get('height')
    avatar = data.get('avatar')

    heroe = next((heroe for heroe in superheroes if heroe["id"] == id), None)
    if heroe:
        data = request.json
        heroe.update(data)
        return jsonify(heroe)
    return ('', 404)

# Ruta para borrar un superhéroe
@app.route('/superheroes/<int:id>', methods=['DELETE'])
def delete_superheroe(id):
    global superheroes
    superheroes = [heroe for heroe in superheroes if heroe["id"] != id]
    return ('', 204)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
