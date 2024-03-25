from tkinter import *

root = Tk()
root.title('Cat Fight Game')
root.configure()
root.geometry("1500x900")
root.resizable(False,False)

bg = PhotoImage(file="bg5.png")

back_ground = Label(root, image=bg)
back_ground.place(x=0,y=0,relwidth=1,relheight=1)

char_1_img= PhotoImage(file="maine-coon-cat.png")
char_1 = Label(root, image=char_1_img)
char_1.place(x=20,y=600,width=200,height=200)



class MyGame:

    def __init__(hero, name, health,damage,defense,healing,):    
        hero.name = name
        hero.health = health
        hero.damage = damage
        hero.defense = defense
        hero.healing = healing   
        
    def characters(hero):
        img= PhotoImage      

    def displayHealth(hero):#show health
        if hero.health > 0:
            print(hero.name,"'s  Health is ",hero.health,"HP")
        elif hero.health <= 60 and hero.health > 0:
            print(hero.name,"You're running out of life")
        else:
            print(hero.name,"YOUR GAME IS OVER :(")
        print()


    def Skill1(hero):#healing 
        hero.health += hero.healing
        print(hero.name,"'s health now is ", hero.health)

    def Skill2(hero,target):#health protection
        print(hero.name, "activated Protection ")
        if target.damage <= hero.defense:
            target.damage = 0 
            print(target.name,"'s damage is decreased by",hero.defense)
        else:
            target.damage -= hero.defense
            print(target.name,"'s damage is decreased by",hero.defense)
        
    def Skill3(hero):#additional damage
        print(hero.name,"activated Skill 3 ", "**defense+20**")
        hero.damage += 20
        print(hero.name,"'s damage is now : ",hero.damage)
        print()
            
    def Attacked(hero,target):#the opponent attacked the other
        print(hero.name, "--ATTACKED--" , target.name)
        target.health -= hero.damage
        print(target.name,"You are being Attacked!")
        print()
        
nin=MyGame("nin",300,30,115,10)
nin.displayHealth()


root.mainloop()                   





        
        
