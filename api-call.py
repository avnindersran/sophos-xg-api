import requests

# Opening XG-Cerd file.
with open("cerd.txt", "r") as cerd:
    cerd = cerd.read()

# Opening XML request file.
with open("XML-request.xml", "r") as xml:
    xmlrequest = xml.read()

# API call
response = requests.post(
    "https://192.168.10.254:4445/webconsole/APIController?reqxml=" + cerd + xmlrequest, verify=False)
print(response.status_code)
print(response.text)
