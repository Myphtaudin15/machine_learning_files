from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/fake')
def hello():
    return "Fake News Label. NOW!!!"


@app.route('/predict_fake', methods=['POST'])
def predict_fake():
    title = request.form['title']
    author = request.form['author']

    label = util.is_fake(title, author)
    label = label.tolist() # Convert ndarray to a list
    response = jsonify({
        'label': label[0]
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting python Flask Server For Titanic Survival Prediction")
    util.load_saved_artifacts()
    app.run(debug=True)