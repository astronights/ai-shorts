import os
import requests 

def download_image(description, key, uri_template, output_dir='.'):
    '''
    Downloads image based on the list of prompts and saves them to disk.
    '''
    
    img_url = uri_template.format(prompt=description)
    
    res_img = requests.get(img_url)
        
    img_name = f"{key}.jpg"
    img_path = os.path.join(output_dir, img_name)
        
    with open(img_path, 'wb') as file:
        file.write(res_img.content)
        
    return img_path