#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os
import requests
import time

from pprint import pprint

G_url = "http://127.0.0.1:8964"

def runArticut(inputSTR, level="lv2", userDefinedDICT={}, openDataPlaceBOOL=False):
    payload = {"input_str":inputSTR,
               "level": level,
               "user_defined_dict_file":userDefinedDICT,
               "opendata_place":openDataPlaceBOOL}
    respond = requests.post("{}/Articut/API/".format(G_url), json=payload)
    resultDICT = respond.json()
    return resultDICT

if __name__ == "__main__":
    startTime = time.time()
    inputSTR = "你的模型超胖。"
    resultDICT = runArticut(inputSTR, level="lv2")

    pprint(resultDICT)

    print("\n{} 斷詞執行時間: {} 秒 {}".format('+'*11, round(resultDICT["exec_time"], 4), '+'*11))
    print("\n{} 總執行時間: {} 秒 {}".format('='*12, round(time.time()-startTime, 4), '='*12))
