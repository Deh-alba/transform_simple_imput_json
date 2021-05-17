from datetime import datetime  , date
import os
import os.path
import json
import math




#class for open and process files
class ProcessFile:
        
    # function for open json an return dict wich data
    # input -> None
    # output -> dict
    def open_file(self):
        with open('/root/exercising_python/simple-input.json',) as f:
            data = json.load(f)        
        return data



    # function that recive dict and transform for patterns simple_output
    # input -> dict
    # output -> dict
    def processing_json(self,data):
        
        jsonList = list()


        for x in data:

            data_dict = {
                "server": x['server'],
                
            }

            if "process" in x:
                data_dict['process'] = x['process']
            else:
                data_dict['process'] = x['source']        
            
            if type(x['date']) is str:
                data_dict['date']=x['date']
            
                #print(data_dict['date'])
            elif int(math.log10(x['date']))+1 == 13:
                data_dict['date'] = datetime.fromtimestamp(int(x['date'])/1000).isoformat(timespec='microseconds')
            elif int(math.log10(x['date']))+1 == 10:
                data_dict['date'] = datetime.fromtimestamp(int(x['date'])).isoformat(timespec='microseconds')

            if "severity" in x:
                data_dict['severity'] = x['severity']
                data_dict['message'] = x['message']
                jsonList.append(data_dict)    
            else:
                data_dict['severity'] = "WARN"
                for event in x['events']:
                    data_dict['message'] = event['indicator-type']+" "+event['indicator-value']
                    jsonList.append(data_dict)


        return jsonList
   
    # function for save json in file
    def save_json(self,data):
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)        
        
        return print("ok")