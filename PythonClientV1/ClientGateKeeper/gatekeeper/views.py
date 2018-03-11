
from django.http import HttpResponse, JsonResponse
import hashlib
from django.core import serializers

import json
from web3 import Web3, HTTPProvider
from ethereum.utils import ecrecover_to_pub, sha3
from eth_utils.hexidecimal import encode_hex, decode_hex, add_0x_prefix
import codecs
from gatekeeper.models import Details
from django.forms.models import model_to_dict
from django.conf import settings

web3 = Web3(HTTPProvider('https://rinkeby.infura.io'))
contractAddress = getattr(settings, 'CONTRACT_ADDRESS')
thisServiceID = getattr(settings, 'SERVICE_ID')
with open('./gatekeeper/factoryDRS.json', 'r') as abi_definition:
    abi = json.load(abi_definition)
fContract = web3.eth.contract(contractAddress,abi=abi)

def index(request):
    return HttpResponse("Hello, world. You're at the gatekeeper")

def data(request, address_id, signature_id, message_hash, parameter, key):
    keyHex=key
    parameterHex=web3.fromAscii(parameter)
    keyHexData=keyHex[2:]
    parameterHexData=parameterHex[2:]


    key2=web3.toBytes(hexstr=keyHex)
    parameter2=web3.toBytes(hexstr=parameterHex)

    signer = address_id
    message_hash =message_hash
    signature = signature_id
    r = int(signature[0:66], 16)
    s = int(add_0x_prefix(signature[66:130]), 16)
    v = int(add_0x_prefix(signature[130:132]), 16)
    if v not in (27,28):
        v += 27
    pubkey = ecrecover_to_pub(decode_hex(message_hash), v, r, s)

    accountID=fContract.call().getKeyData(key2,parameter2)
    owner=fContract.call().isKeyOwner(key2,address_id)
    hexId=web3.fromAscii(accountID)
    accountID=int(hexId.rstrip("0"), 16)

    #Get the service this key belongs too
    keyData=fContract.call().getKey(key2)
    serviceFromKey = web3.fromAscii(keyData[4])

    if thisServiceID == serviceFromKey and encode_hex(sha3(pubkey)[-20:]) == signer and owner:
        print(':                  success              :')
        result=Details.objects.filter(account_number=accountID)
        dataResult = serializers.serialize('json', result)
        return JsonResponse(dataResult, safe=False)
    else:
        print(':                  fail              :')
        return JsonResponse({'status':'false','message':'Invalid user'}, status=500)



#
