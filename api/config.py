import os

os.makedirs('api/data', exist_ok=True)

class CredentialConfig:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

class ContentConfig:
    WIDTH = 1080
    HEIGHT = 1920
    TMP_DIR = os.getenv('TMP_DIR', '')
    
class URLConfig:    
    TREND_URL = 'https://trends.google.com/trends/api/dailytrends'
    POLLINATION_URL = 'https://pollinations.ai/p'