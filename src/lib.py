#!/usr/bin/python
# -*- coding: utf-8 -*-

from binascii import unhexlify, hexlify

CESAR_DEFAULT_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789"
SEPARATOR = "/"


def cesar_code(char, offset, chars=CESAR_DEFAULT_CHARS):
    return chars[(chars.index(char) + offset) % len(chars)] if char in chars else char


def decrypt(code):
    output = ""

    for rawData in code.split(SEPARATOR):
        encrypted = unhexlify(rawData).decode()
        if encrypted == 'ζ':
            decrypted = '\n'
        else:
            decrypted = chr(ord(encrypted) - 810353)
        output += cesar_code(decrypted, 1)
    return output


def encrypt(data):
    output = []

    for c in data:
        c = cesar_code(c, -1)

        if c == '\n':
            unicode = 'ζ'
        else:
            unicode = chr(ord(c) + 810353)
        unicode = bytes(unicode, 'utf-8').decode()
        unicode = hexlify(unicode.encode('utf8')).decode()
        output.append(unicode)
    return SEPARATOR.join(output)
