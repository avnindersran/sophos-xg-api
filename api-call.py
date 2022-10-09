import requests

# Opening XG-Creds file.
with open("creds.txt", "r") as creds:
    creds = creds.read()

# Opening XML request file.
with open("XML-request.xml", "r") as xml:
    xmlrequest = xml.read()

# API call
response = requests.post(
    "https://192.168.10.254:4445/webconsole/APIController?reqxml=" + creds + xmlrequest, verify=False)
print(response.status_code)
print(response.text)
