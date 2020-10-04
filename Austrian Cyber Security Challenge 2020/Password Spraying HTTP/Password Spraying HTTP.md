# Password Spraying HTTP
## Team
Philogic (Solo)

## Description
This challenge is about the unknown password spraying attack. Instead of brute-forcing a passwords, we keep the password constant and brute-force the usernames. You will find a valid http password for a range of 500 users on the pwspray.vm.vuln.land server. Please find the http account that has this password set. But wait --- the service is protected with fail2ban. Your hacking attempts will get blocked after 10 invalid login attempts. The password will change every hour. 
```
                            +--------------+--------------+
                            |              |              |
                            |              |    http      |
                            |              |              |
+------------------+        |              |              |
|  python3 solver  +------->+  fail2ban    |    ssh       |
+------------------+        |              |              |
                            |              |              |
                            |              |    ftp       |
                            |              |              |
                            +--------------+--------------+
```

- find the username with the given password
- the service is fail2ban protected
- you will find a flag, once successfully authenticated

## Files
- None

## Used tools
- Python3
- VPNGate

## Solution

To be able to password spray the HTTP service I used a network of VPNs. I implemented this with the use of the VPNGate public VPN relay servers.

To be able to automate the process I came up with a python script that loaded the password from https://pwspray.vm.vuln.land/ and then connect to a VPN to make the requests.

When the requests for the given VPN were made and I got no result, I automatically switched to another VPN. With this system I was able to make an unlimited amount of login requests because they were sent from different IPs. I executed the script and found the correct user to the given password:

```
Username: user_140241
Password: 4a7f684a
```

The python3 script I used to solve this challenge consists of some very ugly code. Nevertheless I included it in this folder.

# Flag
```
5275e087-d244-4871-74f4369626c0
```


