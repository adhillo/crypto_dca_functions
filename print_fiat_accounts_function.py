# also put in requirements.txt for Google Cloud Functions with just package name "cbpro"
import cbpro 

# Gathered from Coinbase, replace the '???'
my_passphrase = "???"
my_secret = "???"
my_key = "???"

auth_client = cbpro.AuthenticatedClient(my_key, my_secret, my_passphrase)


def fiat_source_id_finder(request):
    for fiat_account in auth_client.get_payment_methods():
        print(f'name: {fiat_account["name"]}, currency: {fiat_account["currency"]}, type: {fiat_account["type"]}, id_number: {fiat_account["id"]}')
    return 'print fiat accounts function run - check logs'