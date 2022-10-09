# sophos-xg-api
* Make API calls with a simple python script. 

## Getting started with the API

* Enable the API.
  - Go to Backup & Firmware > API 
  - For more details, see documentation [here](https://docs.sophos.com/nsg/sophos-firewall/19.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/BackupAndFirmware/API/APIUsingAPI/index.html+)

## Sophos API documentation
See documentation [here](https://docs.sophos.com/nsg/sophos-firewall/19.0/API/index.html)  

## How to create encypred password for API User.

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

# Update cerd.txt with your username and  encrypted password.

# Update the XML-request.xml as desired.
$ python3 api.call.py

```
---
> GitHub [@avnindersran](https://github.com/avnindersran) &nbsp;&middot;&nbsp;


