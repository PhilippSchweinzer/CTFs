# Enhanced PLC Encryption Standard
## Team
SmashTrash: ctftime.org/team/86655

## Description
Link to original on CTFtime: [Description](http://www.test.com "CTFtime challenge description")
> Our IT department wants us to encrypt our PLC traffic. So we created our own encryption scheme, called the Enhanced PLC Encryption Standard.
> The idea is simple, and brilliant:
- Every PLC gets the shared secret password – this is so long, nobody can brute force it.
- If two devices want to communicate, one of them (A) sends a unique challenge to the other device (B).
- B gets the challenge, and hashes each character of the password with the challenge: response = hash(char + challenge).
- For security purposes, we use SHA-256 here (no insecure MD5 or SHA-1!). We also hash each character separately, so the full password can't be leaked if an attacker records the responses.
- B sends a lot of responses back to A. A knows the length of the password, and the password itself. So A can terminate the connection if responses are missing, or if there are too many responses.
- A also conducts hash(char + challenge), and compares every response. If there is any mismatch, A terminates the connection.
- If every response matches, A and B start to communicate using the shared secret password as the key. We use 3DES in CBC mode here, because our PLCs don't support military-grade AES.
> We sent a sample log to IT. For us, this looks clearly encrypted and secure. Our key is 24 bytes strong. One website says it takes 76 SEXTILLION YEARS to crack this.
> P.S. We didn't find a possibility to implement an IV, so it's 8 times 0.

## Files
A log file called 20191003-epes-test.log was given and the content was a snipped of the self made encryption being used to transfer a message:
INCLUDE PICTURE


## Used tools
- [CyberChef](http://icyberchef.com/)
- Python 3.7

## Solution
The problem was pretty straight forward: Go through every step of the self made encryption and try to reverse it.
As a first step device A sends device B the so called challenge. This is the salt which is then added to every hash operation. The salt is transmitted in clear text.
Then follow 24 messages consisting of a SHA-256 hash.
Because the algorithm hashes every single character on its own it is trivila to brute-force it.
I wrote a little python program to do so:

```python
from hashlib import sha256

hashes = ["5daaa90b563017184bb8dc277f63f02366a59519113b9ac87ba6fd46f93dc1ff",
	"01b4e096bcb756f176beaa2ebbb99ef144dc3fb0bc2d27e5fe63a5601e3abace",
	"db00873b16b99e32c6c67672ea52df6769cf7801ebb3dbf168f5b2e0f2ecc3bf",
	"146797c2afa9e1a2ad2ff8f05de647702949923f9a5dc12b26452b2c520c3340",
	"67dacf84cce58a6bf283d62354ad05052fe42808b59866dfb30137a08b4ff12d",
	"c13dcb97dccf5e3942324409202a103eb9f007866f247ebea48e2a67cbbcd07f",
	"d72a057ba7fddd03cae3d3f7d75f865fb1c2ddbe8ef65afc0ce8fbc0fc4122cb",
	"6eddcbed70839add89ed38c3068ffe6780f7b86f0bc7276e2d7e06f47ea2e05a",
	"146797c2afa9e1a2ad2ff8f05de647702949923f9a5dc12b26452b2c520c3340",
	"d72a057ba7fddd03cae3d3f7d75f865fb1c2ddbe8ef65afc0ce8fbc0fc4122cb",
	"db00873b16b99e32c6c67672ea52df6769cf7801ebb3dbf168f5b2e0f2ecc3bf",
	"4c1b4d5c926c4160b19effa23c93710f3086866a74aca5dad801fd81118d8d68",
	"67dacf84cce58a6bf283d62354ad05052fe42808b59866dfb30137a08b4ff12d",
	"4d4ac18fd35d3707fc3671d372bbe494691b01611632359c7d39b7becbfc1184",
	"4d4ac18fd35d3707fc3671d372bbe494691b01611632359c7d39b7becbfc1184",
	"571aef6ff2d25a7a32c3a9fc3b1c06d874979f082b5e90b0c30a01203885a2b0",
	"fdc984b4a8fec04fcb9faacf99f9dbfd0fbef0a33906c3fa89d9fb0b63947a0e",
	"146797c2afa9e1a2ad2ff8f05de647702949923f9a5dc12b26452b2c520c3340",
	"588917d1f04bbc53aed45c6db061092dde79af4c5fc3f01e96eab2e86b30e581",
	"a122c3b77eaf01341cc0c7da6e45e7ff9ff57f97a4c9542ad7e96a0f28499029",
	"fdc984b4a8fec04fcb9faacf99f9dbfd0fbef0a33906c3fa89d9fb0b63947a0e",
	"8419e8ddded5e57e71db42841f865f9fd751ec3b8e0395ba36818b52a015e47e",
	"af621e444935d03bc563e24982ad25d19c3ca4f52341232c978f7e63c809a27e",
	"572c394ed63437090aec71c806d92a2a10d5e3651eb30a91d1573ba3d37f4ad9",
	"24066241b2c524457a58196640197307469c18fd71bb6de304501a8d50981e25",
	"07d89c21b9dd1eb81e26d52398da02a3d000ba82f9198b2b3311cb1cda901418"]
	
salt = "VkcV29UKCGbfuZyqea7uKbZ9"
	
for hash in hashes:
	for char in range(255):
		data = str(chr(char) + salt).encode('utf-8')
		if str(sha256(data).hexdigest()) == hash:
			print(chr(char), end="")
```

This outputs:

```
ultras3cr3tpa$$w0rd2019!
```

Now i had the password and the IV(8 zeros) of the 3DES CBC encryption and was able to reverse the 2 messages send between the devices.
The decrypted messages contained the flag.

## Flag
```
test{never-roll-your-own-crypto}
```