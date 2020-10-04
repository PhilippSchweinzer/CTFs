# CSP CTF Bypass Level 03
## Team
Philogic (Solo)

## Description
This challenge is about bypassing the CSP (Content-Security-Policy). Please start the service from RESOURCES and enter some java script. If you manage to get your own javascript being executed, you're good. 
CSP:
```
default-src 'self'; script-src https://cutt.ly https://accounts.google.com/secure/
```

## Files
- None

## Used tools
- None




## Solution

The first thing I did was to look at cutt.ly. It is a URL-shortening service, which shortens a given URL and redirects to it when the shortened version is called. The other link which was allowed was https://accounts.google.com/secure/. Checking it there was no website available under this link, which raised some suspicions.

After some research I found out that the CSP only checks the host after a redirect and not the whole URL. This meant that I could create a shortened URL to any service that was hosted on accounts.google.com. So, I tried to abuse a JSONP endpoint to trigger a callback with the URL https://accounts.google.com/o/oauth2/revoke?callback=alert(1) shortened to https://cutt.ly/JdQxLd5. But it would not work when the URL was included into a HTML script-tag, because cutt.ly just sent a 403 Forbidden.

Then I noticed that when I used a script-tag to load the URL, it would include a referer in the request header which was the URL of the site that made the request. Cutt.ly was using this header to forbid certain types of requests made to their site.

But this header could easily be removed by specifying a meta-tag that disabled it:

```
<meta name="referrer" content="no-referrer">
```

Then I just combined the meta and script-tag and successfully executed the XSS:
```
<meta name="referrer" content="no-referrer"><script src="https://cutt.ly/JdQxLd5"></script>
```

![Imgur](https://i.imgur.com/bqKrs3M.png)

## Flag
- None