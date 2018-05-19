#!/usr/bin/python
# encoding: utf-8
# Author: fanxn
# Date: 2018/5/19

'''
python 3.5
pip install pycrypto

argvs:
 - key: encrypt/decrypt key
 - type：operation type, en/de
 - input_str: input text

Test command:
# encrypt
$ python sn_encrypt.py 12345 en whatsupthere

# decrypt
$ python sn_encrypt.py 12345 de o1reBh8ATEHA45fZI9HOZCkxSH5FR6KwuGnYYkq83gA=
'''

from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import sys

BS = AES.block_size
pad = lambda e: '{}{}'.format(e, (BS - len(e) % BS) * chr((BS - len(e) % BS)))


class Pycrypt():
    def __init__(self, key):
        self.key = pad(key)
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        escaped = b64encode(text.encode())
        length = 16
        count = len(escaped)
        padding_cnt = length - (count % length)
        escaped += (b'\0' * padding_cnt)
        ciphered_text = b64encode(cryptor.encrypt(escaped)).decode()
        return ciphered_text

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        bin_text = b64decode(text.encode())
        plain_text = b64decode(cryptor.decrypt(bin_text)).decode()
        return plain_text.rstrip('\0')


def main(key, type, input_str):
    tar_method = type == 'en' and 'encrypt' or 'decrypt'
    pc = Pycrypt(key)
    return getattr(pc, tar_method)(input_str)


if __name__ == '__main__':
    try:
        _, key, type, input_str = sys.argv
        print(main(key, type, input_str))
    except Exception as e:
        # run test
        pc = Pycrypt('123345')
        e = pc.encrypt('Test works')
        d = pc.decrypt(e)
        print('{}\n{}'.format(e, d))
        assert d == 'Test works'
