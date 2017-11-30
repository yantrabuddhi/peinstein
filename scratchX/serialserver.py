#!/usr/bin/env python
#python -m SimpleHTTPServer 8080
import SimpleHTTPServer
import SocketServer
import socket
import serial
import time
import threading
import urllib

class Einstein:

		def __init__(self, ser):
				print("\nopening: "+ser+"\n")
				self.ser = serial.Serial(port=ser, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
				time.sleep(1)

		def connect(self):
                                print("\nconnecting..\n")
				self.ser.write("\nconnect_tcp()\n")

		def execute(self, command):
                                print("\nsending command\n")
				self.ser.write("\nsend_command(\""+command+"\")\n")


class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler, object):
		def end_headers(self):
				self.send_my_headers()
				SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

		def send_my_headers(self):
				self.send_header("Access-Control-Allow-Origin", "*")
				self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
				self.send_header("Pragma", "no-cache")
				self.send_header("Expires", "0")

		def translate_path(self, path):
				global e
				if path == '/walk':
						e.execute("Don't myndifydoo.<MO=EL,1.0,0.5><MO=HN,0,0.5><PM><MO=EL,0.1,0.5><MO=HN,0.3,0.5><PA><WK=W2><PA>")
						path = '/ok.txt'
                                if path == '/connect':
                                                e.connect()
                                                path = '/ok.txt'
				elif path == '/crazy':
						e.execute("You asked for it.<PA=2><MO=EL,1,0.5><PA=1.5><MO=HT,0,0.1><PA=0.8>\
<MO=HT,1,0.2><PA=0.5><MO=HT,0.5,0.2><PM>\
<MO=CH,0,0.1><MO=EB,1,0.1><PM><MO=CH,1,0.1><MO=EB,0,0.1><PM><MO=CH,0,0.1><MO=EB,1,0.1><PM><MO=CH,1,0.1><MO=EB,0,0.1><PM><MO=AR,1,0.5><PM><MO=AR,0,0.5><PM><MO=HN,1,0.2><PM><MO=HN,0,0.2><PM><MO=HN,1,0.2><PM><MO=HN,0,0.2><PM><MO=HN,1,0.2><MO=AR,1,0.5><PM><MO=AR,0,0.5><PM><MO=HT,0.7,0.2><PM><MO=HT,0.3,0.2><PM><MO=HT,0.7,0.2><PM><MO=HT,0.3,0.2><PM><MO=HT,0.7,0.2><PM><MO=HT,0.5,0.2><MO=AR,1,0.5><PM><MO=AR,0,0.5><PM><MO=CH,0,0.1><MO=EB,1,0.1><PM><MO=CH,1,0.1><MO=EB,0,0.1><PM><MO=CH,0,0.1><MO=EB,1,0.1><PM><MO=CH,1,0.1><MO=EB,0,0.1><PM><MO=CH,0,0.1><MO=EB,1,0.1><PM><PM><MO=CH,1,0.1><MO=EB,0,0.1><PM><MO=CH,0,0.1><MO=EB,1,0.1><PM><MO=CH,1,0.1><MO=EB,0,0.1><PM><MO=CH,0,0.1><MO=EB,1,0.1><PM><MO=CH,1,0.1><MO=EB,0,0.1><PM><MO=CH,0,0.1><MO=EB,1,0.1><PM><MO=CH,0,0.1><MO=EB,1,0.1><PM><MO=CH,1,0.1><MO=EB,0,0.1><PM><MO=CH,0,0.1><MO=EB,1,0.1><PM><MO=CH,1,0.1><MO=EB,0,0.1><PM><MO=HT,0,0.1><PA=0.4><MO=HN,1,0.2><MO=HT,1,0.2><PA=0.7><MO=HT,0.5,0.1><MO=CH,0,0.1><MO=EB,1,0.1><PM><MO=AR,1,0.1><MO=MO,1.0,0.3><PA=0.5><MO=AR,0,2><MO=CH,0.5,2><MO=MO,0,2><MO=EB,0,2><MO=HN,0.3,2><PA=1><MO=EL,0.1,0.5><PA=1.5> That's gonna hurt in the morning.<MO=EL,1.0,0.5><MO=HT,0.7,0.5><PM><MO=HT,0.3,0.5><PM><MO=HT,0.5,0.5><MO=EL,0.1,0.5><PA>")
						path = '/ok.txt'
				elif path[:5] =='/say/':
						e.execute(urllib.unquote(path[6:]))
						path = '/ok.txt'
				else:    
						print("DBG:","UNKNOWN COMMAND PASSED")
				return super(MyHTTPRequestHandler, self).translate_path(path)

if __name__ == "__main__":
	print("--- RUNNING - MAIN ---")
	PORT = 8080
	#linux
	e =Einstein('/dev/ttyUSB0')
	#mac
	#e =Einstein('/dev/cu.wchusbserial1440')
	Handler = MyHTTPRequestHandler

	httpd = SocketServer.TCPServer(("", PORT), Handler)

	print "serving at port", PORT

	srv = threading.Thread(target=httpd.serve_forever)
	srv.daemon = True
	srv.start()

	while True:
            time.sleep(10)
            print("working..")
