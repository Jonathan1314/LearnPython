#!/usr/bin/env python3
# -*-coding:gbk -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# ���Ի���Ϊ python3.6

s = '��'
# ��һ��������Python������
# �ڶ�����Python������,��gbk�������� s = '��' �����ڴ�
# ���������ڴ��п���һ��ռ䣬Python3����unicode��ʽ�洢��u'��'������Python3���ʶ���ַ�����������������

s2 = s.encode(encoding='utf-8')
# ִ�й����У�unicode -->encode -->utf-8(bytes)

# utf-8(bytes) -->decode -->unicode
# s.decode('utf-8')  # ���� 'str' object has no attribute 'decode',unicodeֻ��encode()

s3 = s2.decode()  # bytes ֻ��decode

print(s)
print(s2)
print(s3)

# �ļ���ͷָ���ı��룬��Python3��ȡ�ļ�ʱ���ص��ڴ�ı���
# Python3���ַ���(str������������)����ʶ��Ϊunicode�Ľ��

# ִ�й����в����ַ�������

# Python3��������ʽ���ַ���
# str(��unicode, u'��'),
# bytes(�� str.encode()�Ľ����b'\xe6\x9e\x97')

# Python2��Ҳ��������ʽ���ַ���
#  str == bytes
# unicode
