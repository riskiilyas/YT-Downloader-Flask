from flask import Flask, send_file, render_template, request
import pytube
import glob
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/download", methods=['POST'])
def download():
    try:
        old_files = glob.glob('*.mp4')
        for i in range(len(old_files)):
            os.remove(old_files[i])

        vid_url = request.form['vid_url']
        yt = pytube.YouTube(vid_url)
        yt.streams.get_highest_resolution().download()
        mp4_files = glob.glob('*.mp4')
        if mp4_files:
            mp4_filename = mp4_files[0]
            return send_file(mp4_filename, as_attachment=True)
        return "ERROR! PLEASE TRY AGAIN!"
    except Exception as e:
        return "ERROR! PLEASE TRY AGAIN!"


if __name__ == "__main__":
    app.run()
