from flask import Flask, render_template, request, send_from_directory

# FLASK SETUP
app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return render_template('test.html')





@app.route('/js/<path:path>')
def send_js(path): 
    return send_from_directory('js', path)

@app.route('/textures/<path:path>')
def send_textures(path): 
    return send_from_directory('textures', path)

@app.route('/models/<path:path>')
def send_models(path): 
    return send_from_directory('models', path)

@app.route('/build/<path:path>')
def send_build(path): 
    return send_from_directory('build', path)

if __name__ == "__main__":
    # Only for debugging while developing
    # app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT'))
    app.run(host='0.0.0.0', debug=False, port=5000)
