import csv

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
        self.av = []
   
        for index in range(int(len(self.per))):
            if index % 7 == 0:
                k+=1

            self.av[k]+=int(self.per[index])
        
        print(self.av)
                
    def __str__(self):
        return f"id of Professors={self.id}\nTeacher Name={self.name}\nSubject id={self.subj}\nLesson Type={self.type}\nPairs{self.per}"
        

class Cabinets:
    def __init__(self,id,lab,nr):
        self.id=id
        self.lab=bool(lab)
        self.nr=int(nr)
    def __str__(self):
        return f"Cabinet id={self.id}\nIs Lab={self.lab}\nMax Nr of People in Cabinet={self.nr}"

#reading from the file

groups_list = []

with open('Groups and Subjects (FAF Hack) - Grupe.csv',mode='r')as file1:
    grupe=csv.reader(file1)
    for lines in grupe:
        try:
            groups_list.append(Groups(lines[0],lines[1],lines[2],lines[3],lines[4]))
        except Exception:
            continue
        

cab_list = []

with open('Groups and Subjects (FAF Hack) - Cabinete.csv')as file2:
    cabs = csv.reader(file2)
    for lines in cabs:
        try:
            cab_list.append(Cabinets(lines[0],lines[1],lines[2]))
        except :
            continue 



sub_list = []

with open('Groups and Subjects (FAF Hack) - Subiecte.csv')as file3:
    subs = csv.reader(file3)
    for lines in subs:
        try:
            sub_list.append(Subjects(lines[0],lines[1],lines[2],lines[3],lines[4]))
        except:
            continue


prof_list = []

with open('Groups and Subjects (FAF Hack) - Profesori.csv')as file4:
    prof = csv.reader(file4)
    for lines in prof:
        try:
            prof_list.append(Professors(lines[0],lines[1],lines[2],lines[3],lines[4:-1]))
        except:
            print('except')
            continue

