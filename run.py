#!/usr/bin;python

import os

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
url = os.environ.get('URL')

# Example Start
import isi_sdk
import urllib3
urllib3.disable_warnings()

isi_sdk.configuration.username = username
isi_sdk.configuration.password = password
isi_sdk.configuration.verify_ssl = False

host = url
apiClient = isi_sdk.ApiClient(host)

protocolsApi = isi_sdk.ProtocolsApi(apiClient)
nfsExports = protocolsApi.list_nfs_exports()
print "NFS Exports:\n" + str(nfsExports)
# Example End

