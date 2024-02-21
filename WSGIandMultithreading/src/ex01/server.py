from flask import Flask, render_template, request, send_from_directory, jsonify
from wsgiref.simple_server import make_server
import os

app = Flask(__name__)

if not os.path.exists("uploads"):
    os.makedirs("uploads")

app.config["UPLOAD_DIR"] = "uploads"
uploads_folder = os.path.join(os.getcwd(), "uploads")


def get_list_of_audios():
    files = os.listdir("uploads/")
    return files


@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if str(file.filename).endswith((".mp3", ".ogg", ".wav")):
            file.save(os.path.join(app.config["UPLOAD_DIR"], file.filename))
            message = "File uploaded successfully"
        else:
            message = "Non audio file detected"
        return render_template(
            "upload.html", msg=message, music_files=get_list_of_audios()
        )
    return render_template("upload.html", msg="", music_files=get_list_of_audios())


@app.route("/play", methods=["POST"])
def play():
    selected_song = request.form["selected_song"]
    print(request.files)
    return render_template(
        "upload.html", music_files=get_list_of_audios(), selected_song=selected_song
    )


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(uploads_folder, filename)


@app.route("/json")
def index_json():
    files = get_list_of_audios()
    return jsonify(files=files)


if __name__ == "__main__":
    # app.run()
    server = make_server("localhost", 8888, app)
    server.serve_forever()
