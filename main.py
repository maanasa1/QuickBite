from cProfile import label
from cgitb import text
import imp
from optparse import Values
from re import sub
from threading import local
from tkinter import N
from urllib import request
import mysql.connector
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivymd.uix.screen import Screen


import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

# Replace this with your 
# current version
kivy.require('2.1.0')


# mysql connection 
'''
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345"
  database = "qb"
)

'''



#c.execute("create table try(test int) ")
#data = c.fetchone()
#print(data)




class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass



'''class MyRecordWidget(BoxLayout):
  def __init__(self, row, **kwargs):
    super(MyRecordWidget, self).__init__(**kwargs)

    for i in row:
        rname = str(i[0])
        local = str(i[2])
        location = str(i[1])

        submit = "Submit"
            #box +=1
            

            
        #submit = "Submit"
        #self.rname = rname
        #self.local = local
        #self.location = location
        #self.submit = submit
        #i.add_widget(rows)
        self.add_widget(Label(text=rname))
        self.add_widget(Label(text=local))
        self.add_widget(Label(text=location))
        self.add_widget(Label(text=submit))'''
        




class MainApp(MDApp):

    #db_connection = mysql.connector.connect(host="localhost", database="cuickbite", user="root", password="12345")
    
    db_connection = mysql.connector.connect(host="localhost", database="quickbite", user="root", password="12345")
    
    
        #create a cursor
    cursor = db_connection.cursor()


    

    '''
    def __init__(self):


        #super(MDApp, self).__init__(**kwargs)

        db_connection = mysql.connector.connect(host="localhost", database="quickbite", user="root", password="12345")
    
    
        #create a cursor
        self.cursor = db_connection.cursor()
        self.build()

    '''

    def build(self):

        self.cursor.execute("select * from request")
        #cursor.execute()
        rows = self.cursor.fetchall()
        self.db_connection.commit()
        print(rows)



        username = str(list[0])
        print(username)
        
        self.cursor.execute("select userid, firstName from userinfo where firstName = '.*%s.*'" %username,)
        user = self.cursor.fetchall()
        self.db_connection.commit()
        

        '''layout = BoxLayout(orientation='vertical')
        for r in rows:
            widget = MyRecordWidget(r)
            layout.add_widget(widget)
            return layout'''
        
        rname = str(rows[0][0])
        local = str(rows[0][2])
        location = str(rows[0][1])

        submit = "Submit"
            #box +=1
            

            #x = label( text= rname, text = local, text = location, text = submit)
        submit = "Submit"
        self.rname = rname
        self.local = local
        self.location = location
        self.submit = submit
            ########
        
        
            
        rname2 = str(rows[1][0])
        local2 = str(rows[1][2])
        location2 = str(rows[1][1])
        submit2 = "Submit"
            #box +=1
            

            #x = label( text= rname, text = local, text = location, text = submit)
        
        self.rname2 = rname2
        self.local2 = local2
        self.location2 = location2
        self.submit2 = submit2

        
        
            
        rname3 = str(rows[2][0])
        local3 = str(rows[2][2])
        location3 = str(rows[2][1])
        submit3 = "Submit"
            

            #x = label( text= rname, text = local, text = location, text = submit)
        
        self.rname3 = rname3
        self.local3 = local3
        self.location3 = location3
        self.submit3 = submit3



        self.cursor.execute("select * from resturent")
        rows = self.cursor.fetchall()

        resName1 = str(rows[1][5])
        self.resName1 = resName1

        resName2 = str(rows[2][5])
        self.resName2 = resName2

        resName3 = str(rows[3][5])
        self.resName3 = resName3

        resName4 = str(rows[4][5])
        self.resName4 = resName4

        resName5 = str(rows[0][5])
        self.resName5 = resName5



        self.cursor.execute("select * from menue where rid = 1")
        rows = self.cursor.fetchone()

        '''item1 = str(rows[0][1])
        self.item1 = item1

        item2= str(rows[0][3])
        self.item2 = item2

        item3= str(rows[0][5])
        self.item3= item3'''

        item1 = str(rows[1])
        self.item1 = item1

        item2= str(rows[3])
        self.item2 = item2

        item3= str(rows[5])
        self.item3= item3

        item4= str(rows[7])
        self.item4= item4

        item5= str(rows[8])
        self.item5= item5

    # price
        price1 = str(rows[2])
        self.price1 = price1

        price2 = str(rows[4])
        self.price2 = price2

        price3= str(rows[6])
        self.price3= price3

        price4= str(rows[9])
        self.price4= price4

        price5= str(rows[10])
        self.price5= price5

    #quentity
        quentity1 = str(rows[11])
        self.quentity1 = quentity1

        quentity2 = str(rows[12])
        self.quentity2 = quentity2

        quentity3= str(rows[13])
        self.quentity3= quentity3

        quentity4= str(rows[14])
        self.quentity4= quentity4

        quentity5= str(rows[15])
        self.quentity5= quentity5

        
        

        





            

            
            

        
        

        #username = list[0]
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('page01.kv')
    
    def layout(self, rname, local, location, submit):
        submit = "Submit"
        self.rname = rname
        self.local = local
        self.location = location
        self.submit = submit



    def getName(self, name):
        
        
       
        self.cursor.execute(f"INSERT INTO userinfo (firstName) VALUES ('{name.text}')")

        
        

        self.db_connection.commit()


        self.root.current = 'second'
        
    
    def submitRequest(self, rname, local, location):

        self.cursor.execute("select username, total from request where rname = '.*%s.*' and location = '.*%s.*' " % rname % location)
        self.cursor.execute("select username, total from request where rname = (%s) and location = (%s) " % (rname, location) )
        #self.cursor.execute("select username, total from request where rname = '.*%s.*'" % rname )
        cursor.execute()
        #rows = self.cursor.fetchall()
        #self.db_connection.commit()





        self.cursor.execute(f"INSERT INTO matchtable (rname, location ) VALUES ('{rname.text}', '{location.text}' )")
        #self.cursor.execute(f"INSERT INTO matches (rname) VALUES ('{rname.text}')")
        

        self.db_connection.commit()
        self.root.current = 'third'

        

    def newrequest(self):

        




        self.root.current = "fifth"

    def menue(self, res):
        

        

        self.root.current = "fourth"


        return

    def additem1(self,item, price ):

        self.cursor.execute("select *  from menue where ch1 = '.*%s.*'" % (item))
        #self.cursor.execute("select *  from menue where ch1 = '.*%s.*' or ch2 = '.*%s.*' ch3 = '.*%s.*' or ch4 = '.*%s.*' or ch5 = '.*%s.*' " % (item, item, item, item, item)

        row = self.cursor.fetchall()
        self.db_connection.commit()
        print(row)

        




        for i in row:

            q = i[11] 
            new_q = q + 1
            self.quentity1 = new_q
        self.cursor.execute(f"INSERT INTO menue (q1) VALUES (%s )", new_q)

    
    def additem2(self,item, price ):

        self.cursor.execute("select *  from menue where ch3 = '.*%s.*'" % (item))
        #self.cursor.execute("select *  from menue where ch1 = '.*%s.*' or ch2 = '.*%s.*' ch3 = '.*%s.*' or ch4 = '.*%s.*' or ch5 = '.*%s.*' " % (item, item, item, item, item)

        row = self.cursor.fetchall()
        self.db_connection.commit()
        print(row)

        for i in row:

            q = i[12] 
            new_q = q + 1
            self.quentity2 = new_q
        self.cursor.execute(f"INSERT INTO menue (q2) VALUES (%s )", new_q)
    
    def additem3(self,item, price ):

        self.cursor.execute("select *  from menue where ch3 = '.*%s.*'" % (item))
        #self.cursor.execute("select *  from menue where ch1 = '.*%s.*' or ch2 = '.*%s.*' ch3 = '.*%s.*' or ch4 = '.*%s.*' or ch5 = '.*%s.*' " % (item, item, item, item, item)

        row = self.cursor.fetchall()
        self.db_connection.commit()
        print(row)

        for i in row:

            q = i[13] 
            new_q = q + 1
            self.quentity3 = new_q
        self.cursor.execute(f"INSERT INTO menue (q3) VALUES (%s )", new_q)


    def additem4(self,item, price ):

        self.cursor.execute("select *  from menue where ch4 = '.*%s.*'" % (item))
        #self.cursor.execute("select *  from menue where ch1 = '.*%s.*' or ch2 = '.*%s.*' ch3 = '.*%s.*' or ch4 = '.*%s.*' or ch5 = '.*%s.*' " % (item, item, item, item, item)

        row = self.cursor.fetchall()
        self.db_connection.commit()

        print(row)

        for i in row:

            q = i[14] 
            new_q = q + 1
            self.quentity5 = new_q

        self.cursor.execute(f"INSERT INTO menue (q4) VALUES (%s )", new_q)


    def additem5(self,item, price ):

        self.cursor.execute("select *  from menue where ch5 = '.*%s.*'" % (item))
        #self.cursor.execute("select *  from menue where ch1 = '.*%s.*' or ch2 = '.*%s.*' ch3 = '.*%s.*' or ch4 = '.*%s.*' or ch5 = '.*%s.*' " % (item, item, item, item, item)

        row = self.cursor.fetchall()
        self.db_connection.commit()

        print(row)
        for i in row:

            q = i[14] 
            new_q = q + 1
            self.quentity5 = new_q
        self.cursor.execute(f"INSERT INTO menue (q5) VALUES (%s )", new_q)

        


        






        

    def logger(self):
        self.root.current = 'second'
        
        #self.root.manager.transition.direction = "left"


MainApp().run()