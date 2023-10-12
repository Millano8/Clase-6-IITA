from flask import Flask, jsonify, request

app = Flask(__name__)

listaSuper = []


# Obtener todos los todos
@app.route("/api/listaSuper", methods=["GET"])
def get_listaSuper():
    return jsonify(listaSuper)


# Agrego un nuevo producto en la lista
@app.route("/api/listaSuper", methods=["POST"])
def create_todo():
    prod = request.json
    listaSuper.append(prod)
    return jsonify(message="Producto Agregado")


# Obtener un prod por su ID
@app.route("/api/listaSuper/<int:prod_id>", methods=["GET"])
def get_prodLista(prod_id):
    for prod in listaSuper:
        if prod["id"] == str(prod_id):
            return jsonify(prod), 200
    return jsonify(message="Producto no encontrado"), 404


# Actualizar un todo por su ID
@app.route("/api/listaSuper/<int:prod_id>", methods=["PUT"])
def update_lista(prod_id):
    print(request.json)
    for prod in listaSuper:
        if prod["id"] == str(prod_id):
            prod["producto"] = request.json["producto"]
            return jsonify(message="Producto actualizado exitosamente"), 200
    return jsonify(message="Producto no encontrado"), 404


# Eliminar un todo por su ID
@app.route("/api/listaSuper/<int:prod_id>", methods=["DELETE"])
def delete_prod(prod_id):
    for prod in listaSuper:
        if prod["id"] == str(prod_id):
            listaSuper.remove(prod)
            return jsonify(message="Producto eliminado exitosamente"), 200
    return jsonify(message="Producto no encontrado"), 404


if __name__ == "__main__":
    app.run()
