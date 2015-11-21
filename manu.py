global namephone
global flag
import numpy
namephone=numpy.array([['                 ']*6]*10)
namephone[0][0]='Tossapon'
namephone[1][0]='Poowanai'
namephone[2][0]='Norasath'
namephone[0][1]='0811323545'
namephone[1][1]='0835411234'
namephone[1][2]='0823354121'
namephone[2][1]='0850550354'
flag=0
def createuser():

    return
def run():
    x=raw_input('Phonebook - Input your command (h for help):')
    function(x)
def insert():
    insert=raw_input('Enter a phone number to be inserted:')
    i=len(insert)
    #print i
    if (i==10):
        showlist()
        insertphonetoolduser(insert)
        if flag==1:
            run()
            print 'insert suscess'
        else:
            print 'Cant insert Phonenumber'
    elif(i>10):
        print 'Error - the number is too long'
        insert=0
        run()
    elif(i<10):
        print 'Error - the number is too short'
        insert=0
        run()      
    return

def search(digi=0):
    return phone
def allfunc():
    print 'i - insert a phone number'
    print 'd - delete a phone number'
    print 'm - modify a phone number'
    print 's - Search'
    print 'x - exit program'
def function(func):
    if(func=='i'):
        insert()
    elif(func=='d'):
        print 'delete a phone number'
    elif(func=='m'):
        print 'modify a phone number'
    elif(func=='s'):
        print 'Search'
    elif(func=='h'):
        allfunc()
        x=''
        run()
    elif(func=='x'):
        print 'exit program'
    else:
        x=''
        run()
    return 
def insertphonetoolduser(insert):
    return
def showlist():
    j=1
    for j in range(1,6):
        if namephone[0][j] == '                 ':
            j=1
            break
        if j==1:
            print '[%d]'%j,namephone[0][j-1],j,'-',namephone[0][j]
        else:
            print '            ',j,namephone[0][j]
    for j in range(1,6):
        if namephone[1][j] == '                 ':
            j=1
            break
        if j==1:
            print '[%d]'%2,namephone[1][j-1],j,'-',namephone[1][j]
        else:
            print '            ',j,'-',namephone[1][j]
    for j in range(1,6):
        if namephone[2][j] == '                 ':
            j=1
            break
        if j==1:
            print '[%d]'%3,namephone[2][j-1],j,'-',namephone[2][j]
        else:
            print '            ',j,'-',namephone[2][j]
    flag=1
    return flag
run()
