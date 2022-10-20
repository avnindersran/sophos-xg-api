# sophos-xg-api
* A simple Python script can be used to make API calls. 

## Getting started with the API

* Enable the API.
  - Go to Backup & Firmware > API 
  - For more details, see documentation [here](https://docs.sophos.com/nsg/sophos-firewall/19.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/BackupAndFirmware/API/APIUsingAPI/index.html)

## API documentation for Sophos Firewall.
See documentation [here](https://docs.sophos.com/nsg/sophos-firewall/19.0/API/index.html)  

## How to create encrypted password for API User.

* To get your encrypted password, enter the following command in the advanced shell: 
```bash 
$ aes-128-cbc-tool -k Th1s1Ss1mPlygR8A -t 1 -s <password>
```
## How To Use

To clone, you'll need [Git](https://git-scm.com). From your command line:

```bash
# Clone this repository
$ git clone https://github.com/avnindersran/sophos-xg-api.git

# Go into the repository
$ cd sophos-xg-api

# Update the creds.txt with your username and encrypted password.

# Replace the XG Mgmt IP address and port number in api-call.py.

# Update the XML-request.xml as desired.
$ python3 api.call.py

```
---
> GitHub [@avnindersran](https://github.com/avnindersran)


