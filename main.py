from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def saludar():
    return jsonify({'message': f'Hola Saul!'})
    
if __name__ == '__main__':
    print("App iniciando correctamente")
    app.run(host='0.0.0.0', port=5000)


