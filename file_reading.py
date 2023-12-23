import csv
with open('Groups and Subjects (FAF Hack) - Profesori.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
            
with open('Groups and Subjects (FAF Hack) - Grupe.csv',mode='r')as file1:
    grupe=csv.reader(file1)
    for lines in grupe:
        for element in lines:

class Groups:
    def __init__(self,id,sp,lg,nr,sids):
        self.id=int(id)
        self.sp=sp
        self.lg=lg
        self.nr=int(nr)
        self.sids=sids
    def __str__(self):
        return f"id of Group={self.id}\nSpeciality={self.sp}\nLanguage={self.lg}\nNr of people in group={self.nr}\nSubject ids={self.sids}"
class Subjects:
    def __init__(self,id,uc,t,p,l,tot,year,sem):
        self.id=int(id)
        self.uc=uc
        self.t=int(t)
        self.p=int(p)
        self.l=int(l)
        self.tot=int(tot)
        self.year=int(year)
        self.sem=int(sem)
    def __str__(self):
        return f"id of Subject={self.id}\nCourse={self.uc}\nTheory={self.t}\nPractice={self.p}\nLabs={self.l}\nTotal={self.tot}\nYear={self.year}\nSemester={self.sem}"

class Professors:
    def __init__(self,id,name,subj,type,per):
        self.id=int(id)
        self.name=name
        self.subj=subj
        self.type=type
        self.per=per
    def __str__(self):
        return f"id of Professors={self.id}\nTeacher Name={self.name}\nSubject id={self.subj}\nLesson Type={self.type}\nPairs{self.per}"

class Cabinets:
    def __init__(self,id,lab,nr):
        self.id=id
        self.lab=bool(lab)
        self.nr=int(nr)
    def __str__(self):
        return f"Cabinet id={self.id}\nIs Lab={self.lab}\nMax Nr of People in Cabinet={self.nr}"


