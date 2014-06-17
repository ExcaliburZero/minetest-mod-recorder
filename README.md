#minetest-mod-recorder

A set of python scripts for making a data file with information on Minetest mods.

##Libraries Required
- json

##Mod Info
Each mod has entries for the following information:
- **Name** - The general name for a mod. This is often capitalized and usually is slightly different from the folder name.
- **Folder Name** - The name of the folder of a mod. This is generally not capitalized, and usually differs from the normal mod name.
- **Author** - The main author of the mod. If the mod has multiple authors then the author who has contributed the most to the mod should be entered.
- **Dependencies** - A list of dependencies of the mod.
- **Forum Topic** - The URL of the forum topic for the mod on the Minetest Forums, if such a topic exists.
- **Mod Database Entry** - The URL of the mod's entry on the Minetest Mod Database, if such an entry exists.
- **GitHub Repo** - The URL of the the mod's main GitHub repository, if such a repository exists.
