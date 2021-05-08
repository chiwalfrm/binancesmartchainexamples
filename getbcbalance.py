#this is for the Binance Chain (BEP2)
import requests
import sys
if len(sys.argv) < 1:
        print("ERROR: Must specify address.")
        exit()
r = requests.get(url='https://dex.binance.org/api/v1/account/' + sys.argv[1])
for item in r.json()['balances']:
        total = float(item['free']) + float(item['frozen']) + float(item['locked'])
        print(item['symbol'].ljust(15), str(total).rjust(20))
