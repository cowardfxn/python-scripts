#!/usr/bin/env/python3
# _*_ coding: utf-8 _*_


'''
帮网友写的Excel配置文件转换器
运行环境：
Python 3.4+
需要第三方库 openpyxl

'''


from openpyxl import Workbook
import os, re

def getTxtFiles(path, suffix):
    rslt = []
    for dirpath, dirname, filenames in os.walk(path):
        for filename in filenames:
            if filename.lower().endswith("." + suffix.lower()):
                rslt.append(os.path.join(dirpath, filename))

    return rslt

def fileProc(filename):
    row1st_pattern = re.compile(r'第\s+(\d+)\s+层配筋、验算')
    valid_row_pattern = re.compile(r'[a-zA-Z]+\=\s+(?:\-)?\d+(?:\.\d+)?')
    split_ptr = re.compile(r'\=\s+')
    nc_ptr = re.compile(r'[a-zA-Z]+\-[a-zA-Z]+\=\s+\d+')
    titles = []
    lines = []
    try:
        with open(filename) as ifs:
            line_cont = {}
            cont = ifs.read().decode('gb18030').encode('utf-8')
            print('111111')
            for line in cont.trim().split('\n'):
                if line:
                    c0 = row1st_pattern.findall(line)
                    c1 = nc_ptr.findall(line)
                    if c0:
                        line_cont["标准层"] = c0[0]
                        titles.append("标准层")

                    if c1:
                        key_vals = split_ptr.split(c1[0])
                        line_cont[key_vals[0]] = key_vals[1]
                        titles.append(key_vals[0])

                    if line.startswith('( '):
                        for ptrs in valid_row_pattern.findall(line):
                            k_vs = split_ptr.split(split_ptr)
                            line_cont[k_vs[0]] = k_vs[1]
                            titles.append(k_vs[0])

                    if line.startswith('-'*10):
                        lines.append(line_cont)

    except Exception as e:
        print(e, )
    finally:
        return titles, lines

def writeExcel(titles, lines, path):
    wb = Workbook()
    ws1 = wb.active
    ws1.title = "Anything"
    ws1.append(titles)
    for line in lines:
        line_cont = []
        for title in titles:
            line_cont.append(line.get(title))
        ws1.append(line_cont)

    wb.save(filename = path)
    print("生成文件：%s\n" % path)

def proc(path, suffix):
    for filename in getTxtFiles(path, suffix):
        titles, lines = fileProc(filename)
        filepath = filename[:filename.rfind('.')]
        outfilename = filepath + "summaryFile.xlsx"
        writeExcel(titles, lines, outfilename)

if __name__ == '__main__':
    # 输入文件目录的完整路径
    # path = '/Users/helio/Downloads'
    path = '/Users/helio/Downloads'
    # 需要的文件后缀名，不区分大小写
    suffix = "OUT"
    proc(path, suffix)
