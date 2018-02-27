
from django.http import HttpResponse, JsonResponse
import hashlib
from django.core import serializers

import json
from web3 import Web3, HTTPProvider
from ethereum.utils import ecrecover_to_pub, sha3
from eth_utils.hexidecimal import encode_hex, decode_hex, add_0x_prefix
import codecs
# from .models import Episodes
from gatekeeper.models import Details
from django.forms.models import model_to_dict

web3 = Web3(HTTPProvider('https://rinkeby.infura.io'))
contractAddress = '0x1ba6cea196f186e6ee2d8ac46308e6d18018e910'
with open('./gatekeeper/factoryDRS.json', 'r') as abi_definition:
    abi = json.load(abi_definition)
fContract = web3.eth.contract(contractAddress,abi=abi)

def index(request):
    return HttpResponse("Hello, world. You're at the gatekeeper")

def data(request, address_id, signature_id, message_hash, parameter, key):
    keyHex=key#web3.fromAscii(key)
    parameterHex=web3.fromAscii(parameter)
    keyHexData=keyHex[2:]
    parameterHexData=parameterHex[2:]


    key2=web3.toBytes(hexstr=keyHex)
    parameter2=web3.toBytes(hexstr=parameterHex)
#isKeyOwner

    signer = address_id
    message_hash =message_hash
    signature = signature_id
    # signer = "0x9283099a29556fcf8fff5b2cea2d4f67cb7a7a8b"
    # message_hash = "0x6e099d83ea72d1ef62e39a501fe000c1458ba5a511510a0e9348b0dfeb298803"
    # signature = "0x0cf7e2e1cbaf249175b8e004118a182eb378a0b78a7a741e72a0a34e970b59194aa4d9419352d181a4d1827abbad279ad4f5a7b60da5751b82fec4dde6f380a51b"
    r = int(signature[0:66], 16)
    s = int(add_0x_prefix(signature[66:130]), 16)
    v = int(add_0x_prefix(signature[130:132]), 16)
    if v not in (27,28):
        v += 27
    pubkey = ecrecover_to_pub(decode_hex(message_hash), v, r, s)
    print(':                  pubkey              :')
    print(pubkey)
    print(signer)
    print(encode_hex(sha3(pubkey)[-20:]))
    print(':                  pubkey              :')
    accountID=fContract.call().getKeyData(key2,parameter2)
    owner=fContract.call().isKeyOwner(key2,address_id)
    print('is owner: ',owner)
    hexId=web3.fromAscii(accountID)
    print('ascii to hex',hexId)
    accountID=int(hexId.rstrip("0"), 16)

    # episodes=Episodes.objects.filter(account_number=accountID)
    print('return value:  ',accountID)
    # signer = w3.eth.account.recover(message_hash, signature=signature_id)
    episodes='test'
    result=Details.objects.filter(account_number=accountID)
    # for item in result:
    #     item['details'] = model_to_dict(item['details'])
    # print(result)
    dataResult = serializers.serialize('json', result)
    print(dataResult)
    if encode_hex(sha3(pubkey)[-20:]) == signer and owner:
        print(':                  success              :')
        return JsonResponse(dataResult, safe=False)

        # return HttpResponse("You're looking at %s , %s , %s . Here is the data %s" % (address_id, signature_id, parameter,episodes))
    else:
        print(':                  fail              :')
        return JsonResponse({error:"Invalid User"})







#
