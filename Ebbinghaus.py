import datetime
import json

''' 
Few Constants:
DATE_FORMAT: format for decoding datetime object;
E: Ebbinghaus forgetting curve number;
'''
DATE_FORMAT = '%Y-%m-%d'
E = [0, 1, 2, 4, 7, 15, 30, 180, 240]


'''
JSON parser for decoding the json file -- with key 
represents to the label of the project in the list,
and value repersents the starting date of the project --
by converting value into datetime format.

    (k, v) -> (k, datetime(v))
'''
def datetime_parser(dct):
    for k, v in dct.items():
       dct[k] = datetime.datetime.strptime(v, DATE_FORMAT) 
    return dct

D = {}

'''
BTW, I didn't handle exception here ...
'''
with open('record.txt') as f:
    D = json.load(f, object_hook = datetime_parser)

'''
The Calculator, which represents the filtered list that 
all the projects need to be reviewd at TODAY(.today()) 
by applying Ebbinghaus forgetting curve algorithm.
'''
_out = list(filter(lambda k: 
                    (datetime.date.today() - D[k].date()).days in E,
                    D.keys()))

print(_out)
