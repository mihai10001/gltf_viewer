import sys
from os import environ
from os import listdir
from os.path import isdir, isfile, join
from flask import Flask, render_template, request, send_from_directory

# FLASK SETUP
app = Flask(__name__, static_url_path='')
default_selected_model = 'Duck'
default_selected_map = 'venice_sunset_2k.hdr'

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
    global default_selected_model, default_selected_map

    if request.method == 'POST':
        default_selected_model = request.form.get('model_select', default_selected_model)
        default_selected_map = request.form.get('map_select', default_selected_map)

    model_dir_path = models_path + '/' + default_selected_model + '/glTF/'
    model_path = default_selected_model + '.gltf'
    map_dir_path = maps_path + '/' 
    map_path = default_selected_map

    return render_template('home.html',
                           model_dir_path=model_dir_path,
                           model_file_path=model_path,
                           map_dir_path=map_dir_path,
                           map_file_path=map_path,
                           all_models=all_models,
                           all_maps=all_maps,
                           sel_model=default_selected_model,
                           sel_map=default_selected_map)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=environ.get('PORT'))
