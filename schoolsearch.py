import pandas as pd

def studentSearch(cmd, df):
    if len(cmd) < 2:
        return
    stuDf = df.where(cmd[1] == df["StLastName"]).dropna()
    for index, row in stuDf.iterrows():
        if len(cmd) == 2:
           print(f'{row["StLastName"]} {row["StFirstName"]} {int(row["Grade"])} {int(row["Classroom"])} {row["TLastName"]} {row["TFirstName"]}')
        elif len(cmd) == 3:
           print(f'{row["StLastName"]} {row["StFirstName"]} {int(row["Bus"])}')

def teacherSearch(cmd, df):
    if len(cmd) < 2:
        return
    stuDf = df.where(cmd[1] == df["TLastName"]).dropna()
    for index, row in stuDf.iterrows():
        print(f'{row["StLastName"]} {row["StFirstName"]}')
    
def getHighLow(highLow, df):
    if highLow[0] == 'H':
        df = df.nlargest(1,  ["GPA"])
    elif highLow[0] == 'L':
        df = df.nsmallest(1, ["GPA"])
    for index, row in df.iterrows():
         print(f'{row["StLastName"]} {row["StFirstName"]} GPA {row["GPA"]} Teacher {row["TLastName"]} {row["TFirstName"]} Bus {int(row["Bus"])}')

def gradeSearchNoOpt(grade, stuDf):
    for index, row in stuDf.iterrows():
        print(f'{row["StLastName"]} {row["StFirstName"]}')

def gradeSearch(cmd, df):
    cmdLen = len(cmd)
    if cmdLen < 2:
        return
    grade = int(cmd[1])
    stuDf = df.where(grade == df["Grade"]).dropna()
    if cmdLen == 2:
        gradeSearchNoOpt(grade, stuDf)
    elif cmdLen == 3:
        getHighLow(cmd[2], stuDf)
    

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
    if stuDf.empty:
       return
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
    #df = pd.read_csv(r'\Users\Nicole Schwartz\Anaconda3\csc365\csc365lab1\students.txt', header=None, names=["StLastName", "StFirstName", "Grade", "Classroom", "Bus", "GPA", "TLastName", "TFirstName"])
    df = pd.read_csv(r"./students.txt", header=None, names=["StLastName", "StFirstName", "Grade", "Classroom", "Bus", "GPA", "TLastName", "TFirstName"])

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
