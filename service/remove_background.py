from rembg import remove

class RemoveBackgroundService():
    def __init__(self, image) -> None:
        self.image = image

    def remove_backgroud(self):
        image = remove(self.image)
        image.save("static/temp/output.png")
        return "success"