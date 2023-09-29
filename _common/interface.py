import tkinter as tk
from tkinter import ttk, filedialog
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
        self.frame_text_box = ttk.LabelFrame(self.frame_main, text='File data')
        self.frame_menu = ttk.Frame(self.root)
        self.frame_change_file = ttk.LabelFrame(self.frame_menu, text='Select file')
        self.frame_change_options = ttk.LabelFrame(self.frame_menu, text='Choice data')
        self.frame_combo_btn_1 = ttk.Frame(self.frame_change_file)
        self.frame_combo_btn_2 = ttk.Frame(self.frame_change_options)
        self.frame_combo_btn_3 = ttk.Frame(self.frame_change_options)
        self.frame_detect_res = ttk.LabelFrame(self.frame_menu, text='Attach files')
        self.frame_open_html = ttk.LabelFrame(self.frame_menu, text='Generated html file')

    def file_dialog(self):
        self.path = filedialog.askopenfilename(filetypes=[('EML files', '*.eml')])
        return self.path

    def init_buttons(self):
        self.btn_open_file = ttk.Button(self.frame_combo_btn_1,
                                        width=50,
                                        text='Open EML',
                                        command=self.func.open_file)
        self.btn_convert_data = ttk.Button(self.frame_combo_btn_1,
                                           width=50,
                                           text='Processing',
                                           command=self.func.get_convert_data)
        self.btn_get_headers = ttk.Button(self.frame_combo_btn_2,
                                          width=50,
                                          text='Show HEADERS',
                                          command=self.func.set_headers_tex_box)
        self.btn_get_plain = ttk.Button(self.frame_combo_btn_2,
                                        width=50,
                                        text='Show PLAIN',
                                        command=self.func.set_plain_tex_box)
        self.btn_get_html = ttk.Button(self.frame_combo_btn_3,
                                       width=50,
                                       text='Show HTML',
                                       command=self.func.set_html_tex_box)
        self.btn_get_urls = ttk.Button(self.frame_combo_btn_3,
                                       width=50,
                                       text='Show URL\'s',
                                       command=self.func.set_urls_tex_box)

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
            self.btn_open_folder = ttk.Button(self.frame_detect_res, text='Open folder', command=self.func.open_folder)
            self.btn_open_folder.pack(side='top', fill='x', padx=5, pady=5)
        else:
            self.detect_label = ttk.Label(self.frame_detect_res, text='Attached files not found', wraplength=500)
            self.detect_label.pack(side='top', fill='x', padx=5, pady=5)
        self.root.update()

    def create_open_html_widget(self):
        for widget in self.frame_open_html.winfo_children():
            widget.destroy()
        self.btn_open_html = ttk.Button(self.frame_open_html, text='Open the cleared EMAIL', command=self.func.open_clear_html)
        self.btn_open_html.pack(side='top', fill='x', padx=5, pady=5)
        self.root.update()

    def packing_widgets(self):
        self.frame_main.pack(side='left', fill='both', expand=True)
        self.frame_text_box.pack(fill='both', expand=True, padx=5, pady=5)
        self.frame_menu.pack(side='left', fill='y', expand=False, padx=5, pady=5)
        self.frame_change_file.pack(side='top')
        self.frame_combo_btn_1.pack(side='top')
        self.frame_combo_btn_2.pack(side='top')
        self.frame_combo_btn_3.pack(side='top')
        self.frame_change_options.pack(side='top', fill='y', expand=False, padx=5, pady=5)
        self.frame_detect_res.pack(side='top', fill='x', padx=5, pady=5)
        self.frame_open_html.pack(side='top', fill='x', padx=5, pady=5)

        self.scroll_y.pack(side='right', fill='y')
        self.scroll_x.pack(side='bottom', fill='x')
        self.text_box.pack(side='left', fill='both', expand=True)

        self.btn_open_file.pack(side='left', padx=5, pady=5)
        self.btn_convert_data.pack(side='left', padx=5, pady=5)
        self.btn_get_headers.pack(side='left', padx=5, pady=5)
        self.btn_get_plain.pack(side='left', padx=5, pady=5)
        self.btn_get_html.pack(side='left', padx=5, pady=5)
        self.btn_get_urls.pack(side='left', padx=5, pady=5)

    def run_build(self):
        self.init_frames()
        self.init_text_box()
        self.init_buttons()
        self.packing_widgets()
        self.root.mainloop()
