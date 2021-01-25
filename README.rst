***********
pyCoinPayments - Python API client for `CoinPayments <https://www.coinpayments.net>`_
***********

Updates
#####
This library has now been converted to work with python3



This is an unofficial client for CoinPayments, a website that exposes an API which allows you to accept over *75 cryptocurrencies.* 
  
  
The Absolute Basics
#####
CoinPayments has the following API routes available to POST against. This is a POST only api where API calls are made using a 'cmd' parameter.

Their official API endpoint is https://www.coinpayments.net/api.php all calls are made against the same URL. Normally (without this client) you'd need to pass a 'cmd' parameter like below to the endpoint to distinguish between the API calls. This client simplifies things so calling each API method automatically does this for you.

.. code:: bash

    {'cmd':'get_basic_info'}
is how you would call the 'Get Basic Account Information' API, this is handled automatically by the methods in this API so calling

.. code:: python

    CryptoPayments().getBasicInfo()
does this for you.


Basic Program
-------------

To show you a basic using of the program I'm going to be calling the create_transaction method on the CoinPaymentsAPI

.. code:: python

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
    
You can reference any of their return fields within the json as a field on the variable. For example the transaction.amount would print out the amount of requested cryptocurrency, same with the address. Their documentation outlines what it returned for fields in each request. The rest of the API client is very similar. Parameters are passed into the API method using a python dictionary, order in this case does not matter because the HMAC and encoded URL are generated at the same time.
    
