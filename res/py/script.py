import json

import pandas as pd # !pip install pandas si vous ne l'avez pas deja installee



def get_data_df(datas, key):

    if type(key) is list:

        sub_datas = datas

        for k in key[:-1]:

            sub_datas = pd.DataFrame(list(sub_datas[k]))

        return pd.DataFrame(list(sub_datas.pop(key[-1])))

    return pd.DataFrame(list(datas.pop(key)))



def parse_headers(datas):

    values = [{data_dict['name'].lower() : data_dict['value'] for data_dict in data} for data in datas]

    return pd.DataFrame(values)



def get_datas_from_file(filename):

    with open(filename, 'r', encoding='utf-8') as fichier:

        data = json.load(fichier)



    entries = pd.DataFrame(data['log']['entries'])



    elems = ['response', 'request', '_initiator', 'timings', ['response', 'content']]



    datas_df = {}

    for elem_name in elems:

        if type(elem_name) is list:

            key_name, val_name = elem_name

            df = get_data_df(datas_df[key_name], val_name)

        else:

            df = get_data_df(entries, elem_name)



        elem_name = elem_name if type(elem_name) is not list else "_".join(elem_name)

        datas_df[elem_name] = df



    for elem in ['response', 'request']:

        headers = list(datas_df[elem].pop('headers'))

        datas_df['{}_headers'.format(elem)] = parse_headers(headers)

    datas_df['infos'] = pd.DataFrame(entries)
    return datas_df

filename = "www.miniclip.com.har"

datas_df = get_datas_from_file(filename)

print(datas_df.keys()) #Affiche les categories
col = datas_df['infos'].columns
print(col)

datas_df['infos'].to_csv('miniclip.infos.csv')
# df.to_csv('www.miniclip.com.csv')

# help(pd.DataFrame.describe) #donne la signature de la fonction describe
