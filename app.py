from flask import Flask,render_template,request,jsonify, send_file
import pyttsx3, os, random

app=Flask(__name__)

# home page
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # print(request.form['inputText'])
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

# sample file handlers
@app.route('/sample_file',methods=['GET', 'POST'])
def sampleFileHandler():
    if request.method == 'POST':
        file_number = random.choice([1,2,3,4,5])
        file_name = "static/samples/"+str(file_number)+".txt"
        with open(file_name,"r") as file_text:
            return jsonify({"file_name": file_name, "file_text": file_text.read()})

# download url section
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