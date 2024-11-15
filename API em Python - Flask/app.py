from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

API_KEY = "Sua_Chave_Privada"  # Substitua pela sua chave de API do OpenWeatherMap

@app.route('/')
def home():
    return render_template('index.html')  # Carrega o HTML da pasta templates

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    data = response.json()
    weather_info = {
        "cidade": data["name"],
        "temperatura": data["main"]["temp"],
        "descricao": data["weather"][0]["description"],
        "umidade": data["main"]["humidity"],
        "vento": data["wind"]["speed"]
    }

    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(debug=True)
