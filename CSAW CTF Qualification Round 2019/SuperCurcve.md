# Challenge Name
## Team
SmashTrash: [CTFtime](https://ctftime.org/team/86655)

## Description
Link to original on CTFtime: [Description](https://ctftime.org/task/9223 "CTFtime challenge description")
> We are a super legitimate crypto company asking you to complete an audit on our new elliptic curve, SuperCurve, in order to show those hecklers at WhiteHat how legit we are! nc crypto.chal.csaw.io 1000

## Files
A python script of the code running on the server.

## Used tools
- Python

## Solution
In the main method of the server.py script was an implementation of a elliptic-curve crypto scheme.

Since the field, order, a, b and the point G were given, the only thing that was hidden was the "secret_scalar".

I executed the script a couple of times on my own machine and printed the secret for test purposes.

I noticed that it was very small and so it was obvious it was possible to brute-force the algorithm.

```python
for i in range(10000):
        if curve.mult(i, base) == pub:
            print(i)
            break
```

Then I entered the public key the server had given me and brute-forced it.

I entered the secret_scalar into the console and got the flag.

## Flag
```
flag{use_good_params}
```