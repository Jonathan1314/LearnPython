#!/usr/bin/env python3
# -*-coding:gbk -*-
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8800))
sock.listen(5)

while True:
    print('server waiting...')
    conn, addr = sock.accept()  # conn �ͻ��˵��׽��ֶ���
    data = conn.recv(1024)      # ����������������ݣ�����recv�����õ�
    print('data', data)

    # conn.send(b'Hello World')   # �����û�а��ձ�׼��HTTP��Ӧ��ʽ��������������ˣ��ᱨ��
    # conn.send(b'HTTP/1.1 200 OK\r\n\r\n<h1>Hello World!</h1>')

    # with open('index.html', 'r') as f:
    #     content = f.read()
    with open('login.html', 'r') as f:
        content = f.read()

    res = 'HTTP/1.1 200 OK\r\n\r\n%s' % content
    conn.sendall(res.encode('GBK'))

    conn.close()

