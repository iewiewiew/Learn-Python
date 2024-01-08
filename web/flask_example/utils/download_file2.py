from flask import Flask, render_template, send_file
import os

app = Flask(__name__)


@app.route('/')
def index():
    contents = get_contents(BASE_PATH)
    return render_template('download2.html', contents=contents, current_path='')


@app.route('/<path:dir_path>')
def show_directory(dir_path):
    full_path = os.path.join(BASE_PATH, dir_path)
    contents = get_contents(full_path)
    return render_template('download2.html', contents=contents, current_path=dir_path if dir_path else '')


@app.route('/download/<path:file_path>')
def download(file_path):
    full_path = os.path.join(BASE_PATH, file_path)
    return send_file(full_path, as_attachment=True)


def get_contents(base_path):
    contents = []
    for item in os.listdir(base_path):
        full_path = os.path.join(base_path, item)
        if os.path.isfile(full_path):
            contents.append({'type': 'file', 'name': item, 'path': item})
        elif os.path.isdir(full_path):
            contents.append({'type': 'directory', 'name': item, 'path': item})
    return contents


if __name__ == '__main__':
    BASE_PATH = '/Users/menghuawei/PycharmProjects/Learn-Python'
    app.run(debug=True)
