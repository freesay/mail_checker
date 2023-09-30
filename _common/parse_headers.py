from pathlib import Path
import re


def _get_data_headers():
    root_path = Path(__file__).parents[1]
    file_path = Path(root_path, 'resources', 'res_headers.txt')
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data = f.read()
    return data


def received_path_data():
    received_data = []
    received_text = ''
    for el in _get_data_headers().split('\n'):
        if 'Received' in el:
            received_data.append(el)
    received_data.reverse()
    for el in received_data[-3:]:
        for hop in el.split('\t\t\t')[1].split(';'):
            if 'from' in hop:
                received_text += f"From:\t\t\t{hop.strip(' ').split(' ')[1]}\n"
            if 'by' in hop:
                received_text += f"By:\t\t\t{hop.strip(' ').split(' ')[1]}\n"
    return received_text + '-'*100 + '\n'


def return_path_data():
    return_path_text = ''
    for el in _get_data_headers().split('\n'):
        if 'From' == el.split('\t\t\t')[0]:
            return_path_text += 'From:' + '\t\t\t' + re.findall('\<.+\>', el.split('\t\t\t')[1])[0].strip('<>') + '\n'
        if 'Return-Path' == el.split('\t\t\t')[0]:
            return_path_text += 'Return-Path:' + '\t\t\t' + el.split('\t\t\t')[1] + '\n'
        if 'To' == el.split('\t\t\t')[0]:
            try:
                return_path_text += 'To:' + '\t\t\t' + re.findall('\<.+\>', el.split('\t\t\t')[1])[0].strip('<>') + '\n'
            except:
                return_path_text += 'To:' + '\t\t\t' + el.split('\t\t\t')[1] + '\n'
        if 'CC' == el.split('\t\t\t')[0]:
            return_path_text += 'CC:' + '\t\t\t' + re.findall('\<.+\>', el.split('\t\t\t')[1])[0].strip('<>') + '\n'
    return return_path_text + '-'*100 + '\n'


def signatures_data():
    auth_data = {}
    auth_text = ''
    for el in _get_data_headers().split('\n'):
        if 'authentication' in el.split('\t\t\t')[0].lower():
            auth_data[el.split('\t\t\t')[0].strip('\t\t\t')] = el.split('\t\t\t')[1].lstrip('\t\t\t')
        if 'dkim' in el.split('\t\t\t')[0].lower():
            auth_data[el.split('\t\t\t')[0].strip('\t\t\t')] = el.split('\t\t\t')[1].lstrip('\t\t\t')
        if 'spf' in el.split('\t\t\t')[0].lower():
            auth_data[el.split('\t\t\t')[0].strip('\t\t\t')] = el.split('\t\t\t')[1].lstrip('\t\t\t')
        if 'dmark' in el.split('\t\t\t')[0].lower():
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
    return auth_text + '-'*100 + '\n'


def spam_data():
    spam_tag = {}
    spam_tag_text = ''
    for el in _get_data_headers().split('\n'):
        if 'spam' in el.split('\t\t\t')[0].lower():
            spam_tag[el.split('\t\t\t')[0].strip('\t\t\t')] = el.split('\t\t\t')[1].lstrip('\t\t\t')
    if spam_tag:
        for el, val in spam_tag.items():
            spam_tag_text += el + ':' + '\n'
            for v in val.split(';'):
                if v == '':
                    spam_tag_text += '\t\t\t- None \n'
                else:
                    spam_tag_text += '\t\t\t- ' + v.strip(' ;') + '\n'
    return spam_tag_text


def global_result():
    received_data = received_path_data()
    path_data = return_path_data()
    signatures = signatures_data()
    spam = spam_data()
    res = f'{received_data}\n' \
          f'{path_data}\n' \
          f'{signatures}\n' \
          f'{spam}\n'
    # root_path = Path(__file__).parents[1]
    # file_path = Path(root_path, 'resources', 'parse_headers.txt')
    # with open(file_path, 'w', encoding='utf-8-sig') as f:
    #     f.write(res)
    return res
