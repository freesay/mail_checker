import os
import re
from pathlib import Path


def get_path(path, file):
    root_path = Path(__file__).parents[1]
    return Path(root_path, path, file)


def create_dirs():
    try:
        root_path = Path(__file__).parents[1]
        os.mkdir(Path(root_path, 'resources'))
        os.mkdir(Path(root_path, 'attaches'))
    except Exception as error:
        print('generators, create_dirs:', error)


def get_folder_content():
    root_path = Path(__file__).parents[1]
    attaches_path = Path(root_path, 'attaches')
    res_path = Path(root_path, 'resources')
    attaches = []
    resources = []
    for el in os.listdir(attaches_path):
        attaches.append(el)
    for el in os.listdir(res_path):
        resources.append(el)
    return attaches, resources


def clear_folders():
    root_path = Path(__file__).parents[1]
    dirs = [Path(root_path, 'resources'), Path(root_path, 'attaches')]
    for d in dirs:
        for file in os.listdir(d):
            os.remove(Path(d, str(file)))


def generate_temp_eml(raw_data):
    location_file = get_path('resources', 'temp.eml')
    with open(location_file, 'wb') as f:
        raw_data_as_byte = raw_data.encode()
        f.write(raw_data_as_byte)
    return location_file


def generate_file_headers(headers_data):
    location_file = get_path('resources', 'res_headers.txt')
    with open(location_file, 'w', encoding='utf-8-sig') as f:
        for el in headers_data:
            f.writelines(el + '\n')


def generate_file_plain(plain_data, charset):
    location_file = get_path('resources', 'res_plain.txt')
    with open(location_file, 'w', encoding=charset) as f:
        f.write(plain_data)


def generate_file_html(html_data, charset):
    location_file = get_path('resources', 'res_html.txt')
    with open(location_file, 'w', encoding=charset) as f:
        f.write(html_data)


def generate_file_attach(file_name, file_data):
    location_file = get_path('attaches', file_name)
    with open(location_file, 'wb') as f:
        f.write(file_data)


def generate_file_urls(html_data):
    location_file = get_path('resources', 'res_urls.txt')
    with open(location_file, 'w') as f:
        for string in html_data.split('\n'):
            res = re.findall('https?://[^\s<>\"\']+', string)
            for el in res:
                f.write(el + '\n')


def generate_clear_html(html_data, charset):
    location_file = get_path('resources', 'clear_html.html')
    html_data = re.sub('<script.*?>(.*?)</script>', 'SCRIPT_DELETED', html_data, flags=re.DOTALL)
    html_data = re.sub('javascript:.\w+', 'SCRIPT_DELETED', html_data, flags=re.DOTALL)
    html_data = re.sub('https?://[^\s<>\"\']+', 'URL_DELETED', html_data, flags=re.DOTALL)
    with open(location_file, 'w', encoding=charset) as f:
        f.write(html_data)
