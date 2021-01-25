from configparser import SafeConfigParser
from pyCoinPayments import CryptoPayments


# Loading configuration file using configparser with API Keys for CoinPayments.net
parser = SafeConfigParser()
parser.read('config.ini')
API_KEY = parser.get('apikeys', 'API_KEY')
API_SECRET = parser.get('apikeys', 'API_SECRET')
IPN_URL = parser.get('apikeys', 'IPN_URL')


## Parameters for your call, these are defined in the CoinPayments API Docs
## https://www.coinpayments.net/apidoc

create_transaction_params = {
    'amount' : 10,
    'currency1' : 'USD',
    'currency2' : 'BTC'
}

#Client instance
client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)

#make the call to createTransaction crypto payments API
transaction = client.createTransaction(create_transaction_params)


if transaction['error'] == 'ok':  #check error status 'ok' means the API returned with desired result
    print (transaction['amount']) #print some values from the result
    print (transaction['address'])
else:
    print (transaction['error'])


#Use previous tx Id returned from the previous createTransaction method to test the getTransactionInfo call
post_params1 = {
    'txid' : transaction['txn_id'],    
}


transactionInfo = client.getTransactionInfo(post_params1) #call coinpayments API using instance

if transactionInfo['error'] == 'ok': #check error status 'ok' means the API returned with desired result
    print (transactionInfo['amountf']) 
    print (transactionInfo['payment_address'])
else:
    print (transactionInfo['error'])