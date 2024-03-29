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
record.txt actually always exist, but anyway I will 
handle it over here.
'''
FILENAME = 'record.txt'
try:
    f = open(FILENAME, 'rb')
except OSError:
    print('File does not exit')
    sys.exit()

with f:
    D = json.load(f, object_hook = datetime_parser)


'''
The Calculator, which represents the filtered list that 
all the projects need to be reviewd at TODAY(.today()) 
by applying Ebbinghaus forgetting curve algorithm.
'''
f_days = lambda x: (datetime.date.today() - x).days
_out = list(filter(lambda k: 
                    f_days(D[k].date()) in E,
                    D.keys()))

print(', '.join(_out))
