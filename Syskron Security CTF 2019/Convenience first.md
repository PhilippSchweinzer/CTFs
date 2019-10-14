# Convenience first
## Team
SmashTrash: [CTFtime](https://ctftime.org/team/86655)

## Description
Link to original on CTFtime: [Description](https://ctftime.org/task/9439 "CTFtime challenge description")
> If I got access to that warehouse PC, I could check out some nice items. Could you get me a valid username and password combination? It won’t be to your disadvantage.
> Flag format: {username-password}

## Files
A picture of a monitor with some bar codes taped on it was given:
![screen-logistics-center](https://i.imgur.com/9tt5Loh.jpg)

## Used tools
- [Barcode Reader](https://online-barcode-reader.inliteresearch.com/)

## Solution
The first thing i did was scan all the barcodes on screen.

This way i got the username "User0011" from the barcode on the top middle of the screen.

I also found out that these barcodes were in Code128 format, which came in handy in the next step.

On the picture there is one barcode which is partially hidden behind a rubber band. It was obvious that this contained the password, but was not trivial to scan.

So i read some documentation about Code128 and tried to decode it by hand. This was fairly easy and can be seen on the following picture:

![Barcoder decode](https://i.imgur.com/avFXh7O.png)

When it was time to decode the hidden part i saw that it started with 4 black and ended with 1 space unit.

This let to only a tiny subset of possible letters of about 5 choices.

My first thought was to calculate the missing letter with the checksum on the end of the barcode, but i was lazy and tried to just enter one after the other into the flag submission.

Luckily the first one ("m") was the correct one and i got it right away.



## Flag
```
{User0011-AAq5rm11}
```