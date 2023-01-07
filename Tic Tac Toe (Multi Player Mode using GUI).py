from tkinter import *
from random import *
from tkinter import messagebox
def newGame():
     global x,x_box,o_box,nums
     x = 1
     x_box = list()
     o_box = list()
     nums = list()
     b1.configure(bg= 'white')
     b2.configure(bg= 'white')
     b3.configure(bg= 'white')
     b4.configure(bg= 'white')
     b5.configure(bg= 'white')
     b6.configure(bg= 'white')
     b7.configure(bg= 'white')
     b8.configure(bg= 'white')
     b9.configure(bg= 'white')
x = 1
x_box = list()
o_box = list()
nums = list()
def check(box,boo):
     condition = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,5,8],[3,4,5],[6,7,8],[2,4,6]] 
     if len(box) >= 3: 
          for i in range(0,len(box)-2):  
               for j in range(i+1,len(box)-1):      
                    for k in range(j+1,len(box)):   
                         for m in condition:    
                              if box[i] in m and box[j] in m and box[k] in m:
                                   if boo == True:
                                        messagebox.showinfo('Tic Tac Toe','Congratulations\nPlayer 1 won the game')
                                        if messagebox.askretrycancel('Tic Tac Toe','Do You want to Play Again?'):
                                             newGame()
                                        else :
                                             exit()          
                                   else:
                                        messagebox.showinfo('Tic Tac Toe','Congratulations\nPlayer 2 won the game')
                                        if messagebox.askretrycancel('Tic Tac Toe','Do You want to Play Again?'):
                                             newGame()
                                        else :
                                             exit()          
                              else:
                                   continue
def click(b,n):
     global x,x_box,o_box,nums      
     if x % 2 == 1:
          if n not in nums:
               x += 1
               x_box.append(n)
               nums.append(n)
               b.configure(bg='black')
               check(x_box,True)
          else:
               messagebox.showerror('Tic Tac Toe','This square is already filled\nPlease select anyother square')                 
     else:
          if n not in nums:
               x += 1
               o_box.append(n)
               nums.append(n)
               b.configure(bg='red')
               check(o_box,False)
          else:
               messagebox.showerror('Tic Tac Toe','That square is already filled\nPlease select anyother square')             
     if x >= 10:
          messagebox.showerror( 'Tic Tac Toe',"It's a TIE")
          if messagebox.askretrycancel('Tic Tac Toe','Do You want to Play Again?'):
               newGame()
          else :
               exit()
root = Tk()
root.geometry('500x400')
myLabel1 = Label(root,text= 'BLACK - first player',fg='black').grid(row=0,column=1)
myLabel2 = Label(root,text= 'RED - second player',fg = 'red').grid(row=1,column=1)
b1 = Button(root,bg='white',padx=80,pady=45,command = lambda:click(b1,0))
b2 = Button(root,bg='white',padx=80,pady=45,command = lambda:click(b2,1))
b3 = Button(root,bg='white',padx=80,pady=45,command = lambda:click(b3,2))
b4 = Button(root,bg='white',padx=80,pady=45,command = lambda:click(b4,3))
b5 = Button(root,bg='white',padx=80,pady=45,command = lambda:click(b5,4))
b6 = Button(root,bg='white',padx=80,pady=45,command = lambda:click(b6,5))
b7 = Button(root,bg='white',padx=80,pady=45,command = lambda:click(b7,6))
b8 = Button(root,bg='white',padx=80,pady=45,command = lambda:click(b8,7))
b9 = Button(root,bg='white',padx=80,pady=45,command = lambda:click(b9,8))
b1.grid(row= 2,column= 0)
b2.grid(row= 2,column= 1)
b3.grid(row= 2,column= 2)
b4.grid(row= 3,column= 0)
b5.grid(row= 3,column= 1)
b6.grid(row= 3,column= 2)
b7.grid(row= 4,column= 0)
b8.grid(row= 4,column= 1)
b9.grid(row= 4,column= 2)
root.mainloop()



