import open_process_file
import database_tool

process = open_process_file.ProcessFile()
mongoDB = database_tool.databaseTool()

data = process.open_file()
json_list = process.processing_json(data)
#process.save_json(json_list)

mongoDB.insert_data(json_list)

for out_put in json_list:
    print(out_put)


 
