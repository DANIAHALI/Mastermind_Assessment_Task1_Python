'''1.	Write the Pseudo-code (Logic Flow) for a Deluge function 
that catches this specific "Same Child / Different Parent" scenario.


Pseudo-code

IF (New_Lead.Student_Name == Existing_Lead.Student_Name)
  AND (New_Lead.Student_Cnic == Existing_Lead.Student_Cnic)
THEN
  Student Duplicate Flag(potential Flag) = True   #Which means same student from different email/family
  LINK to Existing Family Record also
ELSE
  Create New Lead

'''

import pandas
import pdb
import tkinter as tk
import os

''' Student Cnic and family email is taken from input form and pass through student function'''
def family_functio(cnic_entry, email_entry):
    #pdb.set_trace()
    print('In Family Function!')
    DB_Fmly = pandas.read_csv(str(os.getcwd()) + "\\DB File\\Family Data.csv")
    std_Cnic_list = DB_Fmly['Student Cnic'].tolist()
    Email_list = DB_Fmly['Email'].tolist()
    Fmly_dup_list = DB_Fmly['Possible Duplicate'].tolist()
    
    #pdb.set_trace()
    if int(cnic_entry) in std_Cnic_list:
        print(cnic_entry)
        print(std_Cnic_list)
        print(cnic_entry in std_Cnic_list)
        
        Fmly_dup_flag = True
        
        std_Cnic_list.append(cnic_entry)
        Email_list.append(email_entry)
        Fmly_dup_list.append(Fmly_dup_flag)
        
    else:
        Fmly_dup_flag = False
        
        std_Cnic_list.append(cnic_entry)
        Email_list.append(email_entry)
        Fmly_dup_list.append(Fmly_dup_flag)
        
    Family_DF = pandas.DataFrame()
    Family_DF['Student Cnic'] = std_Cnic_list
    Family_DF['Email'] = Email_list
    Family_DF['Possible Duplicate'] = Fmly_dup_list
    
    Family_DF.to_csv(str(os.getcwd()) + "\\DB File\\Family Data.csv", index=False)
    
    

''' Input Name, Cnic and email from input form '''
    
def Deluge_function(name_entry, cnic_entry, email_entry):
    print('Here!')
    #pdb.set_trace()
    
    DB_Std = pandas.read_csv(str(os.getcwd()) + "\\DB File\\Student Data.csv")
    Name_list = DB_Std['Name'].tolist()
    Cnic_list = DB_Std['Cnic'].tolist()
    dup_list = DB_Std['Student Duplicate Flag'].tolist()
    
    
    if (name_entry in Name_list) and (int(cnic_entry) in Cnic_list):
        Std_dup_flag = True
        
        Name_list.append(name_entry)
        Cnic_list.append(cnic_entry)
        dup_list.append(Std_dup_flag)
        
    else:
        Std_dup_flag = False
        
        Name_list.append(name_entry)
        Cnic_list.append(cnic_entry)
        dup_list.append(Std_dup_flag)
    
    family_functio(cnic_entry, email_entry)
    
    
    Student_DF = pandas.DataFrame()
    Student_DF['Name'] = Name_list
    Student_DF['Cnic'] = Cnic_list
    Student_DF['Student Duplicate Flag'] = dup_list
    
    Student_DF.to_csv(str(os.getcwd()) + "\\DB File\\Student Data.csv", index=False)
    
    
    
    