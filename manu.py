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
        flag=showlist()
        insertphonetoolduser(insert)
        if flag==1:
            x=raw_input('Enter the person id to append the phone number or n for new person:')
            y=raw_input('Enter replaced number or n for new phone number :')
            addphonenumber(x,y,insert)
            print 'insert suscess'
            run()
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
def addphonenumber(x,y,insert):
#    if x=='1':
#        for i in range(1,6):
#            if namephone[0][]
#                namephone[0][j]
#    elif x=='2':

#    elif x=='3':

#    elif x=='4':

#    elif x=='5':
#    showlist()
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
    for k in range(0,10):
        for j in range(1,6):
            if namephone[k][j] == '                 ':
                j=1
                break
            if j==1:
                l=k+1
                print '[%d]'%l,namephone[k][j-1],j,'-',namephone[k][j]
            else:
                print '            ',j,'-',namephone[k][j]
        j=1
        if namephone[k][j]=='                 ':
            break
    flag=1
    return flag
run()
