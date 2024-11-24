from flask import Flask, jsonify, render_template

from animal import BoaConstrictor, Gato, Huron, Perro

app = Flask(__name__, static_folder="static", template_folder="templates")

# Crear instancias de los animales
animales = {
    "gato": Gato(),
    "perro": Perro(),
    "huron": Huron(),
    "boa constrictor": BoaConstrictor(),
}

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/animales', methods=['GET'])
def obtener_todos_los_animales():
  todos_los_animales = [
      {
          "animal": animal.tipo(),
      }
      for animal in animales.values()
  ]
  return jsonify(todos_los_animales)
    
@app.route('/animales/sonido/<string:animal>', methods=['GET'])
def obtener_sonido(animal):
  if animal in animales:
      return jsonify({
          "animal": animales[animal].tipo(),
          "sonido": animales[animal].hacer_sonido()
      })
  else:
      return jsonify({"error": "Animal no encontrado"}), 404

if __name__ == '__main__':
  app.run(debug=True)