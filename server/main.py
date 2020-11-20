from flask import Flask, request

from enums.errors_types import FileUploadErrors
from enums.status_codes import SuccessStatusCodes, ServerErrorStatusCodes

app = Flask(__name__)


# settings CORS policy
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


@app.route('/api/uploadFile', methods=['POST'])
def upload_file():
    file = request.files.get('uploadedUserFile')

    if file is None:
        return _generate_server_error(FileUploadErrors.file_not_found)

    if file.mimetype == 'text/plain':
        data = file.read()
        return {'result': 'success'}, SuccessStatusCodes.ok
    else:
        return _generate_server_error(FileUploadErrors.incorrect_file_extension)


def _generate_server_error(error_type):
    return {'errorType': error_type}, ServerErrorStatusCodes.internal_server_error


if __name__ == "__main__":
    app.run(port=3000)
