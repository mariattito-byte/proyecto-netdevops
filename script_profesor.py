import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Credenciales exactas dadas por el profesor
FORTIGATE_IP = "172.23.18.225"
FORTIGATE_TOKEN = "Nd3wxNjG89gr8Qw5kdxjQms4g5j8yn"

SWITCH_1_IP = "172.23.18.224"
SWITCH_2_IP = "172.23.18.223"
SWITCH_USER = "apiadmin"
SWITCH_PASS = "Cisco12345"

def consultar_fortigate():
    print("\n=== CONSULTANDO FORTIGATE VIA REST API ===")
    url = f"https://{FORTIGATE_IP}/api/v2/cmdb/system/interface"
    headers = {"Authorization": f"Bearer {FORTIGATE_TOKEN}"}
    try:
        res = requests.get(url, headers=headers, verify=False, timeout=5)
        if res.status_code == 200:
            print(" [ÉXITO] Conexión establecida con el FortiGate!")
            data = res.json()
            for intf in data.get("results", [])[:5]:
                print(f"  * Interfaz: {intf.get('name')} | IP: {intf.get('ip')}")
        else:
            print(f" [ERROR] Código HTTP: {res.status_code}")
    except Exception as e:
        print(f" [FALLO DE CONEXIÓN]: {e}")

def consultar_switches(ip):
    print(f"\n=== CONSULTANDO SWITCH CISCO ({ip}) VIA RESTCONF ===")
    url = f"https://{ip}/restconf/data/ietf-interfaces:interfaces"
    headers = {"Accept": "application/yang-data+json"}
    try:
        res = requests.get(url, auth=(SWITCH_USER, SWITCH_PASS), headers=headers, verify=False, timeout=5)
        if res.status_code == 200:
            print(f" [ÉXITO] Conexión establecida con el Switch {ip}!")
        else:
            print(f" [ERROR] Código HTTP: {res.status_code}")
    except Exception as e:
        print(f" [FALLO DE CONEXIÓN]: {e}")

if __name__ == "__main__":
    consultar_fortigate()
    consultar_switches(SWITCH_1_IP)
    consultar_switches(SWITCH_2_IP)
