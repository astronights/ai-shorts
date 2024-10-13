import os
from flask import Blueprint, current_app as app, send_from_directory

serving = Blueprint('serving', __name__)

@serving.route('/image/<img>', methods=['GET'])
def get_image(img):

    IMAGE_DIR = os.path.join(app.root_path, '..', app.config['TMP_DIR'])
    print(IMAGE_DIR, img)

    return send_from_directory(IMAGE_DIR, img)