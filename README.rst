***********
pyCoinPayments - Python API client for `CoinPayments <https://www.coinpayments.net>`_
***********


This is an unofficial client for CoinPayments, a website that exposes an API which allows you to accept over *75 cryptocurrencies.* The documentation was a little strange at times so I made this to simplify and help others overcome some of the initial hurdles of trying to use their API. There's some interesting functionality I added to this so you never have to deal directly with the returned json. A c#.net version is coming soon with javascript soon after. 
  
  
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

    API_KEY     = 'You Public API Key'
    API_SECRET  = 'You API Secret'
    IPN_URL = 'Your Callback URL'

    ## Parameters for your call, these are defined in the CoinPayments API Docs
    ## https://www.coinpayments.net/apidoc
    post_params = {
        'amount' : 10,
        'currency1' : 'USD',
        'currency2' : 'LTCT'
    }

    client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)

    transaction = client.createTransaction(post_params)

    print transaction
    #Prints out transaction details
    
    print transaction.amount
    print transaction.address
    
You can reference any of their return fields within the json as a field on the variable. For example the transaction.amount would print out the amount of requested cryptocurrency, same with the address. Their documentation outlines what it returned for fields in each request. The rest of the API client is very similar. Parameters are passed into the API method using a python dictionary, order in this case does not matter because the HMAC and encoded URL are generated at the same time.
    
