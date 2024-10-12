from .prompts import prompt

from flask import Blueprint, current_app as app
import requests

instagram = Blueprint('instagram', __name__)

@instagram.route('/daily', methods=['POST'])
def generate_daily():
    return 'To Be Implemented'
    

@instagram.route('/trend/<trend>', methods=['POST'])
def edit_caption(trend):

    
    url = f"{app.config['IG_GRAPH_API_URL']}/{media_id}"
    payload = {'caption': new_caption}
    params = {'access_token': access_token, 'comment_enabled': True}

    response = requests.post(url, params=params, data=payload)

    return response.json()
