
from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render
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
from eth_utils import encode_hex, decode_hex, add_0x_prefix
import codecs
from gatekeeper.models import Details, Accounts
from django.forms.models import model_to_dict
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadForm

import requests


#TODO setup to allow user to determine network
web3 = Web3(HTTPProvider('https://rinkeby.infura.io'))

contractAddress = getattr(settings, 'CONTRACT_ADDRESS')
thisServices = set(getattr(settings, 'SERVICE_IDS'))

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
    try:
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

        if parameter == 'account_number':
            account_id=int(hexId.rstrip("0"), 16)

        #Get the service this key belongs too
        keyData=fContract.call().getKey(key_bytes)
        serviceFromKey = web3.fromAscii(keyData[4])
        phuse_number=Accounts.objects.get(public_key=address_id)
        print(parameter, serviceFromKey, thisServices, owner, encode_hex(sha3(pubkey)[-20:]), address_id)
        if parameter == 'file' and serviceFromKey in thisServices and encode_hex(sha3(pubkey)[-20:]) == address_id and owner:
            module_dir = os.path.dirname(__file__)  # get current directory
            filename=module_dir+'/file/'+account_id
            filename=filename.strip()
            filename=filename.strip('\x00')
            url = 'http://localhost:3000/asset/upload/'+str(phuse_number)
            files = {'file':open(filename,'rb')}
            r = requests.post(url, files=files)
            return FileResponse(open(filename, 'rb'))
        else:
            print(':                  fail              :')
            return JsonResponse({'status':'false','message':'Invalid user'}, status=500)

    except Exception as inst:
         print(type(inst))
         print(inst.args)
         print(inst)
def register(request, address_id, signature, message_hash, phuse_number ):
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
    try:
        #recover public key
        r = int(signature[0:66], 16)
        s = int(add_0x_prefix(signature[66:130]), 16)
        v = int(add_0x_prefix(signature[130:132]), 16)
        if v not in (27,28):
            v += 27
        pubkey = ecrecover_to_pub(decode_hex(message_hash), v, r, s)
        #Get the service this key belongs too
        if encode_hex(sha3(pubkey)[-20:]) == address_id:
            # accountUpdate, createdAccount = Accounts.object.update_or_create(phuse_number=address_id, public_key=phuse_number)
            obj, created = Accounts.objects.update_or_create(
                public_key=address_id,
                defaults={'phuse_number': phuse_number, 'public_key':address_id},
            )
            print('correct2',created,obj)
            return JsonResponse({'status':'Success','message':'Account Registered'}, status=201)
        else:
            return JsonResponse({'status':'false','message':'Invalid user'}, status=500)
    except Exception as inst:
         print(type(inst))
         print(inst.args)
         print(inst)

def handle_uploaded_file(f):
    print('FILE: ', f)
    with open('file/name.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_exempt
def upload_file(request, address_id, signature, message_hash):
    try:
        #recover public key
        r = int(signature[0:66], 16)
        s = int(add_0x_prefix(signature[66:130]), 16)
        v = int(add_0x_prefix(signature[130:132]), 16)
        if v not in (27,28):
            v += 27
        pubkey = ecrecover_to_pub(decode_hex(message_hash), v, r, s)
        #Get the service this key belongs too
        if encode_hex(sha3(pubkey)[-20:]) == address_id:
            if request.method == 'POST':
                print('FILES: ', request.FILES)
                form = UploadForm(request.POST, request.FILES)
                print('form: ', form, form.is_valid())
                if form.is_valid():
                    form.save()
                return JsonResponse({'status':'Success','message':'File Saved'}, status=201)
                # form = UploadFileForm(request.POST, request.FILES)
                # file_data = csv_file.read().decode("utf-8")
                # print('FORM: ', form, form.is_valid())
                # handle_uploaded_file(request.FILES['file'])
                # if form.is_valid():
                #     handle_uploaded_file(request.FILES['file'])
                #     return JsonResponse({'status':'Success','message':'Account Registered'}, status=201)
                # else:
                #     form = UploadFileForm()
                return render(request, 'upload.html', {'form': form})
    except Exception as inst:
         print(type(inst))
         print(inst.args)
         print(inst)
