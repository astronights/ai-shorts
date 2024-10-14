from .prompts import prompt
from .trends import get_searches
from .llm import get_text
from .media import download_image

import os
from uuid import uuid4

from flask import Blueprint, request, current_app as app

instagram = Blueprint('instagram', __name__)

@instagram.route('/daily', methods=['POST'])
def generate_daily():
    trend_url = app.config['TREND_URL']
    topics = get_searches(trend_url)
    
    for topic in topics:
        llm_prompt = prompt.format(topic=topic, country='worldwide')
        prompts = get_text(llm_prompt)

        return prompts
    

@instagram.route('/trend/<trend>', methods=['POST'])
def get_trend(trend):

    w, h = app.config['WIDTH'], app.config['HEIGHT']
    IMAGE_URI = app.config['POLLINATION_URL'] + '/{prompt}' + f'?width={w}&height={h}&seed=42'
    SAVE_DIR = app.config['TMP_DIR']

    topic = trend.split('_')

    llm_prompt = prompt.format(topic=topic, country='worldwide')
    prompts = get_text(llm_prompt)

    video_descs = [e['description'] for e in prompts['video']]

    medias = []
    for i, desc in enumerate(video_descs):
        key = f'video_{i}_{uuid4()}'
        path = download_image(desc, key, IMAGE_URI, SAVE_DIR)
        medias.append(f'{request.host_url}serving/image/{os.path.basename(path)}')

    return {'text': prompts, 'images': medias}
