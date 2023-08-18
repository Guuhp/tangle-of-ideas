from flask import Flask
from routers.dowload_file_from_n_link_router import downloader_file

app = Flask(__name__)

app.register_blueprint(downloader_file)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)