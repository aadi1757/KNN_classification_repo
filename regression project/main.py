from flask import Flask, render_template, request
from utils import Prediction

app = Flask(__name__)

@app.route("/")
def start():
    return render_template(r"KNN_regression_html.html")

@app.route('/predict', methods=["POST", "GET"])
def PREDICT_PRICE():
    data = request.form
    pred_obj = Prediction()
    predicted_price = pred_obj.Price(data)
    print(predicted_price)

    return str(predicted_price)


if __name__ == ("__main__"):
    app.run(host='127.0.0.1', port=5000, debug=True)