# coding=utf-8
import hashlib
import base64


def sha1_encode(string):
    sha1 = hashlib.sha1
    return sha1(string).hexdigest()


def md5_encode(string):
    md5 = hashlib.md5
    return md5(string).hexdigest()


def base64_encode(string):
    return base64.b64encode(string)


def base64_decode(encoding_string):
    return base64.b64decode(encoding_string)

