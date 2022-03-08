# Schema Generator

schema_ = {}

def merge(org_json):
    for dev_d in org_json:
        
        if type(dev_d) is dict:
            
            for key, value in dev_d.items():
                
                if type(value) is str:
                    schema_[key]=""
                
                elif type(value) is list:
                    
                    if type(value[0]) is str:
                        schema_[key]=[""]
                    keys_list=[]
                    values_list=[]
                    
                    if type(value[0]) is dict:
                        nested_dic=value[0]
                        for k, values in nested_dic.items():
                            keys_list.append(k)
                            values_list.append("")

                        zip_iterator = zip(keys_list, values_list)
                        a_dictionary = dict(zip_iterator)
                        schema_[key]=[a_dictionary]
        
            
        elif type(dev_d) is list:
            for item in dev_d:
                merge(item)
       
        else:
            raise Exception()
            
    return schema_