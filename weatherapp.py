from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

api_key = "d7fcc888f9c930253aad15b1560d29dc"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"
        response = requests.get(url)
        data = response.json()
        print("RESPONSE:", data)
        if str(data["cod"]) == "200":
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
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)