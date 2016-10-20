import tarfile
import os.path

'''
tarfile库使用验证
压缩/解压缩文件用
'''

class tarFile(object):
    def __init__(self, path):
        self.path = path
        self.tf = ""
        self.names = []

    def load(self, mode='r'):
        assert os.path.exists(path)
        self.tf = tarfile.open(path， mode=mode)
        self.names = self.tf.getnames()

    def extract(self, path="./", target=""):
        if target:
            self.extract(target, path)
        else:
            self.tf.extractall(path)
