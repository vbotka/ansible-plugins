# All rights reserved (c) 2020-2022, Vladimir Botka <vbotka@gmail.com>
# Simplified BSD License, https://opensource.org/licenses/BSD-2-Clause

# Ansible filters for operating on ACME data
#
# Glossary
#
# ACME: Automatic Certificate Management Environment
#      https://tools.ietf.org/html/rfc8555
# Letsencrypt: Certificate Authority providing TLS certificates
#      https://letsencrypt.org/
# Certbot: Software tool for automatically using Lets Encrypt certificates
#      https://certbot.eff.org/
# ASN1: Abstract Syntax Notation One
#      https://www.oss.com/asn1/resources/standards-define-asn1.html
# JSON: JavaScript Object Notation
#      https://www.json.org/
# DER: Distinguished Encoding Rules
#      https://support.ssl.com/Knowledgebase/Article/View/19/0/der-vs-crt-vs-cer-vs-pem-certificates-and-how-to-convert-them
# PEM: Privacy Enhanced Mail
#      https://support.ssl.com/Knowledgebase/Article/View/19/0/der-vs-crt-vs-cer-vs-pem-certificates-and-how-to-convert-them
#
# Variables
#
# pk_json: JSON encoded ACME private key
# pk_asn1: ASN1 encoded ACME private key
# pk_der: DER encoded ACME private key
# pk_pem: PEN encoded ACME private key

import base64
import binascii
import subprocess


def acme_enc_hex(data):
    ''' Convert data to hexadecimal '''
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'=' * missing_padding
    return '0x' + binascii.hexlify(base64.b64decode(data, b'-_')).decode().upper()


def acme_pk_json2asn1(pk_json):
    ''' Convert ACME private key from JSON to ASN1 '''
    for k, v in pk_json.items():
        if k == 'kty':
            continue
        pk_json[k] = acme_enc_hex(v.encode())
    pk_asn1 = '\n'.join(i for i in ("asn1=SEQUENCE:private_key",
                                    "[private_key]",
                                    "version=INTEGER:0",
                                    "n=INTEGER:{}".format(pk_json[u'n']),
                                    "e=INTEGER:{}".format(pk_json[u'e']),
                                    "d=INTEGER:{}".format(pk_json[u'd']),
                                    "p=INTEGER:{}".format(pk_json[u'p']),
                                    "q=INTEGER:{}".format(pk_json[u'q']),
                                    "dp=INTEGER:{}".format(pk_json[u'dp']),
                                    "dq=INTEGER:{}".format(pk_json[u'dq']),
                                    "qi=INTEGER:{}".format(pk_json[u'qi'])))
    return pk_asn1


def acme_pk_asn12der(pk_asn1_file, pk_der_file):
    ''' Convert ACME private key from ASN1 to DER
        Read ASN1 file, convert data to DER, and write to DER file '''
    result = subprocess.check_output(["openssl", "asn1parse", "-noout",
                                      "-out", pk_der_file,
                                      "-genconf", pk_asn1_file],
                                     stderr=subprocess.STDOUT)
    return result


def acme_pk_der2pem(pk_der_file):
    ''' Convert ACME private key from DER to PEM
        Read DER file, convert data to PEM, and return PEM string '''
    return subprocess.check_output(["openssl", "rsa",
                                    "-in", pk_der_file,
                                    "-inform", "der"],
                                   stderr=subprocess.STDOUT)


class FilterModule(object):
    ''' Ansible filters for operating on ACME data '''

    def filters(self):
        return {
            'acme_pk_json2asn1': acme_pk_json2asn1,
            'acme_pk_asn12der': acme_pk_asn12der,
            'acme_pk_der2pem': acme_pk_der2pem,
        }

# EOF
