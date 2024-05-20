from flask import Flask, jsonify, request # type: ignore

app = Flask(__name__)

@app.route('/')
def root():
    return 'Home'

"""
GET -> obtener información
POST -> Crear información
PUT -> Actualizar información
DELETE -> Borrar información

"""
@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id": user_id, "name": "test", "telefono": "410-11-22-33"}
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200  # Asegúrate de devolver una respuesta en todos los casos

@app.route('/users',methods=['POST'])
def create_user():
    data =request.get_json()
    data["status"] = "user created"
    return jsonify(data),201

if __name__ == "__main__":
    app.run(debug=True)