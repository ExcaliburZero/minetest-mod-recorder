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
    folder = mod["Folder"]
    author = mod["Author"]
    depends = mod["Depends"]
    forum = mod["Forum"]
    database = mod["Database"]
    gitHub = mod["GitHub"]

#Wrtie HTML code from mod list
def writeHTML():

    html_code = [""]
    
    #Prints general beginning HTML
    #Note that "style.css" can be used to style the generated page
    html_code.append("<html><title>List of Mods</title><link rel=\"stylesheet\" href=\"style.css\" type=\"text/css\" /><body><div id=\"holder\">")
    
    #Prints info for each mod in alphabetical order
    for modName, mod in sorted(master_dict.items()):
        html_code.append("<h3>" + mod["Name"] + "</h3>")
        html_code.append("<ul>")
        html_code.append("<li>" + "Folder Name: " + mod["Folder"] + "</li>")
        html_code.append("<li>" + "Author: " + mod["Author"] + "</li>")
        html_code.append("<li>" + "Depends: " + mod["Depends"] + "</li>")
        
        #Prints values that are links as HTML links
        #Forum Topic
        if mod["Forum"] != "None":
            html_code.append("<li>" + "Forum Topic: " + "<a href=\"" + mod["Forum"] + "\">" + mod["Forum"] + "</a>" + "</li>")
        else:
            html_code.append("<li>" + "Forum Topic: None</li>")
            
        #Mod Database Entry
        if mod["Database"] != "None":
            html_code.append("<li>" + "MMDB Entry: " + "<a href=\"" + mod["Database"] + "\">" + mod["Database"] + "</a>" + "</li>")
        else:
            html_code.append("<li>" + "MMDB Entry: None</li>")
            
        #GitHub repo
        if mod["GitHub"] != "None":
            html_code.append("<li>" + "GitHub Repo: " + "<a href=\"" + mod["GitHub"] + "\">" + mod["GitHub"] + "</a>" + "</li>")
        else:
            html_code.append("<li>" + "GitHub Repo: None</li>")
        html_code.append("</ul>")
        html_code.append("</br>")

    #Prints general ending HTML code
    html_code.append("</div></body></html>")

    #Create HTML file
    html_file = open("mod_list.html", "w")

    #Write to HTML file
    html_file.write(str.join("\n", html_code))

    #Print HTML
    print(str.join("\n", html_code))

    #Close HTML file
    html_file.close()

#Open data file and get master directory from data file
data_file = "mod_data.txt"
global master_dict
master_dict = {}
master_dict = json.load(open(data_file))

#Call writeHTML function
writeHTML()
