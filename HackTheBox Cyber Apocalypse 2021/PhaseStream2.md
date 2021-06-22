# Phase Stream 2
## Team
cyberwehr: [CTFtime](https://ctftime.org/team/35295)

## Description
Link to original on CTFtime: [Description](https://ctftime.org/task/15689 "CTFtime challenge description")

> The aliens have learned of a new concept called "security by obscurity". Fortunately for us they think it is a great idea and not a description of a common mistake. We've intercepted some alien comms and think they are XORing flags with a single-byte key and hiding the result inside 9999 lines of random data, Can you find the flag?

## Files
file with 9999 newline-terminated strings

## Used tools
- Python

## Solution

Because the key was just 1 byte sized, I simply iterated over all strings in the file. Then I XORed the first byte with the character "C" and compared it to the second XORed byte which should then yield "H".
Thus i could easily iterate over a large number of strings.

Ciphertext: 060d11073e2b76762129761a742b1a711a2d713c363171262e38

Key: 0x45

The Python code:
```
with open('./output.txt', 'r') as f:
    lines = f.readlines()
# C: 0x43
# H: 0x48
# T: 0x54
# B: 0x42
for line in lines:
    key = int(line[:2], 16) ^ 0x43
    if int(line[2:4], 16) ^ key == 0x48:
        if int(line[4:6], 16) ^ key == 0x54:
            print('Found:', line, key)
```

## Flag
```
CHTB{n33dl3_1n_4_h4yst4ck}
```