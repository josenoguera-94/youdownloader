import datetime
from pytube import YouTube
from flask import flash


def info_video(url):
    '''obtinene la descripción general del link como
       título, duración... Además, la información
       de video y audio para descargar'''
    yt = YouTube(url)

    # DESCRIPCIÓN
    title = yt.title
    autor = yt.author
    duration = str(datetime.timedelta(seconds=yt.length))
    info = [title, autor, duration]

    # AUDIO
    audio = yt.streams.filter(only_audio=True).order_by("abr").desc().all()
    list_audio = []
    for i in audio[:5]:
        list_items = [
                i.itag, 
                i.type, 
                i.abr, 
                round((i.filesize / 1048576), 2), 
                i.mime_type
            ]
        list_audio.append(list_items)

    # VIDEO
    video = (
        yt.streams.filter(adaptive=True, subtype="mp4")
        .order_by("resolution")
        .desc()
        .all()
    )
    list_video = []

    for i in video[:5]:
        list_items = [
            i.itag,
            i.type,
            i.resolution,
            round((i.filesize / 1048576), 1),
            i.mime_type
        ]
        list_video.append(list_items)

    # MATRIZ DE LA INFORMACIÓN DEL VIDEO
    infor_video = [list_video, list_audio, info, url]

    return infor_video


def download_video(url_short, itag, dirname):
    '''Para descargar el video o audio seleccionado'''

    def progress_function(stream, chunk, bytes_remaining):
        print(round((1 - bytes_remaining / stream.filesize) * 100, 2), "% listo...")

    def complete_func(stream, file_handle):
        print("file downloaded successfully !")
        flash(u"¡El archivo ha sido descargado con exito!", "success")

    url = "https://www.youtube.com/watch?v=" + url_short

    yt = YouTube(
        url,
        on_progress_callback=progress_function,
        on_complete_callback=complete_func,
    )

    stream = yt.streams.get_by_itag(itag)
    stream.download(dirname)
    return True
