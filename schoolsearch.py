import pandas as pd

def studentSearch():
    
def handleAsk(cmd, df):
    if cmd[0][0] = 'S' :
        studentSearch(cmd, df)
    if cmd[0][0] = 'T' :
        teacherSearch(cmd, df)

    if cmd[0][0] = 'G' :
        gradeSearch(cmd, df)

    if cmd[0][0] = 'B' :
        busSearch(cmd, df)

    if cmd[0][0] = 'A' :
        avgSearch(cmd, df)

    if cmd[0][0] = 'I' :
        inforSearch(cmd, df)
    

def main():
    df = pd.read_csv("./students.txt", header=None, names=["StLastName", "StFirstName", "Grade", "Classroom", "Bus", "GPA", "TLastName", "TFirstName"])
    cmd = input()
    while cmd is not "Q":
        print(f"• S[tudent]: <lastname> [B[us]]
        \n• T[eacher]: <lastname>
        \n• B[us]: <number>
        \n• G[rade]: <number> [H[igh]|L[ow]]
        \n• A[verage]: <number>
        \n• I[nfo]
        \n• Q[uit]")
        cmd = cmd.split()
        handleAsk(cmd, df)
        cmd = input()
   return 

if __name__ == '__main__':
    main()
