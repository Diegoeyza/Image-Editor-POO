How do I add a new filter/composition to the image editor?
	1) You will need to create a new .py file in the filters/compositions folder accordingly. This file should have the name of the filter
	2) Inside the file, create the corresponding class (inhereting from the abstract class filter/composition) for the filter with the corresponding init and the apply method (to make this easier, copy one of the existing filters and modify it accordingly)
	3) Modify the init file in the filters/compositions folder to include the new filter
	4) Create a new file in the intermediary folder with the name Intermfiltername.py
	5) Inside the new file, copy one of the already existing interm files and modify it, make sure that your new interm class inherits from the intermediary class (keep in mind there are 2, choose which one to use based on the filter/composition you made)
	6) Modify the init file in the folder to include the new interm you made

Now you can use your new filter by running the main file (Image Editor.py), enjoy!!

What format should the script have?
The script shall follow JSON formatting, meaning it's contents are inside {}, defining a name and a string of commands, delimiting the various filters or compositions applied by the '/' character, each one specifies the variables needed for it's class constructor in order, delimited by a ';' character, you can check the syntax for each action in the params method. For example:
{"Name": "Your script name here", "Commands": "Base Image/Pixelate; 90/Draw rectangle; 50; 50; 500; 200; (255, 0, 0); 5/Draw a smiling face; 50; 50; (255, 0, 0); 400/"}


Usage instructions

To start, run the file Image Editor.py, then proceed with one of the following actions:
1-Start a new project: This allows the user to create a new project with an image (the file must be provided with the parth relative to the runner), this new project will save a copy of the file to edit, a base file to undo changes, a changelog and a script log. The project must have a unique name, but the file can be the same between projects
2-Work on an existing project: This allows the user to work on a previously created project
3-Show an image from a project: This allows the user to see the current status of the image inside of a project
4-Show the changes on a project: This shows the changelog with chronological order
5-Undo changes on a project: Allows the user to undo any change (there is no need to do it one by one) and also tells the user what to enter to undo a script
6-Save a project: Saves a project with its image so that it can be imported another time
7-Load a previously saved project: Loads a previously saved project with all of the changes, features and scripts
8-Save a script: Allows the user to save a script based on the changelog (The user must give a unique name to the script, otherwise it will be called Script_ as default). This script can be then applied to any project
9-Load a script: Load a previously saved script into the current project
To close the editor, type END\n

After starting a project or working on an existing project, the user will be able to apply filters or compositions to the image, each with its own parameters, which are described as needed