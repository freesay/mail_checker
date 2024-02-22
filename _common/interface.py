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

        self.frame_text_box = ttk.LabelFrame(self.frame_data, text='File data')
        self.frame_menu = ttk.Frame(self.frame_functions)
        self.frame_change_file = ttk.LabelFrame(self.frame_menu, text='Select file')
        self.frame_processing_data = ttk.LabelFrame(self.frame_menu, text='Get data')
        self.frame_change_options = ttk.LabelFrame(self.frame_menu, text='Choice data')
        self.frame_headline_details = ttk.LabelFrame(self.frame_menu, text='Headline details')

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

    def run_build(self):
        self.init_frames()
        self.init_text_box()
        self.init_buttons()
        self.packing_widgets()
        self.root.mainloop()
