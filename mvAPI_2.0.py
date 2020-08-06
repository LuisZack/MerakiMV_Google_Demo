import requests, json
from pprint import pprint

api_key="9aad4b4218a0fcddfb28a22a7c97a688baad529f"
url="https://api.meraki.com/api/v0/organizations"

#Recursos de Imagga
imagga_url = 'https://api.imagga.com/v2/tags'
api_key_imagga="acc_37646972c0d69bd"
api_secret_imagga="512cb775d1d2c13ced537af528dc7025"

headers={"X-Cisco-Meraki-API-Key":api_key}
respo1=requests.get(url,headers=headers)
#pprint(respo1.json())

url_net="https://api.meraki.com/api/v0/organizations/122494/networks"
respo_net= requests.get(url_net,headers=headers)
#pprint(respo_net.json())
print(type(respo_net.json()))

for i in respo_net.json():
    if i["name"]=="BCIC":
        print("El ID de BCIC es: ",i["id"])
        break
        print("...---...")
for i in respo_net.json():
    if i["name"]=="POD 3 - FullStack":
        print("El ID de POD3_FullStack es: ",i["id"])
        break
        print("...---...")

BCIC_Peru="L_611363649415547288"
MV12_BCIC="Q2GV-2V9V-NMDF"
#-----
POD3_FullStack="L_611363649415547249"
MV21_POD3="Q2BV-DGX6-HLES"
meraki_snapshot_url='https://api.meraki.com/api/v0/networks/{network_ID}/cameras/{SN_mv}/snapshot'.format(network_ID=BCIC_Peru,SN_mv=MV12_BCIC)
meraki_snapshot_response= requests.post(meraki_snapshot_url,headers=headers)
body_meraki_snap=meraki_snapshot_response.json()
pprint(body_meraki_snap)

#body_meraki_snap["url"]
def getImage(url_mv):
    code_url=404
    while code_url != 200:
        response_URL=requests.get(url_mv)
        code_url= response_URL.status_code

    print("RESPONSE URL: ",response_URL)
    print("CODE URL= ",code_url)
    #print("RESPONSE CONTENT", response_URL.content)
    return response_URL.content

def getAnalyze(url_imagga,image_mv,key_i,secret_i):
    responseImagga= requests.post(url_imagga, auth=(key_i,secret_i), files={'image':image_mv})
    return responseImagga

def listToString(list):
    cad=""
    i=0
    while i<5:
        cad = cad + list[i] + ", "
        i+=1
    return cad

print("-------"*5)
print(body_meraki_snap["url"])
print("-------"*5,"\n")
imagen_mv=getImage(body_meraki_snap["url"])
#pprint(imagen_mv)
print("---oo---"*5)
responseImagga1=getAnalyze(imagga_url,imagen_mv,api_key_imagga,api_secret_imagga)
print("responseImagga1: ",responseImagga1)
print("responseImagga1.json(): ")
pprint(responseImagga1.json())
tags = [item['tag']['en'] for item in responseImagga1.json()['result']['tags']]
print("TAGS:\n", tags)
speech = listToString(tags)
print("SPEECH:\n",speech)
print("---oo---"*5)

print('-----\nMV Sense Live API-----')
meraki_live_url = 'https://api.meraki.com/api/v0/devices/{SN_MV}/camera/analytics/live'.format(SN_MV=MV12_BCIC)
response_live= requests.get(meraki_live_url, headers=headers)
body_meraki_live=response_live.json()
pprint(body_meraki_live)

"""def __name__=='__main__':
    main()
"""
