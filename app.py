from flask import Flask,render_template,request
import pyttsx3

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

if __name__ == '__main__':
    app.run(port=5000,debug=True)