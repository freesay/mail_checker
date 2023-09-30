import os
from pathlib import Path
from _common import parse_headers
from _common import parser
from _common import generators as gen


def _get_data(file):
    try:
        root_path = Path(__file__).parents[1]
        file_path = Path(root_path, file)
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            data = f.read()
        return data
    except:
        return 'There is no data of this type.\n'


def _create_dirs():
    try:
        root_path = Path(__file__).parents[1]
        os.mkdir(Path(root_path, 'resources'))
        os.mkdir(Path(root_path, 'attaches'))
    except:
        pass


class Functions:
    def __init__(self, interface):
        self.interface = interface
        _create_dirs()

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
        os.system(fr'{attaches_folder}')

    def update_detect_text(self, detect_file):
        self.interface.detect_label.config(text=detect_file)

    def set_data_text_box(self, data):
        self.interface.text_box.configure(state='normal')
        self.interface.text_box.delete('1.0', 'end-1c')
        self.interface.text_box.insert('1.0', data)
        self.interface.text_box.configure(state='disabled')

    def get_convert_data(self):
        gen.clear_folders()
        parser.parse_content(self.raw_data)
        data = gen.get_folder_content()
        self.interface.create_files_widget(data)
        self.interface.create_open_html_widget()

    def set_parse_headers_tex_box(self):
        data = parse_headers.global_result()
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
        location_file = Path('resources', 'res_html.html')
        data = _get_data(location_file)
        self.set_data_text_box(data)

    def set_urls_tex_box(self):
        location_file = Path('resources', 'res_urls.txt')
        data = _get_data(location_file)
        self.set_data_text_box(data)
