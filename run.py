#!/usr/bin/python

import os

username = os.environ.get('USERNAME')
if not username:
    print "No username set, defaulting to root"
    username = 'root'

password = os.environ.get('PASSWORD')
if not password:
    print "No password set, defaulting to 'a'"
    password = 'a'

url = os.environ.get('URL')
if not url:
    print "No url set, defaulting to 'https://172.16.10.10:8080'"
    url = 'https://172.16.10.10:8080'

# Example Start
import isi_sdk_8_0_1
import urllib3
urllib3.disable_warnings()

isi_sdk_8_0_1.configuration.username = username
isi_sdk_8_0_1.configuration.password = password
isi_sdk_8_0_1.configuration.verify_ssl = False

host = url
apiClient = isi_sdk_8_0_1.ApiClient(host)

protocolsApi = isi_sdk_8_0_1.ProtocolsApi(apiClient)
nfsExports = protocolsApi.list_nfs_exports()
print "NFS Exports:\n" + str(nfsExports)
# Example End

