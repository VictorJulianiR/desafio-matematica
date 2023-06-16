from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/getNumberOfChallenges')
def get_number_of_challenges():
    path = "./desafios"
    return str(len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]))

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

@app.route('/get_challange_image/<int:challange_id>')
def get_challange_image(challange_id):
    return send_from_directory('desafios', f'{challange_id}.jpg')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
