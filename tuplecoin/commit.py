import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json; charset=utf-8',
    'Origin': 'https://tuplecoin.cha.hackpack.club',
    'Connection': 'keep-alive',
    'Referer': 'https://tuplecoin.cha.hackpack.club/app/index.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'transaction': {
        'from_acct': 314159265,
        'to_acct': 452139554,
        'num_tuco': 101000,
    },
    'auth_tag': 'd4f7afe3dd729d535319a72bda14951ffbc822ce10c91b8fd8a4d7d87f97498b',
}

response = requests.post('https://tuplecoin.cha.hackpack.club/api/transaction/commit', headers=headers, json=json_data)
print(response.content)