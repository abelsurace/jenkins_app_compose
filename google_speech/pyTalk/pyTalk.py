from google_speech import Speech
from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/say/', methods = ['POST'])
def say():
    lang = 'en'
    if request.method == 'POST':
            text = request.args.get('text')
            lang = request.args.get('lang')
            speech = Speech(text, lang)
            speech.play()
            return "pyTalk said {}!".format(text)
    else:
         return "pyTalk say works only on POST"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5600)