# CSP CTF Bypass Level 02
## Team
Philogic (Solo)

## Description
This challenge is about bypassing the CSP (Content-Security-Policy). Please start the service from RESOURCES and enter some java script. If you manage to get your own javascript being executed, you're good. 

## Files
- None

## Used tools
- None

## Security Problem

The CSP of the site allows script-tags from accounts.google.com. Because it is possible to embed HMTL into the site via the input box, if accounts.google.com has a JSONP endpoint it could be abused to execute javascript code. 


## Solution

After some search online i found the JSONP endpoint https://accounts.google.com/o/oauth2/revoke. I then used it to craft the exploit:

Exploit:
```
<script src="https://accounts.google.com/o/oauth2/revoke?callback=alert(1)"></script>
```
Due to the workings of the JSONP system, a request is made and the callback is executed as soon as the response arrives.

![Imgur](https://i.imgur.com/HzpuH4o.png)

## Flag
- None