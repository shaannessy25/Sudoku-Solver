
from cx_Freeze import setup, Executable
import sys

executables = [Executable("GUI.py")]

setup(
    name = "Sudoku Solver",
    options = {"build_exe": {"packages": ["pygame"], "includes":["icons.png"]}},
    executables = executables
)






# from cx_Freeze import setup, Executable

# # Process the includes, excludes and packages first

# includes = []
# excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
#         'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
#         'Tkconstants', 'Tkinter']
# packages = ["pygame", "OpenGL"]
# path = []

# GUI2Exe_Target_1 = Executable(
#     # what to build
#     script = "..\esp\main.py",
#     initScript = None,
#     base = 'Win32GUI',
#     targetDir = r"dist",
#     targetName = "acup_new.exe",
#     compress = True,
#     copyDependentFiles = True,
#     appendScriptToExe = False,
#     appendScriptToLibrary = False,
#     icon = None
#     )

# setup(

#     version = "0.1",
#     description = "No Description",
#     author = "No Author",
#     name = "cx_Freeze Sample File",

#     options = {"build_exe": {"includes": includes,
#                  "excludes": excludes,
























# import cx_Freeze

# executables = [cx_Freeze.Executable("GUI.py")]

# cx_Freeze.setup(
#     name="Sudoku",
#     options={"build_exe": {"packages": ["pygame"], "include_files": ["icons.png"]}},
#     description="Sudoku Solver",

#     executables = executables
#     )

