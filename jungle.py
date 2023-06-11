from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import PIL.Image
import os
import numpy as np

def ChooseCamp():
	global root2
	global render1, render2, render3, render4, render5, render6, render7
	addb.configure(state='disabled')
	root2 = Toplevel(root)
	root2.resizable(0,0)
	root2.title('Choose')
	cv2 = Canvas(root2,width=220,height=420)
	cv2.pack()
	load1 = PIL.Image.open("Red.png")
	load1 = load1.resize((60,60),PIL.Image.ANTIALIAS)
	render1 = ImageTk.PhotoImage(load1,master=root2)
	RedButton = Button(cv2,image=render1,command=RedChosen)
	RedButton.place(x=20,y=20,width=80,height=80)

	load2 = PIL.Image.open("Blue.png")
	load2 = load2.resize((70,70),PIL.Image.ANTIALIAS)
	render2 = ImageTk.PhotoImage(load2,master=root2)
	BlueButton = Button(cv2,image=render2,command=BlueChosen)
	BlueButton.place(x=120,y=20,width=80,height=80)

	load3 = PIL.Image.open("Raptors.png")
	load3 = load3.resize((70,70),PIL.Image.ANTIALIAS)
	render3 = ImageTk.PhotoImage(load3,master=root2)
	RaptorsButton = Button(cv2,image=render3,command=RaptorsChosen)
	RaptorsButton.place(x=20,y=120,width=80,height=80)

	load4 = PIL.Image.open("Krugs.png")
	load4 = load4.resize((70,70),PIL.Image.ANTIALIAS)
	render4 = ImageTk.PhotoImage(load4,master=root2)
	KrugsButton = Button(cv2,image=render4,command=KrugsChosen)
	KrugsButton.place(x=20,y=220,width=80,height=80)

	load5 = PIL.Image.open("Gromp.png")
	load5 = load5.resize((70,70),PIL.Image.ANTIALIAS)
	render5 = ImageTk.PhotoImage(load5,master=root2)
	GrompButton = Button(cv2,image=render5,command=GrompChosen)
	GrompButton.place(x=120,y=220,width=80,height=80)

	load6 = PIL.Image.open("Wolves.png")
	load6 = load6.resize((70,70),PIL.Image.ANTIALIAS)
	render6 = ImageTk.PhotoImage(load6,master=root2)
	WolvesButton = Button(cv2,image=render6,command=WolvesChosen)
	WolvesButton.place(x=120,y=120,width=80,height=80)

	load7 = PIL.Image.open("Crab.png")
	load7 = load7.resize((70,70),PIL.Image.ANTIALIAS)
	render7 = ImageTk.PhotoImage(load7,master=cv2)
	CrabButton = Button(cv2,image=render7,command=CrabChosen)
	CrabButton.place(x=70,y=320,width=80,height=80)

	root2.mainloop()

def RedChosen():
	global campn, cimages, campstaken
	buttons[campn]['image'] = render1
	cimages.append(render1)
	campstaken.append('Red')
	buttons[campn].configure(command="")
	campn = campn + 1
	if campn < len(buttons):
		buttons[campn].configure(state='active')
	root2.destroy()

def RaptorsChosen():
	global campn, cimages, campstaken
	buttons[campn]['image'] = render3
	cimages.append(render3)
	campstaken.append('Raptors')
	buttons[campn].configure(command="")
	campn = campn + 1
	if campn < len(buttons):
		buttons[campn].configure(state='active')
	root2.destroy()

def KrugsChosen():
	global campn, cimages, campstaken
	cimages.append(render4)
	campstaken.append('Krugs')
	buttons[campn]['image'] = render4
	buttons[campn].configure(command="")
	campn = campn + 1
	if campn < len(buttons):
		buttons[campn].configure(state='active')
	root2.destroy()

def BlueChosen():
	global campn, cimages, campstaken
	cimages.append(render2)
	campstaken.append('Blue')
	buttons[campn]['image'] = render2
	buttons[campn].configure(command="")
	campn = campn + 1
	if campn < len(buttons):
		buttons[campn].configure(state='active')
	root2.destroy()

def GrompChosen():
	global campn, cimages, campstaken
	cimages.append(render5)
	campstaken.append('Gromp')
	buttons[campn]['image'] = render5
	buttons[campn].configure(command="")
	campn = campn + 1
	if campn < len(buttons):
		buttons[campn].configure(state='active')
	root2.destroy()

def WolvesChosen():
	global campn, cimages, campstaken
	cimages.append(render6)
	campstaken.append('Wolves')
	buttons[campn]['image'] = render6
	buttons[campn].configure(command="")
	campn = campn + 1
	if campn < len(buttons):
		buttons[campn].configure(state='active')
	root2.destroy()

def CrabChosen():
	global campn, cimages, campstaken
	cimages.append(render7)
	campstaken.append('Crab')
	buttons[campn]['image'] = render7
	buttons[campn].configure(command="")
	campn = campn + 1
	if campn < len(buttons):
		buttons[campn].configure(state='active')
	root2.destroy()

def Calculate():
	global ptc
	print(ptc.get())
	krugslvl = 0
	redlvl = 0
	raptorslvl = 0
	wolveslvl = 0
	bluelvl = 0
	gromplvl = 0
	crablvl = 0
	totalxp = 0
	totalgold = 0
	currentlvl = 0
	xptonextlvl = 0
	xpfromlastlvl = 0
	cumulativexp = [0,280,660,1140,1720,2400,3180,4060,5040,6120,7300,8580,9960,11440,13020,14700,16480,18360]
	if ptc.get() == '11.4':
		raptorsxp = [85,87,91,98,106,115]
		krugsxp = [153,153.93,158.68,167.25,179.65,194.95]
		grompxp = [125,128.13,134.38,143.75,156.25,168.75]
		krugsgold = 125
		raptorsgold = 75
		grompgold = 85
	elif ptc.get() == '11.3':
		raptorsxp = [95,97,102,109,119,128]
		grompxp = [135,138.375,145.125,155.25,168.75,182.25]
		krugsxp = [175,167.175,181.725,191.65,205.95,223.45]
		raptorsgold = 85
		krugsgold = 135
		grompgold = 105
	elif ptc.get() == '11.6':
		raptorsxp = [85,87,91,98,106,115]
		krugsxp = [153,153.93,158.68,167.25,179.65,194.95]
		grompxp = [135,138.38,145.13,155.25,168.75,182.25]
		krugsgold = 125
		raptorsgold = 75
		grompgold = 85
	
	wolvesxp = [95,97.39,102.14,109.25,118.75,128.25]
	bluexp = [110,112.75,118.25,126.5,137.5,148.5]
	redxp = bluexp
	crabxp = [115,138,149.5,161,184,207]

	wolvesgold = 85
	bluegold = 100
	redgold = 100
	crabgold = 70


	z = 0
	for camp in campstaken:
		level = int(lvls[z].get())
		if level == 1:
			camplvl = 0
		elif level == 3:
			camplvl = 1
		elif level == 5:
			camplvl = 2
		elif level == 7:
			camplvl = 3
		elif level == 9:
			camplvl = 4
		if camp == 'Red':
			totalxp = totalxp + redxp[camplvl]
			xps[z]['text'] = str(int(redxp[camplvl]))
			golds[z]['text'] = redgold
			totalgold+=redgold
		if camp == 'Blue':
			totalxp = totalxp + bluexp[camplvl]
			xps[z]['text'] = str(int(bluexp[camplvl]))
			golds[z]['text'] = bluegold
			totalgold+=bluegold
		if camp == 'Crab':
			totalxp = totalxp + crabxp[camplvl]
			xps[z]['text'] = str(int(crabxp[camplvl]))
			golds[z]['text'] = crabgold
			totalgold+=crabgold
		if camp == 'Gromp':
			totalxp = totalxp + grompxp[camplvl]
			xps[z]['text'] = str(int(grompxp[camplvl]))
			golds[z]['text'] = grompgold
			totalgold+=grompgold
		if camp == 'Wolves':
			totalxp = totalxp + wolvesxp[camplvl]
			xps[z]['text'] = str(int(wolvesxp[camplvl]))
			golds[z]['text'] = wolvesgold
			totalgold+=wolvesgold
		if camp == 'Krugs':
			totalxp = totalxp + krugsxp[camplvl]
			xps[z]['text'] = str(int(krugsxp[camplvl]))
			golds[z]['text'] = krugsgold
			totalgold+=krugsgold
		if camp == 'Raptors':
			totalxp = totalxp + raptorsxp[camplvl]
			xps[z]['text'] = str(int(raptorsxp[camplvl]))
			golds[z]['text'] = raptorsgold
			totalgold+=raptorsgold
		z = z+1

	cv.configure(height=570+160*column)
	cv.create_line(0,170+160*column,740,170+160*column)
	


	totalxp = totalxp + 150 + 60*len(campstaken)


	for i in range(0,len(cumulativexp)):
		if i == len(cumulativexp)-1:
			currentlvl = len(cumulativexp)
		else:
			if totalxp > cumulativexp[i] and totalxp <= cumulativexp[i+1]:
				currentlvl = i
				xptonextlvl = cumulativexp[i+1] - totalxp
				xpfromlastlvl = cumulativexp[i+1] - cumulativexp[i]
				lastlvlxp = cumulativexp[i]
				break

	currentlvl = currentlvl + 1
	missingperc = (totalxp - lastlvlxp) / xpfromlastlvl
	missingperc = round(missingperc, 2)
	ext = missingperc * 360

	

	global rc, lvlb, gt, xt, lvlleft
	#rc = cv.create_arc(280,220+160*column,580,520+160*column,start=270,extent=0,fill="Red",style="arc",width=25,outline="Red")
	try:
		cv.delete(rc)
		cv.delete(lvlb)
		cv.delete(gt)
		cv.delete(xt)
		cv.delete(lvlleft)
		
	except:
		pass

	cv.create_arc(280,220+160*column,580,520+160*column,start=270,extent=359,style="arc",width=25,outline="gray50")
	rc = cv.create_arc(280,220+160*column,580,520+160*column,start=270,extent=ext,fill="Red",style="arc",width=25,outline="Red",tag="rc")

	cv.create_line(320,370+160*column,540,370+160*column)

	gt = cv.create_text(100,340 + 160*column,text="Total Gold:    " + str(totalgold),font="calibri 12 bold",tag="gt")
	xt = cv.create_text(100,380 + 160*column,text="Total XP:    "+str(int(totalxp)),font="calibri 12 bold",tag="xt")
	lvlleft = cv.create_text(430,390 + 160*column,text=str(int(missingperc*100))+"% to next level",font="calibri 12")

	lvlb = cv.create_text(430,350 + 160*column,text="Level " + str(currentlvl),font="calibri 12 bold",tag="lvlb")

def AddButton():
	global column
	prevbutton = len(buttons)
	buttons.append('b'+str(len(buttons)+1))
	llabels.append('ll'+str(len(buttons)+1))
	lvls.append('lvl'+str(len(buttons)+1))
	golds.append('G'+str(len(buttons)+1))
	xps.append('XP'+str(len(buttons)+1))
	print(prevbutton)
	row = 0
	column = 0
	for i in range(len(buttons)):
		if row == 7:
			column = column + 1
			row = 0
			cv.configure(height=170*(column+1))
		if column < 3:
			buttons[i] = Button(cv,image=render,command=ChooseCamp)
			buttons[i].place(x=20+90*row,y=30+160*column,width=80,height=80)
			buttons[i].configure(state='disabled')
			XPl1 = Label(cv,text="XP",font="calibri 11 bold")
			XPl1.place(x=20+90*row,y=110+160*column)
			gl1 = Label(cv,text="Gold",font="calibri 11 bold")
			gl1.place(x=60+90*row,y=110+160*column)
			llabels[i] = Label(cv,text="Lvl:",font="calibri 11")
			llabels[i].place(x=20+90*row,y=7+160*column)
			lvls[i] = ttk.Spinbox(root,from_=1,to=9,increment=2,justify="center")
			lvls[i].place(x=60+90*row,y=10+160*column,width=40)
			lvls[i].set(1)

			golds[i] = Label(cv,text="-",font="calibri 11")
			golds[i].place(x=65+90*row,y=130+160*column)

			xps[i] = Label(cv,text="-",font="calibri 11")
			xps[i].place(x=17+90*row,y=130+160*column)
		else:
			addb.configure(state='disabled')
			break
		row = row + 1
	buttons[0].configure(state='active')
	print(len(buttons))

global buttons, campn, xps
global campstaken, cimages
cimages = []
campstaken = []
column = 0
campn = 0

root = Tk()
root.resizable(0,0)
root.title('Jungle XP')

cv = Canvas(root,width=740,height=170)
cv.pack()

#------------- XP Labels ----------------------

XPl1 = Label(cv,text="XP",font="calibri 11 bold")
XPl1.place(x=20,y=110)

XP1 = Label(cv,text="-",font="calibri 11")
XP1.place(x=17,y=130)

XPl2 = Label(cv,text="XP",font="calibri 11 bold")
XPl2.place(x=110,y=110)

XP2 = Label(cv,text="-",font="calibri 11")
XP2.place(x=107,y=130)

XPl3 = Label(cv,text="XP",font="calibri 11 bold")
XPl3.place(x=200,y=110)

XP3 = Label(cv,text="-",font="calibri 11")
XP3.place(x=197,y=130)

XPl4 = Label(cv,text="XP",font="calibri 11 bold")
XPl4.place(x=290,y=110)

XP4 = Label(cv,text="-",font="calibri 11")
XP4.place(x=287,y=130)

XPl5 = Label(cv,text="XP",font="calibri 11 bold")
XPl5.place(x=380,y=110)

XP5 = Label(cv,text="-",font="calibri 11")
XP5.place(x=377,y=130)

XPl6 = Label(cv,text="XP",font="calibri 11 bold")
XPl6.place(x=470,y=110)

XP6 = Label(cv,text="-",font="calibri 11")
XP6.place(x=467,y=130)

XPl7 = Label(cv,text="XP",font="calibri 11 bold")
XPl7.place(x=560,y=110)

XP7 = Label(cv,text="-",font="calibri 11")
XP7.place(x=557,y=130)

#----------- Gold labels ----------------------


gl1 = Label(cv,text="Gold",font="calibri 11 bold")
gl1.place(x=60,y=110)

G1 = Label(cv,text="-",font="calibri 11")
G1.place(x=65,y=130)

gl2 = Label(cv,text="Gold",font="calibri 11 bold")
gl2.place(x=150,y=110)

G2 = Label(cv,text="-",font="calibri 11")
G2.place(x=155,y=130)

gl3 = Label(cv,text="Gold",font="calibri 11 bold")
gl3.place(x=240,y=110)

G3 = Label(cv,text="-",font="calibri 11")
G3.place(x=245,y=130)

gl4 = Label(cv,text="Gold",font="calibri 11 bold")
gl4.place(x=330,y=110)

G4 = Label(cv,text="-",font="calibri 11")
G4.place(x=335,y=130)

gl5 = Label(cv,text="Gold",font="calibri 11 bold")
gl5.place(x=420,y=110)

G5 = Label(cv,text="-",font="calibri 11")
G5.place(x=425,y=130)

gl6 = Label(cv,text="Gold",font="calibri 11 bold")
gl6.place(x=510,y=110)

G6 = Label(cv,text="-",font="calibri 11")
G6.place(x=515,y=130)

gl7 = Label(cv,text="Gold",font="calibri 11 bold")
gl7.place(x=600,y=110)

G7 = Label(cv,text="-",font="calibri 11")
G7.place(x=605,y=130)

#--------- Camps level ------------------

llabels = ['ll1', 'll2', 'll3', 'll4', 'll5', 'll6', 'll7']

for i in range(len(llabels)):
	llabels[i] = Label(cv,text="Lvl:",font="calibri 11")
	llabels[i].place(x=20+90*i,y=7)

lvls = ['lvl1','lvl2','lvl3','lvl4','lvl5','lvl6','lvl7']

for i in range(len(lvls)):
	lvls[i] = ttk.Spinbox(root,from_=1,to=9,increment=2,justify="center")
	lvls[i].place(x=60+90*i,y=10,width=40)
	lvls[i].set(1)

#lvl1 = ttk.Spinbox(cv,from_=1,to=9,increment=2,justify="center")
#lvl1.place(x=60,y=10,width=40)
#lvl1.set(1)





#--------- Camps input -------------------

load1 = PIL.Image.open("None.png")
load1 = load1.resize((50,50),PIL.Image.ANTIALIAS)
render = ImageTk.PhotoImage(load1,master=root)

b1 = Button(cv,text="",image=render,command=ChooseCamp)
b1.place(x=20,y=30,width=80,height=80)

b2 = Button(cv,text="",image=render,command=ChooseCamp)
b2.place(x=110,y=30,width=80,height=80)
b2.configure(state='disabled')

b3 = Button(cv,text="",image=render,command=ChooseCamp)
b3.place(x=200,y=30,width=80,height=80)
b3.configure(state='disabled')

b4 = Button(cv,text="",image=render,command=ChooseCamp)
b4.place(x=290,y=30,width=80,height=80)
b4.configure(state='disabled')

b5 = Button(cv,text="",image=render,command=ChooseCamp)
b5.place(x=380,y=30,width=80,height=80)
b5.configure(state='disabled')

b6 = Button(cv,text="",image=render,command=ChooseCamp)
b6.place(x=470,y=30,width=80,height=80)
b6.configure(state='disabled')

b7 = Button(cv,text="",image=render,command=ChooseCamp)
b7.place(x=560,y=30,width=80,height=80) 
b7.configure(state='disabled')

addb = Button(cv,text="Add",command=AddButton)
addb.place(x=660,y=45,width=80,height=30)

cb = Button(cv,text="Calculate",command=Calculate)
cb.place(x=660,y=75,width=80,height=30)

global ptc

ptc = StringVar()
patch = ttk.Combobox(root,justify="center",textvar=ptc)
patch['values'] = ['11.3','11.4','11.6']
patch.set('11.4')
patch.place(x=660,y=20,width=80)



buttons = [b1,b2,b3,b4,b5,b6,b7]
xps = [XP1,XP2,XP3,XP4,XP5,XP6,XP7]
golds = [G1,G2,G3,G4,G5,G6,G7]

root.mainloop()