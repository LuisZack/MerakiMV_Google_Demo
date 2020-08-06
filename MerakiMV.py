import requests, json
from pprint import pprint
#Recursos de Meraki
api_key_meraki="9aad4b4218a0fcddfb28a22a7c97a688baad529f"
headers={"X-Cisco-Meraki-API-Key":api_key_meraki}
network_Id="L_611363649415547288"
SN_MV_Meraki="Q2GV-2V9V-NMDF"

#Recursos de Imagga
imagga_url = 'https://api.imagga.com/v2/tags'
api_key_imagga="acc_37646972c0d69bd"
api_secret_imagga="512cb775d1d2c13ced537af528dc7025"

#
def getSnapshot(networkID,SN_MV):
    meraki_snapshot_url='https://api.meraki.com/api/v0/networks/{net_ID}/cameras/{SN}/snapshot'.format(net_ID=networkID,SN=SN_MV)
    meraki_snapshot_response= requests.post(meraki_snapshot_url,headers=headers)
    body_meraki_snap=meraki_snapshot_response.json()
    return body_meraki_snap["url"]

def getNumPeople(SN_MV):
    meraki_url_live='https://api.meraki.com/api/v0/devices/{SN}/camera/analytics/live'.format(SN=SN_MV)
    body_meraki_live_requests= requests.get(meraki_url_live, headers=headers).json()
    num_people= body_meraki_live_requests['zones']['0']['person']
    return num_people

def getImage(url_mv):
    code_url=404
    while code_url != 200:
        response_URL=requests.get(url_mv)
        code_url= response_URL.status_code
    return response_URL.content

def getAnalyze(url_imagga,image_m,key_i,secret_i):
    responseImagg= requests.post(url_imagga, auth=(key_i,secret_i), files={'image':image_m})
    return responseImagg

def getTop5Tags(list):
    cad=""
    i=0
    while i<5:
        cad = cad + list[i] + ", "
        i+=1
    return cad

def mainReturn():
    url_snapshot_mv=getSnapshot(network_Id,SN_MV_Meraki)
    print("URL Snapshot Meraki MV: ", url_snapshot_mv)
    image_mv=getImage(url_snapshot_mv)
    responseImagga=getAnalyze(imagga_url,image_mv,api_key_imagga,api_secret_imagga)
    print("<<Analisis de la imagen>>")
    pprint(responseImagga.json())
    tagsImagga = [item['tag']['en'] for item in responseImagga.json()['result']['tags']]
    cadena= getTop5Tags(tagsImagga)
    print("\nTop 5 de resultados de la imagen: ",cadena)
    return (cadena, url_snapshot_mv)
"""
if __name__=='__main__':
    mainReturn()
"""
