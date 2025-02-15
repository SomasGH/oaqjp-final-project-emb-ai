''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5004.
'''
# Import Flask, render_template, request methods from flask
from flask import Flask, render_template, request

# Import emotion_detector from the package EmotionDetection
from EmotionDetection.emotion_detection import emotion_detector

#Initialize the Application
app = Flask("Emotion Detection Application")

@app.route("/emotionDetector")

def emotion_detectors():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the different emotions, the score
        and the dominant emotion based on the highest score.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Return a formatted string with the emotions and score
    rstmt = "For the given statement, the system response is "
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again"
    for emotion, score in response.items():
        if emotion not in ('dominant_emotion', 'sadness'):
            rstmt = f"{rstmt} '{emotion}' : {score},"
        elif emotion == 'sadness':
            rstmt = f"{rstmt} and '{emotion}' : {score}"
    rstmt = f"{rstmt}. The dominant emotion is {response['dominant_emotion']}."
    return rstmt

@app.route("/")

def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel'''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5004
    app.run(host="0.0.0.0", port=5004)
