
from django.http import HttpResponse, JsonResponse
import hashlib
from django.core import serializers
import base64
import os
from wsgiref.util import FileWrapper
import zipfile
from io import BytesIO
from wsgiref.util import FileWrapper

import json
from web3 import Web3, HTTPProvider
from ethereum.utils import ecrecover_to_pub, sha3
from eth_utils.hexidecimal import encode_hex, decode_hex, add_0x_prefix
import codecs
from gatekeeper.models import Details
from django.forms.models import model_to_dict
from django.conf import settings

#TODO setup to allow user to determine network
web3 = Web3(HTTPProvider('https://rinkeby.infura.io'))

contractAddress = getattr(settings, 'CONTRACT_ADDRESS')
thisServiceID = getattr(settings, 'SERVICE_ID')

with open('./gatekeeper/factoryDRS.json', 'r') as abi_definition:
    abi = json.load(abi_definition)
fContract = web3.eth.contract(contractAddress,abi=abi)

def index(request):
    """Index to test connection to server.

    Tests connection to server

    Args:
        request: a request object
    Returns:
        A successful connection string string
    """
    return HttpResponse("Hello, You're at the gatekeeper")

def data(request, address_id, signature, message_hash, parameter, key_hex):
    """Fetches rows data from sql database or file folder.

    Validates user and request agains the blockchain.
    If passes either returns json object or file based on request

    Args:
        request: a request object
        address_id: The address id of the address_id
        signature: The requesters signature.
        message_hash:  The hashed message.  Used for signature verification
        parameter: the parameter to use to determine the database and parameter
        key:  the id of the key to check against

    Returns:
        A json object containing data or a file to the requestor
    """
    parameter_hex=web3.fromAscii(parameter)
    parameter_hex_data=parameter_hex[2:]
    key_bytes=web3.toBytes(hexstr=key_hex)
    parameter_bytes=web3.toBytes(hexstr=parameter_hex)

    #recover public key
    r = int(signature[0:66], 16)
    s = int(add_0x_prefix(signature[66:130]), 16)
    v = int(add_0x_prefix(signature[130:132]), 16)
    if v not in (27,28):
        v += 27
    pubkey = ecrecover_to_pub(decode_hex(message_hash), v, r, s)

    #retrieves information from key based on parameter
    account_id=fContract.call().getKeyData(key_bytes,parameter_bytes)
    account_id=account_id.strip()
    owner=fContract.call().isKeyOwner(key_bytes,address_id)
    hexId=web3.fromAscii(account_id)

    #TODO setup up to allow for custom parameters

    if parameter == 'account_number':
        account_id=int(hexId.rstrip("0"), 16)

    #Get the service this key belongs too
    keyData=fContract.call().getKey(key_bytes)
    serviceFromKey = web3.fromAscii(keyData[4])

    #if parameter is an account number it retreives and returns the json object
    #TODO break into seperate endpoints

    if parameter == 'account_number' and thisServiceID == serviceFromKey and encode_hex(sha3(pubkey)[-20:]) == address_id and owner:
        print(':                  success              :')
        result=Details.objects.filter(account_number=account_id)
        dataResult = serializers.serialize('json', result)
        return JsonResponse(dataResult, safe=False)

        #if it is a file it sends the filie for download
    elif parameter == 'file' and thisServiceID == serviceFromKey and encode_hex(sha3(pubkey)[-20:]) == address_id and owner:
        #TODO finalize file download
        module_dir = os.path.dirname(__file__)  # get current directory
        filename=module_dir+'/file/'+account_id
        filename=filename.strip()
        filename=filename.strip('\x00')
        with open(filename, 'rb') as f:
            response = HttpResponse(f.read())
            response['Content-Type'] = 'application/octet-stream'
            response['Access-Control-Expose-Headers'] = 'Content-Disposition'
            response['responseType'] = 'application/download'
            response['Content-Disposition'] = 'attachment; filename="'+account_id+'"'
            response['Content-Length'] = os.path.getsize(filename)
            return response
    else:
        print(':                  fail              :')
        return JsonResponse({'status':'false','message':'Invalid user'}, status=500)
