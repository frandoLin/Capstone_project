from flask import Flask, render_template, request, jsonify
from tweet_store import TweetStore

app = Flask(__name__)
store = TweetStore()

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/tweets', methods=['POST'])
def process():

    name = request.form['name']

    if name:
    
        tweets = store.tweets()

        return render_template('tweets.html', tweets=tweets)

if __name__ == '__main__':
    app.run(debug=True)