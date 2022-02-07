# also put in requirements.txt for Google Cloud Functions with just package name "cbpro"
import cbpro 

# Gathered from Coinbase, replace the '???'
my_passphrase = "???"
my_secret = "???"
my_key = "???"

auth_client = cbpro.AuthenticatedClient(my_key, my_secret, my_passphrase)

# Gathered from running "print_fiat_accounts_function.py", replace the '???' with the ID 
# of the fiat funding account which will deposit money into Coinbase
fiat_funding_account_id = "???"


# Your choice on whether to deposit everytime you run this, switch to False if you just want to buy 
# note if you don't have funds, buying will fail
deposit_on_run = True

# quantity of dollar investment for each round buying; if "deposit_on_run" is True, you will first bring
# in this quantity as USD
investment_size = 100

# Set up your recurring buy goals, add new pairs to buy with USD
# for example to buy link add the line -> "buys['LINK-USD'] = {'percent': .1, 'rounding': 3}"
# make sure your percentages do not go above a total of 1 (i.e, 100%)
# the ronding is set based on the smallest unit can buy on Coinbase Pro
# check logs for failed buys for more details - you may need to adjust rounding for different coins
buys = {}
buys['BTC-USD'] = {'percent': .8, 'rounding': 5}
buys['ETH-USD'] = {'percent': .2, 'rounding': 5}


########################################################
# There should be no need to touch any of the below code
# unless you are comfortable with coding
########################################################

def deposit_and_invest(event, context):

    # check if we will deposit on each run
    if deposit_on_run:
        deposit_response = auth_client.deposit(amount=investment_size, currency='USD', payment_method_id=fiat_funding_account_id)
        print(f'Deposit Info:{deposit_response}')
        print('\n')

    # iterate through dictionary of buys & 
    for key in buys.keys():

        print(key)

        # get bid price of a product
        currentPrice = auth_client.get_product_ticker(key)['bid']

        print(currentPrice)

        # place limit order based on bid price, reduce total spend by 3% to account for possible fees (highly conservative)
        order = auth_client.buy(
                price=currentPrice,
                size=round(buys[key]['percent']*investment_size/float(currentPrice) * .97, buys[key]['rounding']),
                order_type='limit',
                product_id= key,
                overdraft_enabled=False
            )
        
        print(order)
        print('\n')

    return 'deposit & buy functon ran - check logs'