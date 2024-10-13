import os 
import glob

def cleanup():
    TMP_DIR = os.getenv('TMP_DIR', '')

    patterns = ['*.jpg', '*.mp3']
    deleted_files = {}

    for pattern in patterns:
        search_pattern = os.path.join(TMP_DIR, pattern)
        files_to_delete = glob.glob(search_pattern)
        deleted_files[pattern[2:]] = len(files_to_delete)
        
        for file_path in files_to_delete:
            os.remove(file_path)
            print(f"Deleted: {file_path}")

    return deleted_files