# csvtojson.py
import json,codecs
from logging import getLogger
LOGGER = getLogger(__name__)

from xtojson import XtoJSON

class CSVtoJSON(XtoJSON):
    """ csvのJSON変換クラス  """
    def convert(self,formatdata,filepath,errorfilepath):
        """ CSVファイルをJSONへ変換 """
        c1 = CSVtoJSON()
        csv_dict = {'data':None}
        try:
            with open(formatdata,'r') as file:
                json_dict = json.load(file)

            list = []
            list_i = []
            with codecs.open(filepath,'r','UTF-8') as file2:
                for i in file2:
                    d = i.rstrip()
                    list_i.append(d)
                    line = i.strip().split(',')
                    list.append(line)

            x=0
            y=0
            z=0
            list_csv =[]
            while z < len(list):
                dict_csv = {}
                for a in json_dict:
                    result = c1.validate(json_dict[a],list[y][x])
                    if result == None:
                        c1.writeerror(errorfilepath,list_i[z])
                    dict_csv[a] = result
                    x += 1
                list_csv.append(dict_csv)
                x = 0
                y += 1
                z += 1

            csv_dict['data'] = list_csv
            return csv_dict

        except:
            return None

# c1 = CSVtoJSON()
# csv_dict = {'data':None}
# try:
#     #正常ファイル
#     with open('./resources/format/csv.json','r') as file:
#     #異常ファイル
#     # with open('./resources/format/bad-csv.json','r') as file:
#         json_dict = json.load(file)
    
#     list = []
#     list_i = []
#     #正常ファイル
#     with codecs.open('./resources/data/20xx-csv.csv','r','UTF-8') as file2:
#     #異常ファイル
#     # with codecs.open('./resources/data/bad-20xx-csv.csv','r','UTF-8') as file2:
#         for i in file2:
#             d = i.rstrip()
#             list_i.append(d)
#             line = i.strip().split(',')
#             list.append(line)
    
#     # print(list_i)
#     # print(json_dict)
#     # print(list)

#     # def validate(self,datatype,value):
#     x=0
#     y=0
#     z=0
#     list_csv = []
#     while z < len(list):
#         dict_csv = {}
#         for a in json_dict:
#             result = c1.validate(json_dict[a],list[y][x])
#             if result == None:
#                 c1.writeerror('20xx-csv_error.csv',list_i[z])
#             dict_csv[a] = result
#             x += 1
#         list_csv.append(dict_csv)
#         x = 0
#         y += 1
#         z += 1

#     # print(list_csv)

#     csv_dict['data'] = list_csv

#     # return csv_dict
#     print(csv_dict)
# except:
#     print(None)
    # return None


# list = []
# dict = {}
# for val in range(5):
#     # dict = {}
#     dict[str(val)] = str(val)
#     list.append(dict)

# print(list)
# print(dict)