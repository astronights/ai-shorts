from flask import current_app as app
import google.generativeai as genai

import os
from ast import literal_eval

genai.configure(api_key=os.environ['GEMINI_API_KEY'])
llm_model = genai.GenerativeModel('gemini-1.5-flash')

def get_text(prompt: str, json=True):

    text = llm_model.generate_content(prompt).text
    
    if json:
        json_text = text.lstrip('```json').strip('```')
        return literal_eval(json_text)

    return text