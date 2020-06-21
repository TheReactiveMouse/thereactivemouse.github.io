import requests
import os
import sys
import time
import html2text
import unicodedata
import base64
import random
from proxy_requests import ProxyRequests
import urllib.request as urllib2
hostname = open("relay.txt", 'r').read()
port = 80
proxy_base = ['144.76.174.21:33238']
print(f"{time.ctime()} | Loading mouseTor Connection..")
if ( hostname == "" or ' ' in hostname ):
    print(f"{time.ctime()} | Connection declined!")
else:
    print(f"{time.ctime()} | Connection establishing...")

    if ( requests.get(f"http://{hostname}/config.dns").status_code == 200 ):
        print(f"{time.ctime()} | Checking DNS Data base...")
        print(f"{time.ctime()} | Checking the record for main channel...")

        if ( requests.get(f"http://{hostname}/certificate.ttp").status_code == 200 ):
            print(f"{time.ctime()} | CERTIFICATE FOUND, CHECKING VALIDALITY...")

            valid_base = requests.get(f"http://mousenet.tk/valid_certificates.ttp").text
            certificate = requests.get(f"http://{hostname}/certificate.ttp").text
            data_s = base64.b64decode(certificate)
            if str(data_s.decode('utf8')) in valid_base:
                print(f"{time.ctime()} | CERTIFICATE FOUND AND IS VALID! RELAY STATUS: STABLE! :)")
                print("Welcome to the mouseTor Browser! This browser is made to connect to mouseNET Web Sites and for own network ^-^, if you want to open your own relay, you will need to read this instruction: http://mousenet.tk/instruction.html")
                while True:
                
                    url  = input("Enter a url:\nmousetor://")
                    if ( url == "" or ' ' in url ):
                        print("BAD_URL_ERROR")
                    else:
                        print("Connecting..")
                        record_get = requests.get(f"http://{hostname}/config.dns").text
                        record_split = record_get.split('\n')
                        record = record_get.split(f"{url} ")

                        if f'{url}/' in url:
                            fileget = url.split(f'{url}/')
                        
                        list2 = []
                        for line in record_get.split("\n"):
                            if not line.strip():
                                    continue
                            list2.append(line.lstrip())

                        for x2 in range(0, len(list2)):
                            if url in list2[x2]:
                                try:
                                    print(f"{time.ctime()} | Record found, connecting...")
                                    host_2 = list2[x2].split(f"{url} ")
                                    os_Version = random.randint(5, 10)
                                    version1 = random.randint(0, 10)
                                    version2 = random.randint(0, 10)
                                    version3 = random.randint(0, 10)
                                    windows_64_or_not_randomize = random.randint(0, 1)
                                    fake_rv = random.randint(0, 100)
                                    if windows_64_or_not_randomize == "1":
                                        windows_x64_or_not_2 = "32"
                                        windows_x64_or_not = "86"
                                    else:
                                        windows_x64_or_not = "64"
                                    if f'{url}/' in url:
                                        h = {'User-Agent': f'mouseTor/{version1}.{version2}.{version3} (Windows NT {os_Version}.0; Win64; x86; rv:{fake_rv}.0) mouseTor Relay/A9H8G88F mouseTor/1.0.0'}
                                        r = ProxyRequests('http://' + host_2[1] + "/" + fileget[1])
                                        r.set_headers(h)
                                        data = r.get_with_headers()
                                        print (html2text.html2text(str(data)))
                                        break
                                    else:
                                        os_Version = random.randint(5, 10)
                                        h = {'User-Agent': f'mouseTor/{version1}.{version2}.{version3} (Windows NT {os_Version}.0; Win64 x86; rv:{fake_rv}.0) mouseTor Relay/A9H8G88F mouseTor/1.0.0'}
                                        r = ProxyRequests('http://' + host_2[1])
                                        r.set_headers(h)
                                        r.get_with_headers()
                                        print (html2text.html2text(str(r)))
                                        break
                                except:
                                    print(f"{time.ctime()} | Connection failed. Try again.")
                            else:
                                print(f"{time.ctime()} | Record not found, reload netrelay at 000F:000{x2} for {url}:{hostname}!")
                        

            else:
                print(f"{time.ctime()} | CERTIFICATE FOUND, BUT CERTIFICATE ISN'T VALID! IF YOU ARE A RELAY OWNER - REPLACE THE CERTIFICATE! Or tell about this to 🐀Mouse🐀#2870 on Discord.")
                print(F"VALID RECORD : {str(data_s.decode('utf8'))}")
        else:
                print(f"{time.ctime()} | CERTIFICATE NOT FOUND! RELAY STATUS: UNSTABLE! /!\\")
    else:
        print(f"{time.ctime()} | Checking DNS Database failed.")
