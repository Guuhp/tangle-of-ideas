from flask import Blueprint, request
from service.remove_background import RemoveBackgroundService 
from PIL import Image
import io


remove_background = Blueprint('remove_background/',
                        __name__,
                        template_folder='../templates',
                        static_folder='../static',
                        url_prefix='/remove_background')

@remove_background.route("/get_image")
def get_image():
    image =  request.files['image']
    image = Image.open(io.BytesIO(image.stream.read()))
    image = RemoveBackgroundService(image).remove_backgroud()
    return "success" 