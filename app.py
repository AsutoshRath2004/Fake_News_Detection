from flask import Flask,request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

vector = TfidfVectorizer(stop_words='english',max_df=0.7)
model = pickle.load(open("finalized_model.pkl",'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/prediction",methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        news = request.form['news']
        print(news)
        predict = model.predict(vector.transform([news]))
        print(predict)
        return render_template("index.html", prediction_text="News headline is -> {}".format(predict))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()