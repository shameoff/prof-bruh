import os
import uuid
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

RESULT_DIR = 'result'
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "ProfBuh2023 API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/render')
def render():
    filename = uuid.uuid4()
    temp_file = os.path.join(RESULT_DIR, f'{filename}.temp')
    with open(temp_file, 'w') as f:
        f.write(str(filename))
    return jsonify({
        'status': 'rendering',
        'filename': filename
    })


@app.route('/check/<file_id>')
def check(file_id: uuid):
    temp_file = os.path.join(RESULT_DIR, f'{file_id}.temp')
    if os.path.exists(temp_file):
        return jsonify({'status': 'waiting',
                        'filename': file_id, })
    else:
        result_file = os.path.join(RESULT_DIR, f'{file_id}.txt')
        with open(result_file, 'r') as f:
            result = f.read()
            return jsonify({'status': 'done',
                            'content': result,
                            'filename': file_id, })


if __name__ == '__main__':
    app.run()
