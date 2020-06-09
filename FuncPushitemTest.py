# -*- coding: utf-8 -*-

import requests
import time

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# photo
def main(token):

    payload = "{\"task_id\": \"123456\"," \
              "\"timestamp\": \"1536991270851\"," \
              "\"image_base64\": \"" \
              "\",\"object_list\": [" \
              "{" \
                    "\"object_id\": \"71804\"," \
                    "\"min\": 1," \
                    "\"max\": 15," \
                    "\"critical_info\": \"\"}]}"

    # payload = "{\"image_base64\": \"\"," \
    #           "\"mode\": \"noah-doc\"}"

    # payload = "{\"image_base64\": \"\"}"

    headers = {
    'Content-Type': "application/json",
    'Authorization': 'Bearer ' + token,
    }

    url = "https://10.137.106.120:8343/qcheck2/api/v1/te/detect"
    # url = "https://10.137.106.120:8343/qcheck/api/v1/ics/detect"
    # url = "https://10.137.106.120:8343/qcheck/api/v1/ehs/detect"
    # url = "https://10.137.106.120:8343/qcheck/api/v1/ocr/general-text"
    # url = "https://10.137.106.120:8343/qcheck/api/v1/ocr/detection-text"
    # url = "https://10.137.106.120:8343/qcheck/api/v1/ocr/recognition-text"

    response = requests.request("POST", url, data = payload, headers = headers,verify = False)


    return response




