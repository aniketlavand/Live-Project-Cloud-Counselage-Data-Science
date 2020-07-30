# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:23:54 2020

@author: ANIKET
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 
import sys

import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

arg1 = sys.argv[1]

str=''
str = arg1
data=pd.read_csv(str)

#Read the data


from matplotlib.backends.backend_pdf import PdfPages


pd.set_option('display.max_columns', None)




df1=data.dropna(axis=1)



#encoding
df3=df1[["Gender","Have you worked core Java","Have you worked on MySQL or Oracle database","Have you studied OOP Concepts","Label"]]
dummy_df=pd.get_dummies(df3,drop_first=True)




df1[["Gender","Have you worked core Java","Have you worked on MySQL or Oracle database","Have you studied OOP Concepts","Label"]]=dummy_df[["Gender_Male","Have you worked core Java_Yes","Have you worked on MySQL or Oracle database_Yes","Have you studied OOP Concepts_Yes","Label_ineligible"]]

                                                                                                                                        



df1['Label'] = df1['Label'].replace([1,0],[0,1])





with PdfPages('visualization-output.pdf') as pdf:
#1.no of students applied to diff technologies
 df1['Areas of interest'].value_counts().plot.bar()
 plt.title("No. Of Students applied to different technologies")
 plt.tight_layout()
 pdf.savefig()
 plt.close()






 df2 = df1[df1['Areas of interest']=='Data Science ']





 df3 = df2[df2['Programming Language Known other than Java (one major)']=='Python']
 df4=df2[df2['Programming Language Known other than Java (one major)']!='Python']          





 df4.loc[:, 'Programming Language Known other than Java (one major)'] = 'Not Python'


 # 2.no. of students who knew python and who did not



 
 plt.hist(df3['Programming Language Known other than Java (one major)'], 
         facecolor='orangered', 
         edgecolor='maroon'
         )

 plt.hist(df4['Programming Language Known other than Java (one major)'], 
         facecolor='green', 
         edgecolor='blue'
         )
 plt.title("No. of Students who knew python and who didn't")
 pdf.savefig()
 plt.close()

 # 3.Different ways students learned about this program




 df1['How Did You Hear About This Internship?'].value_counts().plot.bar()
 plt.title("Diff. ways student learned about this program")
 plt.tight_layout()
 pdf.savefig()
 plt.close()

#  4.studying in 4th year having cgpa >8.0



 df5 = df1[df1['Which-year are you studying in?']=='Fourth-year']





 df5 = df5[df5['CGPA/ percentage']>8.0]




 plt.hist(df5['Which-year are you studying in?'], 
         facecolor='orangered', 
         edgecolor='maroon'
         )
 plt.title('Students in Fourth-year ,having CGPA>8.0')

 pdf.savefig()
 plt.close()

#  5.digital marketing with score>8 in  verbal and written comm.



 df6 = df1[df1['Areas of interest']=='Digital Marketing ']




 df6 = df6[df6['Rate your verbal communication skills [1-10]']>8]
 df6 = df6[df6['Rate your written communication skills [1-10]']>8]




 plt.hist(df6['Areas of interest'], 
         facecolor='orangered', 
         edgecolor='maroon'
         )
 plt.xlabel('Students,having verbal and written comm. score>8')

 pdf.savefig()
 plt.close()

 # f.year wise & area of study wise


 sns.countplot(data=df1,x='Which-year are you studying in?',hue='Major/Area of Study')
 plt.title("Year-wise and area of study wise classification of students")
 pdf.savefig(bbox_inches='tight')
 plt.close()





#  g.City wise and College wise


 plt.figure(figsize=(10,8))
 sns.countplot(y ='College name', hue = "City", data = df1)
 plt.title("City and college wise classification of students")
 pdf.savefig(bbox_inches='tight')
 plt.close()



#  h.relationship b/w cgpa and target variable




 plt.scatter(df1['Label'], df1['CGPA/ percentage'],c="r")
 plt.xlabel("Eligibility")
 plt.title("Relationship b/w cgpa and target variable")
 plt.ylabel("CGPA/percentage")
 pdf.savefig()
 plt.close()

#  i. relationship b/w the Area of Interest and target variable



 plt.scatter(df1['Label'], df1['Areas of interest'],c="r",marker="*")
 plt.xlabel("eligibility")
 plt.ylabel("Areas Of Interest")
 plt.title("Relationship b/w area of interest and target variable")
 pdf.savefig(bbox_inches='tight')
 plt.close()

#  j.relationship b/w year of study, major, and the target variable




 df1['Which-year are you studying in?'] = df1['Which-year are you studying in?'].replace(['First-year','Second-year','Third-year','Fourth-year'],[1,2,3,4])
 sns.stripplot(x='Which-year are you studying in?' , y='Major/Area of Study' , data = df1,  
              jitter = True, hue ='Label', dodge = True)
 plt.title("Relationship b/w year of study ,major and target variable")
 pdf.savefig(bbox_inches='tight')
 plt.close()
