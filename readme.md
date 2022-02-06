## Repeating Deposits & Buys on Coinbase

The detailed walkthrough lives on my Substack - https://sandcastle.substack.com/publish/post/48075762

This is a project designed to make it straightforward to repeatedly buy a fixed amount of the cyrptos of your choice. 

There are 2 files - designed as functions to be easy to automate in Google Cloud Functions or AWS Lambda. 


_print_fiat_accounts_function.py_ - This code will print out all the possible fiat funding accounts connected to your Coinbase account. It is intended for one time use to identify the ID of the account you wish to funnel recurring deposits from. 

_deposit_buy_function.py_ - This code will deposit a fixed amount of $ & invest it by percentage into the set of cryptos you chose. It will be set to run on an automated schedule per Google Cloude Scheduler in the substack walk through. 

