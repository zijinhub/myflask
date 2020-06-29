#!/bin/bash/env python

'''
MD5模块
'''

import hashlib

def md5to32(dt):
    '''
    md5转码，默认返回32位长度的MD5码
    :param dt:
    :return: 返回32位长度大写的MD5码
    '''
    h1 = hashlib.md5()
    h1.update(dt.encode("utf-8"))
    return h1.hexdigest().upper()

def md5to16(dt):
    '''
    md5转码，截取返回16位长度大写的MD5码
    :param dt:
    :return:
    '''
    md5_data=md5to32(dt)
    return md5_data[8:24]

def md5to24(dt):
    '''
    在16位长度的MD5码基础上，将32位长度的MD5码中下标能被4整除的字符拼接返回
    :param dt:
    :return: 16位MD5码+32位MD5码中下标能被4整除的字符
    '''
    tmp32 = md5to32(dt)
    tmp16 = md5to16(dt)
    tmp = ""
    for i in range(1,33):
        if i%4 == 0:
            tmp = tmp + tmp32[i-1:i]
    return tmp16 + tmp

def md5to24new(dt):
    '''
    在16位长度的MD5码基础上，将32位长度的MD5码中下标能被4整除的字符拼接返回
    :param dt:
    :return: 32位MD5码中下标能被4整除的字符+16位MD5码
    '''
    tmp32 = md5to32(dt)
    tmp16 = md5to16(dt)
    tmp = ""
    for i in range(1,33):
        if i%4 == 0:
            tmp = tmp + tmp32[i-1:i]
    return tmp + tmp16

if __name__ == '__main__':
    print(md5to32('123456'))