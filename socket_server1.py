# 文件位置
# coding:utf-8

import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello, world! <h1> form the5fire 《Django 企业开发实践》'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun, 27 may 2018 01:01:01 GMT',
    'Content-Length: {}\r\n'.format(len(body.encode())),
    body,
]
response = '\r\n'.join(response_params)


def handle_connection(conn, addr):    
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode()) # response转为bytes后传输


def main():
    # socket.AF_INET 用于服务器与服务器之间的网络通信
    # socket.STREAM 用于基于 TCP 的流式 socket 通信
    serversocket = socket.socket(socket.AF_INET, socket.STREAM)
    serversocket.setsockopt
