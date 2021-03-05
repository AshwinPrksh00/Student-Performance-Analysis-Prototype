import streamlit as strm
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import clear_output
#%matplotlib inline

df1 = pd.read_excel('Student1.xlsx')
df1 = pd.DataFrame(df1)
df1 = df1.drop('Unnamed: 0', axis=1)
maths = df1.iloc[1:11,:]
phy = df1.iloc[12:22,:]
chem = df1.iloc[23:, :]
#strm.write(df1)
strm.title("\t\tStudent Performance Analysis")

chap = df1.columns.tolist()
chap.remove('TestNumber')
m=[]
p=[]
ch=[]
for i in range(10):
    m.append(maths[chap[i]].astype(str).astype(int).mean())
    p.append(phy[chap[i]].astype(str).astype(int).mean())
    ch.append(chem[chap[i]].astype(str).astype(int).mean())

def awareplot(df,mean1,st,st1):
    for i in df.index:
        if(float(df[st][i])<=mean1-2):
            df['Label'][i] = "Danger Zone"
        elif(float(df2[st][i])>(mean1-2) and float(df2[st][i])<=mean1):
            df['Label'][i] = "Safe Zone"
        elif(float(df2[st][i])>=9):
            df['Label'][i] = "Keep It Up"
        elif(float(df2[st][i])>mean1 and float(df2[st][i])<=mean1+2):
            df['Label'][i] = "Above Average"
        else:
            df['Label'][i] = "Keep It Up"
    df.reset_index(inplace = True)
    fig2 = px.scatter(x =df.index+1 , y = df[st].astype(str).astype(int), color = df['Label'], color_discrete_map={"Danger Zone" : "red", "Safe Zone" : "orange", "Above Average" : "blue", "Keep It Up" : "green"}, hover_name = df['Label'], size = (df[st].astype(str).astype(int))*10)
    fig2.update_layout(title = st1+" "+st+" Analysis", xaxis_title = 'Tests', yaxis_title = 'Marks')
    fig2.update_traces(hovertemplate = '<i>TestNo</i>: %{x}'+
                                        '<br><b>Marks</b>: %{y}<br>')
    strm.write(fig2)

strm.write("## Maths Chapter Analysis")
str3 = strm.selectbox("Choose any chapter : ", chap, key="Chapter1")
df2 = pd.DataFrame(maths[str3])
df2.insert(1,'Label',"")
for i in range(10):
    if(str3==chap[i]):
        keyw = i
        break               
    
awareplot(df2,m[keyw],str3,'Maths')

#Chapterwise Analysis of Physics Subject
strm.write("## Physics Chapter Analysis")
str4 = strm.selectbox("Choose any chapter : ", chap, key="Chapter2")
df2 = pd.DataFrame(phy[str4])
df2.insert(1,'Label',"")
for i in range(10):
    if(str4==chap[i]):
        keyw1 = i
        break 

awareplot(df2,p[keyw1],str4,'Physics')

#Chapterwise Analysis of Chemistry Subject
strm.write("## Chemistry Chapter Analysis")
str5 = strm.selectbox("Choose any chapter : ", chap, key="Chapter3")
df2 = pd.DataFrame(chem[str5])
df2.insert(1,'Label',"")
for i in range(10):
    if(str5==chap[i]):
        keyw2 = i
        break 

awareplot(df2,ch[keyw2],str5,'Chemistry')

#Algorithm for calculating grade
dummy = []
dummy1 = [0,0,0,0,0,0,0,0,0,0]
class sort:
    marks = []
    index = []
    grade = []
    count = 0
    
    def inputval(j):
        for i in range(1,11):
            sort.marks.append(dump.iloc[j,i])

    def sorting(k):
            index = [1,2,3,4,5,6,7,8,9,10]
            sort.inputval(k)
            marks = sort.marks
            for i in range(0,10):
                for j in range(i+1,10):
                    if marks[i] > marks[j]:
                        temp = marks[i]
                        marks[i] = marks[j]
                        marks[j] = temp
                        temp = index[i]
                        index[i] = index[j]
                        index[j] = temp
            sort.index.append(index)
            for i in range(0,10):
                dummy.append(int(marks[i]))

    def increase(k):
        temp = sum[k]
        if temp < 50:
            marker = 50
        elif temp < 75:
            marker = 75
        elif temp < 90:
            marker = 90
        elif temp < 95:
            marker = 95
        markerO=10
        markerA=9
        markerB=8
        markerC=5
        marks = sort.marks
        for i in range(0,10):
            if int(marks[i]) < markerC:
                temp = temp + markerC-int(marks[i])
                marks[i] = markerC
            elif int(marks[i]) < markerB:
                temp = temp + markerB-int(marks[i])
                marks[i] = markerB
            elif int(marks[i]) < markerA:
                temp = temp + markerA-int(marks[i])
                marks[i] = markerA
            elif int(marks[i]) < markerO:
                temp = temp + markerO-int(marks[i])
                marks[i] = markerO
                
            if temp >= marker:
                sort.count = i+1
                break
        if i == 9:
            for j in range(0,10):
                if int(marks[j]) < markerB:
                    temp = temp + markerB-int(marks[j])
                    marks[j] = markerB
                elif int(marks[j]) < markerA:
                    temp = temp + markerA-int(marks[j])
                    marks[j] = markerA
                elif int(marks[j]) < markerO:
                    temp = temp + markerO-int(marks[j])
                    marks[j] = markerO
                if temp >= marker:
                    j=j+10
                    sort.count = j+1
                    break
        for i in range(0,10):
            dummy1[i] = int(marks[i]) - int(dummy[i])
        sort.marks.clear()

    def increaselev(number):
        dummy2 = [0,0,0,0,0,0,0,0,0,0]
        if number <= 10:
            for i in range(0,number):
                dummy2[i] = 1
        elif number > 10 and number <= 20:
            temp = number - 10
            for i in range(0,temp):
                dummy2[i] = 2
            for i in range(temp,10):
                dummy2[i] = 1
        sort.grade.append(dummy2)

ref = pd.DataFrame({'Tests':[f"Test{i+1}" for i in range(0,10)]})

def dlists(dff1, dff2, str2, dedstr):
    opt = ['Any']
    for i in range(10):
        opt.append("Test"+str(i+1))
    option = strm.selectbox("Choose Tests: ", opt,key=dedstr)
    str1 = option
    if(str1=='Any'):
        strm.write("Choose Any others")
    else:
        fig = px.scatter(x = dff1.loc[str1,:], y = dff2.loc[str1,:], size = (dff2.loc[str1,:]+1)*10, color =dff2.loc[str1,:], color_discrete_map={0 : "red", 1 : "yellow", 2 : "orange", 3 : "green"})
        fig.update_layout(title=str2+" "+str1+" Improvement Analysis", xaxis_title ='Chapters', yaxis_title = 'Grades to Improve')
        fig.update_traces(hovertemplate = '<b>Chapter No</b>: %{x}'+
                                     '<br><b>Grades to Improve</b>: %{y}<br>')
        strm.write(fig)

strm.write("## Maths Test Improvement Analysis")
#Assigning Maths dataframe to common dataframe
dump = maths

#Finding the total sum of elements on each row
sum=[]
s = 0

for i in range(0,10):
    for j in range(1,11):
        s+=int(dump.iloc[i,j])
    sum.append(s)
    s = 0

#Algorithm to find improvement of grade
obj = sort
obj.index.clear()
obj.grade.clear()
for m in range(0,10):
    obj.sorting(m)
    obj.increase(m)
    obj.increaselev(obj.count)

#Plotting the values as a scatter plot
df3 = pd.DataFrame(obj.index)
df4 = pd.DataFrame(obj.grade)
df4 = df4.set_index(ref['Tests'])
df3 = df3.set_index(ref['Tests'])
dlists(df3,df4,'Maths','Test1')


strm.write("## Physics Test Improvement Analysis")
#Assigning Physics dataframe to common dataframe
dump = phy

#Finding the total sum of elements on each row
sum=[]
s = 0

for i in range(0,10):
    for j in range(1,11):
        s+=int(dump.iloc[i,j])
    sum.append(s)
    s = 0

#Algorithm to find improvement of grade
obj1 = sort
obj1.index.clear()
obj1.grade.clear()
for m in range(0,10):
    obj1.sorting(m)
    obj1.increase(m)
    obj1.increaselev(obj1.count)

#Plotting the values as a scatter plot
df5 = pd.DataFrame(obj1.index)
df6 = pd.DataFrame(obj1.grade)
df6 = df6.set_index(ref['Tests'])
df5 = df5.set_index(ref['Tests'])
dlists(df5,df6,'Physics','Test2')


strm.write("## Chemistry Test Improvement Analysis")
#Assigning Chemistry dataframe to common dataframe
dump = chem

#Finding the total sum of elements on each row
sum=[]
s = 0

for i in range(0,10):
    for j in range(1,11):
        s+=int(dump.iloc[i,j])
    sum.append(s)
    s = 0

#Algorithm to find improvement of grade
obj2 = sort
obj2.index.clear()
obj2.grade.clear()
for m in range(0,10):
    obj2.sorting(m)
    obj2.increase(m)
    obj2.increaselev(obj2.count)

#Plotting the values as a scatter plot
df7 = pd.DataFrame(obj2.index)
df8 = pd.DataFrame(obj2.grade)
df8 = df8.set_index(ref['Tests'])
df7 = df7.set_index(ref['Tests'])
dlists(df7,df8,'Chemistry','Test3')
    
