#!/usr/bin/env python3

"""
Names: tmplty, project, mkprj, mkp

"""

import os
import sys
import subprocess



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


def parser():
    """
    The parser will parse the command line argv into their appropriate functions and variables
    
    Command line Args:
        -c : c++ 
        -p : py
    """
    
    argv = sys.argv
    size = len(argv)
    
    if size <= 2:
        raise Exception("There are missing arguments that are needed for the command to work!")
    
    project_name = argv[1]
    
    if "-c" in argv:
        cppFolders(project_name)
    elif "-p" in argv:
        pyFolders(project_name)
    else:
        raise Exception("The given arguments aren't reconized by the command!")
        


def main():
    parser()
