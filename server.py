from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detection  # Import your Python package and module

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the emotion detector API
@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    # Get the 'textToAnalyze' parameter from the query string
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({"error": "textToAnalyze parameter is missing"}), 400

    # Call your function from the Python package
    try:
        # Assuming emotion_detector() returns a dictionary
        result = emotion_detection.emotion_detector(text_to_analyze)
        print("HIIII: ", result)
        # Return the result as JSON
        return result
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
