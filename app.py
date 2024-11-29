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
  
@app.route('/animales/cedula/<string:cedula>', methods=['GET'])
def obtener_animal_por_cedula(cedula):
    # Validar que la cédula sea completamente numérica
    if not cedula.isdigit():
        return jsonify({"error": "La cédula debe ser un valor numérico"}), 400

    # Determinar el último dígito
    ultimo_digito = int(cedula[-1])

    # Asignar animal según el último dígito
    if 0 <= ultimo_digito <= 3:
        animal = "gato"
    elif 4 <= ultimo_digito <= 6:
        animal = "huron"
    elif 7 <= ultimo_digito <= 9:
        animal = "boa constrictor"
    else:
        return jsonify({"error": "No se pudo determinar el animal"}), 500

    # Obtener información del animal y devolverla
    if animal in animales:
        return jsonify({
            "cedula": cedula,
            "animal": animales[animal].tipo(),
            "sonido": animales[animal].hacer_sonido()
        })
    else:
        return jsonify({"error": "Animal no encontrado"}), 404

if __name__ == '__main__':
  app.run(debug=True)