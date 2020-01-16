#!/usr/bin/env python3

import json
import requests
import numpy as np
import pandas as pd
import schedule
import time

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def query_nbebikes(api_url_base):
    response = requests.get(api_url_base)
    #print(response.status_code)
    #print(response.json())
    #jprint(response.json()["records"][1])
    nbebike = response.json()["records"][0]["fields"]["nbebike"]
    nbbike = response.json()["records"][0]["fields"]["nbbike"]

    return nbebike,nbbike

def add_to_dF(api_url_base):
    
    global dF_main
    
    neb,nb = query_nbebikes(api_url_base)
    dF_add  = pd.DataFrame({"neb" : [neb], "nb" : [nb]})
    dF_main = dF_main.append(dF_add, ignore_index = True )
    dF_main.to_pickle('test')
    return


dF_main = pd.DataFrame({"neb" : [0],"nb"  : [0] })

def main():
    global dF_main
    
    dF_main = pd.read_pickle('velib_at_EtienneMarcel.backup')

    print(dF_main)
    
    return 

main()