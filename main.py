from flask import Flask, render_template, request
import colorgram

app = Flask(__name__)
app.config["SECRET_KEY"] = "TOP SECRET SHIT"


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb



@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        intro = False
        image = request.form.get("url").replace("\\", "/")
        colors = colorgram.extract(image, 10)
    else:
        intro = True
        image = "static/Motorcycle.jpg"
        colors = colorgram.extract(image, 10)
    return render_template("index.html", colors=colors, image=image, hex_=rgb_to_hex, intro=intro)


if __name__ == "__main__":
    app.run(debug=True)
