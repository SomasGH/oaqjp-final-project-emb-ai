from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Application")
@app.route("/emotionDetector")
def emotion_detectors():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    rstmt = "For the given statement, the system response is "
    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again"
    for i in response:
        if i != 'dominant_emotion' and i != 'sadness':
            rstmt = f"{rstmt} '{i}' : {response[i]},"
        elif i == 'sadness':
            rstmt = f"{rstmt} and '{i}' : {response[i]}"
    rstmt = f"{rstmt}. The dominant emotion is {response['dominant_emotion']}."    
    return rstmt
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel'''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000'''
    app.run(host="0.0.0.0", port=5004)