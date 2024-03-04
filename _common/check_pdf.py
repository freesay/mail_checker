from utils import pdfid


def analyze_pdfs_by_filenames(filenames):
    options = pdfid.get_fake_options()
    options.scan = True
    options.json = True
    list_of_dict = pdfid.PDFiDMain(filenames, options)
    return list_of_dict


def get_report(filename):
    filenames = [filename]
    res_filenames = analyze_pdfs_by_filenames(filenames)['reports'][0]
    res = ''
    for el, val in res_filenames.items():
        res += f'{el.ljust(20, "_")} {val}\n'
    return res
