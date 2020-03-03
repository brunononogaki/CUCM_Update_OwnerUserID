import requests, urllib3, csv
import json
urllib3.disable_warnings()

with open ("config.json") as config:
    data_acesso = json.load(config)
    url = data_acesso["url"]
    username = data_acesso["username"]
    password = data_acesso["password"]
    auth = (username,password)

with open ('lista_usuarios.csv') as arquivo:
    readCSV = csv.reader(arquivo, delimiter=",")
    for linha in readCSV:
        usuario = linha[0]
        device = linha[1]

        data = """
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <SOAP-ENV:Body>
        <axl:updatePhone xmlns:axl="http://www.cisco.com/AXL/API/1.0" sequence="12055">
        <ownerUserName>""" + usuario + """</ownerUserName>
        <name>""" + device+ """</name>
        </axl:updatePhone>
        </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
        """

        p = requests.post(url,verify=False,auth=auth,data=data)

        if p.status_code == 200:
            print("Sucesso! Usuario {} foi associado ao device {} com sucesso".format(usuario,device))
        else:
            print("Erro! O Usuario {} nao foi associado ao device {}.".format(usuario,device))

arquivo.close()