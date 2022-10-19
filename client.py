#!/usr/bin/python3

import socket
import sys

if len(sys.argv) != 3:
    print("modo de uso: python3 client.py <porta do servidor> <chave de deslocamento do servidor>")
    exit()

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = sys.argv[2]

def encrypt(plaintext, key):
    string = ""
    for i in plaintext:
        if i not in alphabet:
            string += i
            continue
        for j in alphabet:
            if i == j:
                index = alphabet.index(i)
                c_index = (index + int(key)) % 26
                string += alphabet[c_index]
                continue
    return string

def decrypt(plaintext, key):
     string = ""
     for i in plaintext:
         if i not in alphabet:
             string += i
             continue
         for j in alphabet:
             if i == j:
                 index = alphabet.index(i)
                 c_index = (index - int(key)) % 26
                 string += alphabet[c_index]
                 continue
     return string


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', int(sys.argv[1])))

while True:
    msg = str(input("you: "))
    if msg == 'bye':
        break
    else:
        msg = encrypt(msg.lower(), key)
        client.send(msg.encode('utf-8'))
        msg_from = client.recv(2048).decode('utf-8')
        msg_from = decrypt(msg_from.lower(), key)
        print(f"< he > {msg_from}")
client.close()


