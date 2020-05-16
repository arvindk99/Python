from pathlib import Path
import os
import glob
import shutil
import sys
import traceback


def main():
    """Takes a string input. If it's D or R, the string following the character is converted into a path object
    and then used as a parameter in their respective functions. Otherwise, ERROR is printed and the function runs again."""
    firstInput = str(input())
    if (firstInput[0:2] == "D "):
        p = Path(firstInput[2:])      
        pressD(p)
    elif(firstInput[0:2] == "R "):
        p = Path(firstInput[2:])        
        pressR(p)
    else:
        print("ERROR")
        main()
    
def pressD(p:'path'):
    """Checks if the path exists and is a directory. If so, all files and subdirectories are ordered and then printed.
    Otherwise, ERROR is printed and main() runs again."""
    listD = []
    if p.exists() and p.is_dir():
        try:
            for x in p.iterdir():
                listD.append(x)
        except:
            pass
        if not listD:
            return
        listD = lexi(listD)
        alphaprint(listD)
        second(listD)
        
    else:
        print("ERROR") 
        main()
        
def pressR(p: 'path'):
    """Checks if the path exists and is a directory.If so, the path, along with an empty list, is used as a parameter in a recursive search.
    Then, the files within thelist are ordered and then printed. Otherwise, ERROR is printed and main() runs again."""
    if p.exists() and p.is_dir():
        listR = []
        recursionTest(p, listR)
        if not listR:
            return
        listR = lexi(listR)
        alphaprint(listR)
        second(listR)
        
    else:
        print("ERROR")
        main()                   
    
def recursionTest(p:'path', listR):
    """Appends files within the directory to listR. Otherwise, subdirectories are appended to mylist. Subdirectories in mylist are recursively searched."""
    mylist = []
    try:
        for x in p.iterdir():
            if x.is_file():
                listR.append(x)
            else:
                mylist.append(x)
    except:
        pass
    for x in mylist:
        recursionTest(x, listR)
    
    
def alphaprint(printList:'list'):
    """Prints out paths in the sent list."""
    for x in printList:
        print(x)
    
def lexi(lexicoList:list) -> list:
    """Sorts the list (input) lexicographically."""
    
    for x in sorted(lexicoList, key = lambda x: (x, os.path.basename(x)),reverse=True):
        x=Path(x)
    return lexicoList 


def second(listTwo:'list'):
    """Takes the list from pressR or pressD as a parameter. Depending on the user's input, the list and the input are sent to respective functions.
    If the input does not match a requirement, error is printed and 'second' is called again."""
    secondInput = input()
    if (secondInput == "A"):
        third(listTwo)
    elif (secondInput[0:2] == "N "):
        q = secondInput[2:]
        pressN(q, listTwo)        
    elif (secondInput[0:2] == "E "):
        q = secondInput[2:]
        pressE(q, listTwo)        
    elif (secondInput[0:2] == "T "):
        q = secondInput[2:]
        pressT(q, listTwo)        
    elif (secondInput[0:2] == "< "):
              
        try:
            q = int(secondInput[2:])  
            pressLessThan(q, listTwo)
        except:
            print("ERROR")
            second(listTwo)
                  
    elif (secondInput[0:2] == "> "):
        try:
            q = int(secondInput[2:])  
            pressMoreThan(q, listTwo)
            
        except:
            print("ERROR")
            second(listTwo)
    else:
        print("ERROR")
        second(listTwo)

def pressA(fileName:"string name of a file", listTwo: "list"):
    for x in listTwo:
        aList.append(x)
        print(x)
    if not aList:
        return
    else:
        third(aList)        
            
def pressN(fileName:"string name of a file", listTwo: "list"):
    """"Searches for a file with the same name as the input through the organized list. Interesting files are sent to thirdInput through a list."""
    nList=[]
    for x in listTwo:
        if x.name == fileName:
            print(x)
            nList.append(x)
    if not nList:
        return
    else:
        third(nList)
    
def pressE(q: 'int', listTwo:'list'):
    """Searches for files with the user's preferred extension. Sends interesting files to third through a list, if any."""
    eList = []
    if q[0:1]!=".":
        q = "."+q
    for x in listTwo:
        if x.suffix==(q):
            print(x)
            eList.append(x)
    if not eList:
        return
    else:
        third(eList)
            
def pressT(q: 'string', listTwo:'list'):
    """Searches for files that contains the user's string input. Sends interesting files to third through a list, if any."""
    tList=[]
    for x in listTwo:
        try:
            f = x.open('r')
            va = f.read()
            #print(x)
            if q in va:
                print(x)
                tList.append(x)
        except:
            print("NOT TEXT")                
        finally:
            f.close()
    if not tList:
        return
    else:
        third(tList)
            
def pressLessThan(q: 'int', listTwo: 'list'):
    """Iterates through the list and adds files lesser in size than the input to lessList. Interesting files are sent to third, if any."""
    lessList=[]
    for x in listTwo:
        if os.path.getsize(x) < q:
            print(x)
            lessList.append(x)
    if not lessList:
        return
    else:
        third(lessList)
def pressMoreThan(q: 'int', listTwo: 'list'):
    """Iterates through the list and adds files greater in size than the input to lessList. Interesting files are sent to third, if any."""
    moreList=[]
    for x in listTwo:
        if os.path.getsize(x) > q:
            print (x)
            moreList.append(x)
    if not moreList:
        return
    else:
        third(moreList)

def third(r: 'interesting lists'):
    """Takes list r as an input. Depending on the input, the function will either print the first line of the file, duplicate the file, or
    change the 'time modified' part of the file."""
    thirdInput = str(input())        
    if (thirdInput == "F"):
        for x in r:
            try:
                f=x.open('r') 
                va = f.readline().strip()
                print(va)
            except:
                print("NOT TEXT")  
            finally:
                f.close()
        return
            
    elif(thirdInput == "D"):
        
        for filename in r:
            shutil.copyfile(str(filename),str(filename) + '.dup')
        sys.exit()
        
    elif (thirdInput == "T"):
        for filename in r:
            os.utime(filename)
        return
    else:
        print ("ERROR")
        third(r)
    return

if __name__ == '__main__': main()
