# CSP CTF Bypass Level 01
## Team
Philogic (Solo)

## Description
This challenge is about bypassing the CSP (Content-Security-Policy). Please start the service from RESOURCES and enter some java script. If you manage to get your own javascript being executed, you're good. 
CSP: 
```
default-src 'self'; script-src 'nonce-MTMuMDUuMjAyMC8xNjo0Nw=='
```

## Files
- None

## Used tools
- None

## Solution

The security problem of the CSP was the use of a predictable nonce. The current timestamp was base64-encoded and used as a nonce for a javascript section.
Due to the fact that the nonce is predictable, it is possible to craft a payload with the correct nonce. Then the Browser thinks that the code belongs to the page and executes it.

Exploit:
```
<script nonce="MTMuMDUuMjAyMC8xNjo0Nw==">alert(1)</script>
```
![Imgur](https://i.imgur.com/4wCBCol.png)

## Flag
- None