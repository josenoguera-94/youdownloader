from flask import render_template, request, redirect, url_for, flash
from app import app
from app.modules.select_folder import select_dir
from app.modules.downloader import download_video, info_video


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download", methods=["POST", "GET"])
def download():
    if (
        request.method == "POST"
        and request.form["url"][:32] == "https://www.youtube.com/watch?v="
    ):

        url = request.form["url"]
        try:
            infor_video = info_video(url)
        except:
            flash(
                u"No se ha podido obtener la información requerida, compruebe su url.",
                "error",
            )
            return redirect(url_for("index"))
        return render_template("index.html", result=infor_video)
    else:
        flash(
                u"No se ha podido obtener la información requerida, compruebe su url.",
                "error",
            )
        return redirect(url_for("index"))


@app.route("/download/<url_short>&<itag>", methods=["POST", "GET"])
def select_directory(url_short, itag):
    if request.method == "GET":
        url = "https://www.youtube.com/watch?v=" + url_short
        dirname = select_dir()
        print(dirname)

        if dirname != "":
            try:
                download_video(url_short, itag, dirname)
            except:
                flash(u"No se ha podido descargar el archivo.", "error")
                return redirect(url_for("index"))

        infor_video = info_video(url)
        return render_template("index.html", result=infor_video)
    else:
        return redirect(url_for("index"))
