# Invitation
## Team
cyberwehr: [CTFtime](https://ctftime.org/team/35295)

## Description
Link to original on CTFtime: [Description](https://ctftime.org/task/15697 "CTFtime challenge description")
- None

## Files
- Invite.docx

## Used tools
- Powershell

## Solution

The only thing that was given was a Word document with Macros enabled. So the first thing I did was to check the Macros that were implemented.
There was just one file with one function and some additional code. Everything was pretty obfuscated. 
So after some time understanding the code I knew the following things:
- The code was 99% hex strings
- These strings were used to construct code on runtime and thus hide it
- After some processing, these strings were passed into the Visual Basic SHELL function which executes code.

After deobfuscating the strings, they were revealed to be malware.
After some more deobfuscating and looking, the key was in this malware constructed of many different commands


The obfuscation-function which takes the strings and converts them into Powershell commands:

```
Private Function byteToChar(ByVal gwndcowqyulk As String) As String
    Dim cjzkqjwvtdxr As Long
    For cjzkqjwvtdxr = 1 To Len(gwndcowqyulk) Step 2
        byteToChar = byteToChar & Chr$(Val("&H" & Mid$(gwndcowqyulk, cjzkqjwvtdxr, 2)))
    Next cjzkqjwvtdxr
End Function
```

## Flag
```
CHTB{maldocs_are_the_new_meta}
```