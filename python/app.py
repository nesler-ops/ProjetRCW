from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    
    # Calcular total con impuestos
    total = float(data['total'])
    total_taxe = total * 1.15
    
    # Agregar el total con impuestos a los datos
    data['total_taxe'] = round(total_taxe, 2)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)