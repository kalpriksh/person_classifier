from flask import Flask, request, jsonify, render_template, url_for, redirect
import util

app = Flask(__name__)

@app.route('/test2')
def test2():
  return 'hi'

@app.route('/classify_person', methods = ['GET', 'POST'])
def classify_person():
  image_data = request.form['image_data']
  
  response = jsonify(util.classify_image(image_data))
  response.headers.add('Access-Control-Allow-Origin', '*')
  
  return response

if __name__ == "__main__":
  util.load_saved_artifacts()
  print(util.test_fuction())
  app.run(port=5000)