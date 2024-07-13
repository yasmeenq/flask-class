from pathlib import Path 
from flask import current_app 
from uuid import uuid4 
class ImageHandler:

    @staticmethod
    def save_image(image): 
        suffix = Path(image.filename).suffix # suffix of a.png is png. suffix of h.jpeg is jpeg 
        image_name = str(uuid4()) + suffix # create unique name 
        image_path = ImageHandler.get_image_path(image_name) # static/images/122323-323wedwewe--32323-wewe.png 
        image.save(image_path) # save the image on the server side on static/images/122323-323wedwewe--32323-wewe.png
        return image_name # return the name because i want to save it on db

    @staticmethod
    def get_image_path(image_name):
        image_path = Path(current_app.root_path) / "static/images" / image_name
        return image_path