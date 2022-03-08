# Recursive Parser

dic={}

def parse_json_recursively(json_object, pre_key = ""):
    
    if type(json_object) is dict:
        for index, k in enumerate(json_object):
            
            if type(json_object[k]) is str:
                
                if pre_key:
                    #print("a")
                    kk = "{}_{}".format(pre_key, k)
                else:
                    kk = "{}".format(k)
                    
                
                if kk not in dic:
                    dic[kk]=[]

                if index==0:
                    dic[kk].append(json_object[k])

                elif kk in dic:
                    dic[kk].append(json_object[k])
                    
            if type(json_object[k]) is list:
                list_length=len(json_object[k])

                if list_length==1:

                    parse_json_recursively(json_object[k][0], k)
                else:
                    for item in json_object[k]:
                        parse_json_recursively(item, k)
                
                
            if type(json_object[k]) is dict:
                parse_json_recursively(json_object[k], k)

    elif type(json_object) is list:
        for item in json_object:
            parse_json_recursively(item)
    
    else:
        # List case handling                        
        if pre_key not in dic:
            dic[pre_key] = []
        dic[pre_key].append(json_object)
        
        
    return dic
