import sqlite3

def intro():
    print("\n\n\n\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")
intro()

try:
    con = sqlite3.connect('Banking.sqlite3')
    cur = con.cursor()
    ls = []
    depst=[]
    new_account=[]
    d=[]
    
    #cur.execute("create table Bank (Acno int, Name text, Balance int)")   
    while True:
        ch = int(input("\n\nEnter operation to perform :\n\n1) DEPOSIT \n\n2) WITHDRAWL \n\n3) ADD ACCOUNT \n\n4) DELETE ACCOUNT \n\n5) SHOW_DETAILS\n\n6) UPDATE DETAILS \n\n7) Quit\n\nYour Choice :-> "))
                         
        if ch==1:
            ac  = int(input("Enter your account number     :--> "))
            ls.append(ac)
            dep = int(input("Enter the amount to deposit   :--> "))
            cur.execute('select Balance from Bank where Acno = (?)',ls)
            bl = cur.fetchone()
            dep= bl[0] + dep     
            depst.append(dep)
            depst.append(ac)
            cur.execute('Update Bank set Balance = (?) where Acno = (?)',depst)
            print("\nDeposit Completed\n")
            ls.pop()
            depst.pop()
            con.commit()
    
    
        elif ch==2:
            ac  = int(input("Enter your account number     :--> "))
            ls.append(ac)
            wid = int(input("Enter the amount to withdraw  :--> "))
            cur.execute('select Balance from Bank where Acno = (?)',ls)
            bal = cur.fetchone()
            old_balance = []
            old_balance.append(bal[0]) 
            if old_balance[0]<wid:
                print("Insufficient amount")
                
    
            else:
                new_bal=old_balance[0]-wid
                old_balance.pop()
                old_balance.append(new_bal)
                old_balance.append(ac)
                cur.execute('Update Bank set Balance = (?) where Acno =(?) ',old_balance)
                print("\nWithdrawl Completed \n")
            del ls[0:] 
            del old_balance[0:]  
            con.commit()
            con.close()
            
        elif ch==3:
          print("Enter -> Acno , Name, Intial Balance\n")
          for i in range(0,3):
              x = input("Enter value:-> ")
              new_account.append(x)
          cur.execute('insert into Bank values (?,?,?)',new_account)
          con.commit()
          del new_account[0:]

        
        elif ch==4:
            dl = input("Enter account number to delete :-> ")
            d.append(dl)
            cur.execute('DELETE from Bank where Acno = (?)',d)
            del d[0:]
            con.commit()

        elif ch==5:
            choice = input("Press 'A' for all customer details or enter particular Name of Person :-> ")
            na=[]
            na.append(choice)
            if choice== 'A':
             with con:
              cur.execute('SELECT * FROM Bank')
              rows = cur.fetchall()
              print("Total records",len(rows))
              for row in rows:
                  print("\n",row)
            else:
                cur.execute('SELECT * FROM Bank where Name =(?)',na)
                rows = cur.fetchall()
                for row in rows:
                  print("\n",row)

        elif ch==6:
            ac = input("Enter Account Number to do updation:-> ")
            nm = input("\nEnter new Name:-> ")
            ls = []
            ls.append(nm)
            ls.append(ac)
            cur.execute('UPDATE Bank set Name=(?) where Acno=(?)',ls)
            con.commit()
        
        
        
        elif ch==7:
            print("Quit")
            con.commit()
            con.close()
            break
    
    else:
        print("Invalid input")
    
except Exception as err:
    print(err)