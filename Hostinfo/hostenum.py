#!/usr/bin/python3
import sys
import requests
import socket
import json


def help():
    print("""Usage:
 python3 hostenum [arguments]

List of arguments:
 ip
 city
 region
 org
 country
 loc
 postal
 timezone

Examples:
 python3 hostenum.py --help
 python3 hostenum.py example.com ip org
 python3 hostenum.py example.com --all
 python3 hostenum.py example.com --all > out.text
 python3 hostenum.py example.com ip org region city  | tee output.txt (verbose)
 ./hostenum.py example.com --all (chmod +x hostenum.py)
""")

try:
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        help()
    else:
        ip = requests.get("https://"+sys.argv[1])
        header = ip.headers
        print("[Headers]")
        for x, y in header.items():
            print(x+":"+y)
        host = socket.gethostbyname(sys.argv[1])
        print("\n")

        req_ip = requests.get("https://ipinfo.io/"+host+"/json")
        resp = json.loads(req_ip.text)
        try:
            if sys.argv[2] == "--all":
                print("[Host Info]")
                for i in resp:
                    print(i +":"+ resp[i])
            else:
                for i in sys.argv[2:]:
                    print(i+":"+resp[i])
        except KeyError:
            help()
        except IndexError as error:
            print("Ooops")
            print("python3 hostenum.py example.com --help")
            sys.exit
except Exception as error:
    help()
