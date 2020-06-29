#!/bin/bash/env python

'''
3DES加解密模块
'''

from pyDes import triple_des, ECB, PAD_PKCS5

class Des(object):
	'''
	3DES加解密类
	'''
	def __init__(self, k, mode=ECB):
		self.k = k
		self.mode = mode

	def encrypt(self, dt):
		des = triple_des(self.k, mode=ECB, padmode=PAD_PKCS5)
		# 将字符串转换为bytes字节
		data_byte = bytes(dt, encoding='UTF-8')
		return des.encrypt(data_byte)

	def decrypt(self, en):
		des = triple_des(self.k, mode=ECB, padmode=PAD_PKCS5)
		dec = des.decrypt(en)
		# 将bytes类型转换为str
		return bytes.decode(dec,encoding='UTF-8')