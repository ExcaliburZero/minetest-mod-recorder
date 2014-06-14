"""
Minetest Mod HTML Generator Program
"""

#Imports
import json

#Grabs dictionary of mod from master dictionary
def grabMod(modName):
    mod = master_dict[modName]
    return mod

#Extracts each part from mod dictionary
def extractMod(mod):
    name = mod["Name"]
    author = mod["Author"]
    depends = mod["Depends"]
    forum = mod["Forum"]
    database = mod["Database"]
    gitHub = mod["GitHub"]

#Wrtie HTML code from mod list
def writeHTML():

    #Prints general beginning HTML
    #Note that "style.css" can be used to style the generated page
    print("<html><title>List of Mods</title><link rel=\"stylesheet\" href=\"style.css\" type=\"text/css\" /><body><div id=\"holder\">")

    #Prints info for each mod
    for modName, mod in master_dict.items():
        print("<h3>" + mod["Name"] + "</h3>")
        print("<ul>")
        print("<li>" + "Name: " + mod["Name"] + "</li>")
        print("<li>" + "Author: " + mod["Author"] + "</li>")
        print("<li>" + "Depends: " + mod["Depends"] + "</li>")
        
        #Prints values that are links as HTML links
        #Forum Topic
        if mod["Forum"] != "None":
            print("<li>" + "Forum Topic: " + "<a href=\"" + mod["Forum"] + "\">" + mod["Forum"] + "</a>" + "</li>")
        else:
            print("<li>" + "Forum Topic: None</li>")
            
        #Mod Database Entry
        if mod["Database"] != "None":
            print("<li>" + "MMDB Entry: " + "<a href=\"" + mod["Database"] + "\">" + mod["Database"] + "</a>" + "</li>")
        else:
            print("<li>" + "MMDB Entry: None</li>")
            
        #GitHub repo
        if mod["GitHub"] != "None":
            print("<li>" + "GitHub Repo: " + "<a href=\"" + mod["GitHub"] + "\">" + mod["GitHub"] + "</a>" + "</li>")
        else:
            print("<li>" + "GitHub Repo: None</li>")
        print("</ul>")
        print("</br>")

    #Prints general ending HTML code
    print("</div></body></html>")

#Open data file and get master directory from data file
data_file = "Mod_Data.txt"
global master_dict
master_dict = {}
master_dict = json.load(open(data_file))

#Grab mod info
grabMod("brazier")

writeHTML()
