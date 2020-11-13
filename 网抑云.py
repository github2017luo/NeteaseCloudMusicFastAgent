import os
import sys
import socket
import subprocess

class NeteaseMusic():
    def __init__(self):
        pass

    def is_connected(self):
        try:
            host = socket.gethostbyname('music.163.com')
            socket.create_connection((host, 80), 2)
            return True
        except Exception:
            return False
    

    def proxy_crack(self, path):        
         subprocess.call(path + r'\to_node.bat', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    exe_path = os.path.dirname(sys.argv[0])
    music = NeteaseMusic()
    while not music.is_connected():
        pass
    music.proxy_crack(exe_path)

