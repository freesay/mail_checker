import re
from pathlib import Path


def _get_data_headers():
    root_path = Path(__file__).parents[1]
    file_path = Path(root_path, 'resources', 'res_headers.txt')
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data = f.read()
    return data


def received_path_data(text_data):
    temp = text_data.split('\n')
    received_text = ''
    received_data = []
    for el in temp:
        if 'Received' in el:
            received_data.append(el.lstrip('Received'))
    received_data.reverse()
    day_of_weak = ['Mon,', 'Tue,', 'Wed,', 'Thu,', 'Fri,', 'Sat,', 'Sun,']
    for el in received_data:
        if 'from ' in el or 'from;' in el:
            el = el.replace('from ', '\nFrom: \t')
            el = el.replace('from;', '\nFrom: \t')
        if 'by ' in el or 'by;' in el:
            el = el.replace('by ', '\nBy: \t')
            el = el.replace('by;', '\nBy: \t')
        if 'for ' in el or 'for;' in el:
            el = el.replace('for ', '\nFor: \t')
            el = el.replace('for;', '\nFor: \t')
        for day in day_of_weak:
            if day in el:
                el = el.replace(day, f'\n\t{day}')
        received_text += f'{el.lstrip()}\n\n'
    return received_text


def return_path_data(text_data):
    return_path_text = ''

    def _collect_data(word):
        data = ''
        try:
            data += f'{word}:' + '\t\t\t' + re.findall('\<.+\>', el.split('\t\t\t')[1])[0].strip('<>') + '\n'
        except Exception as error:
            print('parse_headers, _collect_data:', error)
            data += f'{word}:' + '\t\t\t' + el.split('\t\t\t')[1] + '\n'
        return data

    for el in text_data.split('\n'):
        if 'From' == el.split('\t\t\t')[0]:
            return_path_text += _collect_data('From')
        if 'Return-Path' == el.split('\t\t\t')[0]:
            return_path_text += _collect_data('Return-Path')
        if 'To' == el.split('\t\t\t')[0]:
            return_path_text += _collect_data('To')
        if 'CC' == el.split('\t\t\t')[0]:
            return_path_text += _collect_data('CC')
    return return_path_text


def signatures_data(text_data):
    auth_data = {}
    auth_text = ''
    for el in text_data.split('\n'):
        string = el.split('\t\t\t')[0].lower()
        if 'authentication' in string or 'dkim' in string or 'spf' in string or 'dmark' in string:
            auth_data[el.split('\t\t\t')[0].strip('\t\t\t')] = el.split('\t\t\t')[1].lstrip('\t\t\t')
    if auth_data:
        for el, val in auth_data.items():
            auth_text += el + ':' + '\n'
            for v in val.split(';'):
                if v == '':
                    continue
                else:
                    auth_text += '\t\t\t- ' + v.strip(' ') + '\n'
            auth_text += '\n'
    else:
        auth_text += 'There is no data on signatures and policies.\n'
    return auth_text


def x_tags_data(text_data):
    spam_tag = {}
    x_tags_text = ''
    for el in text_data.split('\n'):
        if 'x-' in el.split('\t\t\t')[0].lower():
            spam_tag[el.split('\t\t\t')[0].strip('\t\t\t')] = el.split('\t\t\t')[1].lstrip('\t\t\t')
    if spam_tag:
        for el, val in spam_tag.items():
            x_tags_text += el + ':' + '\n'
            for v in val.split(';'):
                if v == '':
                    x_tags_text += '\t\t\t- None \n'
                else:
                    x_tags_text += '\t\t\t- ' + v.strip(' ;') + '\n'
    return x_tags_text


def global_result(text_data):
    received_data = received_path_data(text_data)
    path_data = return_path_data(text_data)
    signatures = signatures_data(text_data)
    spam = x_tags_data(text_data)
    split = '-' * 100 + '\n'
    res = f'{split}' \
          f'{received_data}{split}' \
          f'{path_data}{split}' \
          f'{signatures}{split}' \
          f'{spam}{split}'
    return res
