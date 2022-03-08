# Json Editor vis-a-vis schema

from schema import merge
import json

def json_editor(file):
    with open(file, "r") as read_file:
        developer = json.load(read_file)
        
        # schema call
        schema_ = merge(developer)

        for key in schema_:
            
            for item in developer:
                
                for d_key in list(item):
                    
                    if key not in item.keys():
                        item[key]=schema_[key]
    
        return developer