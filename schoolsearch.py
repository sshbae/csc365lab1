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


def gradeSearchNoOpt(stuDf):
    for index, row in stuDf.iterrows():
        print(f'{row["StLastName"]} {row["StFirstName"]}')

def gradeSearch(cmd, df):
    cmdLen = len(cmd)
    if cmdLen < 2:
        return
    grade = int(cmd[1])
    stuDf = df.where(grade == df["Grade"]).dropna()
    if cmdLen == 2:
        gradeSearchNoOpt(stuDf)
    elif cmdLen == 3:
        if cmd[2] == 'T':
            xtraSearchTeacher(stuDf)
        else:
            getHighLow(cmd[2], stuDf)
    

def busSearch(cmd, df):
    if len(cmd) < 2:
        return
    stuDf = df.where(int(cmd[1]) == df["Bus"]).dropna()
    for index, row in stuDf.iterrows():
        print(f'{row["StLastName"]} {row["StFirstName"]} Grade {int(row["Grade"])} Classroom {int(row["Classroom"])}')

def xtraSearchTeacher(df):
    names = df.loc[:,"TLastName"] + df.loc[:,"TFirstName"]
    names = names.unique()
    for name in names:
        print(name)


def classSearch(cmd, df):
    if len(cmd) < 2:
        return
    stuDf = df.where(int(cmd[1]) == df["Classroom"]).dropna()
    if len(cmd) > 2:
        if cmd[2] == 'T':
            xtraSearchTeacher(stuDf)
    else:
        for index, row in stuDf.iterrows():
            print(f'{row["StLastName"]}{row["StFirstName"]}')

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

    if cmd[0][0] == 'C' :
        classSearch(cmd, df)
    

def main():
    try:
       studf = pd.read_csv(r"./list.txt", header=None, names=["StLastName", "StFirstName", "Grade", "Classroom", "Bus", "GPA"])
    except FileNotFoundError:
        return
    try:
       teachdf = pd.read_csv(r"./teachers.txt", header=None, names=["TLastName", "TFirstName", "Classroom"])
    except FileNotFoundError:
        return
    df = pd.merge(studf,teachdf, indicator=True)

    print(f"""• S[tudent]: <lastname> [B[us]]
    \n• T[eacher]: <lastname>
    \n• B[us]: <number>
    \n• G[rade]: <number> [H[igh]|L[ow]|T[eacher]]
    \n• A[verage]: <number>
    \n* C[lassroom]: <number> [T[eacher]]
    \n• I[nfo]
    \n• Q[uit]""")
    cmd = input(">>")

    while cmd is not "Q":
        cmd = cmd.split()
        handleAsk(cmd, df)
        print(f"""• S[tudent]: <lastname> [B[us]]
        \n• T[eacher]: <lastname>
        \n• B[us]: <number>
        \n• G[rade]: <number> [H[igh]|L[ow]|T[eacher]]
        \n• A[verage]: <number>
        \n* C[lassroom]: <number> [T[eacher]]
        \n• I[nfo]
        \n• Q[uit]""")
        cmd = input(">>")
    return 

if __name__ == '__main__':
    main()
