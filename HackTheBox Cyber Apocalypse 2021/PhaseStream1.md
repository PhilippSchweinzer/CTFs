# Phase Stream 1
## Team
cyberwehr: [CTFtime](https://ctftime.org/team/35295)

## Description
Link to original on CTFtime: [Description](https://ctftime.org/task/15696 "CTFtime challenge description")

> The aliens are trying to build a secure cipher to encrypt all our games called "PhaseStream". They've heard that stream ciphers are pretty good. The aliens have learned of the XOR operation which is used to encrypt a plaintext with a key. They believe that XOR using a reapeted 5-byte key is enough to build a strong stream cipher. Such silly aliens! Here's a flag they encrypted this way earlier. Can you decrypt it (hint: what's the flag format?)

## Files
- None

## Used tools
- Python

## Solution

The given ciphertext was a hex string. To decrypt it one needs to know the correct 5-byte key to decrypt it with XOR.
Because the first 5 characters of the plaintext were known due to the flag format (CHTB{...}), I simply calculated the key.

Ciphertext: 2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904

Key: 6d796b6579

Plaintext: CHTB{u51ng_kn0wn_pl41nt3xt}

## Flag
```
CHTB{u51ng_kn0wn_pl41nt3xt}
```