from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Rota para obter dados do IBGE por estado
@app.route('/ibge/estado', methods=['GET'])
def get_estado():
    uf = request.args.get('uf')  # Exemplo: 'SP'
    if not uf:
        return jsonify({"erro": "Parâmetro 'uf' é obrigatório"}), 400
    
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return jsonify(resposta.json())
    return jsonify({"erro": "Estado não encontrado"}), 404


# Rota para buscar dados de uma empresa via CNPJ
@app.route('/cnpj', methods=['GET'])
def get_cnpj():
    cnpj = request.args.get('cnpj')  # Exemplo: '00000000000191'
    if not cnpj:
        return jsonify({"erro": "Parâmetro 'cnpj' é obrigatório"}), 400
    
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return jsonify(resposta.json())
    return jsonify({"erro": "CNPJ inválido ou não encontrado"}), 404


# Rota para verificar BIN de cartão
@app.route('/bin', methods=['GET'])
def get_bin():
    bin_number = request.args.get('bin')  # Exemplo: '45717360'
    if not bin_number:
        return jsonify({"erro": "Parâmetro 'bin' é obrigatório"}), 400
    
    url = f"https://lookup.binlist.net/{bin_number}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return jsonify(resposta.json())
    return jsonify({"erro": "BIN não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)