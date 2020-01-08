import cx_Freeze
import sys

executables = [cx_Freeze.Executable("GUI.py")]

cx_Freeze.setup(
    name = "Sudoku Solver",
    options = {"build_exe": {"packages": ["pygame"], "include_files":["icons.png"]}},
    executables = executables 
)