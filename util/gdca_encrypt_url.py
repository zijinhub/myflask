# !/usr/bin/env python
# -*-coding: utf-8-*-

import json
from ..util import sm4_tool,md5_tool

class DataHandleToolkit:

    @classmethod
    def get_pre_url(cls, province_id):
        if province_id == 22:
            secret_ip = "10.10.22.236"
            http_port = "8941"
        else:
            secret_ip = "10.10.22.236"
            http_port = "8941"
        pre_url = "http://" + secret_ip + ":" + http_port
        return pre_url

    @classmethod
    def req_set_md5(cls, req_data, key=''):
        # 使用separators参数去掉dumps生成的字符串中逗号和冒号后面的空格
        json_string = json.dumps(req_data, separators=(',', ':'))
        # sm4加密
        md5_bytes = sm4_tool.sm4_encrype(key, json_string)
        # md5加密
        md5_hash = md5_tool.md5to32(md5_bytes)
        return md5_bytes, md5_hash

    @classmethod
    def decode_res_data(cls, res_data, key=''):
        # 解密返回数据，得到String类型的数据
        java_byte_array = sm4_tool.sm4_decrypt(key, res_data.content)
        return java_byte_array
