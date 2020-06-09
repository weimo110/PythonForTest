# -*- coding: utf-8 -*-

import requests
import time

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# photo
def main(token):

    payload = "{}"

    headers = {
    'Content-Type': "application/json",
    'Authorization': 'Bearer ' + token,
    }

    url = "https://"


    response = requests.request("POST", url, data = payload, headers = headers,verify = False)


    return response




