"""
Minetest Mod Recorder Program
"""

#Imports
import json

#Get info of Mod
name = input("Name: ") #Get name of mod
folder = input("Folder Name: ") #Get name of the folder of the mod
author = input("Main Author: ") #Get main author of mod
depends = [] # Create depends list

#Get depends of mod
i = 0
while i == 0:
    entered = input("Depends (0 when done): ")
    if entered != "0":
        depends.append(entered) #Add depend to list
    else:
        i = 1 #End while loop

#Get link to mod's forum topic
forum = input("Forum Topic Link (0 if none): ")
if forum == "0":
    forum = "None"

#Get link to mod's entry on the Mod Database
database = input("Mod Database Link (0 if none): ")
if database == "0":
    database = "None"

#Get link to mod's repo on GitHub
gitHub = input("Main GitHub Repo (0 if none): ")
if gitHub == "0":
    gitHub = "None"

#Get mod's categories
categories = [] # Create categories list
i = 0
while i == 0:
    entered = input("Categories (0 when done): ")
    if entered != "0":
        categories.append(entered) #Add depend to list
    else:
        i = 1 #End while loop

#Print mod information
print("\n====Mod Info====")
print("Name: " + name)
print("Folder Name: " + folder)
print("Author: " + author)
print("Dependencies: " + ", ".join(depends))
print("Forum Topic: " + forum)
print("Mod Database: " + database)
print("GitHub Repo: " + gitHub)
print("Categories: " + ", ".join(categories))

#Assemble new mod dictionary
mod = {"Name": name, "Folder": folder, "Author": author, "Depends": ", ".join(depends), "Forum": forum, "Database": database, "GitHub": gitHub, "Categories": ", ".join(categories)}

#Open data file and get master directory from data file
data_file = "mod_data.txt"
master_dict = {}
master_dict = json.load(open(data_file))

#Add new mod to master dictionary
master_dict[name] = mod

#Write to data file
json.dump(master_dict, open(data_file,'w'))
