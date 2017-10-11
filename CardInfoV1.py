'''
Project: PayU Turkey Card Info v1 Python3 Sample Code
Author: Göktürk Enez
'''
# Importing required libraries.
import hmac
import hashlib
from urllib.request import Request, urlopen
import collections
import time

#Secret Key
secret = 'SECRET_KEY'
binno = "557829"
array = collections.OrderedDict()
array['merchant'] = 'OPU_TEST'
array['timestamp'] = str(time.time()).split('.')[0]

# Initializing the hashstring @param
hashstring = ''

# Sorting Array @params
for k, v in array.items():
    print(v)

# Adding the UTF-8 byte length of each field value at the beginning of field value
    hashstring += str(v)
print(hashstring)

# Calculating signature
signature = hmac.new(secret.encode('utf-8'), hashstring.encode('utf-8'), hashlib.sha256).hexdigest()
print(signature)

# Adding Signature @param to dict
array['signature'] = signature

# Endpoint
url = 'https://secure.payu.com.tr/api/card-info/v1/{0}?merchant={merchant}&timestamp={timestamp}&signature={signature}'.format(binno, **array)
print(url)

# Sending Request to Endpoint
request = Request(url)
response = urlopen(request).read().decode()

# Printing result/response
print(response)

