## exercising_python

This small project aims to exercise some small concepts and play a little bit with the transformation of a json file.
o initially we will take a json entry, normalize it and put it in the default file saida_simples. In the sequence we will put this information in a simple mongoDB base and retrieve that information.
It should be noted that the files simple_input.json and simple_output.json have different structures, so the functions developed here deal with these differences and put all of them in the pattern of the simple_output.json file, which will also be used as a standard for entering the MongoDB database.

OBS: For run this code you should 
> 1 - You can install pymongo -> pip install pymongo
> 
> 2 - You can create one cluster in Atlas and add connfiguration in file database_tool.py
   
