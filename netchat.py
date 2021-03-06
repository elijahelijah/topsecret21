#!/usr/bin/env python

import sys
from socket import socket, gethostbyname, gethostname, error

from encrypt import scramble

MIN_PORT = 49152
MAX_PORT = 65535


def get_server_socket():
    s = socket()
    try:
        ip = gethostbyname(gethostname())
        print 'Server IP address: %s' % ip
    except:
        ip = ''
        print 'could not get IP address, will bind to all interfaces'
    for port in range(MIN_PORT, MAX_PORT):
        try:
            s.bind((ip, port))
            print 'Server port: %s' % port
            break
        except:
            pass

    s.listen(0)
    return s.accept()[0]


def get_client_socket(server_ip, port):
    s = socket()
    s.connect((server_ip, int(port)))
    return s


def print_received(message):
    print '[RECV]', message


def print_sent(message):
    print '[SENT]', message


def get_and_send(sock):
    message = raw_input('MSG> ')
    sock.send(message)
    print_sent(message)


def receive(sock):
    message = sock.recv(1000)
    print_received(message)


def conversation(sock, receive_first=False):
    if receive_first:
        while 1:
            receive(sock)
            get_and_send(sock)
    else:
        while 1:
            get_and_send(sock)
            receive(sock)


if __name__ == '__main__':
    if 'server' in sys.argv:
        while 1:
            try:
                sock = get_server_socket()
                conversation(sock, receive_first=True)
            except error:
                pass
    else:
        while 1:
            try:
                sock = get_client_socket(sys.argv[1], sys.argv[2])
                conversation(sock)
            except error:
                pass
