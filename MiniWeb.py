#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bsj
#
# Created:     14-12-2013
# Copyright:   (c) bsj 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest
import socket
import threading
import time

class MiniWeb(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.s = None

    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(("localhost", self.port))
        self.s.listen(1)
        while 1:
            print ('이해를 할 수 없군')
            try:

                conn, addr = self.s.accept()
                print('한글이 왜 깨지지' , addr)
                recvmsg = conn.recv(1024)
                conn.send('sdfasd'.encode('utf-8'))
                conn.close()
            except socket.error:
                break

    def simpleResponse(self, msg):
        return """HTTP/1.1 200 OK
        Server: SimpleHttpServer
        Content-type: text/plain
        Content-Length: %s
        %s""" % (len(msg), msg)


    def stop(self):
        if self.s:
            self.s.close()
            self.join()


class TestMiniWeb(unittest.TestCase):
    def test1(self):
        miniweb = MiniWeb(port=8080)
        miniweb.start()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", 8080))
        #s.send("abc")
        s.close()
        time.sleep(0.5)
        miniweb.stop()

if __name__ == "__main__":
    #unittest.main()
    MiniWeb(port=8081).start()
