from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "d7fcc888f9c930253aad15b1560d29dc"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind": data["wind"]["speed"]
        }
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)