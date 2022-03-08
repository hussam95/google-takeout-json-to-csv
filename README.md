# google_takeoutJSONtoCSV

## Background
Google allows its users to [download](https://accounts.google.com/signin/v2/identifier?passive=1209600&osid=1&continue=https%3A%2F%2Ftakeout.google.com%2Fsettings%2Ftakeout&followup=https%3A%2F%2Ftakeout.google.com%2Fsettings%2Ftakeout&flowName=GlifWebSignIn&flowEntry=ServiceLogin) thier account activity data. Users can either download their data in json or html file formats. While useful, these file formats have certain limitations when it comes to data wrangling. 

On the other hand, csv is a very manuverable file format. With an aim to leverage the wrangling capabilities of csvs, this repository provides a solution to generate csvs of Google Takeouts downloaded in json file format. 


## Approach
The problem at hand is solved using a recursive technique. The idea is to continue parsing the jsons untill we reach the base keys. While recursive appraoch may have certain computational inefficiencies, it is very easy to understand. Therefore, any developer can very easily understand the logic used throughout this project due to its simplicity.


## File Structure and Explanation 
There are four .py files in this repo:

1. `main.py` is where all the magic happens. You have to only run this file. Provide "MyActivity" directory's path as input and the path of location where you want to save csvs as the output. You can use command line to provide these arguments. 

2. `parser.py` is the engine of this repository. This file has the recursive logic that is used in main.py to parse incoming jsons into csvs

3. `schema.py` solves the problem of loosing correspondence in the output csvs that may aruse due to missing keys/values in the jsons

4. `json_editor.py` appends empty values against missing values in the incoming jsons. It makes use of `schema.py` to make that happen. 

## How to Use
Run `main.py` using terminal. Provide --input and --dest arguments which correspond to the input and output locations.

Here is an example of how you can use your terminal to run this repository:
![Screenshot from 2022-03-09 00-35-00](https://user-images.githubusercontent.com/77602201/157312212-3a20d8c2-fe71-4c94-953f-3d0b55a26d22.png)

