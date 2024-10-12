import os

os.makedirs('api/data', exist_ok=True)

class CredentialConfig:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

class ContentConfig:
    WIDTH = 1080
    HEIGHT = 1920
    
class URLConfig:    
    POLLINATION_URL = 'https://pollinations.ai/p/'
