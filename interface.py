import tkinter as tk
from tkinter import ttk, filedialog
from idlelib.percolator import Percolator
from idlelib.colorizer import ColorDelegator
from _common.functions import Functions


class BuildInterface:
    def init_frames(self):
        self.root = tk.Tk()
        self.root.geometry('1400x800')
        self.root.minsize(1400, 800)

        self.frame_main = ttk.Frame(self.root)
        self.frame_text_box = ttk.LabelFrame(self.frame_main, text='Result')
        self.frame_menu = ttk.Frame(self.root)
        self.frame_change_options = ttk.LabelFrame(self.frame_menu, text='Options')
        self.frame_combo_btn_1 = ttk.Frame(self.frame_change_options)
        self.frame_combo_btn_2 = ttk.Frame(self.frame_change_options)

        self.frame_detect_res = ttk.LabelFrame(self.frame_menu, text='Detected')

        self.func = Functions(self)

    def file_dialog(self):
        self.path = filedialog.askopenfilename(filetypes=[('EML files', '*.eml')])
        return self.path

    def init_buttons(self):
        self.btn_open_file = ttk.Button(self.frame_main,
                                        text='Open EML-file',
                                        command=self.func.open_file)
        self.btn_convert_data = ttk.Button(self.frame_main,
                                           text='Converting data',
                                           command=self.func.get_convert_data)
        self.btn_get_headers = ttk.Button(self.frame_combo_btn_1,
                                          width=50,
                                          text='Show HEADERS',
                                          command=self.func.set_headers_tex_box)
        self.btn_get_plain = ttk.Button(self.frame_combo_btn_1,
                                        width=50,
                                        text='Show PLAIN',
                                        command=self.func.set_plain_tex_box)
        self.btn_get_html = ttk.Button(self.frame_combo_btn_2,
                                       width=50,
                                       text='Show HTML',
                                       command=self.func.set_html_tex_box)
        self.btn_get_urls = ttk.Button(self.frame_combo_btn_2,
                                       width=50,
                                       text='Show URL\'s',
                                       command=self.func.set_urls_tex_box)

    def init_detect_res_text(self):
        self.detect_label = ttk.Label(self.frame_detect_res, text='None', wraplength=500)

    def init_text_box(self):
        self.text_box = tk.Text(self.frame_text_box, width=1, height=1, wrap='none')
        self.scroll_y = ttk.Scrollbar(self.frame_text_box, orient='vertical', command=self.text_box.yview)
        self.scroll_x = ttk.Scrollbar(self.frame_text_box, orient='horizontal', command=self.text_box.xview)
        self.text_box.config(yscrollcommand=self.scroll_y.set)
        self.text_box.config(xscrollcommand=self.scroll_x.set)
        Percolator(self.text_box).insertfilter(ColorDelegator())

    def packing_widgets(self):
        self.frame_main.pack(side='left', fill='both', expand=True)
        self.frame_text_box.pack(fill='both', expand=True, padx=5, pady=5)
        self.frame_menu.pack(side='left', fill='y', expand=False)
        self.frame_combo_btn_1.pack(side='top')
        self.frame_combo_btn_2.pack(side='top')
        self.frame_change_options.pack(side='top', fill='y', expand=False, padx=5, pady=5)
        self.frame_detect_res.pack(side='top', fill='x', padx=5, pady=5)

        self.scroll_y.pack(side='right', fill='y')
        self.scroll_x.pack(side='bottom', fill='x')
        self.text_box.pack(side='left', fill='both', expand=True)

        self.btn_open_file.pack(side='left', expand=True, fill='x', padx=5, pady=5)
        self.btn_convert_data.pack(side='left', expand=True, fill='x', padx=5, pady=5)
        self.btn_get_headers.pack(side='left', padx=5, pady=5)
        self.btn_get_plain.pack(side='left', padx=5, pady=5)
        self.btn_get_html.pack(side='left', padx=5, pady=5)
        self.btn_get_urls.pack(side='left', padx=5, pady=5)

        self.frame_detect_res.pack(fill='both', padx=5, pady=5)
        self.detect_label.pack(side='left', fill='both', padx=5, pady=5)

    def run_build(self):
        self.init_frames()
        self.init_text_box()
        self.init_buttons()
        self.init_detect_res_text()
        self.packing_widgets()
        self.root.mainloop()
