#!/bin/bash/env python
'''
计算密钥和新国密
获取验证码
'''

from ..util import  md5_tool,des3_tool
import base64


def get_agent_key(agent_id,insert_time):
    '''
    获取密钥
    :param agent_id: 商户ID
    :param insert_time: 商户的创建时间，数据库表的insert_time字段值
    :return: 密钥
    '''
    dt = agent_id + insert_time[0:8] + "sino" + insert_time[8:]
    agent_key = md5_tool.md5to24(dt)
    return agent_key

def get_new_agent_key(agent_id,insert_time):
    '''
    获取密钥，新国密
    :param agent_id: 商户ID
    :param insert_time: 商户的创建时间，数据库表的insert_time字段值
    :return: 密钥
    '''
    dt = agent_id + insert_time[0:8] + "sino" + insert_time[8:]
    agent_key = md5_tool.md5to24new(dt)
    return agent_key

def get_check_code(input_string):
    '''
    获取校验码
    :param input_string: 根据接口文档中要求的几个字段组合字符串
    :return: 校验码
    '''
    ret = 0
    for c in input_string:
        ret += ord(c)
    ret = ret % 100000
    output_string = str(ret)
    for i in range(5-len(output_string)):
        output_string = "0" + output_string
    return output_string

def file_decrypt(file_path):
    '''
    文件解密函数
    :param file_path: 加密文件的路径
    :return:解密后的字符串
    '''
    with open(file=file_path,mode='rb') as f:
        content = f.read()
        bc = base64.b64decode(content)
        des = des3_tool.Des('shandongfucaiftpfile2015')
        output = des.decrypt(bc)
        return output

def file_content_decrypt(content):
    '''
    文件内容解密函数
    :param content: 加密文件内容
    :return: 解密后的文件内容
    '''
    bc = base64.b64decode(content)
    des = des3_tool.Des('shandongfucaiftpfile2015')
    output = des.decrypt(bc)
    return output

if __name__=="__main__":
    get_check_code("20151225123017857"+"00001"+"3760100000058"+"20151225123017857	2	000101020304051617^"+"2"+"8D64725BE5EC3DE2D0C857BE07EC8B58")#05640