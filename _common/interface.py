import tkinter as tk
from tkinter import ttk, filedialog
import webbrowser as web
from _common.functions import Functions


class BuildInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('EML checker')
        self.root.geometry('1400x800')
        self.root.minsize(1400, 800)
        self.func = Functions(self)

    def init_frames(self):
        self.frame_main = ttk.Frame(self.root)

        self.frame_data = ttk.Frame(self.frame_main)
        self.frame_functions = ttk.Frame(self.frame_main)

        self.frame_tabs = ttk.Notebook(self.frame_functions)
        self.frame_tab_functions = ttk.Frame(self.frame_tabs)
        self.frame_tab_checklist = ttk.Frame(self.frame_tabs)
        self.frame_tabs.add(self.frame_tab_functions, text='Functions')
        self.frame_tabs.add(self.frame_tab_checklist, text='Check List')

        self.frame_text_box = ttk.LabelFrame(self.frame_data, text='File data')
        self.frame_menu = ttk.Frame(self.frame_tab_functions)
        self.frame_change_file = ttk.LabelFrame(self.frame_menu, text='Select file')
        self.frame_processing_data = ttk.LabelFrame(self.frame_menu, text='Get data')
        self.frame_change_options = ttk.LabelFrame(self.frame_menu, text='Choice data')
        self.frame_headline_details = ttk.LabelFrame(self.frame_menu, text='Headline details')

        self.frame_checklist = ttk.Frame(self.frame_tab_checklist)
        self.frame_checklist_headers = ttk.LabelFrame(self.frame_checklist, text='Проверка заголовков:')
        self.frame_checklist_body = ttk.LabelFrame(self.frame_checklist, text='Проверка тела письма::')
        self.frame_checklist_attach = ttk.LabelFrame(self.frame_checklist, text='Проверка вложений:')
        self.frame_checklist_message = ttk.LabelFrame(self.frame_checklist, text='Проверка обращений из сервисов:')

        self.frame_buttons_open_decode = ttk.Frame(self.frame_change_file)
        self.frame_buttons_headers_plain = ttk.Frame(self.frame_change_options)
        self.frame_buttons_html_urls = ttk.Frame(self.frame_change_options)
        self.frame_buttons_check_urls = ttk.LabelFrame(self.frame_menu, text='Go to')

        self.frame_detect_res = ttk.LabelFrame(self.frame_menu, text='Attach files')
        self.frame_button_open_html = ttk.LabelFrame(self.frame_menu, text='Generated html file')

    def file_dialog(self):
        self.path = filedialog.askopenfilename(filetypes=[('EML files', '*.eml')])
        return self.path

    def init_buttons(self):
        self.btn_open_file = ttk.Button(self.frame_buttons_open_decode,
                                        width=40,
                                        text='Open EML',
                                        command=self.func.open_file)
        self.btn_decode_data = ttk.Button(self.frame_buttons_open_decode,
                                          width=40,
                                          text='Decode BASE64',
                                          command=self.func.decode_base64)
        self.btn_processing_data = ttk.Button(self.frame_processing_data,
                                              width=40,
                                              text='Processing',
                                              command=self.func.get_parse_data)
        self.btn_show_headers = ttk.Button(self.frame_buttons_headers_plain,
                                           width=40,
                                           text='Show HEADERS',
                                           command=self.func.set_headers_tex_box)
        self.btn_show_plain = ttk.Button(self.frame_buttons_headers_plain,
                                         width=40,
                                         text='Show PLAIN',
                                         command=self.func.set_plain_tex_box)
        self.btn_show_html = ttk.Button(self.frame_buttons_html_urls,
                                        width=40,
                                        text='Show HTML',
                                        command=self.func.set_html_tex_box)
        self.btn_show_urls = ttk.Button(self.frame_buttons_html_urls,
                                        width=40,
                                        text='Show URL\'s',
                                        command=self.func.set_urls_tex_box)
        self.btn_parse_headers = ttk.Button(self.frame_headline_details,
                                            text='Parse HEADERS',
                                            command=self.func.set_parse_headers_tex_box)
        self.btn_urlscan = ttk.Button(self.frame_buttons_check_urls,
                                      width=40,
                                      text='URLSCAN',
                                      command=lambda: web.open('https://urlscan.io/'))
        self.btn_virustotal = ttk.Button(self.frame_buttons_check_urls,
                                         width=40,
                                         text='VIRUSTOTAL',
                                         command=lambda: web.open('https://www.virustotal.com'))

    def init_checkboxes(self):
        self.checks = [tk.IntVar(value=0) for _ in range(20)]
        self.check_box_1 = ttk.Checkbutton(self.frame_checklist_headers, variable=self.checks[0], text='В поле Received нет доменов/IP адресов с сомнительной репутацией')
        self.check_box_2 = ttk.Checkbutton(self.frame_checklist_headers, variable=self.checks[1], text='Домен отправителя не обладает сомнительной репутацией')
        self.check_box_3 = ttk.Checkbutton(self.frame_checklist_headers, variable=self.checks[2], text='Поле From совпадает с Return-Path')
        self.check_box_4 = ttk.Checkbutton(self.frame_checklist_headers, variable=self.checks[3], text='Имя отправителя соответствует домену в email')
        self.check_box_5 = ttk.Checkbutton(self.frame_checklist_headers, variable=self.checks[4], text='В поле X-Mailer отсутствуют подозрительные клиенты')

        self.check_box_6 = ttk.Checkbutton(self.frame_checklist_body, variable=self.checks[5], text='Содержание сообщения не является подозрительным')
        self.check_box_7 = ttk.Checkbutton(self.frame_checklist_body, variable=self.checks[6], text='Сообщение не содержит ошибок или низкокачественной графики')
        self.check_box_8 = ttk.Checkbutton(self.frame_checklist_body, variable=self.checks[7], text='Поля в подписи соответствуют отправителю или компании, от лица которой ведется диалог')
        self.check_box_9 = ttk.Checkbutton(self.frame_checklist_body, variable=self.checks[8], text='Ссылки в тексте указывают на легитимные домены')
        self.check_box_10 = ttk.Checkbutton(self.frame_checklist_body, variable=self.checks[9], text='Ссылки в тексте не являются короткими ссылками (исключением является сервис nda.ya.ru)')
        self.check_box_11 = ttk.Checkbutton(self.frame_checklist_body, variable=self.checks[10], text='Ссылки не ведут на форму авторизации')
        self.check_box_12 = ttk.Checkbutton(self.frame_checklist_body, variable=self.checks[11], text='Ссылки не приводят к автоматической загрузки файлов')
        self.check_box_13 = ttk.Checkbutton(self.frame_checklist_body, variable=self.checks[12], text='Ссылки не ведут на страницу ввода данных о банковской карте или иных данных')

        self.check_box_14 = ttk.Checkbutton(self.frame_checklist_attach, variable=self.checks[13], text='Хэш-вложения имеет хорошую репутацию на VT')
        self.check_box_15 = ttk.Checkbutton(self.frame_checklist_attach, variable=self.checks[14], text='Вложение не является исполняемым файлом')
        self.check_box_16 = ttk.Checkbutton(self.frame_checklist_attach, variable=self.checks[15], text='Вложение не хранится в зашифрованном архиве')
        self.check_box_17 = ttk.Checkbutton(self.frame_checklist_attach, variable=self.checks[16], text='Вложение не копирует реальную страницу и не содержит ссылок на иные ресурсы')

        self.check_box_18 = ttk.Checkbutton(self.frame_checklist_message, variable=self.checks[17], text='Сообщение не побуждает вступить в иное сообщество или воспользоваться ботом')
        self.check_box_19 = ttk.Checkbutton(self.frame_checklist_message, variable=self.checks[18], text='В сообщении не содержится ссылок на сторонние ресурсы')
        self.check_box_20 = ttk.Checkbutton(self.frame_checklist_message, variable=self.checks[19], text='В сообщении не содержится вложений')


    def init_text_box(self):
        self.text_box = tk.Text(self.frame_text_box, width=1, height=1, wrap='none')
        self.scroll_y = ttk.Scrollbar(self.frame_text_box, orient='vertical', command=self.text_box.yview)
        self.scroll_x = ttk.Scrollbar(self.frame_text_box, orient='horizontal', command=self.text_box.xview)
        self.text_box.config(yscrollcommand=self.scroll_y.set)
        self.text_box.config(xscrollcommand=self.scroll_x.set)

    def create_files_widget(self, data):
        for widget in self.frame_detect_res.winfo_children():
            widget.destroy()
        if data:
            for file in data:
                self.detect_label = ttk.Label(self.frame_detect_res, text=f" - {file}", wraplength=500)
                self.detect_label.pack(side='top', fill='x', padx=5, pady=5)
            self.btn_open_folder = ttk.Button(self.frame_detect_res,
                                              text='Open folder',
                                              command=self.func.open_folder)
            self.btn_open_folder.pack(side='top', fill='x', padx=5, pady=5)
        else:
            self.detect_label = ttk.Label(self.frame_detect_res, text='Attached files not found', wraplength=500)
            self.detect_label.pack(side='top', fill='x', padx=5, pady=5)
        self.root.update()

    def create_open_html_widget(self, data):
        for widget in self.frame_button_open_html.winfo_children():
            widget.destroy()
        if 'clear_html.html' in data:
            self.detect_label = ttk.Label(self.frame_button_open_html, text='clear_html.html')
            self.detect_label.pack(side='top', fill='x', padx=5, pady=5)
            self.btn_open_html = ttk.Button(self.frame_button_open_html,
                                            text='Open the cleared EMAIL',
                                            command=self.func.open_clear_html)
            self.btn_open_html.pack(side='top', fill='x', padx=5, pady=5)
        else:
            self.html_label = ttk.Label(self.frame_button_open_html, text='HTML data not found', wraplength=500)
            self.html_label.pack(side='top', fill='x', padx=5, pady=5)
        self.root.update()

    def packing_widgets(self):
        self.frame_main.pack(side='left', fill='both', expand=True)

        self.frame_data.pack(side='left', expand=True, fill='both')
        self.frame_functions.pack(side='right', fill='both')

        self.frame_tabs.pack(expand=True, fill='both')

        self.frame_checklist.pack(side='left', fill='both', padx=5, pady=5)
        self.frame_checklist_headers.pack(expand=True, fill='both')
        self.frame_checklist_body.pack(expand=True, fill='both')
        self.frame_checklist_attach.pack(expand=True, fill='both')
        self.frame_checklist_message.pack(expand=True, fill='both')

        self.frame_text_box.pack(fill='both', expand=True, padx=5, pady=5)
        self.frame_menu.pack(side='left', fill='y', expand=False, padx=5, pady=5)
        self.frame_change_file.pack(side='top')
        self.frame_processing_data.pack(side='top', fill='x', padx=5, pady=5)

        self.frame_buttons_open_decode.pack(side='top')
        self.frame_processing_data.pack(side='top')
        self.frame_buttons_headers_plain.pack(side='top')
        self.frame_buttons_html_urls.pack(side='top')
        self.frame_change_options.pack(side='top', fill='y', expand=False, padx=5, pady=5)
        self.frame_headline_details.pack(side='top', fill='x', padx=5, pady=5)
        self.frame_detect_res.pack(side='top', fill='x', padx=5, pady=5)
        self.frame_button_open_html.pack(side='top', fill='x', padx=5, pady=5)
        self.frame_buttons_check_urls.pack(side='bottom')

        self.scroll_y.pack(side='right', fill='y')
        self.scroll_x.pack(side='bottom', fill='x')
        self.text_box.pack(side='left', fill='both', expand=True)

        self.btn_open_file.pack(side='left', padx=5, pady=5)
        self.btn_processing_data.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        self.btn_decode_data.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        self.btn_parse_headers.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        self.btn_show_headers.pack(side='left', padx=5, pady=5)
        self.btn_show_plain.pack(side='left', padx=5, pady=5)
        self.btn_show_html.pack(side='left', padx=5, pady=5)
        self.btn_show_urls.pack(side='left', padx=5, pady=5)
        self.btn_urlscan.pack(side='left', padx=5, pady=5)
        self.btn_virustotal.pack(side='left', padx=5, pady=5)

        self.check_box_1.pack(fill='both', pady=2)
        self.check_box_2.pack(fill='both', pady=2)
        self.check_box_3.pack(fill='both', pady=2)
        self.check_box_4.pack(fill='both', pady=2)
        self.check_box_5.pack(fill='both', pady=2)
        self.check_box_6.pack(fill='both', pady=2)
        self.check_box_7.pack(fill='both', pady=2)
        self.check_box_8.pack(fill='both', pady=2)
        self.check_box_9.pack(fill='both', pady=2)
        self.check_box_10.pack(fill='both', pady=2)
        self.check_box_11.pack(fill='both', pady=2)
        self.check_box_12.pack(fill='both', pady=2)
        self.check_box_13.pack(fill='both', pady=2)
        self.check_box_14.pack(fill='both', pady=2)
        self.check_box_15.pack(fill='both', pady=2)
        self.check_box_16.pack(fill='both', pady=2)
        self.check_box_17.pack(fill='both', pady=2)
        self.check_box_18.pack(fill='both', pady=2)
        self.check_box_19.pack(fill='both', pady=2)
        self.check_box_20.pack(fill='both', pady=2)

    def run_build(self):
        self.init_frames()
        self.init_text_box()
        self.init_buttons()
        self.init_checkboxes()
        self.packing_widgets()
        self.root.mainloop()
