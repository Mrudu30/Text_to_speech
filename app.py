from flask import Flask,render_template,request,jsonify, send_file
import pyttsx3, os

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        print(request.form['inputText'])
        text = request.form['inputText']
        voice = int(request.form['voice'])
        rate = int(request.form['rate'])
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', rate)
        engine.setProperty('voice', voices[voice].id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        return render_template('index.html')
    return render_template('index.html')

@app.route('/download',methods=['POST'])
def speech_download():
    if request.method == 'POST':
        text = request.form['inputText']
        voice = int(request.form['voice'])
        rate = int(request.form['rate'])
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', rate)
        engine.setProperty('voice', voices[voice].id)

        try:
            engine.save_to_file(text,'Speech Output.mp3')
            return jsonify({'outcome':'success', 'download_url': '/download_file'})
        except Exception as e:
            print(e)
            return jsonify({'outcome':'failure'})
        finally:
            engine.runAndWait()
            engine.stop()

@app.route('/download_file')
def download_file():
    file_path = 'Speech Output.mp3'
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({'outcome': 'failure', 'message': 'File not found'})

if __name__ == '__main__':
    app.run(port=5000,debug=True)