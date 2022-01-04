import requests
import re
import json
import numpy as np
import pandas as pd


cik_stata = pd.read_stata('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/cik.dta')
cik_list = list(cik_stata['CIK'])


#get accno 
url_prefix = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="
url_suffix = "&type=10-K&dateb=&owner=include&count=100&search_text=C"

re_accno = re.compile(r'Acc-no: (\d\d\d\d\d\d\d\d\d\d-\d\d-\d\d\d\d\d\d)')

accno = []

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40'
}

for i in range(0, len(cik_list)):
    r = requests.get(url_prefix + cik_list[i] + url_suffix, headers = headers)
    accno.append(re_accno.findall(r.text))
    if accno[i] != []:
        print(i)
        print(accno[i])

#save data
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/1cik.json', 'w') as handle:
    json.dump(cik_list, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/1accno.json', 'w') as handle:
    json.dump(accno, handle, indent=2)