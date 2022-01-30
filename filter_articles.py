import os
import glob
import shutil

def get_all_htmls(directory_path):
    return glob.iglob(os.path.join(directory_path, '*.html'))

def is_article(html_path):
    try:
        with open(html_path, 'rb') as f:
            return b'<article>' in f.read()
    except:
        pass

def save_articles(directory_path, output_directory_path):
    os.mkdir(output_directory_path)

    for html_path in get_all_htmls(directory_path):
        if is_article(html_path):
            shutil.copy2(html_path, output_directory_path)

save_articles(r"\users\Eden Cohen\news-please-repo\data\2022\01\04\mako.co.il", r"C:\Users\Eden Cohen\Desktop\Project\Articles")