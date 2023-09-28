from pathlib import Path
from _common import parser
from _common import generators as gen


def _get_data(file):
    root_path = Path(__file__).parents[1]
    file_path = Path(root_path, file)
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data = f.read()
    return data


class Functions:
    def __init__(self, interface):
        self.interface = interface

    def open_file(self):
        file = self.interface.file_dialog()
        self.data = parser.get_raw_data(file)
        self.set_data_text_box(self.data)
        self.update_detect_text(f'Open file: {file}')

    def update_detect_text(self, detect_text):
        self.interface.detect_label.config(text=detect_text)

    def set_data_text_box(self, data):
        self.interface.text_box.configure(state='normal')
        self.interface.text_box.delete('1.0', 'end-1c')
        self.interface.text_box.insert('1.0', data)
        self.interface.text_box.configure(state='disabled')

    def get_convert_data(self):
        gen.clear_folders()
        parser.parse_content(self.data)
        data = gen.get_folder_content()
        self.update_detect_text(f'Attached files were found in the email: {data}')

    def set_headers_tex_box(self):
        location_file = Path('resources', 'res_headers.txt')
        try:
            data = _get_data(location_file)
            self.set_data_text_box(data)
        except:
            self.update_detect_text('There is no content of this type')

    def set_plain_tex_box(self):
        location_file = Path('resources', 'res_plain.txt')
        try:
            data = _get_data(location_file)
            self.set_data_text_box(data)
        except:
            self.update_detect_text('There is no content of this type')


    def set_html_tex_box(self):
        location_file = Path('resources', 'res_html.html')
        try:
            data = _get_data(location_file)
            self.set_data_text_box(data)
        except:
            self.update_detect_text('There is no content of this type')

    def set_urls_tex_box(self):
        location_file = Path('resources', 'res_urls.txt')
        try:
            data = _get_data(location_file)
            self.set_data_text_box(data)
        except:
            self.update_detect_text('There is no content of this type')
