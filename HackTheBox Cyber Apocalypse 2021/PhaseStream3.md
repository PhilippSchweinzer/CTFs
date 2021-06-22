# Challenge Name
## Team
cyberwehr

## Description
Link to original on CTFtime: [Description](https://ctftime.org/task/15690 "CTFtime challenge description")

The aliens have learned the stupidity of their misunderstanding of Kerckhoffs's principle. Now they're going to use a well-known stream cipher (AES in CTR mode) with a strong key. And they'll happily give us poor humans the source because they're so confident it's secure!

## Files
- 2 ciphertexts

## Used tools
- Python

## Solution

Given were two AES-CTR encrypted ciphertexts. The python script with which they were encrypted was also known.
When I analyzed the script I noticed that both of the ciphertexts used the same initialization vector and key.
Since the plain text of one ciphertext was also known I was able to get the flag with the following XOR operations:

```
plaintext_flag = (ciphertext1 XOR plaintext1 XOR) XOR ciphertext_flag
```

The encryption script:
```
KEY = os.urandom(16)

def encrypt(plaintext):
    c = Counter.new(128)
    #print(c)
    cipher = AES.new(KEY, AES.MODE_CTR, counter=c)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext.hex()

test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."
print(encrypt(test))

with open('flag.txt', 'rb') as f:
    flag = f.read().strip()

print(encrypt(flag))
```

## Flag
```
CHTB{r3u53d_k3Y_4TT4cK}
```