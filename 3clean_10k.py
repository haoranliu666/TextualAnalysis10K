import re
import json
import os

#
path = '/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/10k/'

file_list = os.listdir(path)

re_10k = re.compile(r'<DOCUMENT>([\s\S]*?)</DOCUMENT>')

count = 0

#html element
#\n
#\t
#utf8 element
#html space
#single character except a
#muliple white spaces
for file_name in file_list:
    if file_name != '.DS_Store':
        with open(path + file_name, 'r') as f:
            content = f.read()
            temp = re_10k.findall(content)
            print(file_name)
            print(len(temp))
            if len(temp) != 0:
                temp = temp[0]
                temp = re.sub(r'<[\s\S]*?>', ' ', temp)
                temp = re.sub(r'\n', ' ', temp)
                temp = re.sub(r'\t', ' ', temp)
                temp = re.sub(r'&and;', '&', temp)
                temp = re.sub(r'&nbsp;', ' ', temp)
                temp = re.sub(r'&amp;', '&', temp)
                temp = re.sub(r'&#[\s\S]*?;', ' ', temp)
                temp = re.sub(r'\.', ' ', temp)
                temp = re.sub(r',', ' ', temp)
                temp = re.sub(r';', ' ', temp)
                temp = re.sub(r'\(', ' ', temp)
                temp = re.sub(r'\)', ' ', temp)
                temp = re.sub(r'\'', ' ', temp)
                temp = re.sub(r'\*', ' ', temp)
                temp = re.sub(r' [bcdefghijklmnopqrstuvwxyzBCDEFGHIJKLMNOPQRSTUVWXYZ] ', ' ', temp)
                temp = re.sub(r' +', ' ', temp)
                with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/10k_cleaned/' + file_name, 'w') as f:
                    f.write(temp)
                



#unknown stuff from the top
# temp = re.sub(r'\A[\s\S]*?FORM 10-K', ' ', temp)

