import requests

params = {
    'acct_num': '314159265',
}

response = requests.post('https://tuplecoin.cha.hackpack.club/api/account/claim', params=params)
print(response.content)