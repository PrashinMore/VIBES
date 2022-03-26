import os
import subprocess
import csv
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import re
import sqlite3 as sq
'''Creating Database'''
eventsCheck={}
eventVariable={}
con=sq.connect("VIBES_DATABASE.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Students_database9(fName varchar(16),lName varchar(16),STD varchar(6),Email_ID text ,College_Name text ,Mobile_No num,Gender varchar(8),Totalammo num)")
con.commit()
cur.execute("CREATE TABLE IF NOT EXISTS New_Events_list9(EventName char(20), Fee int(3), Participants int(2), deleted int(1))")
cur.execute('select * from New_Events_list9')
eventslist = cur.fetchall()
con.commit()
'''##############################################'''

def outside_program():
    
    def pokemon():
        pikachu=Tk()
        pikachu.attributes("-fullscreen",True)
        pikachu.config(bg="black")
        pikachu.title('Vibes')
        raichu=Label(pikachu,text="Vibes Registration",font=("Times",30,"bold"),bg="blue",fg="yellow")
        raichu.pack(side=TOP,fill=X)
        
        
        def reg_button_1():

            '''Button 1 Functions The following Program '''
            

            reg_button.place_forget()
            About_Vibes_button.place_forget()
            Vibes_Events.place_forget()
            Vibes_Events_All_Info_button.place_forget()
            Admin_Login_button.place_forget()
            Remove_label_button.place_forget()
            Edit_label_button.place_forget()
            Exit_button.place_forget()
            Admin_label.place_forget()
            Edit_label.place_forget()
            Exit_label.place_forget()
            Vibes_label.place_forget()
            reg_label.place_forget()
            eventall_label.place_forget()
            About_label.place_forget()
            Remove_label.place_forget()
            
            def pokeball():
                ''''''
                
                ''''''

                '''CHECKING FNAME DATA '''
                fnames=megapikachu0.get()
                fnames=fnames.upper()
                if len(fnames)>15 or len(fnames)<2:
                     showinfo("RECHECK", "Invalid \nFirst name should be more than 2 characters and less than 15 characters")
                    
                    

                elif fnames.isalpha()==False:
                    showerror("RECHECK","Invalid \nFirst Name Should Not Be In Integers or contain space")
                    
                
                else:
                    '''CHECKING LNAME DATA '''
                    lnames=megapikachu20.get()
                    lnames=lnames.upper()
                    if len(lnames)>15 or len(lnames)<2:
                         showinfo("RECHECK","Invalid \nLast Name Should Be more than 2 characters and less than 15 characters")
                        
                        

                    elif lnames.isalpha()==False:
                        showerror("RECHECK","Invalid \nLast Name Should Not Be In Integers or contain space")
                    

                    else:
                        '''CHECKING STANDARD DATA '''
                        std=megapikachu30.get()
                        std=std.upper()
                        if len(std)>8 :
                             showinfo("RECHECK","Invalid \nStandard Should Be less than 15 characters or contain space")

                        else:
                            '''CHECKING EMAIL-ID DATA '''
                            deadspy_email=megapikachu40.get()
                            if len(deadspy_email)>30 or len(deadspy_email)<6:
                                    showerror("RECHECK","Error \nEmail  Should Be more than 4 characters and less than 15 characters")
                                    
                               
                            else:
                                gmail=bool(re.search(".com$",deadspy_email))
                                
                                if '@'  not in deadspy_email:
                                    ''''''
                                    showinfo("RECHECK","Invalid \nEnter Your Valid Email Address")
                                elif gmail == False:
                                    showinfo("RECHECK","Invalid \nEnter Your Valid Email Address")
                                    
                                else:
                                    '''CHECKING COLLEGE DATA'''
                                    
                                    CLG=megapikachu50.get()
                                    CLG=CLG.upper()
                                    if len(CLG)>25 or len(CLG)<2:
                                         showinfo("RECHECK", "Invalid \nCollege Name Should Be more than 5 characters and less than 25 characters")
                                        
                                        

                                    elif CLG.isdigit()==True:
                                        showerror("RECHECK","Invalid \nCollege Name Should Not Be In Integers")
                                    else:
                                        '''CHECKING MOBILE DATA'''
                                        oneplus=megapikachu60.get()
                                        v=cur.execute('select * from Students_database9')
                                        vo=str(cur.fetchall())
                                        
                                        if  len(oneplus)<10:
                                            showerror("RECHECK","Invalid \nMobile Number Should Not Be Less Than 10 Integers")
                                        elif len(oneplus)>10:
                                            showerror("RECHECK","Invalid \nMobile Number Should Not Be More Than 10 Integers")
                                        elif oneplus in vo:
                                            showinfo("RECHECK", "Invalid \nThis Mobile No Is Registered\nPlease Go To\Admin Login To add participation")
                                        elif oneplus.isdigit()==False:
                                            showerror("RECHECK","Invalid \nMobile Number Should Not Be In Characters")
                                        else:
                                            '''Check Gender'''
                                            MF=__MOF__.get()
                                            if MF == "Male" or MF == "Female" :
                                                '''CHECK the CHECK-buttons'''
                                                arceus.configure(state=DISABLED)
                                                columns=""    
                                                for idx, event in enumerate(eventslist):
                                                    # if event[3] != 1:
                                                    columns+=",\"\""
                                                cur.execute(f'Insert Into Students_database9 values("{fnames}","{lnames}","{std}","{deadspy_email}","{CLG}","{oneplus}","{MF}",""{columns})')
                                                
                                                con.commit()

                                                
                                                
                                                    
                                                TotalSum=[]

                                                def BC():
                                                
                                                  
                                                    
                                                    for idx,event in enumerate(eventslist):
                                                        if event[3] == 1:
                                                            continue
                                                        brock=eventVariable[idx].get()  

                                                        if brock == 1:
                                                            ''''''
                                                            
                                                            cur.execute(f'Update Students_database9 set {event[0]} = "yes"  where Mobile_No="{oneplus}"  ')
                                                            
                                                            print(event)
                                                            TotalSum.append(event[1])

                                                            

                                                        else:
                                                            cur.execute(f'Update Students_database9 set {event[0]} = "no"  where Mobile_No="{oneplus}"  ')
                                                        
                                                        # RF()
                                                        # BD()
                                                        # CRS()
                                                        # CRD()
                                                        # TT()
                                                        # CSS()
                                                        # CT5()
                                                        # CT3()
                                                        # PGS()
                                                        # PGD()
                                                        # PGT()
                                                        # PGST()
                                                        # DCS()
                                                        # DSD()
                                                        # DSG()
                                                        # SG()
                                                        # FF()
                                                        # RP()
                                                        # BTBX()
                                                        # PGY()
                                                        # MDI()
                                                        # Elist()
                                                        
                                                        bj=sum(TotalSum)
                                                        cur.execute(f'Update Students_database9 set Totalammo = "{bj}"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        dialga="Total Amount = RS."+str(bj)
                                                        print("total amount 2")
                                                        MEGA_ARCEUS=Label(pikachu,text=dialga,width=30,bg='blue',fg='yellow',font=("Times",50,"bold"))
                                                        MEGA_ARCEUS.place(x=0,y=360)

                                                        ''''''
                                                        def hommming11():
                                                            ''''''
                                                            reg_button.configure(state=NORMAL)
                                                            RB1.place_forget()
                                                            RB2.place_forget()
                                                            zapados.place_forget()
                                                            
                                                            
                                                            Exit_button.place(x=690,y=530)
                                                            Admin_Login_button.place(x=480,y=530)
                                                            Remove_label_button.place(x=880,y=310)
                                                            Edit_label_button.place(x=890,y=530)

                                                            Vibes_Events_All_Info_button.place(x=690,y=310)
                                                            Vibes_Events.place(x=480,y=310)
                                                            About_Vibes_button.place(x=690,y=90)
                                                            reg_button.place(x=480,y=90)

                                                            ''''''
                                                            Admin_label.place(x=494,y=690)
                                                            Remove_label.place(x=880,y=470)
                                                            Edit_label.place(x=890,y=530)
                                                            Exit_label.place(x=756,y=690)
                                                            Vibes_label.place(x=507,y=470)
                                                            eventall_label.place(x=720,y=470)
                                                            reg_label.place(x=515,y=250)
                                                            About_label.place(x=706,y=250)


                                                            ''''''
                                                            MEGA_ARCEUS.place_forget()
                                                            moltress.place_forget()
                                                            moltresssssssp.place_forget()
                                                            pikachu.mainloop()
                                                            

                                                        ash000000=os.getcwd()
                                                        ookoooooo=ash000000+"//home.png"
                                                        
                                                        photo2222222 = PhotoImage(file=ookoooooo)
                                                        moltresssssssp = Button(pikachu,cursor='hand2',command=hommming11,bd=0,bg="black",activeforeground="orange",activebackground='black',image=photo2222222 ,width=73,height=65,highlightthickness=0)
                                                        moltresssssssp.place(x=1289,y=62)
                                                        ''''''
                                                        ll1.place_forget()
                                                        # pl9.place_forget()
                                                        # pl8.place_forget()
                                                        # pl7.place_forget()
                                                        # pl4.place_forget()

                                                        ''''''
                                                        mega.place_forget()
                                                        megapikachu.place_forget()
                                                        mega2.place_forget()
                                                        megapikachu2.place_forget()
                                                        mega3.place_forget()
                                                        megapikachu3.place_forget()
                                                        mega4.place_forget()
                                                        megapikachu4.place_forget()
                                                        mega5.place_forget()
                                                        megapikachu5.place_forget()
                                                        mega6.place_forget()
                                                        megapikachu6.place_forget()
                                                        mega7.place_forget()
                                                        
                                                        arceus.place_forget()
                                                        # p01.place_forget()
                                                        # p02.place_forget()
                                                        # p03.place_forget()
                                                        # p04.place_forget()
                                                        # p044.place_forget()
                                                        # p05.place_forget()
                                                        # p06.place_forget()
                                                        # p07.place_forget()
                                                        # p077.place_forget()
                                                        # p08.place_forget()
                                                        # p088.place_forget()
                                                        # p0888.place_forget()
                                                        # p08888.place_forget()
                                                        # p09.place_forget()
                                                        # p099.place_forget()
                                                        # p0999.place_forget()
                                                        # p010.place_forget()
                                                        # p011.place_forget()
                                                        # p012.place_forget() 
                                                        # p013.place_forget()
                                                        # p014.place_forget()
                                                        # p015.place_forget()
                                                        for idx, event in enumerate(eventslist):
                                                            if event[3] == 1:
                                                                continue        
                                                            eventsCheck[idx].place_forget()
                                                        
            

                                                        
                                                        
                                                        
                                                        def backbtn000():
                                                            MEGA_ARCEUS.place_forget()
                                                            reg_button.configure(state=NORMAL)
                                                            megapikachu0.set('')
                                                            megapikachu20.set('')
                                                            megapikachu30.set('')
                                                            megapikachu40.set('')
                                                            megapikachu50.set('')
                                                            megapikachu60.set('')
                                                            __MOF__.set('')
                                                            p1.set(0)
                                                            p2.set(0)
                                                            p3.set(0)
                                                            p4.set(0)
                                                            p5.set(0)
                                                            p6.set(0)
                                                            p7.set(0)
                                                            p8.set(0)
                                                            p9.set(0)
                                                            p10.set(0)
                                                            p11.set(0)
                                                            p12.set(0)
                                                            p13.set(0)
                                                            p14.set(0)
                                                            p15.set(0)
                                                            p44.set(0)
                                                            p77.set(0)
                                                            p88.set(0)
                                                            p888.set(0)
                                                            p8888.set(0)
                                                            p99.set(0)
                                                            p999.set(0)
                                                            RB1.place(y=391,x=225)
                                                            RB2.place(y=391,x=300)
                                                            ''''''
                                                            moltresssssssp.place_forget()

                                                            ''''''
                                                            ll1.place(x = 800, y = 115) 
                                                            # pl9.place(x = 820, y = 310)
                                                            # pl8.place(x = 820, y = 290)
                                                            # pl7.place(x = 820, y = 270)
                                                            # pl4.place(x = 820, y = 210)
                                                            
                                                            ''''''
                                                            arceus.place(x=600,y=640)
                                                            mega.place(x=110,y=150)
                                                            megapikachu.place(x=240,y=151)
                                                            mega2.place(x=450,y=150)
                                                            megapikachu2.place(x=580,y=151)
                                                            mega3.place(x=110,y=230)
                                                            megapikachu3.place(x=240,y=231)
                                                            mega4.place(x=450,y=230)
                                                            megapikachu4.place(x=580,y=231)
                                                            mega5.place(x=110,y=310)
                                                            megapikachu5.place(x=240,y=311)
                                                            mega6.place(x=450,y=310)
                                                            megapikachu6.place(x=580,y=311)
                                                            mega7.place(x=110,y=390)
                                                            ''''''
                                                            MEGA_ARCEUS.place_forget()
                                                            ''''''
                                                            # p01.place(x = 800, y = 150)
                                                            # p02.place(x = 800, y = 170)
                                                            # p03.place(x = 800, y = 190)
                                                            # p04.place(x = 960, y = 210)
                                                            # p044.place(x = 1020, y = 210)
                                                            # p05.place(x = 800, y = 230)
                                                            # p06.place(x = 800, y = 250)
                                                            # p07.place(x = 960, y = 270)
                                                            # p077.place(x = 1020, y = 270)
                                                            # p08.place(x = 960, y = 290)
                                                            # p088.place(x = 1020, y = 290)
                                                            # p0888.place(x = 1100, y = 290)
                                                            # p08888.place(x = 1170, y = 290) 
                                                            # p09.place(x = 960, y = 310) 
                                                            # p099.place(x = 1020, y = 310) 
                                                            # p0999.place(x = 1100, y = 310)
                                                            # p010.place(x = 800, y = 330)
                                                            # p011.place(x = 800, y = 350)
                                                            # p012.place(x = 800, y = 370) 
                                                            # p013.place(x = 800, y = 390)
                                                            # p014.place(x = 800, y = 410) 
                                                            # p015.place(x = 800, y = 430)

                                                            moltress.place_forget()
                                                            pikachu.mainloop()
                                                            
                                                        ash=os.getcwd()
                                                        ook=ash+"//reply.png"
                                                        
                                                        photo22 = PhotoImage(file=ook)
                                                        moltress = Button(pikachu,cursor='hand2',highlightthickness=0,activeforeground="black",activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,command=backbtn000)
                                                        moltress.place(x=0,y=62)
                                                        
                                                        pikachu.mainloop()
                                                        
                                                        
                                                                        


                                                        

                                                    else:
                                                        ''''''
                                                        # cur.execute(f'Update Students_database9 set Box_Cricket = "no"  where Mobile_No="{oneplus}"  ')
                                                        # pass
                                                        con.commit()
                                                        # RF()
                                                        # BD()
                                                        # CRS()
                                                        # CRD()
                                                        # TT()
                                                        # CSS()
                                                        # CT5()
                                                        # CT3()
                                                        # PGS()
                                                        # PGD()
                                                        # PGT()
                                                        # PGST()
                                                        # DCS()
                                                        # DSD()
                                                        # DSG()
                                                        # SG()
                                                        # FF()
                                                        # RP()
                                                        # BTBX()
                                                        # PGY()
                                                        # MDI()
                                                        Elist()
                                                        # pl7.place_forget()
                                                        bj=sum(TotalSum)

                                                        cur.execute(f'Update Students_database9 set Totalammo = "{bj}"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        print("total amount1")
                                                        dialga="Total Amount = RS."+str(bj)
                                                        def hommming2():
                                                            ''''''
                                                            reg_button.configure(state=NORMAL)
                                                            RB1.place_forget()
                                                            RB2.place_forget()
                                                            zapados.place_forget()
                                                            
                                                            Admin_label.place(x=494,y=690)
                                                            Remove_label.place(x=880,y=470)
                                                            Edit_label.place(x=890,y=530)
                                                            Exit_label.place(x=756,y=690)
                                                            Vibes_label.place(x=507,y=470)
                                                            eventall_label.place(x=720,y=470)
                                                            reg_label.place(x=515,y=250)
                                                            About_label.place(x=706,y=250)
                                                            MEGA_ARCEUS.place_forget()
                                                            moltress0.place_forget()


                                                            Exit_button.place(x=690,y=530)
                                                            Admin_Login_button.place(x=480,y=530)
                                                            Remove_label_button.place(x=880,y=310)
                                                            Edit_label_button.place(x=890,y=530)
                                                            Vibes_Events_All_Info_button.place(x=690,y=310)
                                                            Vibes_Events.place(x=480,y=310)
                                                            About_Vibes_button.place(x=690,y=90)
                                                            reg_button.place(x=480,y=90)

                                                            
                                                            moltressssss.place_forget()
                                                            pikachu.mainloop()

                                                        ash000000=os.getcwd()
                                                        ookoooooo=ash000000+"//home.png"
                                                        
                                                        photo2222222 = PhotoImage(file=ookoooooo)
                                                        moltressssss = Button(pikachu,cursor='hand2',command=hommming2,bd=0,bg="black",activeforeground="orange",activebackground='black',image=photo2222222 ,highlightthickness=0,width=73,height=65)
                                                        moltressssss.place(x=1289,y=62)
                                                        ''''''
                                                        ''''''
                                                        ll1.place_forget()
                                                        pl9.place_forget()
                                                        pl8.place_forget()
                                                        pl7.place_forget
                                                        pl4.place_forget()


                                                        ''''''
                                                        

                                                        mega.place_forget()
                                                        megapikachu.place_forget()
                                                        mega2.place_forget()
                                                        megapikachu2.place_forget()
                                                        mega3.place_forget()
                                                        megapikachu3.place_forget()
                                                        mega4.place_forget()
                                                        megapikachu4.place_forget()
                                                        mega5.place_forget()
                                                        megapikachu5.place_forget()
                                                        mega6.place_forget()
                                                        megapikachu6.place_forget()
                                                        mega7.place_forget()



                                                        MEGA_ARCEUS=Label(pikachu,text=dialga,width=30,bg='orange',fg='black',font=("Arial Black",50,"bold"))
                                                        MEGA_ARCEUS.place(x=0,y=360)
                                                        arceus.place_forget()
                                                        ''''''
                                                        p01.place_forget()
                                                        p02.place_forget()
                                                        p03.place_forget()
                                                        p04.place_forget()
                                                        p044.place_forget()
                                                        p05.place_forget()
                                                        p06.place_forget()
                                                        p07.place_forget()
                                                        p077.place_forget()
                                                        p08.place_forget()
                                                        p088.place_forget()
                                                        p0888.place_forget()
                                                        p08888.place_forget()
                                                        p09.place_forget()
                                                        p099.place_forget()
                                                        p0999.place_forget()
                                                        p010.place_forget()
                                                        p011.place_forget()
                                                        p012.place_forget() 
                                                        p013.place_forget()
                                                        p014.place_forget()
                                                        p015.place_forget()
                                                        for idx, event in enumerate(eventslist):
                                                            eventsCheck[idx].place_forget()
                                                        
                                                        
                                                        
                                                        def backbtn0001():
                                                            ''''''
                                                            reg_button.configure(state=NORMAL)
                                                            arceus.configure(state=NORMAL)
                                                            megapikachu0.set('')
                                                            megapikachu20.set('')
                                                            megapikachu30.set('')
                                                            megapikachu40.set('')
                                                            megapikachu50.set('')
                                                            megapikachu60.set('')
                                                            __MOF__.set('')
                                                            p1.set(0)
                                                            p2.set(0)
                                                            p3.set(0)
                                                            p4.set(0)
                                                            p5.set(0)
                                                            p6.set(0)
                                                            p7.set(0)
                                                            p8.set(0)
                                                            p9.set(0)
                                                            p10.set(0)
                                                            p11.set(0)
                                                            p12.set(0)
                                                            p13.set(0)
                                                            p14.set(0)
                                                            p15.set(0)
                                                            p44.set(0)
                                                            p77.set(0)
                                                            p88.set(0)
                                                            p888.set(0)
                                                            p8888.set(0)
                                                            p99.set(0)
                                                            p999.set(0)
                                                            ''''''
                                                            moltressssss.place_forget()
                                                            moltress0.place_forget()

                                                            RB1.place(y=391,x=225)
                                                            RB2.place(y=391,x=300)
                                                            
                                                            ll1.place(x = 800, y = 115) 
                                                            pl9.place(x = 820, y = 310)
                                                            pl8.place(x = 820, y = 290)
                                                            pl7.place(x = 820, y = 270)
                                                            pl4.place(x = 820, y = 210)

                                                            ''''''
                                                            mega.place(x=110,y=150)
                                                            megapikachu.place(x=240,y=151)
                                                            mega2.place(x=450,y=150)
                                                            megapikachu2.place(x=580,y=151)
                                                            mega3.place(x=110,y=230)
                                                            megapikachu3.place(x=240,y=231)
                                                            mega4.place(x=450,y=230)
                                                            megapikachu4.place(x=580,y=231)
                                                            mega5.place(x=110,y=310)
                                                            megapikachu5.place(x=240,y=311)
                                                            mega6.place(x=450,y=310)
                                                            megapikachu6.place(x=580,y=311)
                                                            mega7.place(x=110,y=390)
                                                            ''''''
                                                            MEGA_ARCEUS.place_forget()

                                                            
                                                            ''''''
                                                            arceus.place(x=600,y=640)
                                                            ''''''
                                                            p01.place(x = 800, y = 150)
                                                            p02.place(x = 800, y = 170)
                                                            p03.place(x = 800, y = 190)
                                                            p04.place(x = 960, y = 210)
                                                            p044.place(x = 1020, y = 210)
                                                            p05.place(x = 800, y = 230)
                                                            p06.place(x = 800, y = 250)
                                                            p07.place(x = 960, y = 270)
                                                            p077.place(x = 1020, y = 270)
                                                            p08.place(x = 960, y = 290)
                                                            p088.place(x = 1020, y = 290)
                                                            p0888.place(x = 1100, y = 290)
                                                            p08888.place(x = 1170, y = 290) 
                                                            p09.place(x = 960, y = 310) 
                                                            p099.place(x = 1020, y = 310) 
                                                            p0999.place(x = 1100, y = 310)
                                                            p010.place(x = 800, y = 330)
                                                            p011.place(x = 800, y = 350)
                                                            p012.place(x = 800, y = 370) 
                                                            p013.place(x = 800, y = 390)
                                                            p014.place(x = 800, y = 410) 
                                                            p015.place(x = 800, y = 430)
                                                            pikachu.mainloop()
    
                                                        ash=os.getcwd()
                                                        ook=ash+"//reply.png"
                                                        
                                                        photo22 = PhotoImage(file=ook)
                                                        moltress0 = Button(pikachu,cursor='hand2',activeforeground="black",activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,highlightthickness=0,command=backbtn0001)
                                                        moltress0.place(x=0,y=62)
                                                        
                                                        pikachu.mainloop()
                                                        
                                                def RF():
                                                    brock=p2.get()  

                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Rink_Football = "yes"  where Mobile_No="{oneplus}"  ')
                                                        
                                                        
                                                        TotalSum.append(p2p)
                                                        

                                                    else:
                                                        cur.execute(f'Update Students_database9 set Rink_Football = "no"  where Mobile_No="{oneplus}"  ')
                                                        ''''''
                                                        
                                                def Elist():
                                                    for idx,event in enumerate(eventslist):
                                                        brock=eventVariable[idx].get()  

                                                        if brock == 1:
                                                            ''''''
                                                            
                                                            cur.execute(f'Update Students_database9 set {event[0]} = "yes"  where Mobile_No="{oneplus}"  ')
                                                            
                                                            print(event)
                                                            TotalSum.append(event[1])

                                                            

                                                        else:
                                                            cur.execute(f'Update Students_database9 set {event[0]} = "no"  where Mobile_No="{oneplus}"  ')



                                                def BD():
                                                    brock=p3.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Badminton = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()

                                                        TotalSum.append(p3p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Badminton = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def CRS():
                                                    brock=p4.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Carrom_Solo = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p4p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Carrom_Solo = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def CRD():
                                                    brock=p44.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Carrom_Duo = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p44p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Carrom_Duo = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def TT():
                                                    brock=p5.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Table_Tennis = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p5p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Table_Tennis = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def CSS():
                                                    brock=p6.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Chess = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p6p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Chess = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def CT5():
                                                    brock=p7.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Counter_Strike_Five_M = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p7p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Counter_Strike_Five_M = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def CT3():
                                                    brock=p77.get()
                                                    if brock == 1:
                                                        ''''''
                                                       
                                                        cur.execute(f'Update Students_database9 set Counter_Strike_Three_M = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p77p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Counter_Strike_Three_M = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def PGS():
                                                    brock=p8.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Pubg_Solo = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p8p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Pubg_Solo = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def PGD():
                                                    brock=p88.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Pubg_Squad = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p88p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Pubg_Squad = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                       
                                                def PGT():
                                                    brock=p888.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Pubg_TDM = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p888p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Pubg_TDM = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def PGST():
                                                    brock=p8888.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Pubg_Squad_TDM = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p8888p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Pubg_Squad_TDM = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                      
                                                def DCS():
                                                    brock=p9.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Dance_Solo = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p9p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Dance_Solo = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def DSD():
                                                    brock=p99.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Dance_Group_Duo = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p99p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Dance_Group_Duo = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def DSG():
                                                    brock=p999.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Dance_Group_Squad = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p999p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Dance_Group_Squad = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def FF():
                                                    brock=p10.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Fifa = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p10p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Fifa = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def SG():
                                                    brock=p11.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Singing = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p11p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Singing = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def RP():
                                                    brock=p12.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Rapping = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p12p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Rapping = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def BTBX():
                                                    brock=p13.get()
                                                    if brock == 1:
                                                        ''''''
                                                       
                                                        cur.execute(f'Update Students_database9 set Beatboxing = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p13p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Beatboxing = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def PGY():
                                                    brock=p14.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Photography = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p14p)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Photography = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        
                                                def MDI():
                                                    brock=p15.get()
                                                    if brock == 1:
                                                        ''''''
                                                        
                                                        cur.execute(f'Update Students_database9 set Mehndi = "yes"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                        TotalSum.append(p15p)
                                                        bj=sum(TotalSum)
                                                        

                                                    else:
                                                        ''''''
                                                        cur.execute(f'Update Students_database9 set Mehndi = "no"  where Mobile_No="{oneplus}"  ')
                                                        con.commit()
                                                       
                                                BC()
                                                # Elist()                                                
                                                
                                                    
                                                    
                                                    
                                                
                                            else:
                                                showerror("RECHECK","Invalid \nPlease Choose Gender!!")
            ''''''                            
                                                    
                                
                    
                    
                    
            '''VAR'''
            megapikachu0=StringVar()
            megapikachu20=StringVar()
            megapikachu30=StringVar()
            megapikachu40=StringVar()
            megapikachu50=StringVar()
            megapikachu60=StringVar()
            
            '''First Name'''
            mega=Label(pikachu,text="First Name",width=9,bg='orange',fg='black',font=("Arial Black",13,"bold"))
            mega.place(x=110,y=150)
            megapikachu=Entry(pikachu,textvariable=megapikachu0,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=15,font=("Times New Roman",13),fg="orange",bg="black")
            megapikachu.place(x=240,y=151)
            megapikachu.insert(0,'')
            '''Last Name'''
            mega2=Label(pikachu,text="Last Name",width=9,bg='orange',fg='black',font=("Arial Black",13,"bold"))
            mega2.place(x=450,y=150)
            megapikachu2=Entry(pikachu,textvariable=megapikachu20,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=15,font=("Times New Roman",13),fg="orange",bg="black")
            megapikachu2.place(x=580,y=151)
            megapikachu2.insert(0,'')
            '''Standard '''
            mega3=Label(pikachu,text="Standard",width=9,bg='orange',fg='black',font=("Arial Black",13,"bold"))
            mega3.place(x=110,y=230)
            megapikachu3=Entry(pikachu,textvariable=megapikachu30,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=15,font=("Times New Roman",13),fg="orange",bg="black")
            megapikachu3.place(x=240,y=231)
            megapikachu3.insert(0,'')
            '''Email Id '''
            mega4=Label(pikachu,text="Email ID",width=9,bg='orange',fg='black',font=("Arial Black",13,"bold"))
            mega4.place(x=450,y=230)
            megapikachu4=Entry(pikachu,textvariable=megapikachu40,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=15,font=("Times New Roman",13),fg="orange",bg="black")
            megapikachu4.place(x=580,y=231)
            megapikachu4.insert(0,'')
            '''College Name'''
            mega5=Label(pikachu,text="College",width=9,bg='orange',fg='black',font=("Arial Black",13,"bold"))
            mega5.place(x=110,y=310)
            megapikachu5=Entry(pikachu,textvariable=megapikachu50,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=15,font=("Times New Roman",13),fg="orange",bg="black")
            megapikachu5.place(x=240,y=311)
            megapikachu5.insert(0,'')
            '''Mobile'''
            mega6=Label(pikachu,text="Mobile No.",width=9,bg='orange',fg='black',font=("Arial Black",13,"bold"))
            mega6.place(x=450,y=310)
            megapikachu6=Entry(pikachu,textvariable=megapikachu60,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=15,font=("Times New Roman",13),fg="orange",bg="black")
            megapikachu6.place(x=580,y=311)

            megapikachu6.insert(0,'')
            '''Gender'''
            mega7=Label(pikachu,text="Gender",width=9,bg='orange',fg='black',font=("Arial Black",13,"bold"))
            mega7.place(x=110,y=390)
            __MOF__ = StringVar()
            RB1=Radiobutton(pikachu,selectcolor="black",font=("none",12),highlightcolor='black',highlightbackground='black',highlightthickness=2,bd=2,activeforeground='orange',activebackground='black',cursor="target",text="Male",variable=__MOF__,value='Male',width=6,bg="black",fg="orange")
            
            RB2=Radiobutton(pikachu,selectcolor="black",font=("none",12),highlightcolor='black',highlightbackground='black',highlightthickness=2,bd=2,activeforeground='orange',activebackground='black',cursor="target",text="Female",variable=__MOF__,value='Female',width=6,bg="black",fg="orange")
            RB1.place(y=391,x=225)
            RB2.place(y=391,x=315)
            '''Check Boxes'''
            '''label for that''' 
            ll1=Label(pikachu, text ='Select Event To Participate',font=("Arial Black",13),bg="orange",fg="black")
            ll1.place(x = 800, y = 115) 
            
                
            '''check buttons '''
            p1=IntVar()
            p2=IntVar()
            p3=IntVar()
            p4=IntVar()
            p5=IntVar()
            p6=IntVar()
            p7=IntVar()
            p8=IntVar()
            p9=IntVar()
            p10=IntVar()
            p11=IntVar()
            p12=IntVar()
            p13=IntVar()
            p14=IntVar()
            p15=IntVar()
            p44=IntVar()
            p77=IntVar()
            p88=IntVar()
            p888=IntVar()
            p8888=IntVar()
            p99=IntVar()
            p999=IntVar()
            
            
                
            
            
            # p01=Checkbutton(pikachu,variable=p1, text ='BOX CRICKET',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p01.place(x = 800, y = 150)
            
            # p1p=550
            # p02=Checkbutton(pikachu,variable=p2, text ='RINK FOOTBALL',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p02.place(x = 800, y = 170) 
            # p2p=450
            # p03=Checkbutton(pikachu,variable=p3, text ='BADMINTON',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p03.place(x = 800, y = 190) 
            # p3p=50
            # pl4 = Label(pikachu, text ='CARROM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
            # pl4.place(x = 820, y = 210) 
            # p04=Checkbutton(pikachu,variable=p4, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p04.place(x = 960, y = 210) 
            # p4p=50
            # p044=Checkbutton(pikachu,variable=p44, text ='Duo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p044.place(x = 1020, y = 210) 
            # p44p=100
            # p05=Checkbutton(pikachu,variable=p5, text ='TABLE TENNIS',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p05.place(x = 800, y = 230) 
            # p5p=50


            # p06=Checkbutton(pikachu,variable=p6, text ='CHESS',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p06.place(x = 800, y = 250) 
            # p6p=50
            # pl7 = Label(pikachu, text ='COUNTER STRIKE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
            # pl7.place(x = 820, y = 270) 
            # p07=Checkbutton(pikachu,variable=p7, text ='5(S)',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p07.place(x = 960, y = 270) 
            # p7p=250
            # p077=Checkbutton(pikachu,variable=p77, text ='3(S)',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p077.place(x = 1020, y = 270) 
            # p77p=150

            # pl8 = Label(pikachu, text ='PUBG MOBILE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
            # pl8.place(x = 820, y = 290) 
                              
            # p08=Checkbutton(pikachu,variable=p8, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p08.place(x = 960, y = 290) 
            # p8p=50
            # p088=Checkbutton(pikachu,variable=p88, text ='Squad',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p088.place(x = 1020, y = 290) 
            # p88p=200
            # p0888=Checkbutton(pikachu,variable=p888, text ='TDM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p0888.place(x = 1100, y = 290) 
            # p888p=200
            # p08888=Checkbutton(pikachu,variable=p8888, text ='Squad + TDM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p08888.place(x = 1170, y = 290) 
            # p8888p=320
            # pl9 = Label(pikachu, text ='DANCE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
            # pl9.place(x = 820, y = 310) 
            # p09=Checkbutton(pikachu,variable=p9, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p09.place(x = 960, y = 310) 
            # p9p=100
            # p099=Checkbutton(pikachu,variable=p99, text ='Duo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p099.place(x = 1020, y = 310) 
            # p99p=200
            # p0999=Checkbutton(pikachu,variable=p999, text ='Group',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p0999.place(x = 1100, y = 310) 
            
            # p999p=400
            # p010=Checkbutton(pikachu,variable=p10, text ='FIFA',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p010.place(x = 800, y = 330) 
            # p10p=50
            # p011=Checkbutton(pikachu,variable=p11, text ='SINGING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p011.place(x = 800, y = 350) 
            # p11p=100
            # p012=Checkbutton(pikachu,variable=p12, text ='RAPPING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p012.place(x = 800, y = 370) 
            # p12p=100
            # p013=Checkbutton(pikachu,variable=p13, text ='BEATBOXING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p013.place(x = 800, y = 390) 
            # p13p=100
            # p014=Checkbutton(pikachu,variable=p14, text ='PHOTOGRAPHY',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p014.place(x = 800, y = 410) 
            # p14p=50
            # p015=Checkbutton(pikachu,variable=p15, text ='MEHNDI',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
            #                    takefocus = 0)
            # p015.place(x = 800, y = 430) 
            # p15p=20
            y=130
            for idx, event in enumerate(eventslist):
                if event[3] == 1:
                    continue
                eventVariable[idx]=IntVar()
                y=y+20
                eventsCheck[idx]=Checkbutton(pikachu,variable=eventVariable[idx], text =event[0],font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                               takefocus = 0)
                eventsCheck[idx].place(x=800,y=y)
            

            arceus=Button(pikachu,command=pokeball,state=NORMAL,activebackground="black",border=0,activeforeground="orange",text="Submit",fg='black',bg='orange',height=3,width=16)
            arceus.place(x=600,y=640)
            
            def backbtn1():
                ''''''
                
                arceus.configure(state=NORMAL)
                ll1.place_forget()
                # pl9.place_forget()
                # pl8.place_forget()
                # pl7.place_forget()
                # pl4.place_forget()
                Admin_label.place(x=494,y=690)
                Remove_label.place(x=880,y=470)
                Exit_label.place(x=756,y=690)
                Edit_label.place(x=890,y=690)
                Vibes_label.place(x=507,y=470)
                eventall_label.place(x=720,y=470)
                reg_label.place(x=515,y=250)
                About_label.place(x=706,y=250)

                ''''''
                
                RB1.place_forget()
                RB2.place_forget()
                mega.place_forget()
                megapikachu.place_forget()
                mega2.place_forget()
                megapikachu2.place_forget()
                mega3.place_forget()
                megapikachu3.place_forget()
                mega4.place_forget()
                megapikachu4.place_forget()
                mega5.place_forget()
                megapikachu5.place_forget()
                mega6.place_forget()
                megapikachu6.place_forget()
                mega7.place_forget()
                arceus.place_forget()
                ''''''
                Exit_button.place(x=690,y=530)
                Admin_Login_button.place(x=480,y=530)
                Remove_label_button.place(x=880,y=310)
                Edit_label_button.place(x=890,y=530)
                Vibes_Events_All_Info_button.place(x=690,y=310)
                Vibes_Events.place(x=480,y=310)
                About_Vibes_button.place(x=690,y=90)
                reg_button.place(x=480,y=90)

                ''''''
                # p01.place_forget()
                # p02.place_forget()
                # p03.place_forget()
                # p04.place_forget()
                # p044.place_forget()
                # p05.place_forget()
                # p06.place_forget()
                # p07.place_forget()
                # p077.place_forget()
                # p08.place_forget()
                # p088.place_forget()
                # p0888.place_forget()
                # p08888.place_forget()
                # p09.place_forget()
                # p099.place_forget()
                # p0999.place_forget()
                # p010.place_forget()
                # p011.place_forget()
                # p012.place_forget() 
                # p013.place_forget()
                # p014.place_forget()
                # p015.place_forget()
                for idx, event in enumerate(eventslist):
                    if event[3] == 1:
                        continue
                    eventsCheck[idx].place_forget()
                ''''''
                zapados.place_forget()
            ash=os.getcwd()
            ook=ash+"//reply.png"
            
            photo22 = PhotoImage(file=ook)
            


            zapados = Button(pikachu,cursor='hand2',activeforeground="black",activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,highlightthickness=0,command=backbtn1)
            zapados.place(x=0,y=62)
            pikachu.mainloop()
        regit=os.getcwd()
        regit2=regit+"//domain.png"
        
        photoRR = PhotoImage(file=regit2)
        reg_button=Button(pikachu,bd=0,cursor='hand2',highlightthickness=2,highlightcolor='orange',highlightbackground='orange',activebackground="black",image=photoRR,width=170,height=170,bg="black",command=reg_button_1)
        reg_button.place(x=480,y=90)
        reg_label=Label(pikachu,font=("Arial Black",15,"bold"),text='Register',bd=0,highlightthickness=0,bg='black',fg='orange')
        reg_label.place(x=515,y=250)
        def About_Vibes_button_2():
            '''Button 2 Functions The following Program '''
           
            
            reg_button.place_forget()
            About_Vibes_button.place_forget()
            Vibes_Events.place_forget()
            Vibes_Events_All_Info_button.place_forget()
            Remove_label_button.place_forget()
            Admin_Login_button.place_forget()
            Edit_label_button.place_forget()
            Edit_label.place_forget()
            Exit_button.place_forget()
            Admin_label.place_forget()
            Exit_label.place_forget()
            Vibes_label.place_forget()
            reg_label.place_forget()
            eventall_label.place_forget()
            About_label.place_forget()
            Remove_label.place_forget()
            def audioplay():
                ''''''
                moltresssssspp.configure(state=DISABLED)
               
                os.system("mpg123 "+"audio//About_Vibes.mp3")
            play=os.getcwd()

            playit=play+"//circular.png"
            
            photop = PhotoImage(file=playit)
            moltresssssspp = Button(pikachu,cursor='hand2',command=audioplay,bd=0,bg="black",activeforeground="orange",activebackground='black',image=photop ,width=73,height=65,highlightthickness=0)
            moltresssssspp.place(x=1289,y=62)
            def backbtn():
                ''''''
                
                moltresssssspp.place_forget()
                
                charizard.place_forget()
                Edit_label.place(x=890,y=530)
                Admin_label.place(x=494,y=690)
                Remove_label.place(x=880,y=470)
                Exit_label.place(x=756,y=690)
                Vibes_label.place(x=507,y=470)
                eventall_label.place(x=720,y=470)
                reg_label.place(x=515,y=250)
                About_label.place(x=706,y=250)
                Exit_button.place(x=690,y=530)
                Admin_Login_button.place(x=480,y=530)
                Edit_label_button.place(x=890,y=530)
                Vibes_Events_All_Info_button.place(x=690,y=310)
                Vibes_Events.place(x=480,y=310)
                About_Vibes_button.place(x=690,y=90)
                reg_button.place(x=480,y=90)
                
                zapados.place_forget()
                

                
                
                    
                
            ash=os.getcwd()
            ook=ash+"//reply.png"
            
            photo22 = PhotoImage(file=ook)
            


            zapados = Button(pikachu,cursor='hand2',activeforeground="black",activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,highlightthickness=0,command=backbtn)
            zapados.place(x=0,y=62)
            

            with open("AboutVibes.txt","r") as op:
                charizard=Label(pikachu,bg="black",font=("Consolas",23,"bold"),fg="orange",text=op.read())
                charizard.place(x=50,y=150)
            pikachu.mainloop()    
        aboutv=os.getcwd()
        aboutv2=aboutv+"//information.png"
        
        photoAB = PhotoImage(file=aboutv2)  
        About_Vibes_button=Button(pikachu,cursor='hand2',bd=0,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,activebackground="black",image=photoAB,width=170,height=170,bg="black",command=About_Vibes_button_2)
        About_Vibes_button.place(x=690,y=90)
        About_label=Label(pikachu,font=("Arial Black",15,"bold"),text='About Vibes',bd=0,highlightthickness=0,bg='black',fg='orange')
        About_label.place(x=706,y=250)
        '''!!!'''


            
        def Vibes_Events_button_3():
            '''Button 3 Functions The following Program '''
           
            
            reg_button.place_forget()
            About_Vibes_button.place_forget()
            Vibes_Events.place_forget()
            Vibes_Events_All_Info_button.place_forget()
            Remove_label_button.place_forget()
            Admin_Login_button.place_forget()
            Edit_label_button.place_forget()
            Edit_label.place_forget()
            Exit_button.place_forget()
            Admin_label.place_forget()
            Exit_label.place_forget()
            Vibes_label.place_forget()
            reg_label.place_forget()
            eventall_label.place_forget()
            About_label.place_forget()
            Remove_label.place_forget()
            def backbtn222():
                ''''''
               
                charizard.place_forget()
                moltress.place_forget()
                
                Admin_label.place(x=494,y=690)
                Remove_label.place(x=880,y=470)
                Exit_label.place(x=756,y=690)
                Edit_label.place(x=890,y=530)
                Vibes_label.place(x=507,y=470)
                eventall_label.place(x=720,y=470)
                reg_label.place(x=515,y=250)
                About_label.place(x=706,y=250)
                Exit_button.place(x=690,y=530)
                Admin_Login_button.place(x=480,y=530)
                Edit_label_button.place(x=890,y=530)
                Vibes_Events_All_Info_button.place(x=690,y=310)
                Vibes_Events.place(x=480,y=310)
                About_Vibes_button.place(x=690,y=90)
                reg_button.place(x=480,y=90)
                
            ash=os.getcwd()
            ook=ash+"//reply.png"
            
            photo22 = PhotoImage(file=ook)
            moltress = Button(pikachu,cursor='hand2',activeforeground="black",activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,highlightthickness=0,command=backbtn222)
            moltress.place(x=0,y=62)
            with open("Events.txt","r") as op:
                charizard=Label(pikachu,bg="black",font=("Consolas",20,"bold"),fg="orange",text=op.read())
                charizard.place(x=160,y=90)
            pikachu.mainloop()
        price=os.getcwd()
        price2=price+"//fee.png"
        
        photoEP = PhotoImage(file=price2)     
        Vibes_Events=Button(pikachu,bd=0,cursor='hand2',highlightthickness=2,highlightcolor='orange',highlightbackground='orange',activebackground="black",image=photoEP,width=170,height=170,bg="black",command=Vibes_Events_button_3)
        Vibes_Events.place(x=480,y=310)
        Vibes_label=Label(pikachu,font=("Arial Black",15,"bold"),text='Entry Fees',bd=0,highlightthickness=0,bg='black',fg='orange')
        Vibes_label.place(x=507,y=470)
        def Vibes_Events_All_Info_button_4():
            '''Button 4 Functions The following Program '''
            
            reg_button.place_forget()
            About_Vibes_button.place_forget()
            Vibes_Events.place_forget()
            Vibes_Events_All_Info_button.place_forget()
            Remove_label_button.place_forget()
            Admin_Login_button.place_forget()
            Edit_label.place_forget()
            Edit_label_button.place_forget()
            Exit_button.place_forget()
            ''''''
            
            
            
            def backbtn90():
                ''''''
               
                moltress.place_forget()
                """ charizard.place_forget() """
                listbox.place_forget()
                
                Edit_label.place(x=890,y=530)
                Admin_label.place(x=494,y=690)
                Exit_label.place(x=756,y=690)
                Vibes_label.place(x=507,y=470)
                eventall_label.place(x=720,y=470)
                reg_label.place(x=515,y=250)
                About_label.place(x=706,y=250)
                Exit_button.place(x=690,y=530)
                Edit_label_button.place(x=890,y=530)
                Remove_label_button.place(x=880,y=310)
                Admin_Login_button.place(x=480,y=530)
                Vibes_Events_All_Info_button.place(x=690,y=310)
                Vibes_Events.place(x=480,y=310)
                About_Vibes_button.place(x=690,y=90)
                reg_button.place(x=480,y=90)
                scrollbar.pack_forget()
                
                
            ash=os.getcwd()
            ook=ash+"//reply.png"
            
            photo22 = PhotoImage(file=ook)
            moltress = Button(pikachu,cursor='hand2',highlightthickness=0,bg="black",image=photo22 ,width=73,height=65,border=0,activeforeground="black",activebackground='black',command=backbtn90)
            moltress.place(x=0,y=62)
            
            scrollbar = Scrollbar(pikachu)
            scrollbar.pack(side=RIGHT, fill=Y)
            listbox = Listbox(pikachu,bg="black",highlightthickness=0,bd=0,font=("Consolas",17,"bold"),fg="orange",width=80,height=20)
            listbox.place(x=100,y=140)
            file = open('allevents.txt', 'r').readlines()
            for i in file:
                listbox.insert(END, i)
            listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=listbox.yview)
            #justscrolly.pack(side=RIGHT,fill=Y)`
            """ with open("allevents.txt","r") as op:
                charizard = Label(pikachu,bg="black",font=("Consolas",10,"bold"),fg="orange",text=op.read())
                charizard.place(x=160,y=90)
                #justscrolly.config(command=charizard.yview)
             """
            pikachu.mainloop()
        allev=os.getcwd()
        alleve=allev+"//podium.png"
        
        photoALV = PhotoImage(file=alleve) 
        Vibes_Events_All_Info_button=Button(pikachu,cursor='hand2',highlightthickness=2,highlightbackground='orange',highlightcolor='orange',bd=0,activebackground="black",image=photoALV,width=170,height=170,bg="black",command=Vibes_Events_All_Info_button_4)
        Vibes_Events_All_Info_button.place(x=690,y=310)
        eventall_label=Label(pikachu,font=("Arial Black",15,"bold"),text='All Events',bd=0,highlightthickness=0,bg='black',fg='orange')
        eventall_label.place(x=720,y=470)
        def Admin_Login_button_5():
            '''Button 5 Functions The following Program '''
           
            
            reg_button.place_forget()
            About_Vibes_button.place_forget()
            Vibes_Events.place_forget()
            Vibes_Events_All_Info_button.place_forget()
            Remove_label_button.place_forget()
            Admin_Login_button.place_forget()
            Edit_label_button.place_forget()
            Edit_label.place_forget()
            Exit_button.place_forget()
            Admin_label.place_forget()
            Exit_label.place_forget()
            Vibes_label.place_forget()
            reg_label.place_forget()
            eventall_label.place_forget()
            About_label.place_forget()
            Remove_label.place_forget()
            def submitpass():
                ''''''
                hoho=diglet1.get()
                
                if hoho=="admin":
                     
                    pubgm.place_forget()
                    moltress.place_forget()
                    
                    '''INSERT FRAME LEFT'''
                    yash_f=Frame(pikachu,bd=1,highlightthickness=3,highlightbackground="orange",relief=SUNKEN,bg="orange")
                    yash_f.place(x=20,y=150,width=510,height=600)
                    ''''''
                    rock=Label(yash_f,text="Registered Data",width=13,bg='orange',fg='black',font=("Arial Black",25,"bold"))
                    rock.pack(side=TOP,fill=X)
                    




                    '''VAR'''
                    megapikachuz1=StringVar()
                    megapikachu2z2=StringVar()
                    megapikachu3z3=StringVar()
                    megapikachu4z4=StringVar()
                    megapikachu5z5=StringVar()
                    megapikachu6z6=StringVar()
                    __MOF__ = StringVar()
                    '''First Name'''
                    megaz=Label(yash_f,text="First Name",bg='orange',fg='black',font=("Arial Black",18,"bold"))
                    megaz.place(x=20,y=70)
                    megapikachuz=Entry(yash_f,textvariable=megapikachuz1,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=25,font=("Times New Roman",14),fg="orange",bg="black")
                    megapikachuz.place(x=180,y=71)
                    megapikachuz.insert(0,'')
                    '''Last Name'''
                    mega2z=Label(yash_f,text="Last Name",bg='orange',fg='black',font=("Arial Black",18,"bold"))
                    mega2z.place(x=20,y=130)
                    megapikachu2z=Entry(yash_f,textvariable=megapikachu2z2,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=25,font=("Times New Roman",14),fg="orange",bg="black")
                    megapikachu2z.place(x=180,y=131)
                    megapikachu2z.insert(0,'')
                    '''Standard '''
                    mega3z=Label(yash_f,text="Standard",bg='orange',fg='black',font=("Arial Black",18,"bold"))
                    mega3z.place(x=20,y=190)
                    megapikachu3z=Entry(yash_f,textvariable=megapikachu3z3,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=25,font=("Times New Roman",14),fg="orange",bg="black")
                    megapikachu3z.place(x=180,y=191)
                    megapikachu3z.insert(0,'')
                    '''Email Id '''
                    mega4z=Label(yash_f,text="Email ID",bg='orange',fg='black',font=("Arial Black",18,"bold"))
                    mega4z.place(x=20,y=250)
                    megapikachu4z=Entry(yash_f,textvariable=megapikachu4z4,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=25,font=("Times New Roman",14),fg="orange",bg="black")
                    megapikachu4z.place(x=180,y=251)
                    megapikachu4z.insert(0,'')
                    '''College Name'''
                    mega5z=Label(yash_f,text="College",bg='orange',fg='black',font=("Arial Black",18,"bold"))
                    mega5z.place(x=20,y=310)
                    megapikachu5z=Entry(yash_f,textvariable=megapikachu5z5,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=25,font=("Times New Roman",14),fg="orange",bg="black")
                    megapikachu5z.place(x=180,y=311)
                    megapikachu5z.insert(0,'')
                    '''Mobile'''
                    mega6z=Label(yash_f,text="Mobile No.",bg='orange',fg='black',font=("Arial Black",18,"bold"))
                    mega6z.place(x=20,y=370)
                    megapikachu6z=Entry(yash_f,textvariable=megapikachu6z6,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=25,font=("Times New Roman",14),fg="orange",bg="black")
                    megapikachu6z.place(x=180,y=371)

                    megapikachu6z.insert(0,'')
                    '''Gender'''
                    mega7z=Label(yash_f,text="Gender",bg='orange',fg='black',font=("Arial Black",18,"bold"))
                    mega7z.place(x=20,y=430)
                    
                    RB1z=Radiobutton(yash_f,selectcolor="orange",font=("none",12),highlightcolor='orange',highlightbackground='black',highlightthickness=2,bd=2,activeforeground='orange',activebackground='black',cursor="target",text="Male",variable=__MOF__,value='Male',width=7,bg="orange",fg="black")
                    RB1z.place(y=431,x=180)
                    RB2z=Radiobutton(yash_f,selectcolor="orange",font=("none",12),highlightcolor='orange',highlightbackground='black',highlightthickness=2,bd=2,activeforeground='orange',activebackground='black',cursor="target",text="Female",variable=__MOF__,value='Female',width=7,bg="orange",fg="black")
                    RB2z.place(y=431,x=300)
                    
                    # pupdate=Label(yash_f,text="To Participate\nIn Other Events",width=13,bg='orange',fg='black',font=("none",12))
                    def Pupdates():
                        """ Pradeep_K.place_forget()
                        Pradeep_K.place(x=2,y=40,width=760,height=530) """
                        moltresssss.place_forget()
                        
                        
                        #moltresssss.place_forget()
                        moltressx.place_forget()
                        yash_f.place_forget()
                        neelC.grid_forget()
                        apreetiC.grid_forget()
                        omC.grid_forget()

                        imraan=Frame(pikachu,bd=1,highlightthickness=3,highlightbackground="orange",relief=RIDGE,bg="orange")
                        imraan.place(x=20,y=150,width=510,height=600)
                        
                        '''Check Boxes'''
                        '''label for that''' 
                        ll1=Label(imraan, text ='Select Event To Participate',font=("Arial Black",14,'bold'),bg="orange",fg="black")
                        ll1.pack(side=TOP,fill=X) 
                        
                            
                        '''check buttons '''
                        p1=IntVar()
                        p2=IntVar()
                        p3=IntVar()
                        p4=IntVar()
                        p5=IntVar()
                        p6=IntVar()
                        p7=IntVar()
                        p8=IntVar()
                        p9=IntVar()
                        p10=IntVar()
                        p11=IntVar()
                        p12=IntVar()
                        p13=IntVar()
                        p14=IntVar()
                        p15=IntVar()
                        p44=IntVar()
                        p77=IntVar()
                        p88=IntVar()
                        p888=IntVar()
                        p8888=IntVar()
                        p99=IntVar()
                        p999=IntVar()

                        ''''''
                        pqrs=Label(imraan,text='F-Name : ',bg='orange',font=("Arial Black",10,"bold"),fg='black',width=8,bd=0,highlightthickness=1,highlightcolor='black')
                        pqrst=Label(imraan,text='Mobile-No : ',bg='orange',font=("Arial Black",10,"bold"),fg='black',width=10,bd=0,highlightthickness=1,highlightcolor='black')
                        pqrs.place(x=5,y=70)
                        pqrst.place(x=250,y=70)

                        ''''''
                        
                        p01=Checkbutton(imraan,variable=p1,text ='BOX CRICKET',font=("Arial Black",9,"bold"),highlightcolor='orange',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p01.place(x = 10, y = 100)
                        
                        p1p=550
                        p02=Checkbutton(imraan,variable=p2, text ='RINK FOOTBALL',font=("Arial Black",9,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p02.place(x = 190, y = 100) 
                        p2p=450
                        p03=Checkbutton(imraan,variable=p3, text ='BADMINTON',font=("Arial Black",9,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p03.place(x = 390, y = 100) 
                        p3p=50
                        pl4 = Label(imraan, text ='CARROM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='orange',highlightthickness=1,bd=1 )
                        pl4.place(x = 0, y = 150) 
                        p04=Checkbutton(imraan,variable=p4, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p04.place(x = 190, y = 150) 
                        p4p=50
                        p044=Checkbutton(imraan,variable=p44, text ='Duo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p044.place(x = 280, y = 150) 
                        p44p=100
                        p05=Checkbutton(imraan,variable=p5, text ='TABLE TENNIS',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p05.place(x = 10, y = 200) 
                        p5p=50


                        p06=Checkbutton(imraan,variable=p6, text ='CHESS',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p06.place(x = 190, y = 200) 
                        p6p=50
                        pl7 = Label(imraan, text ='COUNTER STRIKE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
                        pl7.place(x = 0, y = 250) 
                        p07=Checkbutton(imraan,variable=p7, text ='5-Members(S)',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p07.place(x = 160, y = 250) 
                        p7p=250
                        p077=Checkbutton(imraan,variable=p77, text ='3-Members(S)',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p077.place(x = 310, y = 250) 
                        p77p=150

                        pl8 = Label(imraan, text ='PUBG MOBILE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
                        pl8.place(x = 0, y = 300) 
                                        
                        p08=Checkbutton(imraan,variable=p8, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p08.place(x = 120, y = 300) 
                        p8p=50
                        p088=Checkbutton(imraan,variable=p88, text ='Squad',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p088.place(x = 190, y = 300) 
                        p88p=200
                        p0888=Checkbutton(imraan,variable=p888, text ='TDM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p0888.place(x = 280, y = 300) 
                        p888p=200
                        p08888=Checkbutton(imraan,variable=p8888, text ='Squad + TDM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p08888.place(x = 350, y = 300) 
                        p8888p=320
                        pl9 = Label(imraan, text ='DANCE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='orange',highlightthickness=1,bd=1 )
                        pl9.place(x = 0, y = 350) 
                        p09=Checkbutton(imraan,variable=p9, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p09.place(x = 190, y = 350) 
                        p9p=100
                        p099=Checkbutton(imraan,variable=p99, text ='Duo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p099.place(x = 280, y = 350) 
                        p99p=200
                        p0999=Checkbutton(imraan,variable=p999, text ='Group',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p0999.place(x = 370, y = 350) 
                        
                        p999p=400
                        p010=Checkbutton(imraan,variable=p10, text ='FIFA',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p010.place(x = 10, y = 400) 
                        p10p=50
                        p011=Checkbutton(imraan,variable=p11, text ='SINGING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p011.place(x = 190, y =400) 
                        p11p=100
                        p012=Checkbutton(imraan,variable=p12, text ='RAPPING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p012.place(x = 390, y = 400) 
                        p12p=100
                        p013=Checkbutton(imraan,variable=p13, text ='BEATBOXING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p013.place(x = 10, y = 450) 
                        p13p=100
                        p014=Checkbutton(imraan,variable=p14, text ='PHOTOGRAPHY',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p014.place(x = 190, y = 450) 
                        p14p=50
                        p015=Checkbutton(imraan,variable=p15, text ='MEHNDI',font=("Arial Black",10,"bold"),highlightcolor='orange',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p015.place(x = 390, y =450) 
                        p15p=20
                        gavin=Frame(imraan,bd=0,highlightthickness=3,highlightbackground="orange",relief=RIDGE,bg="black")
                        gavin.place(x=10,y=510,width=480,height=70)
                        shalom=Label(gavin,relief=RIDGE,highlightcolor='black',highlightbackground='black',highlightthickness=0,activebackground="black",border=0,activeforeground="black",text="",fg='black',bg='black',height=2,width=14)
                        shalom.grid(row=0,column=0,padx=10,pady=9)
                        
                        angel=Button(gavin,relief=RIDGE,highlightcolor='orange',highlightbackground='orange',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",text="Update",command=deletesoftskills,fg='black',bg='orange',height=2,width=14)
                        angel.config(state=DISABLED)
                        angel.place(relx=0.5,rely=0.5,anchor=CENTER)
                        def selector(ev):
                             
                            
                            select_row=preeti.focus()
                            cdata=preeti.item(select_row)
                            row=cdata['values']
                            
                            p01.config(state=NORMAL)
                            p02.config(state=NORMAL)
                            p03.config(state=NORMAL)
                            p04.config(state=NORMAL)
                            p044.config(state=NORMAL)
                            p05.config(state=NORMAL)
                            p06.config(state=NORMAL)
                            p07.config(state=NORMAL)
                            p077.config(state=NORMAL)
                            p08.config(state=NORMAL)
                            p088.config(state=NORMAL)
                            p0888.config(state=NORMAL)
                            p08888.config(state=NORMAL)
                            p09.config(state=NORMAL)
                            p099.config(state=NORMAL)
                            p0999.config(state=NORMAL)
                            p010.config(state=NORMAL)
                            p011.config(state=NORMAL)
                            p012.config(state=NORMAL)
                            p013.config(state=NORMAL)
                            p014.config(state=NORMAL)
                            p015.config(state=NORMAL)
                            ''''''
                            
                            
                            try:
                                xyz=row[0]
                                abc=row[5]
                               
                              
                                pqr=Label(imraan,text=f'{xyz}',font=("Arial Black",10,"bold"),bg='orange',fg='black',width=15,bd=0)
                                pq=Label(imraan,text=f'{abc}',font=("Arial Black",10,"bold"),bg='orange',fg='black',width=10,bd=0)
                                pqr.place(x=90,y=70)
                                pq.place(x=360,y=70)
                                Ulist=[]
                                Utotal=row[7]
                                
                                
                                oneplus=(row[5])
                                
                                
                                def bc():
                                    if (row[8]=='yes'):
                                        p01.config(state=DISABLED)
                                        p1.set(1)
                                        
                                        rf()
                                        bd()
                                        crs()
                                        crd()
                                        tt()
                                        css()
                                        ct5()
                                        ct3()
                                        pgs()
                                        pgd()
                                        pgt()
                                        pgst()
                                        dcs()
                                        dsd()
                                        dsg()
                                        sg()
                                        ff()
                                        rp()
                                        btbx()
                                        pgy()
                                        mdi()

                                        

                                        
                                    else:
                                        p1.set(0)
                                        rf()
                                        bd()
                                        crs()
                                        crd()
                                        tt()
                                        css()
                                        ct5()
                                        ct3()
                                        pgs()
                                        pgd()
                                        pgt()
                                        pgst()
                                        dcs()
                                        dsd()
                                        dsg()
                                        sg()
                                        ff()
                                        rp()
                                        btbx()
                                        pgy()
                                        mdi()
                                        
                                        
                                
                                
                                def rf():
                                    
                                    if (row[9]=='yes'):
                                        p02.config(state=DISABLED)
                                        p2.set(1)
                                    else:
                                        p2.set(0)
                                def bd():
                                    
                                    if (row[10]=='yes'):
                                        p03.config(state=DISABLED)
                                        p3.set(1)
                                        
                                    else:
                                        p3.set(0)
                                        
                                
                                
                                def crs():
                                    
                                    if (row[11]=='yes'):
                                        p04.config(state=DISABLED)
                                        p4.set(1)
                                    else:
                                        p4.set(0)
                                def crd():
                                    
                                    if (row[12]=='yes'):
                                        p044.config(state=DISABLED)
                                        p44.set(1)
                                    else:
                                        p44.set(0)
                                
                                def tt():
                                    
                                    if (row[13]=='yes'):
                                        p05.config(state=DISABLED)
                                        p5.set(1)
                                        
                                    else:
                                        p5.set(0)
                                        
                                
                                
                                def css():
                                    
                                    if (row[14]=='yes'):
                                        p06.config(state=DISABLED)
                                        p6.set(1)
                                    else:
                                        p6.set(0)
                                def ct5():
                                    
                                    if (row[15]=='yes'):
                                        p07.config(state=DISABLED)
                                        p7.set(1)
                                        
                                    else:
                                        p7.set(0)
                                        
                                
                                
                                def ct3():
                                    
                                    if (row[16]=='yes'):
                                        p077.config(state=DISABLED)
                                        p77.set(1)
                                    else:
                                        p77.set(0)
                                def pgs():
                                    
                                    if (row[17]=='yes'):
                                        p08.config(state=DISABLED)
                                        p8.set(1)
                                        
                                    else:
                                        p8.set(0)
                                        
                                
                                
                                def pgd():
                                    
                                    if (row[18]=='yes'):
                                        p088.config(state=DISABLED)
                                        p88.set(1)
                                    else:
                                        p88.set(0)
                                def pgt():
                                    
                                    if (row[19]=='yes'):
                                        p0888.config(state=DISABLED)
                                        p888.set(1)
                                        
                                    else:
                                        p888.set(0)
                                        
                                
                                
                                def pgst():
                                    
                                    if (row[20]=='yes'):
                                        p08888.config(state=DISABLED)
                                        p8888.set(1)
                                    else:
                                        p8888.set(0)
                                def dcs():
                                    
                                    if (row[21]=='yes'):
                                        p09.config(state=DISABLED)
                                        p9.set(1)
                                        
                                    else:
                                        p9.set(0)
                                        
                                
                                
                                def dsd():
                                    
                                    if (row[22]=='yes'):
                                        p099.config(state=DISABLED)
                                        p99.set(1)
                                    else:
                                        p99.set(0)
                                def dsg():
                                    
                                    if (row[23]=='yes'):
                                        p0999.config(state=DISABLED)
                                        p999.set(1)
                                        
                                    else:
                                        p999.set(0)
                                        
                                
                                
                                def ff():
                                    
                                    if (row[24]=='yes'):
                                        p010.config(state=DISABLED)
                                        p10.set(1)
                                    else:
                                        p10.set(0)
                                def sg():
                                    
                                    if (row[25]=='yes'):
                                        p011.config(state=DISABLED)
                                        p11.set(1)
                                    else:
                                        p11.set(0)
                                def rp():
                                    
                                    if (row[26]=='yes'):
                                        p012.config(state=DISABLED)
                                        p12.set(1)
                                        
                                    else:
                                        p12.set(0)
                                        
                                
                                
                                def btbx():
                                    
                                    if (row[27]=='yes'):
                                        p013.config(state=DISABLED)
                                        p13.set(1)
                                    else:
                                        p13.set(0)
                                def pgy():
                                    
                                    if (row[28]=='yes'):
                                        p014.config(state=DISABLED)
                                        p14.set(1)
                                        
                                    else:
                                        p14.set(0)

                                        
                                
                                
                                def mdi():
                                    
                                    if (row[29]=='yes'):
                                        p015.config(state=DISABLED)
                                        p15.set(1)
                                       
                                        
                                    else:
                                        p15.set(0)
                                        
                                        
                                def Eupdate():
                                    
                                    
                                    TotalSum=[]
                                    def BC():
                                        
                                        brock=p1.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Box_Cricket = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p1p)
                                            
                                            RF()
                                            BD()
                                            CRS()
                                            CRD()
                                            TT()
                                            CSS()
                                            CT5()
                                            CT3()
                                            PGS()
                                            PGD()
                                            PGT()
                                            PGST()
                                            DCS()
                                            DSD()
                                            DSG()
                                            SG()
                                            FF()
                                            RP()
                                            BTBX()
                                            PGY()
                                            MDI()
                                            Elist()
                                            bj=sum(Ulist)
                                            cur.execute(f'Update Students_database9 set totalammo = {bj} where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            showalldata()
                                            """ bj=sum(TotalSum)
                                            cur.execute(f'Update Students_database9 set Totalammo = "{bj}"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            dialga="Total Amount = RS."+str(bj) """
                                            """ MEGA_ARCEUS=Label(pikachu,text=dialga,width=30,bg='orange',fg='black',font=("Arial Black",50,"bold"))
                                            MEGA_ARCEUS.place(x=0,y=360) """
                                            ''''''
                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Box_Cricket = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            RF()
                                            BD()
                                            CRS()
                                            CRD()
                                            TT()
                                            CSS()
                                            CT5()
                                            CT3()
                                            PGS()
                                            PGD()
                                            PGT()
                                            PGST()
                                            DCS()
                                            DSD()
                                            DSG()
                                            SG()
                                            FF()
                                            RP()
                                            BTBX()
                                            PGY()
                                            MDI()
                                            Elist()
                                            bj=sum(Ulist)
                                            cur.execute(f'Update Students_database9 set totalammo = {bj} where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            showalldata()
                                            
                                    def RF():
                                        brock=p2.get()  

                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Rink_Football = "yes"  where Mobile_No="{oneplus}"  ')
                                            
                                            
                                            Ulist.append(p2p)
                                            

                                        else:
                                            cur.execute(f'Update Students_database9 set Rink_Football = "no"  where Mobile_No="{oneplus}"  ')
                                            ''''''
                                            
                                    def BD():
                                        brock=p3.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Badminton = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()

                                            Ulist.append(p3p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Badminton = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def CRS():
                                        brock=p4.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Carrom_Solo = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p4p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Carrom_Solo = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def CRD():
                                        brock=p44.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Carrom_Duo = "yes"  where Mobile_No="{oneplus}" ')
                                            con.commit()
                                            Ulist.append(p44p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Carrom_Duo = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def TT():
                                        brock=p5.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Table_Tennis = "yes" where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p5p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Table_Tennis = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def CSS():
                                        brock=p6.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Chess = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p6p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Chess = "no"  where Mobile_No="{oneplus}" ')
                                            con.commit()
                                            
                                    def CT5():
                                        brock=p7.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Counter_Strike_Five_M = "yes"  where Mobile_No="{oneplus}" ')
                                            con.commit()
                                            Ulist.append(p7p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Counter_Strike_Five_M = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def CT3():
                                        brock=p77.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Counter_Strike_Three_M = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p77p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Counter_Strike_Three_M = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def PGS():
                                        brock=p8.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Pubg_Solo = "yes"  where Mobile_No="{oneplus}" ')
                                            con.commit()
                                            Ulist.append(p8p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Pubg_Solo = "no"  where Mobile_No="{oneplus}" ')
                                            con.commit()
                                            
                                    def PGD():
                                        brock=p88.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Pubg_Squad = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p88p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Pubg_Squad = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def PGT():
                                        brock=p888.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Pubg_TDM = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p888p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Pubg_TDM = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def PGST():
                                        brock=p8888.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Pubg_Squad_TDM = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p8888p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Pubg_Squad_TDM = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def DCS():
                                        brock=p9.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Dance_Solo = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p9p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Dance_Solo = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def DSD():
                                        brock=p99.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Dance_Group_Duo = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p99p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Dance_Group_Duo = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def DSG():
                                        brock=p999.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Dance_Group_Squad = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p999p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Dance_Group_Squad = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def FF():
                                        brock=p10.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Fifa = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p10p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Fifa = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def SG():
                                        brock=p11.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Singing = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p11p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Singing = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def RP():
                                        brock=p12.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Rapping = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p12p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Rapping = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def BTBX():
                                        brock=p13.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Beatboxing = "yes" where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p13p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Beatboxing = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def PGY():
                                        brock=p14.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Photography = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p14p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Photography = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def MDI():
                                        brock=p15.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Mehndi = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p15p)

                                            
                                            
                                            con.commit()

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Mehndi = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                    def Elist():
                                        for idx,event in enumerate(eventslist):
                                            brock=eventsCheck[idx].get()  

                                            if brock == 1:
                                                ''''''
                                                
                                                cur.execute(f'Update Students_database9 set {event[0]} = "yes"  where Mobile_No="{oneplus}"  ')
                                                
                                                print(event)
                                                Ulist.append(event[1])

                                                

                                            else:
                                                cur.execute(f'Update Students_database9 set {event[0]} = "no"  where Mobile_No="{oneplus}"  ')
                                        showalldata()

                                        
                                        p1.set(0)
                                        p2.set(0)
                                        p3.set(0)
                                        p4.set(0)
                                        p44.set(0)
                                        p5.set(0)
                                        p6.set(0)
                                        p7.set(0)
                                        p77.set(0)
                                        p8.set(0)
                                        p88.set(0)
                                        p888.set(0)
                                        p8888.set(0)
                                        p9.set(0)
                                        p99.set(0)
                                        p999.set(0)
                                        p10.set(0)
                                        p11.set(0)
                                        p12.set(0)
                                        p13.set(0)
                                        p14.set(0)
                                        p15.set(0)
                                        p01.config(state=NORMAL)
                                        p02.config(state=NORMAL)
                                        p03.config(state=NORMAL)
                                        p04.config(state=NORMAL)
                                        p044.config(state=NORMAL)
                                        p05.config(state=NORMAL)
                                        p06.config(state=NORMAL)
                                        p07.config(state=NORMAL)
                                        p077.config(state=NORMAL)
                                        p08.config(state=NORMAL)
                                        p088.config(state=NORMAL)
                                        p0888.config(state=NORMAL)
                                        p08888.config(state=NORMAL)
                                        p09.config(state=NORMAL)
                                        p099.config(state=NORMAL)
                                        p0999.config(state=NORMAL)
                                        p010.config(state=NORMAL)
                                        p011.config(state=NORMAL)
                                        p012.config(state=NORMAL)
                                        p013.config(state=NORMAL)
                                        p014.config(state=NORMAL)
                                        p015.config(state=NORMAL)
                                        pqr.place_forget()
                                
                                        pq.place_forget()   
                                        angelreal.configure(state=DISABLED)
                                    BC()
                                    
                                angelreal=Button(gavin,cursor='exchange',command=Eupdate,relief=RIDGE,highlightcolor='orange',highlightbackground='orange',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",text="Update",fg='black',bg='orange',height=2,width=14)
                                angelreal.place(relx=0.5,rely=0.5,anchor=CENTER)
                                
                                bc()
                                pikachu.mainloop()
                            except IndexError:
                                ''''''
                            
                                ''''''
                        preeti.bind("<ButtonRelease-1>",selector) 
                        def backbtn000():
                            ''''''
                            imraan.place_forget()
                            ved.place_forget()
                            
                            submitpass()
                            
                                                
                            pikachu.mainloop()
                            
                        ash=os.getcwd()
                        ook=ash+"//previous.png"
                        
                        photo22 = PhotoImage(file=ook)
                        moltress = Button(imraan,cursor='hand2',bd=0,highlightthickness=0,highlightbackground='black',highlightcolor='black',activebackground="orange",width=40,height=40,bg="orange",image=photo22 ,command=backbtn000)
                        moltress.place(x=1,y=1)
                        pikachu.mainloop()
                    
                    updatep=Button(yash_f,cursor='hand2',command=Pupdates,relief=RIDGE,font=("none",12),highlightcolor='orange',highlightbackground='black',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",fg='black',bg='orange',height=1,width=20)
                    updatep.place(x=20,y=467)
                    updatep.place(y=467,x=180)


                    
                    ''' INSIDE LEFT FRAME'''
                    '''FRAME FOR BUTTONS'''
                    shubham_y=Frame(yash_f,bd=0,highlightthickness=3,highlightbackground="orange",relief=RIDGE,bg="black")
                    shubham_y.place(x=10,y=510,width=480,height=70)
                    '''Inside'''
                    def clearit():
                        megapikachuz1.set('')
                        megapikachu2z2.set('')
                        megapikachu3z3.set('')
                        megapikachu4z4.set('')
                        megapikachu5z5.set('')
                        megapikachu6z6.set('')
                        __MOF__.set('')
                    def vikashit():
                        '''GETTING VALUES'''
                        fnames=megapikachuz.get()
                        fnames=fnames.upper()
                        lnames=megapikachu2z.get()
                        lnames=lnames.upper()
                        std=megapikachu3z.get()
                        std=std.upper()
                        deadspy_email=megapikachu4z.get()
                        CLG=megapikachu5z.get()
                        CLG=CLG.upper()
                        oneplus=megapikachu6z.get()
                        MF=__MOF__ .get()
                        cur.execute(f'update  Students_database9 set fName="{fnames}",lName="{lnames}",STD="{std}",Email_ID="{deadspy_email}",College_Name="{CLG}",Gender="{MF}" where Mobile_No="{oneplus}"')
                        
                        showalldata()
                        
                    
                    
                    def deletesoftskills():
                        oneplus=megapikachu6z.get()
                        
                        
                        cur.execute(f'Delete From Students_database9 where Mobile_No="{oneplus}"')
                        con.commit()
                        for i in preeti.get_children():
                            preeti.delete(i)
                        
                        showalldata()
                        
                        clearit()
                        
                    
                    neelC=Button(shubham_y,cursor='hand2',relief=RIDGE,highlightcolor='orange',highlightbackground='orange',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",text="Update",command=vikashit,fg='black',bg='orange',height=2,width=14)
                    neelC.grid(row=0,column=0,padx=10,pady=9)
                    apreetiC=Button(shubham_y,cursor='hand2',relief=RIDGE,highlightcolor='orange',highlightbackground='orange',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",text="Delete",command=deletesoftskills,fg='black',bg='orange',height=2,width=14)
                    apreetiC.grid(row=0,column=1,padx=10,pady=9)
                    omC=Button(shubham_y,cursor='hand2',relief=RIDGE,highlightcolor='orange',highlightbackground='orange',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",text="Clear",command=clearit,fg='black',bg='orange',height=2,width=14)
                    omC.grid(row=0,column=2,padx=10,pady=9)
                    ''''''
                    
                    
                    '''INSERT FRAME RIGHT'''
                    ved=Frame(pikachu,bd=1,highlightthickness=3,highlightbackground="orange",relief=RIDGE,bg="orange")
                    ved.place(height=600,y=150,x=570,width=770)
                    
                    ''''''
                    py_lb=Label(ved,text="Search By",width=9,bg='orange',fg='black',font=("Arial Black",20,"bold"))
                    py_lb.place(x=2,y=25)
                    try:
                    
                        motorola = ttk.Style()
                        

                        motorola.theme_create('ARD.TCombobox', parent='alt',
                                                settings = {'TCombobox':
                                                            {'configure':
                                                            {'selectbackground': 'orange',
                                                            'selectforeground': 'black',
                                                            'fieldbackground': 'black',
                                                            'background': 'orange'
                                                            }}}
                                                )
                        motorola.theme_use('ARD.TCombobox')
                        
                        
                    except TclError:
                        ''''''
                    try:
                    
                        
                        treestyle = ttk.Style()
                        

                        treestyle.theme_create('treestyle', parent='alt',
                                                settings = {'Treeview':
                                                            {'configure':
                                                            {'selectbackground': 'orange',
                                                            'selectforeground': 'black',
                                                            'fieldbackground': 'orange',
                                                            'background': 'orange'
                                                            }}}
                                                )
                        
                        treestyle.theme_use('treestyle') 

                    except TclError:
                        ''''''
                    
                    def showalldata():
                        
                        
                        ''''''
                        cur.execute("Select * From Students_database9")
                        rows=cur.fetchall()
                        if len(rows)!=0:
                            preeti.delete(*preeti.get_children())
                            for row in rows:
                                preeti.insert('',END,values=row)
                                con.commit()
    
                    nobody_ei=StringVar()
                    
                    
                            
                    
                    def nobody_search():
                        
                        ''''''
                        for i in preeti.get_children():
                            preeti.delete(i)
                        shm=str(nobody_ei.get())

                        try:
                            cur.execute(f'SELECT * FROM Students_database9 WHERE {shm} = "yes"  ;')
                            rows=cur.fetchall()
                            if len(rows)!=0:
                                preeti.delete(*preeti.get_children())
                                for row in rows:
                                    preeti.insert('',END,values=row)
                                    con.commit()
                        except sq.OperationalError:
                            ''''''
                    
                
                    python_select=ttk.Combobox(ved,style='ARD.TCombobox',textvariable=nobody_ei,width=18,font=("Arial Black",17,"bold"),state='readonly')
                    
                    python_select.set('SELECT EVENT')
                    # ogTuple = ('Box_Cricket','Rink_Football','Badminton','Carrom_Solo','Carrom_Duo','Table_Tennis','Chess','Counter_Strike_Five_M','Counter_Strike_Three_M','Pubg_Solo','Pubg_Squad','Pubg_TDM','Pubg_Squad_TDM','Dance_Solo','Dance_Group_Duo','Dance_Group_Squad','Fifa','Singing','Rapping','Beatboxing','Photography','Mehndi')
                    tupleTuple = ()
                    converted = list(tupleTuple)
                    for idx, event in enumerate(eventslist):
                        if event[3] == 1:
                            continue    
                        converted.append(event[0])
                    convertedTuple = tuple(converted)
                    print("this is converted tuple", convertedTuple)
                    python_select['values']=convertedTuple
                    
                    python_select.place(x=170,y=25)
                    
                    python_select.insert(0, "")
                    ash0000000=os.getcwd()
                    ookooooooo=ash0000000+"//search.png"
                    
                    photo22222222 = PhotoImage(file=ookooooooo)
                    python_omC=Button(ved,image=photo22222222,command=nobody_search,activebackground='orange',activeforeground='black',fg='black',bg='orange',height=65)
                    python_omC.place(x=490,y=3)
                    ash00000001=os.getcwd()
                    ookooooooo1=ash00000001+"//alldata.png"
                    
                    photo222222221 = PhotoImage(file=ookooooooo1)
                        
                    prashant_S=Button(ved,command=showalldata,image=photo222222221,activebackground='orange',activeforeground='black',fg='black',bg='orange')
                    prashant_S.place(x=580,y=3)
                    def pdfdn():
                        ''''''
                        syntax="select * from Students_database9"
                        cur.execute(syntax)
                        with open("vibes_offline_data_text.csv","w") as d:
                            writer = csv.writer(d, quoting=csv.QUOTE_NONNUMERIC)
                            writer.writerow(col[0] for col in cur.description)
                            for row in cur:
                                writer.writerow(row)

                        def notification():
                            ''''''
                            
                            subprocess.Popen(['wps','vibes_offline_data_text.csv']).wait()
                            notbutton.place_forget()
                        notbutton=Button(pikachu,relief=RIDGE,highlightcolor='orange',highlightbackground='black',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",fg='black',bg='orange',command=notification,text=' ⛃ Open vibes_text.csv ?',width=16,height=2)
                        notbutton.place(x=2,y=2)
                    ash000000=os.getcwd()
                    ookoooooo=ash000000+"//csv.png"
                    
                    photo2222222 = PhotoImage(file=ookoooooo)
                    pdf=Button(ved,command=pdfdn,image=photo2222222,activebackground='orange',activeforeground='black',fg='black',bg='orange')
                    pdf.place(x=670,y=3)
                    '''Table Frame'''
                    Pradeep_K=Frame(ved,bd=1,highlightthickness=3,highlightbackground="orange",relief=RIDGE,bg="black")
                    Pradeep_K.place(x=2,y=75,width=760,height=515)
                    '''ALL RECOREDS'''
                    
                    justscrollitx=Scrollbar(Pradeep_K,orient=HORIZONTAL)
                    justscrollity=Scrollbar(Pradeep_K,orient=VERTICAL)
                    preeti=ttk.Treeview(Pradeep_K,columns=('fname','lname','std','deadspy_email','CLG','oneplus','MF','Totalammo'),xscrollcommand=justscrollitx.set,yscrollcommand=justscrollity.set)
                    justscrollitx.pack(side=BOTTOM,fill=X)
                    justscrollity.pack(side=RIGHT,fill=Y)
                    justscrollitx.config(command=preeti.xview)
                    justscrollity.config(command=preeti.yview)
                    
                    preeti.heading('fname',text='First Name')
                    preeti.heading('lname',text='Last Name')
                    preeti.heading('std',text='Standard')
                    preeti.heading('deadspy_email',text='Email ID')
                    preeti.heading('CLG',text='College')
                    preeti.heading('oneplus',text='Mobile No.')
                    preeti.heading('MF',text='Gender')
                    preeti.heading('Totalammo',text='Paid Ammount')
                    
                    preeti['show']='headings'
                    preeti.column('fname',width=100)
                    preeti.column('lname',width=100)
                    preeti.column('std',width=100)
                    preeti.column('deadspy_email',width=100)
                    preeti.column('CLG',width=100)
                    preeti.column('oneplus',width=100)
                    preeti.column('MF',width=100)
                    preeti.column('Totalammo',width=100)
                    
                    preeti.pack(fill=BOTH,expand=1)
                    
                    
                    def selector1(ev):
                        select_row=preeti.focus()
                        cdata=preeti.item(select_row)
                        row=cdata['values']
                        try:
                            megapikachu6z.config(state=DISABLED)
                        
                            megapikachuz1.set(row[0])
                            megapikachu2z2.set(row[1])
                            megapikachu3z3.set(row[2])
                            megapikachu4z4.set(row[3])
                            megapikachu5z5.set(row[4])
                            megapikachu6z6.set(row[5])
                            __MOF__.set(row[6])
                            
                    
                        except IndexError:
                            ''''''
                    preeti.bind("<ButtonRelease-1>",selector1)        

                        
                        
                    

                    def hommming():
                        ''''''
                        Admin_Login_button.configure(state=NORMAL)
                        moltressx.place_forget()
                        shubham_y.place_forget()
                        yash_f.place_forget()
                        ved.place_forget()
                        Exit_button.place(x=690,y=530)
                        Edit_label_button.place(x=890,y=530)
                        Remove_label_button.place(x=880,y=310)
                        Admin_Login_button.place(x=480,y=530)
                        Vibes_Events_All_Info_button.place(x=690,y=310)
                        Vibes_Events.place(x=480,y=310)
                        About_Vibes_button.place(x=690,y=90)
                        reg_button.place(x=480,y=90)
                                                
                        Admin_label.place(x=494,y=690)
                        Remove_label.place(x=880,y=470)
                        Edit_label.place(x=890,y=530)
                        Exit_label.place(x=756,y=690)
                        Vibes_label.place(x=507,y=470)
                        eventall_label.place(x=720,y=470)
                        reg_label.place(x=515,y=250)
                        About_label.place(x=706,y=250)
                        moltresssss.place_forget()
                        Pradeep_K.place_forget()
                        
                        

                        


                    ash00000=os.getcwd()
                    ookooooo=ash00000+"//home.png"
                    
                    photo222222 = PhotoImage(file=ookooooo)
                    moltresssss = Button(pikachu,cursor='hand2',command=hommming,bd=0,bg="black",activeforeground="black",activebackground='black',image=photo222222 ,highlightthickness=0,width=73,height=65)
                    moltresssss.place(x=1289,y=62)
                      
                        
                    
                    
            
                    def backbtn9000():
                        
                        ''''''
                        pubgm.place(x=425,y=160,width=510,height=580)
                        moltressx.place_forget()
                        moltress.place(x=0,y=62)
                        moltresssss.place_forget()
                        
                        shubham_y.place_forget()
                        yash_f.place_forget()
                        ved.place_forget()
                        diglet1.set('')
                        
                        
                        

                        
                    ash=os.getcwd()
                    ook=ash+"//reply.png"
                    
                    photo22 = PhotoImage(file=ook)
                    moltressx = Button(pikachu,cursor='hand2',activeforeground="black",activebackground='black',bd=0,bg="black",image=photo22 ,highlightthickness=0,width=73,height=65,command=backbtn9000)
                    moltressx.place(x=0,y=62)
                    pikachu.mainloop()
                elif hoho=="":
                    showerror("RECHECK","Error \nPlease Enter Pass Bot!")
                else:
                    
                    showerror("RECHECK","Error \nWrong Pass Bot!")
                
            pubgm=Frame(pikachu,bd=0,highlightthickness=3,highlightcolor='orange',highlightbackground="orange",relief=RIDGE,bg="black")
            pubgm.place(x=425,y=160,width=510,height=580)
            Label(pubgm,text="Mod-Pass",font=("Arial Black",20,"bold"),bg="black",fg="black").pack()
            diglet1=StringVar()
            diglet=Entry(pubgm,textvariable=diglet1,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=1,insertbackground="orange",width=24,font=("Times New Roman",25),fg="orange",bg="black")
            diglet.config(show="*")
            diglet.place(x=43,y=360)

            diglet.insert(0,'')
            def eyes():
                ''''''
                moltresss.place_forget()
                diglet.config(show="")
                '''hide-eye'''
                def hideeye():
                    diglet.config(show="*")
                    moltressss.place_forget()
                    moltresss.place(x=419,y=363)
                ash0000=os.getcwd()
                ookoooo=ash0000+"//hide.png"
                
                photo22222 = PhotoImage(file=ookoooo)
                moltressss = Button(pubgm,cursor='hand2',activeforeground="black",activebackground='black',command=hideeye,bd=0,bg="black",image=photo22222 ,highlightthickness=0,width=33,height=36)
                moltressss.place(x=419,y=363)
                pikachu.mainloop()

            '''eye'''
            ash000=os.getcwd()
            ookooo=ash000+"//eye.png"
            
            photo2222 = PhotoImage(file=ookooo)
            moltresss = Button(pubgm,cursor='hand2',activeforeground="black",activebackground='black',command=eyes,bd=0,bg="black",image=photo2222 ,highlightthickness=0,width=33,height=36)
            moltresss.place(x=419,y=363)
            

            ''''''
            ekanas=Button(pubgm,command=submitpass,cursor='hand2',activebackground="black",highlightcolor='orange',highlightbackground='orange',highlightthickness=1,bd=0,activeforeground="orange",text="Submit",fg='black',bg='orange',height=3,width=20)
            ekanas.pack(side=BOTTOM)
            ash00=os.getcwd()
            ookoo=ash00+"//user.png"
            
            photo222 = PhotoImage(file=ookoo)
            moltress = Label(pubgm,bd=0,bg="black",image=photo222 ,highlightthickness=0,width=260,height=250)
            moltress.pack(side=TOP)
            Label(pubgm,text="Mod-Pass",font=("Arial Black",20,"bold"),bg="black",fg="black").pack()
            arbrok=Label(pubgm,text="Mod-Pass",font=("Arial Black",20,"bold"),bg="black",fg="orange")
            arbrok.pack()
            def backbtn900():
                ''''''
                
                Exit_button.place(x=690,y=530)
                Admin_Login_button.place(x=480,y=530)
                Remove_label_button.place(x=880,y=310)
                Edit_label_button.place(x=890,y=530)
                Vibes_Events_All_Info_button.place(x=690,y=310)
                Vibes_Events.place(x=480,y=310)
                About_Vibes_button.place(x=690,y=90)
                reg_button.place(x=480,y=90)
                Admin_label.place(x=494,y=690)
                Remove_label.place(x=880,y=470)
                Edit_label.place(x=890,y=530)

                Exit_label.place(x=756,y=690)
                Vibes_label.place(x=507,y=470)
                eventall_label.place(x=720,y=470)
                reg_label.place(x=515,y=250)
                About_label.place(x=706,y=250)
                ekanas.place_forget()
                diglet.place_forget()
                moltress.place_forget()
                arbrok.place_forget()
                pubgm.place_forget()
                
            ash=os.getcwd()
            ook=ash+"//reply.png"
            
            photo22 = PhotoImage(file=ook)
            moltress = Button(pikachu,cursor='hand2',highlightthickness=0,activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,command=backbtn900)
            moltress.place(x=0,y=62)
            pikachu.mainloop()
        admin=os.getcwd()
        admin2=admin+"//hacker.png"
        
        photoA = PhotoImage(file=admin2) 


        
        Admin_Login_button=Button(pikachu,cursor='hand2',bd=0,highlightthickness=2,highlightbackground='orange',highlightcolor='orange',activebackground="black",image=photoA,width=170,height=170,bg="black",command=Admin_Login_button_5)
        Admin_Login_button.place(x=480,y=530)

        Admin_label=Label(pikachu,font=("Times",20,"bold"),text='Admin-Log-In',bd=0,highlightthickness=0,bg='black',fg='orange')
        Admin_label.place(x=494,y=690)
        
        def Exit_button_6():
            
            '''Button 6 Functions The following Program '''
            pikachu.destroy()
           
            exit()

        def Remove_Events_8():
            '''Button 7 Functions The following Program '''
        
            reg_button.place_forget()
            About_Vibes_button.place_forget()
            Vibes_Events.place_forget()
            Edit_label_button.place_forget()
            Edit_label.place_forget()
            Vibes_Events_All_Info_button.place_forget()
            Remove_label_button.place_forget()
            Admin_Login_button.place_forget()
            Exit_button.place_forget()
            Admin_label.place_forget()
            Exit_label.place_forget()
            Vibes_label.place_forget()
            reg_label.place_forget()
            eventall_label.place_forget()
            About_label.place_forget()
            Remove_label.place_forget()

            def submitpass():
                ''''''
                hoho=diglet1.get()
                
                if hoho=="admin":
                     
                    pubgm.place_forget()
                    moltress.place_forget()

                    def pokeball():  

                        # TotalSum = []                                                                                                                  

                        def BC():
                        
                            
                            
                            for idx,event in enumerate(eventslist):
                                print("eventVariable index:", idx)
                                print("eventVariable value:", eventVariable)
                                if event[3] == 1:
                                    continue
                                brock=eventVariable[idx].get()  

                                if brock == 1:
                                    ''''''
                                    
                                    # cur.execute(f'delete from New_Events_list9 where EventName="{event[0]}"  ')
                                    cur.execute(f'Update New_Events_list9 set deleted=1 where EventName="{event[0]}"  ')
                                    # cur.execute(f'Update Students_database9 set {event[0]} = "no"  where Mobile_No="{oneplus}"  ')
                                    # cur.execute('delete from Students_database9 where EventName={event[0]}  ')
                                    # cur.execute(f'Delete From Students_database9 where Mobile_No="{oneplus}"')
                                    
                                    print(event)
                                    # TotalSum.append(event[1])

                                    

                                else:
                                    pass
                                    # cur.execute(f'Update Students_database9 set {event[0]} = "no"  where Mobile_No="{oneplus}"  ')
                                
                                
                                # RF()
                                # BD()
                                # CRS()
                                # CRD()
                                # TT()
                                # CSS()
                                # CT5()
                                # CT3()
                                # PGS()
                                # PGD()
                                # PGT()
                                # PGST()
                                # DCS()
                                # DSD()
                                # DSG()
                                # SG()
                                # FF()
                                # RP()
                                # BTBX()
                                # PGY()
                                # MDI()
                                # Elist()
                                
                                # cur.execute(f'Update Students_database9 set Totalammo = "{bj}"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                bj=5
                                dialga=""
                                # print("total amount 2")
                                # MEGA_ARCEUS=Label(pikachu,text=dialga,width=30,bg='blue',fg='yellow',font=("Times",50,"bold"))
                                # MEGA_ARCEUS.place(x=0,y=360)

                                ''''''
                                def hommming11():
                                    ''''''
                                    reg_button.configure(state=NORMAL)
                                    # RB1.place_forget()
                                    # RB2.place_forget()
                                    zapados.place_forget()
                                    
                                    
                                    Exit_button.place(x=690,y=530)
                                    Admin_Login_button.place(x=480,y=530)
                                    Remove_label_button.place(x=880,y=310)
                                    Edit_label_button.place(x=890,y=530)

                                    Vibes_Events_All_Info_button.place(x=690,y=310)
                                    Vibes_Events.place(x=480,y=310)
                                    About_Vibes_button.place(x=690,y=90)
                                    reg_button.place(x=480,y=90)

                                    ''''''
                                    Admin_label.place(x=494,y=690)
                                    Remove_label.place(x=880,y=470)
                                    Edit_label.place(x=890,y=530)
                                    Exit_label.place(x=756,y=690)
                                    Vibes_label.place(x=507,y=470)
                                    eventall_label.place(x=720,y=470)
                                    reg_label.place(x=515,y=250)
                                    About_label.place(x=706,y=250)


                                    ''''''
                                    MEGA_ARCEUS.place_forget()
                                    moltress.place_forget()
                                    moltresssssssp.place_forget()
                                    pikachu.mainloop()
                                    

                                ash000000=os.getcwd()
                                ookoooooo=ash000000+"//home.png"
                                
                                photo2222222 = PhotoImage(file=ookoooooo)
                                moltresssssssp = Button(pikachu,cursor='hand2',command=hommming11,bd=0,bg="black",activeforeground="orange",activebackground='black',image=photo2222222 ,width=73,height=65,highlightthickness=0)
                                moltresssssssp.place(x=1289,y=62)
                                ''''''

                                ''''''    
                                MEGA_ARCEUS=Label(pikachu,text=dialga,width=30,bg='orange',fg='black',font=("Arial Black",50,"bold"))
                                MEGA_ARCEUS.place(x=0,y=360)
                                arceus.place_forget()                                                                                                                                                                                                                            
                                def backbtn000():
                                    reg_button.configure(state=NORMAL)
                                    ''''''
                                    moltresssssssp.place_forget()

                                    ''''''
                                    ''''''
                                    MEGA_ARCEUS.place_forget()
                                    ''''''
                                    moltress.place_forget()
                                    pikachu.mainloop()
                                    
                                ash=os.getcwd()
                                ook=ash+"//reply.png"
                                
                                photo22 = PhotoImage(file=ook)
                                moltress = Button(pikachu,cursor='hand2',highlightthickness=0,activeforeground="black",activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,command=backbtn000)
                                moltress.place(x=0,y=62)
                                
                                pikachu.mainloop()
                                
                                
                                                


                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Box_Cricket = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                RF()
                                BD()
                                CRS()
                                CRD()
                                TT()
                                CSS()
                                CT5()
                                CT3()
                                PGS()
                                PGD()
                                PGT()
                                PGST()
                                DCS()
                                DSD()
                                DSG()
                                SG()
                                FF()
                                RP()
                                BTBX()
                                PGY()
                                MDI()
                                Elist()
                                # pl7.place_forget()
                                # bj=sum(TotalSum)

                                cur.execute(f'Update Students_database9 set Totalammo = "{bj}"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                print("total amount1")
                                # dialga="Total Amount = RS."+str(bj)
                                def hommming2():
                                    ''''''
                                    reg_button.configure(state=NORMAL)
                                    # RB1.place_forget()
                                    # RB2.place_forget()
                                    zapados.place_forget()
                                    
                                    Admin_label.place(x=494,y=690)
                                    Remove_label.place(x=880,y=470)
                                    Edit_label.place(x=890,y=530)
                                    Exit_label.place(x=756,y=690)
                                    Vibes_label.place(x=507,y=470)
                                    eventall_label.place(x=720,y=470)
                                    reg_label.place(x=515,y=250)
                                    About_label.place(x=706,y=250)
                                    MEGA_ARCEUS.place_forget()
                                    moltress0.place_forget()


                                    Exit_button.place(x=690,y=530)
                                    Admin_Login_button.place(x=480,y=530)
                                    Remove_label_button.place(x=880,y=310)
                                    Edit_label_button.place(x=890,y=530)
                                    Vibes_Events_All_Info_button.place(x=690,y=310)
                                    Vibes_Events.place(x=480,y=310)
                                    About_Vibes_button.place(x=690,y=90)
                                    reg_button.place(x=480,y=90)

                                    
                                    moltressssss.place_forget()
                                    pikachu.mainloop()

                                ash000000=os.getcwd()
                                ookoooooo=ash000000+"//home.png"
                                
                                photo2222222 = PhotoImage(file=ookoooooo)
                                moltressssss = Button(pikachu,cursor='hand2',command=hommming2,bd=0,bg="black",activeforeground="orange",activebackground='black',image=photo2222222 ,highlightthickness=0,width=73,height=65)
                                moltressssss.place(x=1289,y=62)
                                ''''''
                                ''''''
                                ll1.place_forget()
                                # pl9.place_forget()
                                # pl8.place_forget()
                                # pl7.place_forget
                                # pl4.place_forget()


                                ''''''
                                

                                # mega.place_forget()
                                # megapikachu.place_forget()
                                # mega2.place_forget()
                                # megapikachu2.place_forget()
                                # mega3.place_forget()
                                # megapikachu3.place_forget()
                                # mega4.place_forget()
                                # megapikachu4.place_forget()
                                # mega5.place_forget()
                                # megapikachu5.place_forget()
                                # mega6.place_forget()
                                # megapikachu6.place_forget()
                                # mega7.place_forget()



                                MEGA_ARCEUS=Label(pikachu,text=dialga,width=30,bg='orange',fg='black',font=("Arial Black",50,"bold"))
                                MEGA_ARCEUS.place(x=0,y=360)
                                arceus.place_forget()
                                ''''''
                                # p01.place_forget()
                                # p02.place_forget()
                                # p03.place_forget()
                                # p04.place_forget()
                                # p044.place_forget()
                                # p05.place_forget()
                                # p06.place_forget()
                                # p07.place_forget()
                                # p077.place_forget()
                                # p08.place_forget()
                                # p088.place_forget()
                                # p0888.place_forget()
                                # p08888.place_forget()
                                # p09.place_forget()
                                # p099.place_forget()
                                # p0999.place_forget()
                                # p010.place_forget()
                                # p011.place_forget()
                                # p012.place_forget() 
                                # p013.place_forget()
                                # p014.place_forget()
                                # p015.place_forget()
                                for idx, event in enumerate(eventslist):
                                    eventsCheck[idx].place_forget()
                                
                                
                                
                                def backbtn0001():
                                    ''''''
                                    reg_button.configure(state=NORMAL)
                                    arceus.configure(state=NORMAL)
                                    # megapikachu0.set('')
                                    # megapikachu20.set('')
                                    # megapikachu30.set('')
                                    # megapikachu40.set('')
                                    # megapikachu50.set('')
                                    # megapikachu60.set('')
                                    # __MOF__.set('')
                                    p1.set(0)
                                    p2.set(0)
                                    p3.set(0)
                                    p4.set(0)
                                    p5.set(0)
                                    p6.set(0)
                                    p7.set(0)
                                    p8.set(0)
                                    p9.set(0)
                                    p10.set(0)
                                    p11.set(0)
                                    p12.set(0)
                                    p13.set(0)
                                    p14.set(0)
                                    p15.set(0)
                                    p44.set(0)
                                    p77.set(0)
                                    p88.set(0)
                                    p888.set(0)
                                    p8888.set(0)
                                    p99.set(0)
                                    p999.set(0)
                                    ''''''
                                    moltressssss.place_forget()
                                    moltress0.place_forget()

                                    # RB1.place(y=391,x=225)
                                    # RB2.place(y=391,x=300)
                                    
                                    ll1.place(x = 800, y = 115) 
                                    # pl9.place(x = 820, y = 310)
                                    # pl8.place(x = 820, y = 290)
                                    # pl7.place(x = 820, y = 270)
                                    # pl4.place(x = 820, y = 210)

                                    ''''''
                                    # mega.place(x=110,y=150)
                                    # megapikachu.place(x=240,y=151)
                                    # mega2.place(x=450,y=150)
                                    # megapikachu2.place(x=580,y=151)
                                    # mega3.place(x=110,y=230)
                                    # megapikachu3.place(x=240,y=231)
                                    # mega4.place(x=450,y=230)
                                    # megapikachu4.place(x=580,y=231)
                                    # mega5.place(x=110,y=310)
                                    # megapikachu5.place(x=240,y=311)
                                    # mega6.place(x=450,y=310)
                                    # megapikachu6.place(x=580,y=311)
                                    # mega7.place(x=110,y=390)
                                    ''''''
                                    MEGA_ARCEUS.place_forget()

                                    
                                    ''''''
                                    arceus.place(x=600,y=640)
                                    ''''''
                                    # p01.place(x = 800, y = 150)
                                    # p02.place(x = 800, y = 170)
                                    # p03.place(x = 800, y = 190)
                                    # p04.place(x = 960, y = 210)
                                    # p044.place(x = 1020, y = 210)
                                    # p05.place(x = 800, y = 230)
                                    # p06.place(x = 800, y = 250)
                                    # p07.place(x = 960, y = 270)
                                    # p077.place(x = 1020, y = 270)
                                    # p08.place(x = 960, y = 290)
                                    # p088.place(x = 1020, y = 290)
                                    # p0888.place(x = 1100, y = 290)
                                    # p08888.place(x = 1170, y = 290) 
                                    # p09.place(x = 960, y = 310) 
                                    # p099.place(x = 1020, y = 310) 
                                    # p0999.place(x = 1100, y = 310)
                                    # p010.place(x = 800, y = 330)
                                    # p011.place(x = 800, y = 350)
                                    # p012.place(x = 800, y = 370) 
                                    # p013.place(x = 800, y = 390)
                                    # p014.place(x = 800, y = 410) 
                                    # p015.place(x = 800, y = 430)
                                    pikachu.mainloop()

                                ash=os.getcwd()
                                ook=ash+"//reply.png"
                                
                                photo22 = PhotoImage(file=ook)
                                moltress0 = Button(pikachu,cursor='hand2',activeforeground="black",activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,highlightthickness=0,command=backbtn0001)
                                moltress0.place(x=0,y=62)
                                
                                pikachu.mainloop()
                                
                        def RF():
                            brock=p2.get()  

                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Rink_Football = "yes"  where Mobile_No="{oneplus}"  ')
                                
                                
                                # TotalSum.append(p2p)
                                

                            else:
                                cur.execute(f'Update Students_database9 set Rink_Football = "no"  where Mobile_No="{oneplus}"  ')
                                ''''''
                                
                        def Elist():
                            for idx,event in enumerate(eventslist):
                                brock=eventVariable[idx].get()  

                                if brock == 1:
                                    ''''''
                                    
                                    cur.execute(f'Update Students_database9 set {event[0]} = "yes"  where Mobile_No="{oneplus}"  ')
                                    
                                    print(event)
                                    # TotalSum.append(event[1])

                                    

                                else:
                                    cur.execute(f'Update Students_database9 set {event[0]} = "no"  where Mobile_No="{oneplus}"  ')



                        def BD():
                            brock=p3.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Badminton = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()

                                # TotalSum.append(p3p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Badminton = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def CRS():
                            brock=p4.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Carrom_Solo = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p4p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Carrom_Solo = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def CRD():
                            brock=p44.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Carrom_Duo = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p44p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Carrom_Duo = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def TT():
                            brock=p5.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Table_Tennis = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p5p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Table_Tennis = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def CSS():
                            brock=p6.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Chess = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p6p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Chess = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def CT5():
                            brock=p7.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Counter_Strike_Five_M = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p7p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Counter_Strike_Five_M = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def CT3():
                            brock=p77.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Counter_Strike_Three_M = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p77p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Counter_Strike_Three_M = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def PGS():
                            brock=p8.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Pubg_Solo = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p8p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Pubg_Solo = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def PGD():
                            brock=p88.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Pubg_Squad = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p88p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Pubg_Squad = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def PGT():
                            brock=p888.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Pubg_TDM = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p888p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Pubg_TDM = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def PGST():
                            brock=p8888.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Pubg_Squad_TDM = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p8888p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Pubg_Squad_TDM = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def DCS():
                            brock=p9.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Dance_Solo = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p9p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Dance_Solo = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def DSD():
                            brock=p99.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Dance_Group_Duo = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p99p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Dance_Group_Duo = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def DSG():
                            brock=p999.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Dance_Group_Squad = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p999p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Dance_Group_Squad = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def FF():
                            brock=p10.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Fifa = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p10p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Fifa = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def SG():
                            brock=p11.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Singing = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p11p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Singing = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def RP():
                            brock=p12.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Rapping = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p12p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Rapping = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def BTBX():
                            brock=p13.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Beatboxing = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p13p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Beatboxing = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def PGY():
                            brock=p14.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Photography = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p14p)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Photography = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        def MDI():
                            brock=p15.get()
                            if brock == 1:
                                ''''''
                                
                                cur.execute(f'Update Students_database9 set Mehndi = "yes"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                TotalSum.append(p15p)
                                bj=sum(TotalSum)
                                

                            else:
                                ''''''
                                cur.execute(f'Update Students_database9 set Mehndi = "no"  where Mobile_No="{oneplus}"  ')
                                con.commit()
                                
                        BC()
                
                    '''Check Boxes'''
                    '''label for that''' 
                    ll1=Label(pikachu, text ='Select Events To Remove',font=("Arial Black",13),bg="orange",fg="black")
                    ll1.place(x = 800, y = 115) 
                    
                        
                    '''check buttons '''
                    p1=IntVar()
                    p2=IntVar()
                    p3=IntVar()
                    p4=IntVar()
                    p5=IntVar()
                    p6=IntVar()
                    p7=IntVar()
                    p8=IntVar()
                    p9=IntVar()
                    p10=IntVar()
                    p11=IntVar()
                    p12=IntVar()
                    p13=IntVar()
                    p14=IntVar()
                    p15=IntVar()
                    p44=IntVar()
                    p77=IntVar()
                    p88=IntVar()
                    p888=IntVar()
                    p8888=IntVar()
                    p99=IntVar()
                    p999=IntVar()                                                                                
                    
                    # p01=Checkbutton(pikachu,variable=p1, text ='BOX CRICKET',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p01.place(x = 800, y = 150)
                    
                    # p1p=550
                    # p02=Checkbutton(pikachu,variable=p2, text ='RINK FOOTBALL',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p02.place(x = 800, y = 170) 
                    # p2p=450
                    # p03=Checkbutton(pikachu,variable=p3, text ='BADMINTON',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p03.place(x = 800, y = 190) 
                    # p3p=50
                    # pl4 = Label(pikachu, text ='CARROM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
                    # pl4.place(x = 820, y = 210) 
                    # p04=Checkbutton(pikachu,variable=p4, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p04.place(x = 960, y = 210) 
                    # p4p=50
                    # p044=Checkbutton(pikachu,variable=p44, text ='Duo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p044.place(x = 1020, y = 210) 
                    # p44p=100
                    # p05=Checkbutton(pikachu,variable=p5, text ='TABLE TENNIS',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p05.place(x = 800, y = 230) 
                    # p5p=50


                    # p06=Checkbutton(pikachu,variable=p6, text ='CHESS',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p06.place(x = 800, y = 250) 
                    # p6p=50
                    # pl7 = Label(pikachu, text ='COUNTER STRIKE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
                    # pl7.place(x = 820, y = 270) 
                    # p07=Checkbutton(pikachu,variable=p7, text ='5(S)',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p07.place(x = 960, y = 270) 
                    # p7p=250
                    # p077=Checkbutton(pikachu,variable=p77, text ='3(S)',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p077.place(x = 1020, y = 270) 
                    # p77p=150

                    # pl8 = Label(pikachu, text ='PUBG MOBILE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
                    # pl8.place(x = 820, y = 290) 
                                    
                    # p08=Checkbutton(pikachu,variable=p8, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p08.place(x = 960, y = 290) 
                    # p8p=50
                    # p088=Checkbutton(pikachu,variable=p88, text ='Squad',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p088.place(x = 1020, y = 290) 
                    # p88p=200
                    # p0888=Checkbutton(pikachu,variable=p888, text ='TDM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p0888.place(x = 1100, y = 290) 
                    # p888p=200
                    # p08888=Checkbutton(pikachu,variable=p8888, text ='Squad + TDM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p08888.place(x = 1170, y = 290) 
                    # p8888p=320
                    # pl9 = Label(pikachu, text ='DANCE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
                    # pl9.place(x = 820, y = 310) 
                    # p09=Checkbutton(pikachu,variable=p9, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p09.place(x = 960, y = 310) 
                    # p9p=100
                    # p099=Checkbutton(pikachu,variable=p99, text ='Duo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p099.place(x = 1020, y = 310) 
                    # p99p=200
                    # p0999=Checkbutton(pikachu,variable=p999, text ='Group',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p0999.place(x = 1100, y = 310) 
                    
                    # p999p=400
                    # p010=Checkbutton(pikachu,variable=p10, text ='FIFA',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p010.place(x = 800, y = 330) 
                    # p10p=50
                    # p011=Checkbutton(pikachu,variable=p11, text ='SINGING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p011.place(x = 800, y = 350) 
                    # p11p=100
                    # p012=Checkbutton(pikachu,variable=p12, text ='RAPPING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p012.place(x = 800, y = 370) 
                    # p12p=100
                    # p013=Checkbutton(pikachu,variable=p13, text ='BEATBOXING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p013.place(x = 800, y = 390) 
                    # p13p=100
                    # p014=Checkbutton(pikachu,variable=p14, text ='PHOTOGRAPHY',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p014.place(x = 800, y = 410) 
                    # p14p=50
                    # p015=Checkbutton(pikachu,variable=p15, text ='MEHNDI',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                    #                 takefocus = 0)
                    # p015.place(x = 800, y = 430) 
                    # p15p=20
                    y=130
                    for idx, event in enumerate(eventslist):
                        if event[3] == 1:
                            continue
                        eventVariable[idx]=IntVar()
                        y=y+20
                        eventsCheck[idx]=Checkbutton(pikachu,variable=eventVariable[idx], text =event[0],font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="black", 
                                    takefocus = 0)
                        eventsCheck[idx].place(x=800,y=y)
                    

                    arceus=Button(pikachu,command=pokeball,state=NORMAL,activebackground="black",border=0,activeforeground="orange",text="Ssubmit",fg='black',bg='orange',height=3,width=16)
                    arceus.place(x=600,y=640)

                    def backbtn10():
                        '''''' 
                        arceus.configure(state=NORMAL)
                        ll1.place_forget()
                        # pl9.place_forget()
                        # pl8.place_forget()
                        # pl7.place_forget()
                        # pl4.place_forget()
                        Admin_label.place(x=494,y=690)
                        Remove_label.place(x=880,y=470)
                        Exit_label.place(x=756,y=690)
                        Edit_label.place(x=890,y=690)
                        Vibes_label.place(x=507,y=470)
                        eventall_label.place(x=720,y=470)
                        reg_label.place(x=515,y=250)
                        About_label.place(x=706,y=250)

                        ''''''
                        arceus.place_forget()
                        ''''''
                        Exit_button.place(x=690,y=530)
                        Remove_label_button.place(x=880,y=310)
                        Admin_Login_button.place(x=480,y=530)
                        Edit_label_button.place(x=890,y=530)
                        Vibes_Events_All_Info_button.place(x=690,y=310)
                        Vibes_Events.place(x=480,y=310)
                        About_Vibes_button.place(x=690,y=90)
                        reg_button.place(x=480,y=90)

                        ''''''
                        # p01.place_forget()
                        # p02.place_forget()
                        # p03.place_forget()
                        # p04.place_forget()
                        # p044.place_forget()
                        # p05.place_forget()
                        # p06.place_forget()
                        # p07.place_forget()
                        # p077.place_forget()
                        # p08.place_forget()
                        # p088.place_forget()
                        # p0888.place_forget()
                        # p08888.place_forget()
                        # p09.place_forget()
                        # p099.place_forget()
                        # p0999.place_forget()
                        # p010.place_forget()
                        # p011.place_forget()
                        # p012.place_forget() 
                        # p013.place_forget()
                        # p014.place_forget()
                        # p015.place_forget()
                        for idx, event in enumerate(eventslist):
                            if event[3] == 1:
                                continue  
                            eventsCheck[idx].place_forget()
                        ''''''
                        zapados.place_forget()
                    ash=os.getcwd()
                    ook=ash+"//reply.png"
                    
                    photo22 = PhotoImage(file=ook)
                    


                    zapados = Button(pikachu,cursor='hand2',activeforeground="black",activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,highlightthickness=0,command=backbtn10)
                    zapados.place(x=0,y=62)
                    pikachu.mainloop()
                elif hoho=="":
                    showerror("RECHECK","Error \nPlease Enter Pass Bot!")
                else:                    
                    showerror("RECHECK","Error \nWrong Pass Bot!")
                            
            pubgm=Frame(pikachu,bd=0,highlightthickness=3,highlightcolor='orange',highlightbackground="orange",relief=RIDGE,bg="black")
            pubgm.place(x=425,y=160,width=510,height=580)
            Label(pubgm,text="Mod-Pass",font=("Arial Black",20,"bold"),bg="black",fg="black").pack()
            diglet1=StringVar()
            diglet=Entry(pubgm,textvariable=diglet1,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=1,insertbackground="orange",width=24,font=("Times New Roman",25),fg="orange",bg="black")
            diglet.config(show="*")
            diglet.place(x=43,y=360)

            diglet.insert(0,'')
            def eyes():
                ''''''
                moltresss.place_forget()
                diglet.config(show="")
                '''hide-eye'''
                def hideeye():
                    diglet.config(show="*")
                    moltressss.place_forget()
                    moltresss.place(x=419,y=363)
                ash0000=os.getcwd()
                ookoooo=ash0000+"//hide.png"
                
                photo22222 = PhotoImage(file=ookoooo)
                moltressss = Button(pubgm,cursor='hand2',activeforeground="black",activebackground='black',command=hideeye,bd=0,bg="black",image=photo22222 ,highlightthickness=0,width=33,height=36)
                moltressss.place(x=419,y=363)
                pikachu.mainloop()

            '''eye'''
            ash000=os.getcwd()
            ookooo=ash000+"//eye.png"
            
            photo2222 = PhotoImage(file=ookooo)
            moltresss = Button(pubgm,cursor='hand2',activeforeground="black",activebackground='black',command=eyes,bd=0,bg="black",image=photo2222 ,highlightthickness=0,width=33,height=36)
            moltresss.place(x=419,y=363)
            

            ''''''
            ekanas=Button(pubgm,command=submitpass,cursor='hand2',activebackground="black",highlightcolor='orange',highlightbackground='orange',highlightthickness=1,bd=0,activeforeground="orange",text="LogIn",fg='black',bg='orange',height=3,width=20)
            ekanas.pack(side=BOTTOM)
            ash00=os.getcwd()
            ookoo=ash00+"//user.png"
            
            photo222 = PhotoImage(file=ookoo)
            moltress = Label(pubgm,bd=0,bg="black",image=photo222 ,highlightthickness=0,width=260,height=250)
            moltress.pack(side=TOP)
            Label(pubgm,text="Mod-Pass",font=("Arial Black",20,"bold"),bg="black",fg="black").pack()
            arbrok=Label(pubgm,text="Mod-Pass",font=("Arial Black",20,"bold"),bg="black",fg="orange")
            arbrok.pack()
            def backbtn900():
                ''''''
                
                Exit_button.place(x=690,y=530)
                Remove_label_button.place(x=880,y=310)
                Admin_Login_button.place(x=480,y=530)
                Edit_label_button.place(x=890,y=530)
                Vibes_Events_All_Info_button.place(x=690,y=310)
                Vibes_Events.place(x=480,y=310)
                About_Vibes_button.place(x=690,y=90)
                reg_button.place(x=480,y=90)
                Edit_label.place(x=890,y=530)
                Admin_label.place(x=494,y=690)
                Remove_label.place(x=880,y=470)
                Exit_label.place(x=756,y=690)
                Vibes_label.place(x=507,y=470)
                eventall_label.place(x=720,y=470)
                reg_label.place(x=515,y=250)
                About_label.place(x=706,y=250)
                ekanas.place_forget()
                diglet.place_forget()
                moltress.place_forget()
                arbrok.place_forget()
                pubgm.place_forget()
                
            ash=os.getcwd()
            ook=ash+"//reply.png"
            
            photo22 = PhotoImage(file=ook)
            moltress = Button(pikachu,cursor='hand2',highlightthickness=0,activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,command=backbtn900)
            moltress.place(x=0,y=62)
            pikachu.mainloop()

        def Edit_Events_7():
            '''Button 7 Functions The following Program '''
        
            reg_button.place_forget()
            About_Vibes_button.place_forget()
            Vibes_Events.place_forget()
            Edit_label_button.place_forget()
            Edit_label.place_forget()
            Vibes_Events_All_Info_button.place_forget()
            Remove_label_button.place_forget()
            Admin_Login_button.place_forget()
            Exit_button.place_forget()
            Admin_label.place_forget()
            Exit_label.place_forget()
            Vibes_label.place_forget()
            reg_label.place_forget()
            eventall_label.place_forget()
            About_label.place_forget()
            Remove_label.place_forget()
            def submitpass():
                ''''''
                hoho=diglet1.get()
                
                if hoho=="admin":
                     
                    pubgm.place_forget()
                    moltress.place_forget()
                    
                    '''INSERT FRAME LEFT'''
                    yash_f=Frame(pikachu,bd=1,highlightthickness=3,highlightbackground="orange",relief=SUNKEN,bg="orange")
                    yash_f.place(x=20,y=150,width=510,height=600)
                    ''''''
                    rock=Label(yash_f,text="Registered Data",width=13,bg='orange',fg='black',font=("Arial Black",25,"bold"))
                    rock.pack(side=TOP,fill=X)
                    




                    '''VAR'''
                    megapikachuz1=StringVar()
                    megapikachu2z2=StringVar()
                    megapikachu3z3=StringVar()
                    megapikachu4z4=StringVar()
                    megapikachu5z5=StringVar()
                    megapikachu6z6=StringVar()
                    __MOF__ = StringVar()
                    '''Event Name'''
                    megaz=Label(yash_f,text="Event Name",bg='orange',fg='black',font=("Arial Black",18,"bold"))
                    megaz.place(x=20,y=70)
                    megapikachuz=Entry(yash_f,textvariable=megapikachuz1,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=25,font=("Times New Roman",14),fg="orange",bg="black")
                    megapikachuz.place(x=190,y=71)
                    megapikachuz.insert(0,'')
                    '''Fees'''
                    mega6z=Label(yash_f,text="Fees",bg='orange',fg='black',font=("Arial Black",18,"bold"))
                    mega6z.place(x=20,y=130)
                    megapikachu6z=Entry(yash_f,textvariable=megapikachu6z6,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=25,font=("Times New Roman",14),fg="orange",bg="black")
                    megapikachu6z.place(x=190,y=131)

                    megapikachu6z.insert(0,'')
                    '''Standard '''
                    mega3z=Label(yash_f,text="Participants",bg='orange',fg='black',font=("Arial Black",18,"bold"))
                    mega3z.place(x=20,y=190)
                    megapikachu3z=Entry(yash_f,textvariable=megapikachu3z3,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=2,insertbackground="orange",width=25,font=("Times New Roman",14),fg="orange",bg="black")
                    megapikachu3z.place(x=190,y=191)
                    megapikachu3z.insert(0,'')
                    
                    # pupdate=Label(yash_f,text="To Participate2\nIn Other Events",width=13,bg='orange',fg='black',font=("none",12))
                    def Pupdates():
                        """ Pradeep_K.place_forget()
                        Pradeep_K.place(x=2,y=40,width=760,height=530) """
                        moltresssss.place_forget()
                        
                        
                        #moltresssss.place_forget()
                        moltressx.place_forget()
                        yash_f.place_forget()
                        neelC.grid_forget()
                        apreetiC.grid_forget()
                        omC.grid_forget()

                        imraan=Frame(pikachu,bd=1,highlightthickness=3,highlightbackground="orange",relief=RIDGE,bg="orange")
                        imraan.place(x=20,y=150,width=510,height=600)
                        
                        '''Check Boxes'''
                        '''label for that''' 
                        ll1=Label(imraan, text ='Select Event To Participate',font=("Arial Black",14,'bold'),bg="orange",fg="black")
                        ll1.pack(side=TOP,fill=X) 
                        
                            
                        '''check buttons '''
                        p1=IntVar()
                        p2=IntVar()
                        p3=IntVar()
                        p4=IntVar()
                        p5=IntVar()
                        p6=IntVar()
                        p7=IntVar()
                        p8=IntVar()
                        p9=IntVar()
                        p10=IntVar()
                        p11=IntVar()
                        p12=IntVar()
                        p13=IntVar()
                        p14=IntVar()
                        p15=IntVar()
                        p44=IntVar()
                        p77=IntVar()
                        p88=IntVar()
                        p888=IntVar()
                        p8888=IntVar()
                        p99=IntVar()
                        p999=IntVar()

                        ''''''
                        pqrs=Label(imraan,text='F-Name : ',bg='orange',font=("Arial Black",10,"bold"),fg='black',width=8,bd=0,highlightthickness=1,highlightcolor='black')
                        pqrst=Label(imraan,text='Mobile-No : ',bg='orange',font=("Arial Black",10,"bold"),fg='black',width=10,bd=0,highlightthickness=1,highlightcolor='black')
                        pqrs.place(x=5,y=70)
                        pqrst.place(x=250,y=70)

                        ''''''
                        
                        p01=Checkbutton(imraan,variable=p1,text ='BOX CRICKET',font=("Arial Black",9,"bold"),highlightcolor='orange',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p01.place(x = 10, y = 100)
                        
                        p1p=550
                        p02=Checkbutton(imraan,variable=p2, text ='RINK FOOTBALL',font=("Arial Black",9,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p02.place(x = 190, y = 100) 
                        p2p=450
                        p03=Checkbutton(imraan,variable=p3, text ='BADMINTON',font=("Arial Black",9,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p03.place(x = 390, y = 100) 
                        p3p=50
                        pl4 = Label(imraan, text ='CARROM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='orange',highlightthickness=1,bd=1 )
                        pl4.place(x = 0, y = 150) 
                        p04=Checkbutton(imraan,variable=p4, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p04.place(x = 190, y = 150) 
                        p4p=50
                        p044=Checkbutton(imraan,variable=p44, text ='Duo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p044.place(x = 280, y = 150) 
                        p44p=100
                        p05=Checkbutton(imraan,variable=p5, text ='TABLE TENNIS',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p05.place(x = 10, y = 200) 
                        p5p=50


                        p06=Checkbutton(imraan,variable=p6, text ='CHESS',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p06.place(x = 190, y = 200) 
                        p6p=50
                        pl7 = Label(imraan, text ='COUNTER STRIKE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
                        pl7.place(x = 0, y = 250) 
                        p07=Checkbutton(imraan,variable=p7, text ='5-Members(S)',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p07.place(x = 160, y = 250) 
                        p7p=250
                        p077=Checkbutton(imraan,variable=p77, text ='3-Members(S)',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p077.place(x = 310, y = 250) 
                        p77p=150

                        pl8 = Label(imraan, text ='PUBG MOBILE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='black',highlightthickness=1,bd=1 )
                        pl8.place(x = 0, y = 300) 
                                        
                        p08=Checkbutton(imraan,variable=p8, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p08.place(x = 120, y = 300) 
                        p8p=50
                        p088=Checkbutton(imraan,variable=p88, text ='Squad',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p088.place(x = 190, y = 300) 
                        p88p=200
                        p0888=Checkbutton(imraan,variable=p888, text ='TDM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p0888.place(x = 280, y = 300) 
                        p888p=200
                        p08888=Checkbutton(imraan,variable=p8888, text ='Squad + TDM',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p08888.place(x = 350, y = 300) 
                        p8888p=320
                        pl9 = Label(imraan, text ='DANCE',font=("Arial Black",10,"bold"),highlightcolor='black',fg="orange",bg='black',highlightbackground='orange',highlightthickness=1,bd=1 )
                        pl9.place(x = 0, y = 350) 
                        p09=Checkbutton(imraan,variable=p9, text ='Solo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p09.place(x = 190, y = 350) 
                        p9p=100
                        p099=Checkbutton(imraan,variable=p99, text ='Duo',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p099.place(x = 280, y = 350) 
                        p99p=200
                        p0999=Checkbutton(imraan,variable=p999, text ='Group',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p0999.place(x = 370, y = 350) 
                        
                        p999p=400
                        p010=Checkbutton(imraan,variable=p10, text ='FIFA',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p010.place(x = 10, y = 400) 
                        p10p=50
                        p011=Checkbutton(imraan,variable=p11, text ='SINGING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p011.place(x = 190, y =400) 
                        p11p=100
                        p012=Checkbutton(imraan,variable=p12, text ='RAPPING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p012.place(x = 390, y = 400) 
                        p12p=100
                        p013=Checkbutton(imraan,variable=p13, text ='BEATBOXING',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p013.place(x = 10, y = 450) 
                        p13p=100
                        p014=Checkbutton(imraan,variable=p14, text ='PHOTOGRAPHY',font=("Arial Black",10,"bold"),highlightcolor='black',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p014.place(x = 190, y = 450) 
                        p14p=50
                        p015=Checkbutton(imraan,variable=p15, text ='MEHNDI',font=("Arial Black",10,"bold"),highlightcolor='orange',fg="black",bg='orange',highlightbackground='black',highlightthickness=1,bd=1,activeforeground='orange',activebackground='black',selectcolor="orange", 
                                        takefocus = 0)
                        p015.place(x = 390, y =450) 
                        p15p=20
                        gavin=Frame(imraan,bd=0,highlightthickness=3,highlightbackground="orange",relief=RIDGE,bg="black")
                        gavin.place(x=10,y=510,width=480,height=70)
                        shalom=Label(gavin,relief=RIDGE,highlightcolor='black',highlightbackground='black',highlightthickness=0,activebackground="black",border=0,activeforeground="black",text="",fg='black',bg='black',height=2,width=14)
                        shalom.grid(row=0,column=0,padx=10,pady=9)
                        
                        angel=Button(gavin,relief=RIDGE,highlightcolor='orange',highlightbackground='orange',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",text="Update",command=deletesoftskills,fg='black',bg='orange',height=2,width=14)
                        angel.config(state=DISABLED)
                        angel.place(relx=0.5,rely=0.5,anchor=CENTER)
                        def selector(ev):
                             
                            
                            select_row=preeti.focus()
                            row=cdata['values']
                            
                            p01.config(state=NORMAL)
                            p02.config(state=NORMAL)
                            p03.config(state=NORMAL)
                            p04.config(state=NORMAL)
                            p044.config(state=NORMAL)
                            p05.config(state=NORMAL)
                            p06.config(state=NORMAL)
                            p07.config(state=NORMAL)
                            p077.config(state=NORMAL)
                            p08.config(state=NORMAL)
                            p088.config(state=NORMAL)
                            p0888.config(state=NORMAL)
                            p08888.config(state=NORMAL)
                            p09.config(state=NORMAL)
                            p099.config(state=NORMAL)
                            p0999.config(state=NORMAL)
                            p010.config(state=NORMAL)
                            p011.config(state=NORMAL)
                            p012.config(state=NORMAL)
                            p013.config(state=NORMAL)
                            p014.config(state=NORMAL)
                            p015.config(state=NORMAL)
                            ''''''
                            
                            
                            try:
                                xyz=row[0]
                                abc=row[5]
                               
                              
                                pqr=Label(imraan,text=f'{xyz}',font=("Arial Black",10,"bold"),bg='orange',fg='black',width=15,bd=0)
                                pq=Label(imraan,text=f'{abc}',font=("Arial Black",10,"bold"),bg='orange',fg='black',width=10,bd=0)
                                pqr.place(x=90,y=70)
                                pq.place(x=360,y=70)
                                Ulist=[]
                                Utotal=row[7]
                                
                                
                                oneplus=(row[5])
                                
                                
                                def bc():
                                    if (row[8]=='yes'):
                                        p01.config(state=DISABLED)
                                        p1.set(1)
                                        
                                        rf()
                                        bd()
                                        crs()
                                        crd()
                                        tt()
                                        css()
                                        ct5()
                                        ct3()
                                        pgs()
                                        pgd()
                                        pgt()
                                        pgst()
                                        dcs()
                                        dsd()
                                        dsg()
                                        sg()
                                        ff()
                                        rp()
                                        btbx()
                                        pgy()
                                        mdi()
                                        
                                        

                                        
                                    else:
                                        p1.set(0)
                                        rf()
                                        bd()
                                        crs()
                                        crd()
                                        tt()
                                        css()
                                        ct5()
                                        ct3()
                                        pgs()
                                        pgd()
                                        pgt()
                                        pgst()
                                        dcs()
                                        dsd()
                                        dsg()
                                        sg()
                                        ff()
                                        rp()
                                        btbx()
                                        pgy()
                                        mdi()
                                        
                                        
                                
                                
                                def rf():
                                    
                                    if (row[9]=='yes'):
                                        p02.config(state=DISABLED)
                                        p2.set(1)
                                    else:
                                        p2.set(0)
                                def bd():
                                    
                                    if (row[10]=='yes'):
                                        p03.config(state=DISABLED)
                                        p3.set(1)
                                        
                                    else:
                                        p3.set(0)
                                        
                                
                                
                                def crs():
                                    
                                    if (row[11]=='yes'):
                                        p04.config(state=DISABLED)
                                        p4.set(1)
                                    else:
                                        p4.set(0)
                                def crd():
                                    
                                    if (row[12]=='yes'):
                                        p044.config(state=DISABLED)
                                        p44.set(1)
                                    else:
                                        p44.set(0)
                                
                                def tt():
                                    
                                    if (row[13]=='yes'):
                                        p05.config(state=DISABLED)
                                        p5.set(1)
                                        
                                    else:
                                        p5.set(0)
                                        
                                
                                
                                def css():
                                    
                                    if (row[14]=='yes'):
                                        p06.config(state=DISABLED)
                                        p6.set(1)
                                    else:
                                        p6.set(0)
                                def ct5():
                                    
                                    if (row[15]=='yes'):
                                        p07.config(state=DISABLED)
                                        p7.set(1)
                                        
                                    else:
                                        p7.set(0)
                                        
                                
                                
                                def ct3():
                                    
                                    if (row[16]=='yes'):
                                        p077.config(state=DISABLED)
                                        p77.set(1)
                                    else:
                                        p77.set(0)
                                def pgs():
                                    
                                    if (row[17]=='yes'):
                                        p08.config(state=DISABLED)
                                        p8.set(1)
                                        
                                    else:
                                        p8.set(0)
                                        
                                
                                
                                def pgd():
                                    
                                    if (row[18]=='yes'):
                                        p088.config(state=DISABLED)
                                        p88.set(1)
                                    else:
                                        p88.set(0)
                                def pgt():
                                    
                                    if (row[19]=='yes'):
                                        p0888.config(state=DISABLED)
                                        p888.set(1)
                                        
                                    else:
                                        p888.set(0)
                                        
                                
                                
                                def pgst():
                                    
                                    if (row[20]=='yes'):
                                        p08888.config(state=DISABLED)
                                        p8888.set(1)
                                    else:
                                        p8888.set(0)
                                def dcs():
                                    
                                    if (row[21]=='yes'):
                                        p09.config(state=DISABLED)
                                        p9.set(1)
                                        
                                    else:
                                        p9.set(0)
                                        
                                
                                
                                def dsd():
                                    
                                    if (row[22]=='yes'):
                                        p099.config(state=DISABLED)
                                        p99.set(1)
                                    else:
                                        p99.set(0)
                                def dsg():
                                    
                                    if (row[23]=='yes'):
                                        p0999.config(state=DISABLED)
                                        p999.set(1)
                                        
                                    else:
                                        p999.set(0)
                                        
                                
                                
                                def ff():
                                    
                                    if (row[24]=='yes'):
                                        p010.config(state=DISABLED)
                                        p10.set(1)
                                    else:
                                        p10.set(0)
                                def sg():
                                    
                                    if (row[25]=='yes'):
                                        p011.config(state=DISABLED)
                                        p11.set(1)
                                    else:
                                        p11.set(0)
                                def rp():
                                    
                                    if (row[26]=='yes'):
                                        p012.config(state=DISABLED)
                                        p12.set(1)
                                        
                                    else:
                                        p12.set(0)
                                        
                                
                                
                                def btbx():
                                    
                                    if (row[27]=='yes'):
                                        p013.config(state=DISABLED)
                                        p13.set(1)
                                    else:
                                        p13.set(0)
                                def pgy():
                                    
                                    if (row[28]=='yes'):
                                        p014.config(state=DISABLED)
                                        p14.set(1)
                                        
                                    else:
                                        p14.set(0)

                                        
                                
                                
                                def mdi():
                                    
                                    if (row[29]=='yes'):
                                        p015.config(state=DISABLED)
                                        p15.set(1)
                                       
                                        
                                    else:
                                        p15.set(0)
                                     
                                        
                                def Eupdate():
                                    
                                    
                                    TotalSum=[]
                                    def BC():
                                        
                                        brock=p1.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Box_Cricket = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p1p)
                                            
                                            RF()
                                            BD()
                                            CRS()
                                            CRD()
                                            TT()
                                            CSS()
                                            CT5()
                                            CT3()
                                            PGS()
                                            PGD()
                                            PGT()
                                            PGST()
                                            DCS()
                                            DSD()
                                            DSG()
                                            SG()
                                            FF()
                                            RP()
                                            BTBX()
                                            PGY()
                                            MDI()
                                            bj=sum(Ulist)
                                            cur.execute(f'Update Students_database9 set totalammo = {bj} where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            showalldata()
                                            """ bj=sum(TotalSum)
                                            cur.execute(f'Update Students_database9 set Totalammo = "{bj}"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            dialga="Total Amount = RS."+str(bj) """
                                            """ MEGA_ARCEUS=Label(pikachu,text=dialga,width=30,bg='orange',fg='black',font=("Arial Black",50,"bold"))
                                            MEGA_ARCEUS.place(x=0,y=360) """
                                            ''''''
                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Box_Cricket = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            RF()
                                            BD()
                                            CRS()
                                            CRD()
                                            TT()
                                            CSS()
                                            CT5()
                                            CT3()
                                            PGS()
                                            PGD()
                                            PGT()
                                            PGST()
                                            DCS()
                                            DSD()
                                            DSG()
                                            SG()
                                            FF()
                                            RP()
                                            BTBX()
                                            PGY()
                                            MDI()
                                            bj=sum(Ulist)
                                            cur.execute(f'Update Students_database9 set totalammo = {bj} where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            showalldata()
                                            
                                    def RF():
                                        brock=p2.get()  

                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Rink_Football = "yes"  where Mobile_No="{oneplus}"  ')
                                            
                                            
                                            Ulist.append(p2p)
                                            

                                        else:
                                            cur.execute(f'Update Students_database9 set Rink_Football = "no"  where Mobile_No="{oneplus}"  ')
                                            ''''''
                                            
                                    def BD():
                                        brock=p3.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Badminton = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()

                                            Ulist.append(p3p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Badminton = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def CRS():
                                        brock=p4.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Carrom_Solo = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p4p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Carrom_Solo = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def CRD():
                                        brock=p44.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Carrom_Duo = "yes"  where Mobile_No="{oneplus}" ')
                                            con.commit()
                                            Ulist.append(p44p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Carrom_Duo = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def TT():
                                        brock=p5.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Table_Tennis = "yes" where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p5p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Table_Tennis = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def CSS():
                                        brock=p6.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Chess = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p6p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Chess = "no"  where Mobile_No="{oneplus}" ')
                                            con.commit()
                                            
                                    def CT5():
                                        brock=p7.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Counter_Strike_Five_M = "yes"  where Mobile_No="{oneplus}" ')
                                            con.commit()
                                            Ulist.append(p7p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Counter_Strike_Five_M = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def CT3():
                                        brock=p77.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Counter_Strike_Three_M = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p77p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Counter_Strike_Three_M = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def PGS():
                                        brock=p8.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Pubg_Solo = "yes"  where Mobile_No="{oneplus}" ')
                                            con.commit()
                                            Ulist.append(p8p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Pubg_Solo = "no"  where Mobile_No="{oneplus}" ')
                                            con.commit()
                                            
                                    def PGD():
                                        brock=p88.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Pubg_Squad = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p88p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Pubg_Squad = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def PGT():
                                        brock=p888.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Pubg_TDM = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p888p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Pubg_TDM = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def PGST():
                                        brock=p8888.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Pubg_Squad_TDM = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p8888p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Pubg_Squad_TDM = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def DCS():
                                        brock=p9.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Dance_Solo = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p9p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Dance_Solo = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def DSD():
                                        brock=p99.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Dance_Group_Duo = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p99p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Dance_Group_Duo = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def DSG():
                                        brock=p999.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Dance_Group_Squad = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p999p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Dance_Group_Squad = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def FF():
                                        brock=p10.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Fifa = "yes"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p10p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Fifa = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def SG():
                                        brock=p11.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Singing = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p11p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Singing = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def RP():
                                        brock=p12.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Rapping = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p12p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Rapping = "no"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            
                                    def BTBX():
                                        brock=p13.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Beatboxing = "yes" where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            Ulist.append(p13p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Beatboxing = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def PGY():
                                        brock=p14.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Photography = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p14p)
                                            

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Photography = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                            
                                    def MDI():
                                        brock=p15.get()
                                        if brock == 1:
                                            ''''''
                                            
                                            cur.execute(f'Update Students_database9 set Mehndi = "yes"  where Mobile_No="{oneplus}"   ')
                                            con.commit()
                                            Ulist.append(p15p)

                                            
                                            
                                            con.commit()

                                        else:
                                            ''''''
                                            cur.execute(f'Update Students_database9 set Mehndi = "no"  where Mobile_No="{oneplus}"  ')
                                            con.commit()
                                        showalldata()
                                        
                                        p1.set(0)
                                        p2.set(0)
                                        p3.set(0)
                                        p4.set(0)
                                        p44.set(0)
                                        p5.set(0)
                                        p6.set(0)
                                        p7.set(0)
                                        p77.set(0)
                                        p8.set(0)
                                        p88.set(0)
                                        p888.set(0)
                                        p8888.set(0)
                                        p9.set(0)
                                        p99.set(0)
                                        p999.set(0)
                                        p10.set(0)
                                        p11.set(0)
                                        p12.set(0)
                                        p13.set(0)
                                        p14.set(0)
                                        p15.set(0)
                                        p01.config(state=NORMAL)
                                        p02.config(state=NORMAL)
                                        p03.config(state=NORMAL)
                                        p04.config(state=NORMAL)
                                        p044.config(state=NORMAL)
                                        p05.config(state=NORMAL)
                                        p06.config(state=NORMAL)
                                        p07.config(state=NORMAL)
                                        p077.config(state=NORMAL)
                                        p08.config(state=NORMAL)
                                        p088.config(state=NORMAL)
                                        p0888.config(state=NORMAL)
                                        p08888.config(state=NORMAL)
                                        p09.config(state=NORMAL)
                                        p099.config(state=NORMAL)
                                        p0999.config(state=NORMAL)
                                        p010.config(state=NORMAL)
                                        p011.config(state=NORMAL)
                                        p012.config(state=NORMAL)
                                        p013.config(state=NORMAL)
                                        p014.config(state=NORMAL)
                                        p015.config(state=NORMAL)
                                        pqr.place_forget()
                                
                                        pq.place_forget()   
                                        angelreal.configure(state=DISABLED)
                                    BC()
                                    
                                angelreal=Button(gavin,cursor='exchange',command=Eupdate,relief=RIDGE,highlightcolor='orange',highlightbackground='orange',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",text="Update",fg='black',bg='orange',height=2,width=14)
                                angelreal.place(relx=0.5,rely=0.5,anchor=CENTER)
                                
                                bc()
                                pikachu.mainloop()
                            except IndexError:
                                ''''''
                            
                                ''''''
                        def backbtn000():
                            ''''''
                            imraan.place_forget()
                            
                            submitpass()
                            
                                                
                            pikachu.mainloop()
                            
                        ash=os.getcwd()
                        ook=ash+"//previous.png"
                        
                        photo22 = PhotoImage(file=ook)
                        moltress = Button(imraan,cursor='hand2',bd=0,highlightthickness=0,highlightbackground='black',highlightcolor='black',activebackground="orange",width=40,height=40,bg="orange",image=photo22 ,command=backbtn000)
                        moltress.place(x=1,y=1)
                        pikachu.mainloop()
                    
                    updatep=Button(yash_f,cursor='hand2',command=Pupdates,relief=RIDGE,font=("none",12),highlightcolor='orange',highlightbackground='black',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",text="",fg='black',bg='orange',height=1,width=20)
                    pupdate.place(x=20,y=467)
                    updatep.place(y=467,x=180)


                    
                    ''' INSIDE LEFT FRAME'''
                    '''FRAME FOR BUTTONS'''
                    shubham_y=Frame(yash_f,bd=0,highlightthickness=3,highlightbackground="orange",relief=RIDGE,bg="black")
                    shubham_y.place(x=10,y=510,width=480,height=70)
                    '''Inside'''
                    def clearit():
                        megapikachuz1.set('')
                        megapikachu2z2.set('')
                        megapikachu3z3.set('')
                        megapikachu4z4.set('')
                        megapikachu5z5.set('')
                        megapikachu6z6.set('')
                        __MOF__.set('')
                    def addEvent():
                        '''GETTING VALUES'''
                        ename=megapikachuz.get()
                        print(ename)
                        fee=megapikachu6z.get()
                        Participants=megapikachu3z.get()
                        print(3897)
                        print(cur.execute("ALTER TABLE Students_database9 ADD "+ename+" varchar(6)"))
                        print(cur.execute(f'INSERT INTO New_Events_list9 (EventName,Fee,Participants,deleted) values ("{ename}","{fee}","{Participants}", 0)'))
                        

                        for event in eventslist:
                            print(event)

                        print(3902)
                        con.commit()
                        print(3899)
                        
                        with open('allevents.txt', 'a+') as f:
                            f.write('\n'+ename)
                        
                    
                    
                    def deletesoftskills():
                        oneplus=megapikachu6z.get()
                        
                        
                        cur.execute(f'Delete From Students_database9 where Mobile_No="{oneplus}"')
                        con.commit()
                        for i in preeti.get_children():
                            preeti.delete(i)
                        
                        showalldata()
                        
                        clearit()
                        
                    
                    neelC=Button(shubham_y,cursor='hand2',relief=RIDGE,highlightcolor='orange',highlightbackground='orange',highlightthickness=1,activebackground="black",border=0,activeforeground="orange",text="Add Events",command=addEvent,fg='black',bg='orange',height=2,width=14)
                    neelC.grid(row=0,column=0,padx=10,pady=9)
                    ''''''
                    
                    
                    def hommming():
                        ''''''
                        Admin_Login_button.configure(state=NORMAL)
                        moltressx.place_forget()
                        shubham_y.place_forget()
                        yash_f.place_forget()
                        Exit_button.place(x=690,y=530)
                        Admin_Login_button.place(x=480,y=530)
                        Remove_label_button.place(x=880,y=310)
                        Edit_label_button.place(x=890,y=530)
                        Vibes_Events_All_Info_button.place(x=690,y=310)
                        Vibes_Events.place(x=480,y=310)
                        About_Vibes_button.place(x=690,y=90)
                        reg_button.place(x=480,y=90)
                                                
                        Admin_label.place(x=494,y=690)
                        Remove_label.place(x=880,y=470)
                        Edit_label.place(x=890,y=530)
                        Exit_label.place(x=756,y=690)
                        Vibes_label.place(x=507,y=470)
                        eventall_label.place(x=720,y=470)
                        reg_label.place(x=515,y=250)
                        About_label.place(x=706,y=250)
                        moltresssss.place_forget()
                        
                        

                        


                    ash00000=os.getcwd()
                    ookooooo=ash00000+"//home.png"
                    
                    photo222222 = PhotoImage(file=ookooooo)
                    moltresssss = Button(pikachu,cursor='hand2',command=hommming,bd=0,bg="black",activeforeground="black",activebackground='black',image=photo222222 ,highlightthickness=0,width=73,height=65)
                    moltresssss.place(x=1289,y=62)
                      
                        
                    
                    
            
                    def backbtn9000():
                        
                        ''''''
                        pubgm.place(x=425,y=160,width=510,height=580)
                        moltressx.place_forget()
                        moltress.place(x=0,y=62)
                        moltresssss.place_forget()
                        
                        shubham_y.place_forget()
                        yash_f.place_forget()
                        # ved.place_forget()
                        diglet1.set('')
                        
                        
                        

                        
                    ash=os.getcwd()
                    ook=ash+"//reply.png"
                    
                    photo22 = PhotoImage(file=ook)
                    moltressx = Button(pikachu,cursor='hand2',activeforeground="black",activebackground='black',bd=0,bg="black",image=photo22 ,highlightthickness=0,width=73,height=65,command=backbtn9000)
                    moltressx.place(x=0,y=62)
                    pikachu.mainloop()
                elif hoho=="":
                    showerror("RECHECK","Error \nPlease Enter Pass Bot!")
                else:
                    
                    showerror("RECHECK","Error \nWrong Pass Bot!")
                
            pubgm=Frame(pikachu,bd=0,highlightthickness=3,highlightcolor='orange',highlightbackground="orange",relief=RIDGE,bg="black")
            pubgm.place(x=425,y=160,width=510,height=580)
            Label(pubgm,text="Mod-Pass",font=("Arial Black",20,"bold"),bg="black",fg="black").pack()
            diglet1=StringVar()
            diglet=Entry(pubgm,textvariable=diglet1,highlightcolor='orange',highlightbackground='orange',highlightthickness=2,bd=1,insertbackground="orange",width=24,font=("Times New Roman",25),fg="orange",bg="black")
            diglet.config(show="*")
            diglet.place(x=43,y=360)

            diglet.insert(0,'')
            def eyes():
                ''''''
                moltresss.place_forget()
                diglet.config(show="")
                '''hide-eye'''
                def hideeye():
                    diglet.config(show="*")
                    moltressss.place_forget()
                    moltresss.place(x=419,y=363)
                ash0000=os.getcwd()
                ookoooo=ash0000+"//hide.png"
                
                photo22222 = PhotoImage(file=ookoooo)
                moltressss = Button(pubgm,cursor='hand2',activeforeground="black",activebackground='black',command=hideeye,bd=0,bg="black",image=photo22222 ,highlightthickness=0,width=33,height=36)
                moltressss.place(x=419,y=363)
                pikachu.mainloop()

            '''eye'''
            ash000=os.getcwd()
            ookooo=ash000+"//eye.png"
            
            photo2222 = PhotoImage(file=ookooo)
            moltresss = Button(pubgm,cursor='hand2',activeforeground="black",activebackground='black',command=eyes,bd=0,bg="black",image=photo2222 ,highlightthickness=0,width=33,height=36)
            moltresss.place(x=419,y=363)
            

            ''''''
            ekanas=Button(pubgm,command=submitpass,cursor='hand2',activebackground="black",highlightcolor='orange',highlightbackground='orange',highlightthickness=1,bd=0,activeforeground="orange",text="LogIn",fg='black',bg='orange',height=3,width=20)
            ekanas.pack(side=BOTTOM)
            ash00=os.getcwd()
            ookoo=ash00+"//user.png"
            
            photo222 = PhotoImage(file=ookoo)
            moltress = Label(pubgm,bd=0,bg="black",image=photo222 ,highlightthickness=0,width=260,height=250)
            moltress.pack(side=TOP)
            Label(pubgm,text="Mod-Pass",font=("Arial Black",20,"bold"),bg="black",fg="black").pack()
            arbrok=Label(pubgm,text="Mod-Pass",font=("Arial Black",20,"bold"),bg="black",fg="orange")
            arbrok.pack()
            def backbtn900():
                ''''''
                
                Exit_button.place(x=690,y=530)
                Remove_label_button.place(x=880,y=310)
                Admin_Login_button.place(x=480,y=530)
                Edit_label_button.place(x=890,y=530)
                Vibes_Events_All_Info_button.place(x=690,y=310)
                Vibes_Events.place(x=480,y=310)
                About_Vibes_button.place(x=690,y=90)
                reg_button.place(x=480,y=90)
                Edit_label.place(x=890,y=530)
                Admin_label.place(x=494,y=690)
                Remove_label.place(x=880,y=470)
                Exit_label.place(x=756,y=690)
                Vibes_label.place(x=507,y=470)
                eventall_label.place(x=720,y=470)
                reg_label.place(x=515,y=250)
                About_label.place(x=706,y=250)
                ekanas.place_forget()
                diglet.place_forget()
                moltress.place_forget()
                arbrok.place_forget()
                pubgm.place_forget()
                
            ash=os.getcwd()
            ook=ash+"//reply.png"
            
            photo22 = PhotoImage(file=ook)
            moltress = Button(pikachu,cursor='hand2',highlightthickness=0,activebackground='black',bg="black",image=photo22 ,width=73,height=65,bd=0,command=backbtn900)
            moltress.place(x=0,y=62)
            pikachu.mainloop()
            
        editit=os.getcwd()
        edited=editit+"//domain.png"
        photoEd = PhotoImage(file=edited)   

        Edit_label_button=Button(pikachu,cursor='hand2',text='Exit',bd=0,highlightthickness=2,highlightbackground='cyan',highlightcolor='cyan',activebackground="black",image=photoEd,width=170,height=170,bg="black",command=Edit_Events_7)
        Edit_label_button.place(x=890,y=490)
        
        Edit_label=Label(pikachu,font=("Times",20,"bold"),text='Add-Events',bd=0,highlightthickness=0,bg='black',fg='orange')
        Edit_label.place(x=890,y=690)

        removeit=os.getcwd()
        edited=removeit+"//domain.png"
        photoRemove = PhotoImage(file=edited)   

        Remove_label_button=Button(pikachu,cursor='hand2',text='Exit',bd=0,highlightthickness=2,highlightbackground='cyan',highlightcolor='cyan',activebackground="black",image=photoRemove,width=170,height=170,bg="black",command=Remove_Events_8)
        Remove_label_button.place(x=880,y=310)
        
        Remove_label=Label(pikachu,font=("Times",20,"bold"),text='Remove-Events',bd=0,highlightthickness=0,bg='black',fg='orange')
        Remove_label.place(x=880,y=470)


        exitit=os.getcwd()
        exited=exitit+"//exit.png"
        
        photoE = PhotoImage(file=exited)   
            
        Exit_button=Button(pikachu,cursor='hand2',text='Exit',bd=0,highlightthickness=2,highlightbackground='cyan',highlightcolor='cyan',activebackground="black",image=photoE,width=170,height=170,bg="black",command=Exit_button_6)
        Exit_button.place(x=690,y=530)

        Exit_label=Label(pikachu,font=("Times",20,"bold"),text='Exit',bd=0,highlightthickness=0,bg='black',fg='orange')
        Exit_label.place(x=756,y=690)

        pikachu.mainloop()
    pokemon()

outside_program()
