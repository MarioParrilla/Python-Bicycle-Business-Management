import json, os
from src.model.Partner import Partner

PATH = './src/data/admins.json'

def init():

    if(not(os.path.exists(PATH))):
        writeDefault()
    else: 
        os.remove(PATH)
        writeDefault()

def writeDefault(): 
    admin = Partner('admin', 'c/admin', '000000000', 'a@a.com', '00000000A', 'admin', True)
    file = open(PATH, 'a')
    #file.write(',\n')
    json.dump(json.dumps(admin.parseToJSON()), file)
    file.close()