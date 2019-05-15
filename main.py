import sys
from os import listdir
from os.path import isdir, isfile, join
from flask import Flask, render_template, request, send_from_directory

# FLASK SETUP
app = Flask(__name__, static_url_path='')


def models(path):
    all_models = [f for f in listdir(path) if isdir(join(path, f))]
    return all_models


def maps(path):
    all_maps = [f for f in listdir(path) if isfile(join(path, f))]
    return all_maps


@app.route('/', methods=['GET', 'POST'])
def home():

    models_path = 'js/models/gltf'
    maps_path = 'js/textures/equirectangular'
    all_models = models(models_path)
    all_maps = maps(maps_path)

    if request.method == 'POST':
        selected_model = request.form.get('model_select')
        model_dir_path = models_path + '/' + selected_model + '/glTF/'
        model_path = selected_model + '.gltf'
    else:
        model_dir_path = models_path + '/' + 'Duck' + '/glTF/'
        model_path = 'Duck' + '.gltf'

    return render_template('test.html',
                           model_dir_path=model_dir_path,
                           model_file_path=model_path,
                           all_models=all_models,
                           all_maps=all_maps)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


if __name__ == "__main__":
    # Only for debugging while developing
    # app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT'))
    app.run(host='0.0.0.0', debug=False, port=5000)
