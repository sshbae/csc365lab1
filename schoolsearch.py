import pandas as pd

def teacherSearch(cmd, df):
    if len(cmd) < 2:
        return
    stuDf = df.where(cmd[1] == df["TLastName"]).dropna()
    for index, row in stuDf.iterrows():
        print(f'{row["StLastName"]} {row["StFirstName"]}')
    
def gradeSearchNoOpt(grade, df):
    stuDf = df.where(grade == df["Grade"]).dropna()
    for index, row in stuDf.iterrows():
        print(f'{row["StLastName"]} {row["StFirstName"]}')

def gradeSearch(cmd, df):
    cmdLen = len(cmd)
    if cmdLen < 2:
        return
    if cmdLen == 2:
        gradeSearchNoOpt(int(cmd[1]), df)

def busSearch(cmd, df):
    if len(cmd) < 2:
        return
    stuDf = df.where(int(cmd[1]) == df["Bus"]).dropna()
    for index, row in stuDf.iterrows():
        print(f'{row["StLastName"]} {row["StFirstName"]} Grade {int(row["Grade"])} Classroom {int(row["Classroom"])}')

def avgSearch(cmd, df):
    if len(cmd) < 2:
        return
    stuDf = df.where(int(cmd[1]) == df["Grade"]).dropna()
    avg = stuDf["GPA"].mean()
    print(f'Grade level {cmd[1]}\nAverage GPA {avg}')

def infoSearch(cmd, df):
    for i in range(7):
        stuDf = df.where(i == df["Grade"]).dropna()
        print(f'Grade {i}: {stuDf.shape[0]} students')


def handleAsk(cmd, df):
    if cmd[0][0] == 'S' :
        studentSearch(cmd, df)
    if cmd[0][0] == 'T' :
        teacherSearch(cmd, df)

    if cmd[0][0] == 'G' :
        gradeSearch(cmd, df)

    if cmd[0][0] == 'B' :
        busSearch(cmd, df)

    if cmd[0][0] == 'A' :
        avgSearch(cmd, df)

    if cmd[0][0] == 'I' :
        infoSearch(cmd, df)
    

def main():
    df = pd.read_csv("./students.txt", header=None, names=["StLastName", "StFirstName", "Grade", "Classroom", "Bus", "GPA", "TLastName", "TFirstName"])

    print(f"""• S[tudent]: <lastname> [B[us]]
    \n• T[eacher]: <lastname>
    \n• B[us]: <number>
    \n• G[rade]: <number> [H[igh]|L[ow]]
    \n• A[verage]: <number>
    \n• I[nfo]
    \n• Q[uit]""")
    cmd = input(">>")

    while cmd is not "Q":
        cmd = cmd.split()
        handleAsk(cmd, df)
        print(f"""• S[tudent]: <lastname> [B[us]]
        \n• T[eacher]: <lastname>
        \n• B[us]: <number>
        \n• G[rade]: <number> [H[igh]|L[ow]]
        \n• A[verage]: <number>
        \n• I[nfo]
        \n• Q[uit]""")
        cmd = input(">>")
    return 

if __name__ == '__main__':
    main()
