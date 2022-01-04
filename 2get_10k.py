import requests
import json
import re

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/1cik.json', 'r') as handle:
    cik_list = json.load(handle)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/1accno.json', 'r') as handle:
    accno_list_list = json.load(handle)

re_tpye = re.compile(r'CONFORMED SUBMISSION TYPE:\t([\s\S]*?)\n')
re_time = re.compile(r'CONFORMED PERIOD OF REPORT:\t([\s\S]*?)\n')

type_list = []
time_list = []
file_name_list = []

#https://www.sec.gov/Archives/edgar/data/320193/000032019321000105/0000320193-21-000105.txt

#get 10k
url_prefix = "https://www.sec.gov/Archives/edgar/data/"

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
}

file_count = 0

# for i in range(0, len(cik_list)):
for i in range(0, 10):
    if len(accno_list_list[i]) != 0:
        for accno in accno_list_list[i]:
            accno_splited = accno.split('-')
            url = url_prefix + cik_list[i].lstrip('0') + '/' + accno_splited[0] + accno_splited[1] + accno_splited[2] + '/' + accno + '.txt'
            r = requests.get(url, headers = headers)
            if 'File Not Found Error Alert (404)' not in r.text:                            
                file_count += 1
                print(file_count)
                with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/10k/' + str(file_count) + '_' + cik_list[i] + '_' + accno + '.txt', 'w') as f:
                    f.write(r.text)
                file_name_list.append(str(file_count) + '_' + cik_list[i] + '_' + accno)
                type_list.append(re_tpye.findall(r.text))
                time_list.append(re_time.findall(r.text))


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/2file_name.json', 'w') as handle:
    json.dump(file_name_list, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/2type.json', 'w') as handle:
    json.dump(type_list, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/2time.json', 'w') as handle:
    json.dump(time_list, handle, indent=2)