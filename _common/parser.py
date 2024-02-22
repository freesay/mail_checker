import base64
import email
from email.header import decode_header
from _common import generators as gen


def decode_b64(data):
    decode_data = base64.b64decode(data)
    return decode_data


def get_raw_data(email_file):
    with open(email_file, 'r', errors='ignore') as email_file:
        message = email_file.read()
    return message


def parse_content(email_data):
    message = email.message_from_string(email_data)
    headers = []
    for name, value in email.message_from_string(email_data).items():
        val = ''
        for v in value:
            val += v.lstrip('\t').replace('\n', '; ')
        headers.append(f'{name}\t\t\t{val}')
    gen.generate_file_headers(headers)
    if message.is_multipart():
        for part in message.walk():
            get_content(part)
    else:
        get_content(message)


def get_content(msg):
    content_type = msg.get_content_type()
    if content_type == 'text/plain':
        charset = msg.get_content_charset()
        text = msg.get_payload(decode=True).decode(charset, 'ignore')
        gen.generate_file_plain(text, charset)
    elif content_type == 'text/html':
        charset = msg.get_content_charset()
        html = msg.get_payload(decode=True).decode(charset, 'ignore')
        gen.generate_file_html(html, charset)
        gen.generate_clear_html(html, charset)
        gen.generate_file_urls(html)
    else:
        try:
            file_name = msg.get_filename().replace('\n', ' ')
            extension = msg.get_content_type().split('/')[1]
            if decode_header(file_name)[0][1] is not None:
                file_name = decode_header(file_name)[0][0].decode(decode_header(file_name)[0][1])
            if extension not in file_name:
                file_name = f'{file_name}.{extension}'
            file_data = msg.get_payload(decode=True)
            gen.generate_file_attach(file_name, file_data)
        except Exception as error:
            print('parser, get_content:', error)
