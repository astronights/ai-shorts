import requests
from ast import literal_eval

def get_searches(url, geo='US', tz=0):
    '''
    Fetch trending searches from Google Trends.
    
    Parameters:
        url (str): Trends URL
        geo (str): The geographical region code (e.g., 'US', 'GB').
        tz (int): Timezone offset in hours from UTC (0 means today).
    
    Returns:
        dict: A dictionary with trending searches, traffic, articles, and related queries.
    '''

    params = {
        'hl': 'en-US',
        'tz': tz,
        'geo': geo
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data, status code: {response.status_code}")
    
    # Parse the response to extract the JSON content
    json_data = literal_eval(response.text[5:])  # Skip the first 5 characters ')]}\''

    # Extract the relevant day's trending searches, adjusted for the time offset
    searches_data = json_data['default']['trendingSearchesDays'][0]['trendingSearches']

    # Organize the data in a structured dictionary
    results = {}
    for search in searches_data:
        key = search['title']['query']
        results[key] = {
            'traffic': search['formattedTraffic'],
            'articles': [{'title': article['title'], 'time_ago': article['timeAgo'], 
                          'snippet': article['snippet']}
                         for article in search['articles']],
            'related_queries': [related['query'] for related in search['relatedQueries']]
        }

    return results