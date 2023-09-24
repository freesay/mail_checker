import os
import base64
import quopri
import re


def get_file_name():
    content = os.listdir()
    eml_files = []
    for el in content:
        if 'eml' in el:
            eml_files.append(el)
    if len(eml_files) > 1:
        print("В папке находятся несколько EML файлов. Оставьте только один.")
    else:
        print(f'\n\nEML file: {eml_files[0]}')
        return eml_files[0]


def get_all_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        all_data = file.read()
        return all_data


def get_decode_data(all_data):
    chunks = all_data.split('\n\n--')
    encode_set = {}
    all_decode_data = []
    for chunk in chunks:
        for string in chunk.split('\n'):
            if string.startswith('Content-Type:'):
                content_type = string.split(':')[1].split(';')[0]
                charset = string.split('=')[-1]
                encode_set['Content-Type'] = content_type
                encode_set['charset'] = charset.strip('"')
            if string.startswith('Content-Transfer-Encoding:'):
                encode_set['Encoding'] = string.split(': ')[-1]
        if 'text' in encode_set['Content-Type']:
            if encode_set['Encoding'] == 'quoted-printable':
                all_decode_data.append(quopri.decodestring(chunk).decode(f'{encode_set["charset"]}', errors='ignore'))
            if encode_set['Encoding'] == 'base64':
                all_decode_data.append(base64.b64decode(chunk).decode(f'{encode_set["charset"]}', errors='ignore'))
        else:
            all_decode_data.append(chunk)
    return all_decode_data


def create_file_decode_data(decode_data):
    with open('temp.txt', 'w', encoding='utf-8-sig') as file:
        for el in decode_data:
            file.write(el + '\n')


def create_collection_urls(decode_data):
    with open('urls.txt', 'w', encoding='utf-8-sig') as file:
        for chunk in decode_data:
            for string in chunk.split('\n'):
                res = re.findall('https?://[^\s\<\>\"\']+', string)
                for el in res:
                    file.write(el + '\n')


def get_clear_html_data():
    with open('temp.txt', 'r', encoding='utf-8-sig') as file:
        delete_scripts = re.sub('<script.*?>(.*?)</script>', "", file.read(), flags=re.DOTALL)
        clear_scripts = re.sub('javascript:.\w+', "", delete_scripts, flags=re.DOTALL)
        data = clear_scripts.split('\n')
        html_data = []
        clear_html_data = []
        for string in data:
            if '<html' in string:
                html_data += data[data.index(string):]
            if '</html>' in string:
                html_data = html_data[:html_data.index(string) + 1]
                break
        for string in html_data:
            clear_html_data.append(re.sub('https?://[^\s\<\>\"\']+', "", string))
        return clear_html_data


def create_clear_html(clear_html_data):
    with open('example.html', 'w', encoding='utf-8-sig') as file:
        for string in clear_html_data:
            file.write(string + '\n')


def get_routes_mail(all_data):
    routes = all_data.split('\n\n')[0].split('\n')
    tags = []
    for i in range(len(routes)):
        if 'Received' in routes[i] and routes[i + 2].startswith("\t"):
            tags.append(f'{routes[i]} \n\t\t{routes[i + 1]} \n\t\t{routes[i + 2]}')
    print(f'\n\n{"-" * 100}\n\n')
    for tag in list(reversed(tags)):
        print(tag)


def get_x_tags(all_data):
    x_tags = all_data.split('\n\n')[0].split('\n')
    tags = []
    for tag in x_tags:
        if 'X-' in tag or 'Authentication' in tag or 'DKIM' in tag:
            tags.append(tag)
    print(f'\n\n{"-" * 100}\n\n')
    for tag in sorted(tags):
        print(tag)


def get_path_data(all_data):
    seq = all_data.split('\n\n')[0].split('\n')
    path_data = []
    for string in seq:
        if "Return-Path" in string:
            path_data.append(string)
        if "From" in string.split(':') or 'To:' in string or "CC:" in string:
            path = re.findall('\<.+\>', string)
            if path:
                path_data.append(string.split(':')[0] + ': ' + path[0].strip('<>'))
    print(f'\n\n{"-" * 100}\n\n')
    for path in path_data:
        print(path)


def get_collection_urls():
    print(f'\n\n{"-" * 100}\n\n')
    with open('urls.txt', 'r', encoding='utf-8-sig') as file:
        for line in file.read().split('\n'):
            print(line)


if __name__ == '__main__':
    eml_file = get_file_name()
    all_data = get_all_data(eml_file)
    decode_data = get_decode_data(all_data)
    create_file_decode_data(decode_data)
    create_collection_urls(decode_data)
    clear_html_data = get_clear_html_data()
    create_clear_html(clear_html_data)
    get_routes_mail(all_data)
    get_x_tags(all_data)
    get_path_data(all_data)
    get_collection_urls()
