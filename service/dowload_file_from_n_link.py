import requests
import random
import string


class DowloaderFileService():
    def __init__(self, file_url:str) -> None:
        self.file_url = file_url


    def get_random_string(self,length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
    

    def download_file_from_n_link(self):
        r = requests.get(self.file_url, stream = True)
        if 'jpg' in self.file_url:
            name = str(self.get_random_string(6)) + ".jpg"
        elif 'png' in self.file_url:
            name = str(self.get_random_string(6)) + ".png"
        elif 'webp' in self.file_url:
            name = str(self.get_random_string(6)) + ".webp"    
        elif 'jpeg' in self.file_url:
            name = str(self.get_random_string(6)) + ".jpeg"
        else:
            name = str(self.get_random_string(6)) + ".bin"
        with open(name, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        
        with open(name, "rb") as f:
            blob = f.read()
            
        return blob
                    

