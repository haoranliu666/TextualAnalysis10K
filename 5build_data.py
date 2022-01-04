import json
import numpy as np
import pandas as pd

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/2file_name.json', 'r') as handle:
    file_name_list = json.load(handle)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/2time.json', 'r') as handle:
    time_list_list = json.load(handle)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/2type.json', 'r') as handle:
    type_list_list = json.load(handle)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/4offshore.json', 'r') as handle:
    offshore_list_list = json.load(handle)

df = pd.DataFrame()

df_cik = []
df_accno = []
df_year_10k = []
df_type_10k = []
df_type_offshore = []
df_country = []

for i in range(0, len(file_name_list)):
    temp = file_name_list[i].split('_')
    cik_temp = temp[1]
    accno_temp = temp[2]
    year_temp = time_list_list[i][0][0:4]
    type_10k_temp = type_list_list[i][0]
    for data in offshore_list_list:
        if data[0] == file_name_list[i] + '.txt':
            df_cik.append(cik_temp)
            df_accno.append(accno_temp)
            df_year_10k.append(year_temp)
            df_type_10k.append(type_10k_temp)
            df_type_offshore.append(data[1])
            df_country.append(data[2])

df['cik'] = df_cik
df['accno'] = df_accno
df['year'] = df_year_10k
df['type_10k'] = df_type_10k
df['type'] = df_type_offshore
df['country'] = df_country

df.to_stata('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/5offshore.dta', version = 117)