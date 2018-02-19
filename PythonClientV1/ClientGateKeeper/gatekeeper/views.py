
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







# Note: Geth and web3.eth.sign will add a prefix to the data message before signing.
#
# The sign method calculates an Ethereum specific signature with: sign(keccak256("\x19Ethereum Signed Message:\n" + len(message) + message))).
#
# By adding a prefix to the message makes the calculated signature recognisable as an Ethereum specific signature. This prevents misuse where a malicious DApp can sign arbitrary data (e.g. transaction) and use the signature to impersonate the victim.
#
# For this case, the second argument to verify() must be keccak256("\x19Ethereum Signed Message:\n", len(message), message) instead of keccak256(message).

# def sha256(string):
#     return bytes_to_hex_string(bin_sha256(string))
#
# def bytes_to_hex_string(b):
#     return b.encode('hex')
#
# def bin_sha256(string):
#     binary_data = string if isinstance(string, bytes) else bytes(string, 'utf-8')
#     return hashlib.sha256(binary_data).digest()
# # Create your views here.
#
# def ecdsa_raw_verify(msghash, vrs, pub):
#     v, r, s = vrs
#     if not (27 <= v <= 34):
#         return False
#
#     w = inv(s, N)
#     z = hash_to_int(msghash)
#
#     u1, u2 = z*w % N, r*w % N
#     x, y = fast_add(fast_multiply(G, u1), fast_multiply(decode_pubkey(pub), u2))
#     return bool(r == x and (r % N) and (s % N))
#
#
# def decode_pubkey(pub, formt=None):
#     if not formt: formt = get_pubkey_format(pub)
#     if formt == 'decimal': return pub
#     elif formt == 'bin': return (decode(pub[1:33], 256), decode(pub[33:65], 256))
#     elif formt == 'bin_compressed':
#         x = decode(pub[1:33], 256)
#         beta = pow(int(x*x*x+A*x+B), int((P+1)//4), int(P))
#         y = (P-beta) if ((beta + from_byte_to_int(pub[0])) % 2) else beta
#         return (x, y)
#     elif formt == 'hex': return (decode(pub[2:66], 16), decode(pub[66:130], 16))
#     elif formt == 'hex_compressed':
#         return decode_pubkey(safe_from_hex(pub), 'bin_compressed')
#     elif formt == 'bin_electrum':
#         return (decode(pub[:32], 256), decode(pub[32:64], 256))
#     elif formt == 'hex_electrum':
#         return (decode(pub[:64], 16), decode(pub[64:128], 16))
#     else: raise Exception("Invalid format!")
#
#
# def safe_from_hex(s):
#     return bytes.fromhex(s)
#
# def from_byte_to_int(a):
#     return ord(a)
#
# def get_pubkey_format(pub):
#     if is_python2:
#         two = '\x02'
#         three = '\x03'
#         four = '\x04'
#     else:
#         two = 2
#         three = 3
#         four = 4
#
#     if isinstance(pub, (tuple, list)): return 'decimal'
#     elif len(pub) == 65 and pub[0] == four: return 'bin'
#     elif len(pub) == 130 and pub[0:2] == '04': return 'hex'
#     elif len(pub) == 33 and pub[0] in [two, three]: return 'bin_compressed'
#     elif len(pub) == 66 and pub[0:2] in ['02', '03']: return 'hex_compressed'
#     elif len(pub) == 64: return 'bin_electrum'
#     elif len(pub) == 128: return 'hex_electrum'
#     else: raise Exception("Pubkey not in recognized format")
#
#
# def fast_multiply(a, n):
#     return from_jacobian(jacobian_multiply(to_jacobian(a), n))
#
#
# def jacobian_multiply(a, n):
#     if a[1] == 0 or n == 0:
#         return (0, 0, 1)
#     if n == 1:
#         return a
#     if n < 0 or n >= N:
#         return jacobian_multiply(a, n % N)
#     if (n % 2) == 0:
#         return jacobian_double(jacobian_multiply(a, n//2))
#     if (n % 2) == 1:
#         return jacobian_add(jacobian_double(jacobian_multiply(a, n//2)), a)
#
#
# def jacobian_double(p):
#     if not p[1]:
#         return (0, 0, 0)
#     ysq = (p[1] ** 2) % P
#     S = (4 * p[0] * ysq) % P
#     M = (3 * p[0] ** 2 + A * p[2] ** 4) % P
#     nx = (M**2 - 2 * S) % P
#     ny = (M * (S - nx) - 8 * ysq ** 2) % P
#     nz = (2 * p[1] * p[2]) % P
#     return (nx, ny, nz)
#
# def fast_add(a, b):
#     return from_jacobian(jacobian_add(to_jacobian(a), to_jacobian(b)))
#
#
# def from_jacobian(p):
#     z = inv(p[2], P)
#     return ((p[0] * z**2) % P, (p[1] * z**3) % P)
#
# def jacobian_add(p, q):
#     if not p[1]:
#         return q
#     if not q[1]:
#         return p
#     U1 = (p[0] * q[2] ** 2) % P
#     U2 = (q[0] * p[2] ** 2) % P
#     S1 = (p[1] * q[2] ** 3) % P
#     S2 = (q[1] * p[2] ** 3) % P
#     if U1 == U2:
#         if S1 != S2:
#             return (0, 0, 1)
#         return jacobian_double(p)
#     H = U2 - U1
#     R = S2 - S1
#     H2 = (H * H) % P
#     H3 = (H * H2) % P
#     U1H2 = (U1 * H2) % P
#     nx = (R ** 2 - H3 - 2 * U1H2) % P
#     ny = (R * (U1H2 - nx) - S1 * H3) % P
#     nz = (H * p[2] * q[2]) % P
#     return (nx, ny, nz)
#
#
# def to_jacobian(p):
#     o = (p[0], p[1], 1)
#     return o
#
#
# def inv(a, n):
#     if a == 0:
#         return 0
#     lm, hm = 1, 0
#     low, high = a % n, n
#     while low > 1:
#         r = high//low
#         nm, new = hm-lm*r, high-low*r
#         lm, low, hm, high = nm, new, lm, low
#     return lm % n
#
# def hash_to_int(x):
#     if len(x) in [40, 64]:
#         return decode(x, 16)
#     return decode(x, 256)
#
# def decode(string, base):
#     if base == 256 and isinstance(string, str):
#             string = bytes(bytearray.fromhex(string))
#     base = int(base)
#     code_string = get_code_string(base)
#     result = 0
#     if base == 256:
#         def extract(d, cs):
#             return d
#     else:
#         def extract(d, cs):
#             return cs.find(d if isinstance(d, str) else chr(d))
#
#         if base == 16:
#             string = string.lower()
#         while len(string) > 0:
#             result *= base
#             result += extract(string[0], code_string)
#             string = string[1:]
#         return result
#
#
# def get_code_string(base):
#     if base in code_strings:
#         return code_strings[base]
#     else:
#         raise ValueError("Invalid base!")
#
#
# def ecdsa_sign(msg, priv):
#     v, r, s = ecdsa_raw_sign(electrum_sig_hash(msg), priv)
#     sig = encode_sig(v, r, s)
#     assert ecdsa_verify(msg, sig,
#         privtopub(priv)), "Bad Sig!\t %s\nv = %d\n,r = %d\ns = %d" % (sig, v, r, s)
#     return sig
#
#
# def ecdsa_raw_sign(msghash, priv):
#
#     z = hash_to_int(msghash)
#     k = deterministic_generate_k(msghash, priv)
#
#     r, y = fast_multiply(G, k)
#     s = inv(k, N) * (z + r*decode_privkey(priv)) % N
#
#     v, r, s = 27+((y % 2) ^ (0 if s * 2 < N else 1)), r, s if s * 2 < N else N - s
#     if 'compressed' in get_privkey_format(priv):
#         v += 4
#     return v, r, s
#
#
# def privtopub(privkey):
#     f = get_privkey_format(privkey)
#     privkey = decode_privkey(privkey, f)
#     if privkey >= N:
#         raise Exception("Invalid privkey")
#     if f in ['bin', 'bin_compressed', 'hex', 'hex_compressed', 'decimal']:
#         return encode_pubkey(fast_multiply(G, privkey), f)
#     else:
        # return encode_pubkey(fast_multiply(G, privkey), f.replace('wif', 'hex'))
