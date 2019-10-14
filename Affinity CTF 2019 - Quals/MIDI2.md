# MIDI2
## Team
SmashTrash: [CTFtime](https://ctftime.org/team/86655)

## Description
Link to original on CTFtime: [Description](https://ctftime.org/task/9190 "CTFtime challenge description")
> pcap file was given

## Files
A .pcap.gz file was given.

## Used tools
- Wireshark
- Audacity

## Solution
MIDI2 was a rather difficult Misc challange, as it was the one with the most points of its category.

Unpacking the .gz with
###### Command:
```
gunzip midi.pcap.gz
```
gives the .pcap file.

Opening it with wireshark quickly reveals some interesting packets:

![Imgur](https://i.imgur.com/LVwzP5K.png)

here we can see a request for the "/keyfile" and the response to it. Looking at the response:

![Imgur](https://i.imgur.com/xoxGpt3.png)

we can see s string containing the keyword "CLIENT_RANDOM". This is a hint for us to decrypt the TLS1.2 traffic at the beginning of the pcap.
Looking at the Wireshark documentation we see that we have extracted the CLIENT_RANDOM and the hex-encoded clear text master secret:

###### Documentation:
```
"CLIENT_RANDOM xxxx yyyy"
Where xxxx is the client_random from the ClientHello (hex-encoded)
Where yyyy is the cleartext master secret (hex-encoded)
(This format allows non-RSA SSL connections to be decrypted, i.e. ECDHE-RSA.)
```

This is enough information to decrypt the traffic. This is done by going into the Wireshark TLS settings, creating a file with the string we found and linking it there.
This reveals some HTTP2 packets:

![Imgur](https://i.imgur.com/HdDkJm5.png)

The DATA[1] packet looks interesting so we extract its data into a file and look at it with the "file" command tool to reveal its filetype:
###### Command:
```
file http2_data
```

###### Output:
```
midifile.midi: Standard MIDI data (format 1) using 1 track at 1/220
```

Now we know why this challange is called MIDI2. So now we got a MIDI file. Looking at it with Audacity reveals an interesting pattern:

![Imgur](https://i.imgur.com/FsPlC9I.png)

After some investigation it turns out the notes on the top are irrelevant and the ones at the bottom resemble binary numbers:

![Imgur](https://i.imgur.com/Wy1sNYh.png)

and if we look up the ASCII table we can translate those numbers into letters and if we do this for the whole file we get the flag

## Flag
```
AFFCTF{3s0t3r1c_l4ngs_4r3_Fun}
```


