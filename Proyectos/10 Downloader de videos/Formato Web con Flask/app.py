# Importación de los módulos necesarios, ejecutar servidor en la terminal con Flask run
from flask import Flask, request, render_template, redirect, url_for
from pytube import YouTube
from pathlib import Path
import os
import re

# Creación de la aplicación Flask
app = Flask(__name__)

# Ruta para la página principal, redirige a la página de descarga de video
@app.route("/")
def index():
    return redirect(url_for('downloadVideo'))

# Ruta para la descarga del video
@app.route("/download", methods=["GET","POST"])
def downloadVideo():      
    message = ''
    errorType = 0
    # Verificación si la solicitud es de tipo POST y si 'video_url' está en el formulario
    if request.method == 'POST' and 'video_url' in request.form: 
        youtubeUrl = request.form["video_url"]
          # Verificación de si se proporcionó una URL de video
        if youtubeUrl:
            # Expresión regular para validar la URL de YouTube
            validateVideoUrl = (
                r'(https?://)?(www\.)?'
                '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
            )
            validVideoUrl = re.match(validateVideoUrl, youtubeUrl)
            if validVideoUrl:
                try:
                    # Descarga del video utilizando la biblioteca pytube
                    url = YouTube(youtubeUrl)
                    video = url.streams.filter(progressive=True).order_by('resolution').desc().first()
                    downloadFolder = os.path.join(Path.home(), "Downloads")
                    video.download(downloadFolder)
                    message = 'Video Downloaded Successfully!'
                    errorType = 1
                # Captura de excepciones en caso de error durante la descarga del video
                except Exception as e:
                    message = f'Error downloading video: {str(e)}'
                    errorType = 1
            else:
                message = 'Enter Valid YouTube Video URL!'
                errorType = 1
        else:
            message = 'Enter YouTube Video Url.'
            errorType = 1           
    return render_template('youtube.html', message=message, errorType=errorType) 

# Se ejecuta la aplicación si este script es ejecutado directamente
if __name__ == "__main__":
    app.run()
