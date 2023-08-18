from service.dowload_file_from_n_link import DowloaderFileService
from flask import Blueprint, send_file

downloader_file = Blueprint('downloader_file/',
                        __name__,
                        template_folder='../templates',
                        static_folder='../static',
                        url_prefix='/downloader_file')

@downloader_file.route("/get_file")
def get_file():
    file_url = "https://ciclovivo.com.br/wp-content/uploads/2018/10/iStock-536613027-1024x683.jpg"
    file = DowloaderFileService(file_url).download_file_from_n_link()
    return send_file(file, as_attachment=True)