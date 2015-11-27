# coding=utf-8
import encryptTool
import random
import string


def create_nonceStr(num):
    """
    产生随机字符串
    :param num:产生随机字符串的位数
    :return:随机字符串 string
    """
    salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return salt


def get_sign_str(obj):
    """
    将字典按照key排序转换成 key=value&key=value 形式
    :param obj:dict {
    a:1
    c:2
    b:3
    }
    :return: a=1&b=3&c=2
    """
    arr = sorted(obj.iteritems())
    sign_string = ""
    for key, value in arr:
        if value:
            if not bool(sign_string):
                sign_string += key + "=" + unicode(value)
            else:
                sign_string += "&" + key + "=" + unicode(value)
    return sign_string


def get_signature(sign_dict, append_str=''):
    """
    签名算法
    :type append_str: 签名附加字符串
    :param sign_dict: dict 对象
    :return: string signature 字符串
    """
    sign_str = get_sign_str(sign_dict)
    sign_str = sign_str + append_str
    sign = encryptTool.md5_encode(sign_str.encode('utf-8'))
    return sign
