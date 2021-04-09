import json
import os

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcdn.request.v20180510.DescribeUserDomainsRequest import DescribeUserDomainsRequest


def get_DomainNameOnlineCheck(domainname):
    client = AcsClient('LTAI4GGcfxVULU2XhoXpamyY',
                       'Xnnjj0UW1zHMCc50wNfTIbZII5eDW7', 'cn-hangzhou')
    request = DescribeUserDomainsRequest()
    request.set_DomainName(str(domainname))
    response = client.do_action_with_exception(request)
    response_u = str(response, encoding='utf-8')
    response_j = json.loads(response_u)
    return response_j['Domains']['PageData'][0]['DomainStatus']


os.chdir(os.path.dirname(os.path.abspath(__file__)))
DomainsName_file = 'DomainsName.txt'  # 設定要開啟的檔案
DomainStatus_file = 'DomainStatus.txt'
if os.path.exists(DomainsName_file) == False:
    newfile = open('DomainsName.txt', 'w')
    newfile.close()
    print('建立DomainsName.txt')

with open(DomainsName_file, encoding='utf-8-sig') as file_Obj:
    obj_list = file_Obj.read().splitlines()
with open(DomainStatus_file, 'w', encoding='utf-8-sig') as file_Obj:
    for line in obj_list:
        file_Obj.write('%s : %s\n' %
                       (line, get_DomainNameOnlineCheck(line)))
