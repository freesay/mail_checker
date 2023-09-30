import email
from _common import generators as gen


def get_raw_data(file):
    with open(file, 'r') as f:
        email_data = f.read()
    return email_data


def parse_content(email_data):
    msg = email.message_from_string(email_data)
    headers = []
    for name, value in email.message_from_string(email_data).items():
        val = ''
        for v in value:
            val += v.lstrip('\t').replace('\n', '; ')
        headers.append(f'{name}\t\t\t{val}')
    gen.generate_file_headers(headers)
    if msg.is_multipart():
        for part in msg.walk():
            get_content(part)
    else:
        get_content(msg)


def get_content(msg):
    content_type = msg.get_content_type()
    if content_type == 'text/plain':
        charset = msg.get_content_charset()
        text = msg.get_payload(decode=True).decode(charset, 'ignore')
        gen.generate_file_plain(text)
    elif content_type == 'text/html':
        charset = msg.get_content_charset()
        html = msg.get_payload(decode=True).decode(charset, 'ignore')
        gen.generate_file_html(html)
        gen.generate_file_urls(html)
        gen.generate_clear_html(html)
    try:
        if content_type != 'text/plain' or content_type != 'text/html':
            file_name = msg.get_filename()
            file_data = msg.get_payload(decode=True)
            gen.generate_file_attach(file_name, file_data)
    except:
        pass
