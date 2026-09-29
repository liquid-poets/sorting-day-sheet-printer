#Author: Doug Ernst
#Date: 2/2/2021
#!/bin/python3

import string
import os,sys
import re

def IsBeerID(info):
    if len(info) == 4:
        if isAllDigits(0,3,info):
            #print("true")
            return True
    #if len(info) == 5:
        #if info[0] == '#' and isAllDigits(1,4,info):
            #print("true")
        #    return True
    return False
    
def isAllDigits(start,end,info):
    if start > end:
        print("error invalid input to alldigits")
    for i in range(start,end+1):
        if info[i].isalpha():
            return False
    return True
    
def isAllLetters(start,end,info):
    if start > end:
        print("error invalid input to allLetters")
    for i in range(start,end+1):
        if info[i].isdigit():
            return False
    return True

def GetCategoryNumber(info):
    return info[0]
    
def GetMapInfo(info):
    return info[0] + " " + info[1]
    
def GenerateTXTBeerMap(BeerCases,filename):
#Beer Map generation-----------------------------------------
#-----------------------------------------------
#if the iteration is 24 then new page is created
#Map will appear as a 6 X 4 grid per case
#ex:
#             Case A
# 1025 1026 1027 1028 1029 1030
# 1031 1032 1033 1034 1035 1036
# 1036 1037 1038 1039 1040 1041
# 1042 1043 1044 1045 1046 1047
#-----------------------------------------------
    X= 1
    Bermap = open(filename,"w")
    for beer in BeerCases:
        
        Bermap.write("    Case: "+str(X)+" of "+str(CaseTotal))
        Bermap.write('\n')
        Bermap.write("  ---------------------------------\n")
        #print("    Case: ",X," of ",CaseTotal)
        #print("  ---------------------------------")
        X += 1
        #-------
        Display = beer
        #-------
        x = 0
        for i in range(4):
            Bermap.write("  | ")
            #print("  | ",end = "")
            for j in range(6):
                Bermap.write(Display[x])
                Bermap.write(" ")
                #print(Display[x], end = " ")
                x += 1
            Bermap.write("|")
            Bermap.write("\n")
            #print("|",end = "")
            #print()
        Bermap.write("  ---------------------------------\n")
        Bermap.write("\n\n\n\n\n\n\n\n\n\n")
        #print("  ---------------------------------")
        
    Bermap.close()
    
def GenerateNTXTBeerMap(Beerinfo,filename):
#Beer Map generation-----------------------------------------
#-----------------------------------------------
#if the iteration is 24 then new page is created
#Map will appear as a 6 X 4 grid per case
#ex:
#             Case A
# 1025 1026 1027 1028 1029 1030
# 1031 1032 1033 1034 1035 1036
# 1036 1037 1038 1039 1040 1041
# 1042 1043 1044 1045 1046 1047
#-----------------------------------------------
    #print("-"*3)
    Bermap = open(filename,"w")
    num = 0
    mult = 1
    X = 1
    for x in range(0,len(Beerinfo)):
        if x % 6 == 0:
            Bermap.write('\n')
            #print("")
            mult = mult - 3
            
        if x % 24 == 0:
            num = 0
            #mult = mult - 3
            mult = int(mult/4)
            #X += 1
            if X != 1:
                #Bermap.write("----------------------------------------------------\n\n\n")
                Bermap.write("-"*mult)
                Bermap.write("\n\n\n")
            Bermap.write("Case: "+str(X)+" of "+str(CaseTotal))
            Bermap.write('\n')
            if X == 1:
                Bermap.write("-"*58)
            
            #Bermap.write("-----------------------------------------------------\n")
            Bermap.write("-"*mult)
            Bermap.write('\n')
            mult = 0
            #print()
            #print("Case: "+str(X)+" of "+str(CaseTotal))
            X += 1
            #print()
        Bermap.write(Beerinfo[x][0]+ "  " + Beerinfo[x][1]+ "   ")
        mult += len(Beerinfo[x][0]) + len(Beerinfo[x][1]) + 5
        #print(mult)
        #print(Beerinfo[x][0] + " " ,end="")
        #print(Beerinfo[x][1],end=" ")
        num += 1
        
    #print()
    #print(x)
    if num != 0 or num != 24:
        for y in range(num,24):
            if y % 6 == 0:
                Bermap.write('\n')
                #print()
            Bermap.write("xx #xxxx ")
            #print("xx #xxxx",end = " ")
        Bermap.write('\n'+"-"*58)
    Bermap.close()
    
    
def GenerateNCSVBeerMap(Beerinfo,filename):
#Beer Map generation-----------------------------------------
#-----------------------------------------------
#if the iteration is 24 then new page is created
#Map will appear as a 6 X 4 grid per case
#ex:
#             Case A
# 1025 1026 1027 1028 1029 1030
# 1031 1032 1033 1034 1035 1036
# 1036 1037 1038 1039 1040 1041
# 1042 1043 1044 1045 1046 1047
#-----------------------------------------------
    #print("-"*3)
    Bermap = open(filename,"w")
    num = 0
    mult = 1
    X = 1
    for x in range(0,len(Beerinfo)):
        if x % 6 == 0:
            Bermap.write('\n')
            #print("")
            mult = mult - 2
            
        if x % 24 == 0:
            num = 0
            #mult = mult - 3
            mult = int(mult/4)
            #X += 1
            if X != 1:
                #Bermap.write("----------------------------------------------------\n\n\n")
                #Bermap.write("-"*mult)
                Bermap.write("\n\n\n")
            Bermap.write("Case: "+str(X)+" of "+str(CaseTotal))
            Bermap.write('\n')
            #if X == 1:
                #Bermap.write("-"*58)
            
            #Bermap.write("-----------------------------------------------------\n")
            #Bermap.write("-"*mult)
            Bermap.write('\n')
            mult = 0
            #print()
            #print("Case: "+str(X)+" of "+str(CaseTotal))
            X += 1
            #print()
        Bermap.write(Beerinfo[x][0]+ "  " + Beerinfo[x][1]+ ",")
        #mult += len(Beerinfo[x][0]) + len(Beerinfo[x][1]) + 3
        #print(mult)
        #print(Beerinfo[x][0] + " " ,end="")
        #print(Beerinfo[x][1],end=" ")
        num += 1
        
    #print()
    #print(x)
    if num != 0 or num != 24:
        for y in range(num,24):
            if y % 6 == 0:
                Bermap.write('\n')
                #print()
            Bermap.write("xx #xxxx ,")
            #print("xx #xxxx",end = " ")
        #Bermap.write('\n'+"-"*58)
    Bermap.close()
        
    
def GenerateCSVBeerMap(BeerCases,filename):
#Beer Map generation-----------------------------------------
#-----------------------------------------------
#if the iteration is 24 then new page is created
#Map will appear as a 6 X 4 grid per case
#ex:
#             Case A
# 1025 1026 1027 1028 1029 1030
# 1031 1032 1033 1034 1035 1036
# 1036 1037 1038 1039 1040 1041
# 1042 1043 1044 1045 1046 1047
#-----------------------------------------------
    X= 1
    Bermap = open(filename,"w")
    for beer in BeerCases:
        
        Bermap.write("    Case: "+str(X)+" of "+str(CaseTotal))
        Bermap.write('\n')
        #Bermap.write("  ---------------------------------\n")
        Bermap.write("\n")
        #print("    Case: ",X," of ",CaseTotal)
        #print("  ---------------------------------")
        X += 1
        Display = beer
        x = 0
        for i in range(4):
            #Bermap.write("  | ")
            #print("  | ",end = "")
            for j in range(6):
                Bermap.write(Display[x])
                Bermap.write(",")
                #print(Display[x], end = " ")
                x += 1
            #Bermap.write("|")
            Bermap.write("\n")
            #print("|",end = "")
            #print()
        #Bermap.write("  ---------------------------------\n")
        Bermap.write("\n")
        #print("  ---------------------------------")
        Bermap.write("\n\n\n\n\n\n\n\n")
    Bermap.close()
        
def GenerateTXTBeerReport(Beerinfo,filename):
    BeerReport = open(filename,"w")
    X = 1
    iterator = 0
    subiterator = 0
    BeerReport.write("      Case: "+str(X)+" of "+str(CaseTotal))
    BeerReport.write('\n')
    BeerReport.write("   ------------------------\n")
    
    #print("      Case: ",X," of ",CaseTotal)
    #print("    ---------------------")
    for info in Beerinfo:
        BeerReport.write("   |")
        #print("    |",end = "")
        
        for i in info:
            iterator += 1
            BeerReport.write(i + "  ")
            #print(i ,end = " ")
        BeerReport.write("|\n")
        #print("|")
        subiterator += 1
        if subiterator == 24:
            subiterator = 0
            X += 1
            BeerReport.write("   ------------------------\n\n\n\n\n\n\n\n")
            BeerReport.write("      Case: "+str(X)+" of "+str(CaseTotal)+"\n")
            BeerReport.write("   ------------------------\n")
            #print("    ---------------------")
            #print('\n','\n')
            #print("      Case: ",X," of ",CaseTotal)
            #print("    ---------------------")   
    if subiterator != 0:
        for extra in range(subiterator,24):
            BeerReport.write("    |Empty                |\n")
            #print("    |Empty                |")
            subiterator += 1
        BeerReport.write("   ------------------------\n")
        #print("    ---------------------")
    #BeerReport.write("\n")
    #print()
    BeerReport.close()
    
def GenerateCSVBeerReport(Beerinfo,filename):
    BeerReport = open(filename,"w")
    X = 1
    iterator = 0
    subiterator = 0
    BeerReport.write("Case: "+str(X)+" of "+str(CaseTotal))
    BeerReport.write('\n')
    #BeerReport.write("    ---------------------\n")
    
    #print("      Case: ",X," of ",CaseTotal)
    #print("    ---------------------")
    for info in Beerinfo:
        #BeerReport.write("    |")
        #print("    |",end = "")
        
        for i in info:
            iterator += 1
            BeerReport.write(i + " ,")
            #print(i ,end = " ")
        BeerReport.write("\n")
        #print("|")
        subiterator += 1
        if subiterator == 24:
            subiterator = 0
            X += 1
            BeerReport.write("\n\n\n\n\n\n\n\n")
            BeerReport.write("Case: "+str(X)+" of "+str(CaseTotal)+"\n")
            BeerReport.write("\n")
            #print("    ---------------------")
            #print('\n','\n')
            #print("      Case: ",X," of ",CaseTotal)
            #print("    ---------------------")   
    if subiterator != 0:
        for extra in range(subiterator,24):
            BeerReport.write("Empty,Empty,Empty\n")
            #print("    |Empty                |")
            subiterator += 1
        BeerReport.write("\n")
        #print("    ---------------------")
    #BeerReport.write("\n")
    #print()
    BeerReport.close()

def GenerateTXTBeercategories(Beerinfo,filename):
#Create list of Category IDs
    #CategoryIDs = []
    CategoryData = []
    SubCatStore = []
    temp = ""

#Divide data into a list of lists based on category
    for info in Beerinfo:
        Cate = GetCategoryNumber(info)
        if temp == "":
            temp = Cate
            SubCatStore.append(info)
        elif Cate != temp:
            if len(Cate) != len(temp):
                CategoryData.append(SubCatStore)
                SubCatStore = []
                SubCatStore.append(info)
                temp = Cate 
            
            elif len(Cate) == 2:
                if Cate[0].isdigit() and Cate[1].isalpha():
                    if Cate[0] == temp[0]:
                        SubCatStore.append(info)
                        temp = Cate
                    if Cate[0] != temp[0]:
                        CategoryData.append(SubCatStore)
                        SubCatStore = []
                        SubCatStore.append(info)
                        temp = Cate
                if Cate[0].isalpha() and Cate[1].isdigit():
                    if Cate[0] != temp[0]:
                        SubCatStore.append(info)
                        temp = Cate
                    if Cate[0] == temp[0]:
                        CategoryData.append(SubCatStore)
                        SubCatStore = []
                        SubCatStore.append(info)
                        temp = Cate               
                if Cate.isdigit():
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
               

            elif len(Cate) == 3:
                if Cate[0] == temp[0] and Cate[1] == temp[1]:
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[0] == temp[0] and Cate[1] != temp[1]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[0] != temp[0] and Cate[1] != temp[1]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                
            elif len(Cate) == 4:
                if Cate[3] == temp[3]:
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[3] != temp[3]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                
        elif Cate == temp:
            SubCatStore.append(info)
        
    if SubCatStore:
        CategoryData.append(SubCatStore)
        SubCatStore = []
        SubCatStore.append(info)
        temp = Cate
        
    count = 0       
#Create file
    BeerCat = open(filename,"w")
    for T in CategoryData:
        if T[0][0].isdigit():
            BeerCat.write("Category: "+ T[0][0]+"\n")
            
        elif len(T[0][0]) == 2:
            if T[0][0][0].isdigit():
                BeerCat.write("Category: "+ T[0][0][0]+"\n")
            else:
                BeerCat.write("Category: "+ T[0][0]+"\n")
            
        elif len(T[0][0]) == 3:
            BeerCat.write("Category: "+ T[0][0][0:2]+"\n")
            
        else:
            BeerCat.write("Category: "+ T[0][0]+"\n")
            
        #BeerCat.write("Category: "+ T[0][0]+"\n")
        #print("Category: ", T[0][0])
        for t in T:
            for s in t:
                BeerCat.write(s + "  ")
                #print(s, end=" ")
            BeerCat.write("\n")
            #print()
            count += 1
        BeerCat.write("\n")    
        #print()
    BeerCat.close()
    #print("There are: ", count, " entries")
    
def GenerateCSVBeercategories(Beerinfo,filename):
#Create list of Category IDs
    CategoryIDs = []
    CategoryData = []
    SubCatStore = []
    temp = ""

#Divide data into a list of lists based on category
    for info in Beerinfo:
        Cate = GetCategoryNumber(info)
        if temp == "":
            temp = Cate
            SubCatStore.append(info)
        elif Cate != temp:
            if len(Cate) != len(temp):
                CategoryData.append(SubCatStore)
                SubCatStore = []
                SubCatStore.append(info)
                temp = Cate 
            
            elif len(Cate) == 2:
                if Cate[0].isdigit() and Cate[1].isalpha():
                    if Cate[0] == temp[0]:
                        SubCatStore.append(info)
                        temp = Cate
                    if Cate[0] != temp[0]:
                        CategoryData.append(SubCatStore)
                        SubCatStore = []
                        SubCatStore.append(info)
                        temp = Cate
                if Cate[0].isalpha() and Cate[1].isdigit():
                    if Cate[0] != temp[0]:
                        SubCatStore.append(info)
                        temp = Cate
                    if Cate[0] == temp[0]:
                        CategoryData.append(SubCatStore)
                        SubCatStore = []
                        SubCatStore.append(info)
                        temp = Cate               
                if Cate.isdigit():
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
               

            elif len(Cate) == 3:
                if Cate[0] == temp[0] and Cate[1] == temp[1]:
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[0] == temp[0] and Cate[1] != temp[1]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[0] != temp[0] and Cate[1] != temp[1]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                
            elif len(Cate) == 4:
                if Cate[3] == temp[3]:
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[3] != temp[3]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                
        elif Cate == temp:
            SubCatStore.append(info)
        
    if SubCatStore:
        CategoryData.append(SubCatStore)
        SubCatStore = []
        SubCatStore.append(info)
        temp = Cate
        
    count = 0       
#Create file
    BeerCat = open(filename,"w")
    for T in CategoryData:
        if T[0][0].isdigit():
            BeerCat.write("Category: "+ T[0][0]+"\n")
            
        elif len(T[0][0]) == 2:
            if T[0][0][0].isdigit():
                BeerCat.write("Category: "+ T[0][0][0]+"\n")
            else:
                BeerCat.write("Category: "+ T[0][0]+"\n")
            
        elif len(T[0][0]) == 3:
            BeerCat.write("Category: "+ T[0][0][0:2]+"\n")
            
        else:
            BeerCat.write("Category: "+ T[0][0]+"\n")
            
        #BeerCat.write("Category: "+ T[0][0]+"\n")
        #print("Category: ", T[0][0])
        for t in T:
            for s in t:
                BeerCat.write(s + ",")
                #print(s, end=" ")
            BeerCat.write("\n")
            #print()
            count += 1
        BeerCat.write("\n\n\n")    
        #print()
    BeerCat.close()
    
def GenerateTXTBeerEntries(Beerinfo,filename):
#Create list of Category IDs
    #CategoryIDs = []
    CategoryData = []
    SubCatStore = []
    temp = ""

#Divide data into a list of lists based on category
    count = 0
    for info in Beerinfo:
        Cate = GetCategoryNumber(info)
        if temp == "":
            temp = Cate
            SubCatStore.append(info)
        elif Cate != temp:
            if len(Cate) != len(temp):
                CategoryData.append(SubCatStore)
                SubCatStore = []
                SubCatStore.append(info)
                temp = Cate 
            
            elif len(Cate) == 2:
                if Cate[0].isdigit() and Cate[1].isalpha():
                    if Cate[0] == temp[0]:
                        SubCatStore.append(info)
                        temp = Cate
                    if Cate[0] != temp[0]:
                        CategoryData.append(SubCatStore)
                        SubCatStore = []
                        SubCatStore.append(info)
                        temp = Cate
                if Cate[0].isalpha() and Cate[1].isdigit():
                    if Cate[0] != temp[0]:
                        SubCatStore.append(info)
                        temp = Cate
                    if Cate[0] == temp[0]:
                        CategoryData.append(SubCatStore)
                        SubCatStore = []
                        SubCatStore.append(info)
                        temp = Cate               
                if Cate.isdigit():
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
               

            elif len(Cate) == 3:
                if Cate[0] == temp[0] and Cate[1] == temp[1]:
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[0] == temp[0] and Cate[1] != temp[1]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[0] != temp[0] and Cate[1] != temp[1]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                
            elif len(Cate) == 4:
                if Cate[3] == temp[3]:
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[3] != temp[3]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                
        elif Cate == temp:
            SubCatStore.append(info)
        count += 1
        
    if SubCatStore:
        CategoryData.append(SubCatStore)
        SubCatStore = []
        SubCatStore.append(info)
        temp = Cate
        #count += 1
    
#Create file
    BeerEnt = open(filename,"w")
    BeerEnt.write("\n2021 Sweetheart's Revenge Entries Report\n\n")
    BeerEnt.write("Total Entries = "+ str(count) + '\n\n')
    BeerEnt.write("Category         Entries\n")
    #print("2021 Sweetheart's Revenge Entries Report\n")
    #print("There are: ", count, " entries\n")
    #print("Category         Entries")
    #9 spaces of distance
    count = 0
    entries = 0
    sub = 0
    for T in CategoryData:
        if T[0][0].isdigit():
            #print("Category: "+ T[0][0])
            BeerEnt.write(T[0][0])
            #print(T[0][0], end= "")
            sub = len(T[0][0])
            entries = 0
            #BeerCat.write("Category: "+ T[0][0]+"\n")
            
        elif len(T[0][0]) == 2:
            if T[0][0][0].isdigit():
                #print("Category: "+ T[0][0][0])
                BeerEnt.write(T[0][0][0])
                #print(T[0][0][0], end= "")
                sub = len(T[0][0][0])
                entries = 0
                #BeerCat.write("Category: "+ T[0][0][0]+"\n")
            else:
                #print("Category: "+ T[0][0])
                BeerEnt.write(T[0][0])
                #print(T[0][0], end= "")
                sub = len(T[0][0])
                entries = 0
                #BeerCat.write("Category: "+ T[0][0]+"\n")
            
        elif len(T[0][0]) == 3:
            #print("Category: "+ T[0][0][0:2])
            BeerEnt.write(T[0][0][0:2])
            #print(T[0][0][0:2], end= "")
            sub = len(T[0][0][0:2])
            entries = 0
            #BeerCat.write("Category: "+ T[0][0][0:2]+"\n")
            
        else:
            #print("Category: "+ T[0][0])
            BeerEnt.write(T[0][0])
            #print(T[0][0], end= "")
            sub = len(T[0][0])
            entries = 0
            #BeerCat.write("Category: "+ T[0][0]+"\n")
            
        #BeerCat.write("Category: "+ T[0][0]+"\n")
        #print("Category: ", T[0][0])
        for t in T:
            entries += 1
            #for s in t:
                #BeerCat.write(s + " ")
                #entries += 1
                #print(s, end=" ")
                #count += 1
            #BeerCat.write("\n")
            #print()
            #count += 1
        #BeerCat.write("\n")   
        BeerEnt.write(" "*(17-sub) +str(entries)+'\n')
        #print(" "*(17-sub) +str(entries))
    BeerEnt.close()
    
def GenerateCSVBeerEntries(Beerinfo,filename):
#Create list of Category IDs
    #CategoryIDs = []
    CategoryData = []
    SubCatStore = []
    temp = ""

#Divide data into a list of lists based on category
    count = 0
    for info in Beerinfo:
        Cate = GetCategoryNumber(info)
        if temp == "":
            temp = Cate
            SubCatStore.append(info)
        elif Cate != temp:
            if len(Cate) != len(temp):
                CategoryData.append(SubCatStore)
                SubCatStore = []
                SubCatStore.append(info)
                temp = Cate 
            
            elif len(Cate) == 2:
                if Cate[0].isdigit() and Cate[1].isalpha():
                    if Cate[0] == temp[0]:
                        SubCatStore.append(info)
                        temp = Cate
                    if Cate[0] != temp[0]:
                        CategoryData.append(SubCatStore)
                        SubCatStore = []
                        SubCatStore.append(info)
                        temp = Cate
                if Cate[0].isalpha() and Cate[1].isdigit():
                    if Cate[0] != temp[0]:
                        SubCatStore.append(info)
                        temp = Cate
                    if Cate[0] == temp[0]:
                        CategoryData.append(SubCatStore)
                        SubCatStore = []
                        SubCatStore.append(info)
                        temp = Cate               
                if Cate.isdigit():
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
               

            elif len(Cate) == 3:
                if Cate[0] == temp[0] and Cate[1] == temp[1]:
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[0] == temp[0] and Cate[1] != temp[1]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[0] != temp[0] and Cate[1] != temp[1]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                
            elif len(Cate) == 4:
                if Cate[3] == temp[3]:
                    SubCatStore.append(info)
                    temp = Cate
                if Cate[3] != temp[3]:
                    CategoryData.append(SubCatStore)
                    SubCatStore = []
                    SubCatStore.append(info)
                    temp = Cate
                
        elif Cate == temp:
            SubCatStore.append(info)
        count += 1
        
    if SubCatStore:
        CategoryData.append(SubCatStore)
        SubCatStore = []
        SubCatStore.append(info)
        temp = Cate
        #count += 1
    
#Create file
    BeerEnt = open(filename,"w")
    BeerEnt.write("2021 Sweetheart's Revenge Entries Report\n\n")
    BeerEnt.write("Total Entries = "+ str(count)+'\n\n')
    BeerEnt.write("Category         Entries\n")
    #print("2021 Sweetheart's Revenge Entries Report\n")
    #print("There are: ", count, " entries\n")
    #print("Category         Entries")
    #9 spaces of distance
    count = 0
    entries = 0
    sub = 0
    for T in CategoryData:
        if T[0][0].isdigit():
            #print("Category: "+ T[0][0])
            BeerEnt.write(T[0][0]+",")
            #print(T[0][0], end= "")
            sub = len(T[0][0])
            entries = 0
            #BeerCat.write("Category: "+ T[0][0]+"\n")
            
        elif len(T[0][0]) == 2:
            if T[0][0][0].isdigit():
                #print("Category: "+ T[0][0][0])
                BeerEnt.write(T[0][0][0]+",")
                #print(T[0][0][0], end= "")
                sub = len(T[0][0][0])
                entries = 0
                #BeerCat.write("Category: "+ T[0][0][0]+"\n")
            else:
                #print("Category: "+ T[0][0])
                BeerEnt.write(T[0][0]+",")
                #print(T[0][0], end= "")
                sub = len(T[0][0])
                entries = 0
                #BeerCat.write("Category: "+ T[0][0]+"\n")
            
        elif len(T[0][0]) == 3:
            #print("Category: "+ T[0][0][0:2])
            BeerEnt.write(T[0][0][0:2]+",")
            #print(T[0][0][0:2], end= "")
            sub = len(T[0][0][0:2])
            entries = 0
            #BeerCat.write("Category: "+ T[0][0][0:2]+"\n")
            
        else:
            #print("Category: "+ T[0][0])
            BeerEnt.write(T[0][0]+",")
            #print(T[0][0], end= "")
            sub = len(T[0][0])
            entries = 0
            #BeerCat.write("Category: "+ T[0][0]+"\n")
            
        #BeerCat.write("Category: "+ T[0][0]+"\n")
        #print("Category: ", T[0][0])
        for t in T:
            entries += 1
            #for s in t:
                #BeerCat.write(s + " ")
                #entries += 1
                #print(s, end=" ")
                #count += 1
            #BeerCat.write("\n")
            #print()
            #count += 1
        #BeerCat.write("\n")   
        BeerEnt.write(str(entries)+'\n')
        #print(" "*(17-sub) +str(entries))
    BeerEnt.close()

BeerFile = sys.argv[1]
# Open File
Fi = open(BeerFile,"r")
#Fi = open("SR_DougCopy.txt","r")
#Data = Fi.read()
#print(Data)
BeerIDs = []
BeerData = []
BeerCases = []
Beerinfo = []

iteration = 0
subiterator = 0


Str = Fi.read()
Str = Str.replace("\n"," ")
temp = ""
CaseTotal = 0
CaseNumber = 1
#Store Data for later Names of brewers are removed for competition
for X in Str.split():
    if temp != X:
        temp = X
        if IsBeerID(temp):
            iteration += 1
            BeerIDs.append(temp)
            if iteration == 24:
                BeerCases.append(BeerIDs)
                iteration = 0
                BeerIDs = []
                CaseTotal += 1
        else:
            if not isAllLetters(0,len(temp)-1,temp):
                subiterator += 1
                BeerData.append(temp)
                if subiterator == 3:
                    Beerinfo.append(BeerData)
                    subiterator = 0
                    BeerData = []

# makes sure cases with empty slots get stored as well                
if BeerIDs:
    while len(BeerIDs) < 24:
        BeerIDs.append("xxxx")
    BeerCases.append(BeerIDs)
    CaseTotal += 1
Fi.close()





#Storage step end 
Path = "BeerCompMaterials"
if not os.path.isdir(Path):
    os.mkdir(Path, 755 )

#Create list of Category IDs
#GenerateTXTBeercategories(Beerinfo,"BeerCategories.txt")
#GenerateTXTBeercategories(Beerinfo,"BeerCategories.csv")

GenerateTXTBeercategories(Beerinfo,Path+"/BeerCategories.txt")
GenerateTXTBeercategories(Beerinfo,Path+"/BeerCategories.csv")
  
#Generate Beer Report per case
GenerateTXTBeerReport(Beerinfo,Path+"/BeerReport.txt")
GenerateCSVBeerReport(Beerinfo,Path+"/BeerReport.csv")

#Beer Map generation in txt and csv format
#GenerateTXTBeerMap(BeerCases,Path+"/BeerMap.txt")
GenerateNTXTBeerMap(Beerinfo,Path+"/BeerMap.txt")
GenerateNCSVBeerMap(Beerinfo,Path+"/BeerMap.csv")
#GenerateCSVBeerMap(BeerCases,Path+"/BeerMap.csv")

GenerateTXTBeerEntries(Beerinfo,Path+"/BeerEntries.txt")
GenerateCSVBeerEntries(Beerinfo,Path+"/BeerEntries.csv")
   