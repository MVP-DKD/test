import os

from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = "videos"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]
    if file.filename == "":
        return "No selected file"

    if file:
        filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filename)
        return render_template("play.html", video_file=file.filename)


@app.route("/videos/<path:filename>")
def download_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run()
