import re
import json
import os
import xlrd

#read cleaned 10k data
path = '/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/10k_cleaned/'

file_list = os.listdir(path)


#read country keyword data
rb = xlrd.open_workbook("/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/OffshoringDatabase_V1_all/country.xlsx")
sh = rb.sheet_by_name('Sheet1')
country = sh.col_values(0)


#read offshore keyword data
rb = xlrd.open_workbook("/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/OffshoringDatabase_V1_all/offshore.xlsx")
sh = rb.sheet_by_name('Sheet1')

output = sh.col_values(0)[1:]
for i in range(0, len(output)):
    output[i] = output[i].lower()

external_input = sh.col_values(1)[1:]
external_input = list(set(external_input))
external_input.remove('')
for i in range(0, len(external_input)):
    external_input[i] = external_input[i].lower()

internal_input = sh.col_values(2)[1:]
internal_input = list(set(internal_input))
internal_input.remove('')
for i in range(0, len(internal_input)):
    internal_input[i] = internal_input[i].lower()

indeterminate_input = sh.col_values(3)[1:]
indeterminate_input = list(set(indeterminate_input))
indeterminate_input.remove('')
for i in range(0, len(indeterminate_input)):
    indeterminate_input[i] = indeterminate_input[i].lower()


#get offshore data from 10k

offshore_list_list = []

for file_name in file_list:
    if file_name != '.DS_Store':
        with open(path + file_name, 'r') as f:
            content = f.read()
        content = content.lower()
        content = content.split(' ')
        for i in range(25, len(content)-25):
            if content[i] in country:
                for j in range(-25, 26):
                    if content[i + j] in output:
                        offshore_list_list.append([file_name, 'output', content[i]])
                    elif content[i + j] in external_input:
                        offshore_list_list.append([file_name, 'external_input', content[i]])
                    elif content[i + j] in ['purchase', 'purchases', 'purchased'] and content[i + j + 1] == 'from':
                        offshore_list_list.append([file_name, 'external_input', content[i]])
                    elif content[i + j] in internal_input:
                        offshore_list_list.append([file_name, 'internal_input', content[i]])
                    elif content[i + j] in indeterminate_input:
                        offshore_list_list.append([file_name, 'indeterminate_input', content[i]])
            elif content[i] + ' ' + content[i + 1] in country:
                for j in range(-25, 27):
                    if content[i + j] in output:
                        offshore_list_list.append([file_name, 'output', content[i]])
                    elif content[i + j] in external_input:
                        offshore_list_list.append([file_name, 'external_input', content[i]])
                    elif content[i + j] in ['purchase', 'purchases', 'purchased'] and content[i + j + 1] == 'from':
                        offshore_list_list.append([file_name, 'external_input', content[i]])
                    elif content[i + j] in internal_input:
                        offshore_list_list.append([file_name, 'internal_input', content[i]])
                    elif content[i + j] in indeterminate_input:
                        offshore_list_list.append([file_name, 'indeterminate_input', content[i]])
            elif content[i] + ' ' + content[i + 1] + ' ' + content[i + 2] in country:
                for j in range(-25, 28):
                    if content[i + j] in output:
                        offshore_list_list.append([file_name, 'output', content[i]])
                    elif content[i + j] in external_input:
                        offshore_list_list.append([file_name, 'external_input', content[i]])
                    elif content[i + j] in ['purchase', 'purchases', 'purchased'] and content[i + j + 1] == 'from':
                        offshore_list_list.append([file_name, 'external_input', content[i]])
                    elif content[i + j] in internal_input:
                        offshore_list_list.append([file_name, 'internal_input', content[i]])
                    elif content[i + j] in indeterminate_input:
                        offshore_list_list.append([file_name, 'indeterminate_input', content[i]])
            elif content[i] + ' ' + content[i + 1] + ' ' + content[i + 2]  + ' ' + content[i + 3] in country:
                for j in range(-25, 29):
                    if content[i + j] in output:
                        offshore_list_list.append([file_name, 'output', content[i]])
                    elif content[i + j] in external_input:
                        offshore_list_list.append([file_name, 'external_input', content[i]])
                    elif content[i + j] in ['purchase', 'purchases', 'purchased'] and content[i + j + 1] == 'from':
                        offshore_list_list.append([file_name, 'external_input', content[i]])
                    elif content[i + j] in internal_input:
                        offshore_list_list.append([file_name, 'internal_input', content[i]])
                    elif content[i + j] in indeterminate_input:
                        offshore_list_list.append([file_name, 'indeterminate_input', content[i]])

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/4offshore.json', 'w') as handle:
    json.dump(offshore_list_list, handle, indent=2)