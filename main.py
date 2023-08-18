from flask import Flask
from routers.dowload_file_from_n_link_router import downloader_file
from routers.remove_background import remove_background

app = Flask(__name__)

app.register_blueprint(downloader_file)
app.register_blueprint(remove_background)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)