from fileinput import filename
import json
import os
import glob
from black import out
import pandas as pd
import numpy as np
import argparse

from schema import merge
from parser import parse_json_recursively
from json_editor import json_editor


parser = argparse.ArgumentParser(description='Convert google jsons to csvs')
parser.add_argument('--input', help='the input MyActivity directory', required=True)
parser.add_argument('--dest', help='the destination to store csvs', required=True)

args = parser.parse_args()

base_path=args.input
input_dirs=(os.listdir(base_path))


for folder in input_dirs:
    files=(os.listdir(base_path+"/"+folder))
    if "MyActivity.json" in files:
        
        in_file=os.path.join(base_path+"/"+folder+"/"+"MyActivity.json")
        print(in_file)
        
        # input call
        developer=json_editor(in_file)

        # parser call
        dic=parse_json_recursively(developer)
        
        # making df

        df=pd.DataFrame(dict([(k,pd.Series(v)) for k,v in dic.items()]))
        
        # making new dir "csvs" to save output

        out_path=args.dest

        os.makedirs(out_path+"/"+"csvs", exist_ok=True)

        # converting df to csv and saving in csvs dir

        df.to_csv(out_path+"/"+"csvs"+"/"+folder+".csv")
        
        dic.clear()