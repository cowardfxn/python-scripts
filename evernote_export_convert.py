#!/usr/bin/python3
# encoding: utf-8

import re, os
from bs4 import BeautifulSoup

def html2txt(html_file, out_path):
    with open(html_file) as ifs:
        hc = ifs.read()
    soup = BeautifulSoup(hc, 'lxml')
    title = soup.title.string.replace(os.path.sep, "")
    txt_file = os.path.join(out_path, "{}.txt".format(title))
    with open(txt_file, 'w') as ofs:
        for divTag in soup.find('body').find_all('div'):
            hyper_link = ""
            if divTag.find('a'):
                for link in divTag.find_all("a"):
                    if link.getText().strip() == link['href'].strip():
                        hyper_link += "\n{}".format(link.getText())
                    else:
                        hyper_link += "\n{} {}".format(link.getText(), link['href'])
            if divTag.getText():
                ofs.write(divTag.getText() + hyper_link + "\n")
    print("File {} is converted to {}".format(html_file, txt_file))


def main(path, out_path="./"):
    basedir, _, files = list(os.walk(path))[0]
    for file_name in files:
        if file_name.endswith(".html"):
            file_name = os.path.join(basedir, file_name)
            html2txt(file_name, out_path)

if __name__ == '__main__':
    main("/Users/me/Documents/我的笔记", "/Users/me/Desktop/conv_temp")
