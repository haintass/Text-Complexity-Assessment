from flask import Flask, request

app = Flask(__name__)


# settings cors policy
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


@app.route('/api/uploadFile', methods=['POST'])
def upload_file():
    file = request.files['file']

    if file.mimetype == 'text/plain':
        data = file.read()
        return {'result': 'success'}, 200
    else:
        return _return_error('errors.incorrectFileExtension', 500)


def _return_error(error_type, status_code):
    return {'errorType': error_type}, status_code


if __name__ == "__main__":
    app.run(port=3000)
