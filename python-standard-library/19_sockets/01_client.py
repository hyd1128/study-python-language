#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import socket

if __name__ == '__main__':
    # 创建tcp客户端套接字
    # 1. AF_INET: 表示ipv4
    # 2. SOCK_STREAM: TCP传输协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 和服务端程序建立连接
    tcp_client_socket.connect(("127.0.0.1", 8989))
    # 代码执行到此处, 说明连接建立成功
    # 准备发送数据
    send_data = "你好服务端, 我是客户端1!".encode("gbk")
    # 发送数据
    tcp_client_socket.send(send_data)
    # 接收数据, 这次接收的数据的最大字节数是1024
    recv_data = tcp_client_socket.recv(1024)
    # 返回的直接是服务端程序发送的二进制数据
    print(recv_data)
    # 对数据进行解码
    recv_content = recv_data.decode("gbk")
    print("接收服务端的数据为:", recv_content)
    # 关闭套接字
    tcp_client_socket.close()
