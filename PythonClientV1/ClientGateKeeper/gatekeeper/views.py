
from django.http import HttpResponse
import hashlib
import json
from web3 import Web3, HTTPProvider
from ethereum.utils import ecrecover_to_pub, sha3
from eth_utils.hexidecimal import encode_hex, decode_hex, add_0x_prefix

from .models import Episodes

web3 = Web3(HTTPProvider('https://rinkeby.infura.io'))
contractAddress = '0x1ba6cea196f186e6ee2d8ac46308e6d18018e910'
with open('./gatekeeper/factoryDRS.json', 'r') as abi_definition:
    abi = json.load(abi_definition)
fContract = web3.eth.contract(contractAddress,abi=abi)

def index(request):
    return HttpResponse("Hello, world. You're at the gatekeeper")

def data(request, address_id, signature_id, message_hash, parameter, key):
    print(w3.eth)


    print(':                  inputs              :')
    print ('contract: ',fContract.call().getKeyData(key,parameter))
    print(address_id)
    print(message_hash)
    print(signature_id)
    print(':                  inputs              :')
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
    accountID=fContract.call().getKeyData(key,parameter)
    episodes=Episodes.objects.filter(account_number=accountID)
    print(episodes)
    # signer = w3.eth.account.recover(message_hash, signature=signature_id)
    if encode_hex(sha3(pubkey)[-20:]) == signer:
        print(':                  success              :')

        return HttpResponse("You're looking at %s , %s , %s . Here is the data %s" % (address_id, signature_id, parameter,episodes))
    else:
        print(':                  fail              :')
        return HttpResponse("Invalid User")







#
