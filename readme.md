## Repeating Deposits & Buys on Coinbase

The detailed walkthrough lives on my Substack - https://sandcastle.substack.com/p/how-to-build-a-bitcoin-buying-bot

This is a project designed to make it straightforward to repeatedly buy a fixed amount of the cyrptos of your choice. 

There are 2 files - designed as functions to be easy to automate in Google Cloud Functions or AWS Lambda. 


_print_fiat_accounts_function.py_ - This code will print out all the possible fiat funding accounts connected to your Coinbase account. It is intended for one time use to identify the ID of the account you wish to funnel recurring deposits from. 

_deposit_buy_function.py_ - This code will deposit a fixed amount of $ & invest it by percentage into the set of cryptos you chose. It will be set to run on an automated schedule per Google Cloude Scheduler in the substack walk through. 



Other builders whose material I found invaluable:

1. Dan Paquin who wrote the cbpro python library 
2. Ben Dickson who showed me the wisdom of Google Cloud Functions
3. Rhett Reisman who has put together fantastic Youtube walk throughs on crypto, exchanges, and more

