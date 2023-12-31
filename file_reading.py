import csv
import random
import mysql.connector

class Groups:
    def __init__(self,id,sp,lg,nr,list_of_subs_ids):
        self.id=int(id)
        self.sp=sp
        self.lg=lg
        self.nr=int(nr)
        self.list_of_subs_ids= list_of_subs_ids

    def __str__(self):
        return f"id of Group={self.id}\nSpeciality={self.sp}\nLanguage={self.lg}\nNr of people in group={self.nr}\nSubject ids={self.list_of_subs_ids}"
    
    def add_subs_classes(self,class_list):
        self.list_of_subs = []
        self.list_of_subs_ids = list(map(int, self.list_of_subs_ids.split(', ')))

        for id in self.list_of_subs_ids:
            self.list_of_subs.append(class_list[id-1])

        
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
        self.av = [0,0,0,0,0,0]   
        k = -1
   
        for index in range(int(len(self.per))):
            if index % 7 == 0:
                k+=1

            self.av[k]+=int(self.per[index])
                        
    def __str__(self):
        return f"id of Professors={self.id}\nTeacher Name={self.name}\nSubject id={self.subj}\nLesson Type={self.type}\nPairs{self.per}"
    
class Cabinets:
    def __init__(self,id,lab,nr):
        self.id=id
        self.lab=bool(lab)
        self.nr=int(nr)
    def __str__(self):
        return f"Cabinet id={self.id}\nIs Lab={self.lab}\nMax Nr of People in Cabinet={self.nr}"
    
class per_hour:
    def __init__(self,group,cab,subj,type):
        self.group =group
        self.cab =cab
        self.subj =subj
        self.type =type
#reading from the file

# groups_list = []

# with open('Groups and Subjects (FAF Hack) - Grupe.csv',mode='r')as file1:
#     grupe=csv.reader(file1)
#     for lines in grupe:
#         try:
#             groups_list.append(Groups(lines[0],lines[1],lines[2],lines[3],lines[4]))
#         except Exception:
#             continue


# cab_list = []

# with open('Groups and Subjects (FAF Hack) - Cabinete.csv')as file2:
#     cabs = csv.reader(file2)
#     for lines in cabs:
#         try:
#             cab_list.append(Cabinets(lines[0],lines[1],lines[2]))
#         except :
#             print("skipped:",lines)
#             continue 

# sub_list = []

# with open('Groups and Subjects (FAF Hack) - Subiecte.csv')as file3:
#     subs = csv.reader(file3)
#     for lines in subs:
#         try:
#             sub_list.append(Subjects(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],lines[7]))
#         except:
#             print('error at', lines)
#             continue


# prof_list = []

# with open('Groups and Subjects (FAF Hack) - Profesori.csv')as file4:
#     prof = csv.reader(file4)
#     for lines in prof:
#         try:
#             prof_list.append(Professors(lines[0],lines[1],lines[2],lines[3],lines[4:-1]))
#         except:
#             continue

conn = mysql.connector.connect(
    host="sql11.freesqldatabase.com",
    user="sql11672526",
    password="QVkl1fXMYs",
    database="sql11672526"
)
cursor = conn.cursor()


cursor.execute("SELECT * FROM Grupe")
rows = cursor.fetchall()
groups_list = []

for lines in rows:
        try:
            groups_list.append(Groups(lines[0],lines[1],lines[2],lines[3],lines[4]))
        except Exception:
            continue


cursor.execute("SELECT * FROM Cabinete")
rows = cursor.fetchall()
cab_list = []

for lines in rows:
        try:
            cab_list.append(Cabinets(lines[0],lines[1],lines[2]))
        except :
            print("skipped:",lines)
            continue 


cursor.execute("SELECT * FROM Subiecte")
rows = cursor.fetchall()
sub_list = []

for lines in rows:
        try:
            sub_list.append(Subjects(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],lines[7]))
        except :
            print("skipped:",lines)
            continue 


cursor.execute("SELECT * FROM Profesori")
rows = cursor.fetchall()
prof_list = []

for lines in rows:
        try:
            prof_list.append(Professors(lines[0],lines[1],lines[2],lines[3],lines[4:-1]))
        except :
            print("skipped:",lines)
            continue 

conn.close() 


# for i in range(len(groups_list)):
#     groups_list[i].add_subs_classes(sub_list)
# uncomment when the database is updated

