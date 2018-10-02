import requests, time, os, creds
from datetime import date, datetime, timedelta
from pathlib import Path
from pprint import pprint as pp

headers = {
    'X-Auth-Email': creds.login['email'],
    'X-Auth-Key': creds.login['key'],
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
    }

class Audits:

    url_base = "https://api.cloudflare.com/client/v4/"

    def __init__(self, url):
        self.arr = []
        self.url = Audits.url_base + url

    def response(self, action, headers):
        self.r = requests.request(str(action),str(self.url),headers=headers)
        return self.r

    def update_arr(self,update):
        self.arr.append(update)




def getOrgIDs():
    getOrgs = Audits('accounts')
    print(getOrgs.__dict__)
    org_json = getOrgs.response('GET',headers).json()
    totalPages = org_json['result_info']['total_pages']

    for i in range(0, totalPages):
        inner = Audits('accounts?page='+ str(i+1) + '&per_page=20').response('GET',headers).json()

        for org in inner['result']:
            getOrgs.update_arr({"Org_Name": org["name"],"Org_ID" : org["id"]})

    pp(getOrgs.arr)

    return


pp(getOrgIDs())