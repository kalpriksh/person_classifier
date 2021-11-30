from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello')
def hello():
  return 'hi'

@app.route('/classify_person', methods = ['GET', 'POST'])
def classify_person():
  return "hi"

if __name__ == "__main__":
  app.run(port=5000)