#!/usr/bin/env python3

"""
Names: tmplty, project, mkprj, mkp

"""

import os
import sys

folderPath = "C:/Users/roiba/Documents/My Projects/"


def makeFolder(newPath):
    """
    This function makes a folder at the given path.

    Args:
        newPath (str): The path for the new folder
    """

    if not os.path.exists(newPath):
        os.makedirs(newPath)


def makeFile(newPath):
    """This function is used to create a file at the given path.

    Args:
        newPath (str): The file path
    """

    file = open(newPath, "x")
    file.close()


def cppFolders(project_name="./project"):
    """
    The function is used to create the appropriate folder with all the files needed to work with c++ code.
    Used as a template.

    """

    makeFolder(folderPath+project_name+"/Class")
    makeFolder(folderPath+project_name+"/Docs")
    makeFolder(folderPath+project_name+"/Other")

    makeFile(folderPath+project_name+"/main.cpp")
    makeFile(folderPath+project_name+"/makefile")


def pyFolders(project_name):
    """
    The function is used to create the appropriate folder with all the files needed to work with python code.
    Used as a template.

    """

    makeFolder(folderPath+project_name+"/Class")
    makeFolder(folderPath+project_name+"/Docs")
    makeFolder(folderPath+project_name+"/Other")

    makeFile(folderPath+project_name+"/" + project_name + ".py")


def reactFolders(project_name):
    """
    The function is used to create the appropriate folder with all the files needed to work with react code to make an application with React.
    Used as a template.

    """
    makeFolder(folderPath+project_name+"/src")
    makeFolder(folderPath+project_name+"/src/screens")
    makeFolder(folderPath+project_name+"/src/components")
    makeFolder(folderPath+project_name+"/src/utils")
    makeFolder(folderPath+project_name+"/src/assests")

    makeFile(folderPath+project_name+"/App.tsx")


def gdFolders(project_name):
    """
    The function is used to create the appropriate folder with all the files needed to work with react code to make an application with Godot.
    Used as a template.

    """
    makeFolder(folderPath+project_name+"/Model")
    makeFolder(folderPath+project_name+"/View")
    makeFolder(folderPath+project_name+"/Controller")
    makeFolder(folderPath+project_name+"/Other")
    makeFolder(folderPath+project_name+"/Assets")


def project():
    """
    The parser will parse the command line argv into their appropriate functions and variables.

    Command line Args:
        -c : c++ 
        -p : py
        -r : react
        -gd : godot
    """

    argv = sys.argv
    size = len(argv) - 1

    if size <= 1:
        raise Exception(
            "There are missing arguments that are needed for the command to work!\nTry using the following command line arguments: -c: c++, -p: py, -r: react, -gd: godot")

    if "-cpp" in argv:
        project_name = argv[argv.index("-cpp") + 1]
        cppFolders(project_name)

    elif "-py" in argv:
        project_name = argv[argv.index("-py") + 1]
        pyFolders(project_name)
    elif "-p" in argv:
        project_name = argv[argv.index("-p") + 1]
        pyFolders(project_name)
    elif "-r" in argv:
        project_name = argv[argv.index("-r") + 1]
        reactFolders(project_name)

    elif ("-gd" in argv):
        project_name = argv[argv.index("-gd") + 1]
        gdFolders(project_name)

    else:
        raise Exception("The given arguments aren't reconized by the command!\nTry using the following command line arguments: -c: c++, -p: py, -r: react, -gd: godot")


def main():
    argv = sys.argv
    # if "-project" in argv:
    #     project()
    # else:
    #     raise Exception("The given arguments aren't reconized by the command!")
    project()
