#!/usr/bin/python3
import requests
import sys
import re
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError

try:
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    for i in lines:
        try:
            url = "http://" + str(i).strip("\n")
            param = '/get_camera_params.cgi?loginuse=' + str(sys.argv[2]) + '&loginpas=' + str(sys.argv[3])
            fil = url + param
            r = requests.get(fil, timeout=15)
            if re.search(str("Auth Failed"), str(r.content)):
                print(url, "doesn't work")
            else:
                print(url, "works")
        except Timeout as e:
            print(url, e)
        except OSError as e:
            print(url, e)
        except ConnectionError as e:
            print(url, e)
        finally:
            file.close
            sys.exit
except KeyboardInterrupt:
    sys.exit
