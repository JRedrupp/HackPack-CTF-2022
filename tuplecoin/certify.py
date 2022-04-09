import requests

json_data = {
    'from_acct': 314159265,
    'to_acct': 452139554,
    'num_tuco': 1,
}

response = requests.post('https://tuplecoin.cha.hackpack.club/api/transaction/certify', json=json_data)

print(response.content)