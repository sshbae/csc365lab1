title: "csc365 lab1"
@echo off
    for %%a in ("*.in") do (
        "%%~a" < "C:\Users\Nicole Schwartz\Anaconda3\python.exe" "C:\Users\Nicole Schwartz\Anaconda3\csc365\csc365lab1\schoolsearch.py" > ".\output.txt"
    )