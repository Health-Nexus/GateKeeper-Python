
from django.http import HttpResponse, JsonResponse
import hashlib
from django.core import serializers
import base64
import os
from wsgiref.util import FileWrapper

import json
from web3 import Web3, HTTPProvider
from ethereum.utils import ecrecover_to_pub, sha3
from eth_utils import encode_hex, decode_hex, add_0x_prefix
import codecs
from gatekeeper.models import Details
from django.forms.models import model_to_dict
from django.conf import settings
from eth_account.messages import defunct_hash_message
from web3.auto import w3

#web3 = Web3(HTTPProvider('https://rinkeby.infura.io'))
web3 = Web3(HTTPProvider('http://localhost:8545'))
contractAddress = getattr(settings, 'CONTRACT_ADDRESS')
thisServiceID = getattr(settings, 'SERVICE_ID')
with open('./gatekeeper/factoryDRS.json', 'r') as abi_definition:
    abi = json.load(abi_definition)
fContract = web3.eth.contract(web3.toChecksumAddress(contractAddress),abi=abi)

def index(request):
    return HttpResponse("Hello, world. You're at the gatekeeper")

def data(request, address_id, signature_id, message_hash, parameter, key):
    keyHex=key
    parameterHex=web3.toHex(parameter.encode(encoding='UTF-8'))
    keyHexData=keyHex[2:]
    parameterHexData=parameterHex[2:]

    key2=web3.toBytes(hexstr=keyHex)
    parameter2=web3.toBytes(hexstr=parameterHex)
    signer = address_id
    signature = signature_id
    recovered = w3.eth.account.recoverHash(message_hash, signature=signature).lower()

    '''
    # Previous method of recovering public signer
    r = int(signature[0:66], 16)
    s = int(add_0x_prefix(signature[66:130]), 16)
    v = int(add_0x_prefix(signature[130:132]), 16)
    if v not in (27,28):
        v += 27
    pubkey = ecrecover_to_pub(decode_hex(message_hash), v, r, s)
    '''    
  

    #print('pubkey', encode_hex(sha3(pubkey)[-20:]),':',signer,':',recovered.lower())
    accountID=fContract.call().getKeyData(key2,parameter2)
    accountID=accountID.strip()
    print('image account',accountID,':')
    owner=fContract.call().isKeyOwner(key2,web3.toChecksumAddress(address_id))
    hexId=web3.toHex(accountID)
    if parameter=='account_number':
        accountID=int(hexId.rstrip("0"), 16)
    
    print('AccountID: ',accountID)

    #Get the service this key belongs too
    keyData=fContract.call().getKey(key2)
    serviceFromKey = web3.toHex(keyData[4])
    print('if statement ',parameter , thisServiceID, serviceFromKey, accountID)
    if parameter=='account_number' and thisServiceID == serviceFromKey and recovered == signer and owner:
        print(':                  success              :')
        result=Details.objects.filter(account_number=accountID)
        dataResult = serializers.serialize('json', result)
        return JsonResponse(dataResult, safe=False)
        #thisServiceID == serviceFromKey and and encode_hex(sha3(pubkey)[-20:]) == signer
    elif parameter=='image' and owner and thisServiceID == serviceFromKey and recovered == signer: 
        module_dir = os.path.dirname(__file__)  # get current directory
        filename=module_dir+'/images/'+accountID.decode(encoding='UTF-8')
        filename=filename.strip()
        filename=filename.strip('\x00')
        with open(filename, 'rb') as f:
            print(f)
            return HttpResponse(f.read(),content_type="image/jpeg") #base64.b64encode() - removed was causing image not to save correctly

            # return JsonResponse(files, safe=False)
    elif parameter=='audio' and thisServiceID == serviceFromKey and recovered == signer and owner:
        module_dir = os.path.dirname(__file__)  # get current directory
        filename=module_dir+'/audio/'+accountID
        filename=filename.strip()
        filename=filename.strip('\x00')
        # with open(filename, 'rb') as f:
        with open(filename, 'rb') as f:
            print(f)
            wrapper = FileWrapper(f)
            print(wrapper)
            return HttpResponse(f.read(),content_type="audio/mpeg")
        # dataResult = serializers.serialize('json', result)
            # return JsonResponse(files, safe=False)
    else:
        print(':                  fail              :')
        return JsonResponse({'status':'false','message':'Invalid user'}, status=500)
#
