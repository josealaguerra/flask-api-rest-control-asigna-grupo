from flask import Flask, request, jsonify

app = Flask(__name__)

voluntarios = []
grupos = []

# Voluntario

class Voluntario:
    def __init__(self, id, nombre, edad, email):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.email = email

@app.route('/voluntarios', methods=['GET'])
def get_voluntarios():
    return jsonify({'voluntarios': voluntarios})

@app.route('/voluntarios/<int:id>', methods=['GET'])
def get_persona(id):
    voluntario = next((voluntario for voluntario in voluntarios if voluntario.id == id), None)
    if voluntario:
        return jsonify(voluntario.__dict__)
    return jsonify({'message': 'Voluntario no encontrada'})

@app.route('/voluntarios', methods=['POST'])
def add_persona():
    voluntario = Voluntario(request.json['id'], request.json['nombre'], request.json['edad'], request.json['email'])
    voluntarios.append(voluntario)
    return jsonify(voluntario.__dict__)

@app.route('/voluntarios/<int:id>', methods=['PUT'])
def update_persona(id):
    voluntario = next((voluntario for voluntario in voluntarios if voluntario.id == id), None)
    if voluntario:
        voluntario.nombre = request.json['nombre']
        voluntario.edad = request.json['edad']
        voluntario.email = request.json['email']
        return jsonify(voluntario.__dict__)
    return jsonify({'message': 'Voluntario no encontrada'})

@app.route('/voluntarios/<int:id>', methods=['DELETE'])
def delete_persona(id):
    voluntario = next((voluntario for voluntario in voluntarios if voluntario.id == id), None)
    if voluntario:
        voluntarios.remove(voluntario)
        return jsonify({'message': 'Voluntario eliminada'})
    return jsonify({'message': 'Voluntario no encontrada'})

# Grupo

class Grupo:
    def __init__(self, id, nombre, voluntarios):
        self.id = id
        self.nombre = nombre
        self.voluntarios = voluntarios

@app.route('/grupos', methods=['GET'])
def get_grupos():
    return jsonify({'grupos': [grupo.__dict__ for grupo in grupos]})

@app.route('/grupos/<int:id>', methods=['GET'])
def get_grupo(id):
    grupo = next((grupo for grupo in grupos if grupo.id == id), None)
    if grupo:
        return jsonify(grupo.__dict__)
    return jsonify({'message': 'Grupo no encontrado'})

@app.route('/grupos', methods=['POST'])
def add_grupo():
    grupo = Grupo(request.json['id'], request.json['nombre'], request.json['voluntarios'])
    grupos.append(grupo)
    return jsonify(grupo.__dict__)

@app.route('/grupos/<int:id>', methods=['PUT'])
def update_grupo(id):
    grupo = next((grupo for grupo in grupos if grupo.id == id), None)
    if grupo:
        grupo.nombre = request.json['nombre']
        grupo.voluntarios = request.json['voluntarios']
        return jsonify(grupo.__dict__)
    return jsonify({'message': 'Grupo no encontrado'})

@app.route('/grupos/<int:id>', methods=['DELETE'])
def delete_grupo(id):
    grupo = next((grupo for grupo in grupos if grupo.id == id), None)
    if grupo:
        grupos.remove(grupo)
        return jsonify({'message': 'Grupo eliminado'})
    return jsonify({'message': 'Grupo no encontrado'})

if __name__ == '__main__':
    app.run(debug=True)
