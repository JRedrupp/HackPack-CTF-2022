# TupleCoin
## Description

TupleCoin is launching their eponymous cryptocurrency today, and their flamboyant and capricious CEO is challenging you to bring home a bug bounty. Can you crack the crypto?!
`tuplecoin.cha.hackpack.club`

## Exploration
Heading over to that site I see a website where a user can create an account and transfer coins to and from accounts.

There is a bounty page asking hunters to try and steal coins from Tuco

Info:
 - His account number is 314159265, and you can't have it.
 - He absolutely hates robots, especially ones from Silicon Valley.
 - He never found a sack of gold, or crypto, that wasn't worth almost dying for until he thought better of it.
 
 Lets claim an account.

 Number - #452139554 (3.14159 TuCo)

 ## Transferring Money
 I see we can Transfer money. Lets Transfer to Tuco's account and check out the request.

 It made 2 Post Methods:
 1:
 ```python
 url = 'https://tuplecoin.cha.hackpack.club/api/transaction/certify'
 body = {"from_acct":452139554,"to_acct":314159265,"num_tuco":1}
 resp = {
	"transaction": {
		"from_acct": 452139554,
		"to_acct": 314159265,
		"num_tuco": 1
	}
}
 ```
 2:
 ```python
 url = 'https://tuplecoin.cha.hackpack.club/api/transaction/commit'
 body = {
	"auth_tag": "d4f7afe3dd729d535319a72bda14951ffbc822ce10c91b8fd8a4d7d87f97498b",
	"transaction": {
		"from_acct": 452139554,
		"num_tuco": 1,
		"to_acct": 314159265
	}
}
 resp = "OK"
 ```

So i'll try and do the request myself as it is the UI that stops me from entering an account that is not mine as the `from_acct`/

### Change the Requests

I'll look to make the requests in Python.
I Try the following:
```python
import requests

json_data = {
    'from_acct': 314159265,
    'to_acct': 452139554,
    'num_tuco': 1,
}

response = requests.post('https://tuplecoin.cha.hackpack.club/api/transaction/certify', json=json_data)

print(response.content)
```
and get
```python
b'{"detail":"Ha! You think you can steal from Tuco so easily?!!"}'
```

So evidently there is some authentication going on.

Lets look into this `auth_tag` more...

### Decoding the Auth Tag

I get the following Auth Tag - `d4f7afe3dd729d535319a72bda14951ffbc822ce10c91b8fd8a4d7d87f97498b`
Maybe there is something I can do to fake it.

Lets spin up cyberchef and try and decode what looks like hex.
Decoding it in Hex doesn't seem to yield me anything useful.

### Own Tuco's Account
Maybe i can look to see if I can own Tuco's Account somehow.

Lets go back to the accounts page and check what the request is when I create an account.

```bash
curl 'https://tuplecoin.cha.hackpack.club/api/account/claim?acct_num=5464654'

response - {
	"balance": {
		"acct_num": 5464654,
		"num_tuco": 3.141592653589793
	},
	"auth_tag": "2876e7121c1cc941ac25edb58e3ca970bec3c79d547739b51f8e78d47dc37231"
}
```

So a claim sends a post reques with the account number in the parameters and then returns the account numnber, balance and auth_tag.

Lets see what happens if i add Tuco's account number.

```python
import requests

params = {
    'acct_num': '314159265',
}

response = requests.post('https://tuplecoin.cha.hackpack.club/api/account/claim', params=params)
print(response.content)

b'{"detail":"That\'s Tuco\'s account number! Don\'t make Tuco mad!"}'
```


There seems to be some entrypoint i'm not getting here.
Lets wait until the writeups - my thought is that it is to do with reverse engineering the `auth_tag` however I'm not sure where to start as it doesnt decode to anything useful.