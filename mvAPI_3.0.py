
import requests, json
api_key="9aad4b4218a0fcddfb28a22a7c97a688baad529f"
headers={"X-Cisco-Meraki-API-Key":api_key}

def getSnapshot(networdID,SN_MV):
    meraki_snapshot_url='https://api.meraki.com/api/v0/networks/{net_ID}/cameras/{SN}/snapshot'.format(net_ID=networdID,SN=SN_MV)
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

def main():
    print("<<<Bienvenido al Portal de Meraki MV Sense de BCIC-Peru>>>")
    while True:
        print("\n1. Snapshot de la camara\n2. Personas detectadas hoy\n0. Salir")
        opciones=int(input("¿Que desea realizar? (Ingrese una de las opciones): \n"))
        if opciones==0:
            print("Hasta luego.. :D")
            break

        elif opciones==1:
            url_snapshot=getSnapshot("L_611363649415547288","Q2GV-2V9V-NMDF")
            print("URL del Snapshot: ",url_snapshot,"\n")

        elif opciones==2:
            numPeople=getNumPeople("Q2GV-2V9V-NMDF")
            print("Hoy hubo {} personas".format(numPeople))
        else:
            print("Opcion inválida, ingrese una opción válida...")

if __name__=='__main__':
    main()
