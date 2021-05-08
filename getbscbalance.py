import sys
from decimal import *
from os import path
from bscscan import BscScan
bscscankey = 'BSCSCAN_API_KEY'
if len(sys.argv) < 2:
        print("ERROR: Must specify file containing api configuration.")
        print("Optional arguments: 'tokens'")
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
print('INFO: File', sys.argv[1], 'Loaded', file=sys.stderr)
print('INFO: my_address =', my_address, file=sys.stderr)
print('INFO: my_tokens =', my_tokens, file=sys.stderr)
bsc = BscScan(bscscankey)
if len(sys.argv) > 2 and sys.argv[2] == 'tokens':
        for coin, value in my_tokens.items():
                balancetoken = bsc.get_acc_balance_by_token_contract_address(contract_address=value, address=my_address)
                if coin == '':
                        coin = 'blank'
                if coin == 'marscat':
                        divisor = 1
                else:
                        divisor = Decimal(10 ** 18)
                if float(balancetoken) != 0:
                        print(coin.ljust(16), '{0:.18f}'.format(float(balancetoken)/float(divisor)).rjust(37).rstrip('0').rstrip('.'))
else:
        print('BNB             ', '{0:.18f}'.format(float(bsc.get_bnb_balance(address=my_address))/1e+18).rjust(37).rstrip('0').rstrip('.'))
