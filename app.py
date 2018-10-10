from flask import Flask, url_for, send_from_directory, request
from flask import render_template
import logging, os
from werkzeug import secure_filename
from summarizer import summarize
from entity_extracter import entity_extractor
from extract_text import get_text_from_url

app = Flask(__name__, static_url_path='/public')

@app.route('/summarised', methods = ['POST'])
def summerised():
    # Get URL from browser and shared Summaried on it.
	if request.method == 'POST':
		news_url = request.form['news_url']
		# send text to detact Summary from given URL
		article = get_text_from_url(news_url)

		summaried_text = summarize(article)
		# find the entity from summaried text
		entities = entity_extractor(summaried_text)

		return render_template('index.html', summaried_text = summaried_text, entities=entities)
	else:
		return "Where is the image?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('public/js', path)

@app.route('/bootstrap/<path:path>')
def send_bootstrap(path):
    return send_from_directory('public/bootstrap', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('public/css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('public/img', path)

@app.route('/images/<path:path>')
def send_imageg(path):
    return send_from_directory('images', path)

if __name__ == '__main__':
	app.run(debug=False,host='0.0.0.0', port=8080)