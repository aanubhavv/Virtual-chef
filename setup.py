import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['resources']

# TARGET
target = Executable(
    script="app.py",
    base="Win32GUI",        
    icon="resources/logo.ico"
)

# SETUP CX FREEZE
setup(
    name = "Virtual Chef",
    version = "1.0",
    description = "chef for all your kitchen needs",
    author = "Anubhav Garg",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)