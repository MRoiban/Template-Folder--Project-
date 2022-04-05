#!/usr/bin/env python3

"""
Names: tmplty, project, mkprj, mkp

"""

import os
import sys



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
    
    makeFolder(project_name+"/Class")
    makeFolder(project_name+"/Docs")
    makeFolder(project_name+"/Other")
    
    makeFile(project_name+"/main.cpp") 
    makeFile(project_name+"/makefile")
    
    
def pyFolders(project_name):
    """
    The function is used to create the appropriate folder with all the files needed to work with python code.
    Used as a template.
    
    """
    
    makeFolder(project_name+"/Class")
    makeFolder(project_name+"/Docs")
    makeFolder(project_name+"/Other")
    
    makeFile(project_name+"/"+ project_name +".py") 


def reactFolders(project_name):
    """
    The function is used to create the appropriate folder with all the files needed to work with react code to make an application with React.
    Used as a template.
    
    """
    makeFolder(project_name+"/src")
    makeFolder(project_name+"/src/screens")
    makeFolder(project_name+"/src/components")
    makeFolder(project_name+"/src/utils")
    makeFolder(project_name+"/src/assests")
    
    makeFile(project_name+"/App.tsx")   

def gdFolders(project_name):
    """
    The function is used to create the appropriate folder with all the files needed to work with react code to make an application with Godot.
    Used as a template.
    
    """
    makeFolder(project_name+"/Model")
    makeFolder(project_name+"/View")
    makeFolder(project_name+"/Controller")
    makeFolder(project_name+"/Other")
    makeFolder(project_name+"/Assets")

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
    
    if size <= 2:
        raise Exception("There are missing arguments that are needed for the command to work!")
    
    if "-c" in argv:
        project_name = argv[argv.index("-c") + 1]
        cppFolders(project_name)
        
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
        raise Exception("The given arguments aren't reconized by the command!")
        


def main():
    argv = sys.argv
    if "-project" in argv:
        project()
    else:
        raise Exception("The given arguments aren't reconized by the command!")
