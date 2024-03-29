import os
import hashlib
from pathlib import Path
from _common import check_pdf
from _common import parser
from _common import parse_headers
from _common import generators as gen


def _get_data(file):
    try:
        root_path = Path(__file__).parents[1]
        file_path = Path(root_path, file)
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            data = f.read()
        return data
    except Exception as error:
        print('functions, _get_data:', error)
        return 'There is no data of this type.\n'


class Functions:
    def __init__(self, interface):
        self.interface = interface
        gen.create_dirs()
        gen.clear_folders()

    def open_file(self):
        self.file = self.interface.file_dialog()
        self.raw_data = parser.get_raw_data(self.file)
        self.set_data_text_box(self.raw_data)
        self.interface.frame_text_box.config(text=self.file)

    def open_folder(self):
        root_path = Path(__file__).parents[1]
        attaches_folder = (Path(root_path, 'attaches'))
        os.system(f'start {attaches_folder}')

    def open_clear_html(self):
        root_path = Path(__file__).parents[1]
        attaches_folder = str(Path(root_path, 'resources', 'clear_html.html'))
        os.system(f'{attaches_folder}')

    def get_data_text_box(self):
        data = self.interface.text_box.get("1.0", 'end-1c')
        return data

    def set_data_text_box(self, data):
        self.interface.text_box.delete('1.0', 'end-1c')
        self.interface.text_box.insert('1.0', data)

    def decode_base64(self):
        message = self.get_data_text_box()
        decode_message = parser.decode_b64(message)
        self.set_data_text_box(decode_message)

    def get_parse_data(self):
        gen.clear_folders()
        message = self.get_data_text_box()
        parser.parse_content(message)
        attaches = gen.get_folder_content()[0]
        resources = gen.get_folder_content()[1]
        self.interface.create_files_widget(attaches)
        self.interface.create_open_html_widget(resources)

    def set_parse_headers_tex_box(self):
        temp = parse_headers._get_data_headers()
        data = parse_headers.global_result(str(temp))
        self.set_data_text_box(data)

    def set_headers_tex_box(self):
        location_file = Path('resources', 'res_headers.txt')
        data = _get_data(location_file)
        self.set_data_text_box(data)

    def set_plain_tex_box(self):
        location_file = Path('resources', 'res_plain.txt')
        data = _get_data(location_file)
        self.set_data_text_box(data)

    def set_html_tex_box(self):
        location_file = Path('resources', 'res_html.txt')
        data = _get_data(location_file)
        self.set_data_text_box(data)

    def set_urls_tex_box(self):
        location_file = Path('resources', 'res_urls.txt')
        data = _get_data(location_file)
        if data:
            self.set_data_text_box(data)
        else:
            self.set_data_text_box('There is no data of this type.\n')

    def check_hash_sha256(self, file):
        root_path = Path(__file__).parents[1]
        attaches_path = Path(root_path, 'attaches')
        file_path = Path(attaches_path, file)
        hash_sha256 = hashlib.sha256(open(file_path, 'rb').read()).hexdigest()
        return hash_sha256

    def check_pdf_file(self, file):
        root_path = Path(__file__).parents[1]
        attaches_path = Path(root_path, 'attaches')
        file_path = Path(attaches_path, file)
        res_pdfid = check_pdf.get_report(str(file_path))
        self.set_data_text_box(res_pdfid)
        print(res_pdfid)

