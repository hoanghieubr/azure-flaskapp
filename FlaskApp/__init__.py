from flask import Flask, jsonify, render_template

# Always use relative import for custom module
from .package.module import MODULE_VALUE

app = Flask(__name__)

@app.route("/")
def index():
    message = "Welcome to my site hahahaha !!"
    return render_template("index.html", message = message)

@app.route("/hello/<name>", methods=['GET'])
def hello(name: str):
    return f"hello {name}"

@app.route("/module")
def module():
    return f"loaded from FlaskApp.package.module = {MODULE_VALUE}"

@app.route("/api")
def api():
    return "use: api/name/<name>; or api/product/<product_id>"

@app.route("/api/name/<name>", methods=['GET'])
def api_name(name: str):
    return jsonify({"name": name})

@app.route("/api/product/<id>", methods=['GET'])
def api_product(id: str):
    id = int(id)
    product_list = [{"product id": 0, "name": "Car"},
                    {"product id": 1, "name": "Bike"},
                    {"product id": 2, "name": "Computer"}]
    if id > 2:
        return f"No product has ID {id}"
    else:
        return jsonify(product_list[id])

if __name__ == "__main__":
    app.run(host="0.0.0.0", Port=8000)