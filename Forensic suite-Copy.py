from tkinter import *
import subprocess
from tkinter.filedialog import *
import hashlib


class Welcome():
	def __init__(self,master):
		
		self.master=master
		self.master.geometry('700x500+100+200')
		self.master.title('Forensic Suite')
		#self.master.config(bg='#EDE7F6')
		menu = Menu(master)
		master.config(menu=menu)
		acquisition = Menu(menu)
		menu.add_cascade(label='Acquisition', menu=acquisition)
		acquisition.add_command(label='DD.exe')
		acquisition.add_command(label='DumpIT')
		acquisition.add_command(label='Exit', command=master.quit)

		analysis= Menu(menu)
		menu.add_cascade(label='Analysis', menu=analysis)
		analysis.add_command(label='Photorec')
		analysis.add_command(label='Volatality')
		analysis.add_separator()


		helpmenu = Menu(menu)
		menu.add_cascade(label='Help', menu=helpmenu)
		helpmenu.add_command(label='About')
		helpmenu.add_command(label='Contact')
		
		self.label1=Label(self.master,text='Welcome to Forensic Suite',font="Times 16 bold italic",fg="blue").grid(row=0,column=3)
		
		
		########### Acquisition ############
		self.buttonSubmit = Button(master,text='Acquisition',command=self.acquisition,height = 3, width = 10,bg='#7986CB', font='Times 11 bold').grid(row=1,column=0)
		
		#DD 
		
		self.button2 = Button(master,text="DD.exe",height = 1, width = 10,command=self.dd)
		self.hiddenlabel = Label(master,text="             ").grid(row=1,column=2)
		
		
		#DumpIT
		self.button3= Button(master,text="DumpIT",height = 1, width = 10,command=self.dumpit)
		self.hiddenlabel = Label(master,text="             ").grid(row=2,column=1)
		
		
		############ Analysis ###########
		self.buttonSubmit = Button(master,text='Analysis',command=self.analysis,height = 3, width = 10,bg='#7986CB', font='Times 11 bold')
		self.buttonSubmit.grid(row=3,column=0)
		
		
		#volatality Button 
		self.button5= Button(master,text="Volatality",height = 1, width = 10, command=self.VolTrail)
		self.hiddenlabel = Label(master,text="             ")
		self.hiddenlabel.grid(row=4,column=1)
		
		############ Quit ###########
		
		self.buttonSubmit = Button(master,text='Quit',command=self.finish,height = 3, width = 10,bg='#7986CB', font='Times 11 bold')
		self.buttonSubmit.grid(row=6,column=0)
		
	################ Functions ##################
	def acquisition(self):
		self.hiddenlabel.grid_forget()
		self.button2.grid(row=2,column=2)
		self.button3.grid(row=2,column=3)
	
	def analysis(self):
		self.hiddenlabel.grid_forget()
		self.button5.grid(row=4,column=3)
		
	def finish(self):
		self.master.destroy()
	
	def VolTrail(self):
		root2=Toplevel(self.master)
		myGUI=Volatality(root2)
	
	def dd(self):
		root3=Toplevel(self.master)
		myGUI1=Ddexe(root3)	
		
	def dumpit(self):
		p1=subprocess.Popen('DumpIt.exe',stdin=subprocess.PIPE,stdout=subprocess.PIPE, shell=True)
		

	
class Ddexe():
	def __init__(self,master):
		self.master=master
		master.geometry('700x700')
		self.master.title('DD.exe | Forensic Suite')
		scrollbar=Scrollbar(master)
		scrollbar.pack(side=RIGHT,fill=Y)
		
		menu = Menu(master)
		master.config(menu=menu)
		acquisition = Menu(menu)
		menu.add_cascade(label='Acquisition', menu=acquisition)
		acquisition.add_command(label='DD.exe')
		acquisition.add_command(label='DumpIT')
		acquisition.add_command(label='Exit', command=master.quit)

		analysis= Menu(menu)
		menu.add_cascade(label='Analysis', menu=analysis)
		analysis.add_command(label='Photorec')
		analysis.add_command(label='Volatality')
		analysis.add_separator()


		helpmenu = Menu(menu)
		menu.add_cascade(label='Help', menu=helpmenu)
		helpmenu.add_command(label='About')
		helpmenu.add_command(label='Contact')
		
		textbox = Text(master)
		textbox.pack(side=TOP, fill=Y)
		
		cmnd1 = 'dd --list'
		print(cmnd1)
		p1=subprocess.Popen(cmnd1,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p1.communicate()
		sout = out.decode('utf8')
		scrollbar.config(command=textbox.yview)
		textbox.config(yscrollcommand=scrollbar.set)
		textbox.insert(END,sout)
		
		label1 = Label(master, text="Enter The Address of the Drive to be Cloned, Example: '\\\.\Volume{daacaa4a-0000-0000-0000-600000000000}'", fg='red',padx=5,pady=5)
		self.E1 = Entry(master, bd =7,width=35)
		label2 = Label( master, text="Output location, Example: 'd:\ClonedFileName.img'", fg='red',padx=5,pady=5)
		self.E2 = Entry(master, bd =7,width=35)	

		label1.pack()
		self.E1.pack()
		label2.pack()
		self.E2.pack()
		
		submit = Button(master, text ="Submit", command=self.getData)
		submit.pack(side =TOP) 
		
		submit = Button(master, text ="Quit",command=self.myquit)
		submit.pack(side=TOP)
		
		submit = Label(master, text =" ")
		submit.pack(side=TOP)
		
		hash = Button(master, text ="Find Hash Value",command=self.hash)
		hash.pack(side=TOP)
		
		mainloop()
	
	def hash(self):
		self.filename=askopenfilename(initialdir="C:/Users/bhanu/Desktop/Forensic Suite", title="Select a File To Hash")
		cmd='certutil -hashfile "%s" md5' %(self.filename)
		print(cmd)
		p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err=p.communicate()
		sout = out.decode('utf8')
		print (sout)
		self.savefile = asksaveasfilename(defaultextension='.txt',initialdir="/", filetypes=(("Text Files","*.txt"),("All Files","*.*")))
		out=open(self.savefile,"w")
		out.write(str(sout))
		out.close()
		
	
	def getData(self):
		input_drive=self.E1.get()
		output_location=self.E2.get()
		cmd2 = 'dd if=%s of=%s bs=1M'% (input_drive,output_location)
		print(cmd2)
		p2=subprocess.Popen(cmd2.split(),stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p2.communicate()
		sout = out.decode('utf8')
		print(sout)
		
	def myquit(self):
		self.master.destroy()		
	
class Volatality():
	def __init__(self,master):
		self.master=master
		master.geometry('1400x1250')
		self.master.title('Volatality | Forensic Suite')
		#self.master.wm_attributes("-topmost", 1) #Make Window Float on Top 
		
		####################### Menu Bar ####################### 
		
		menu = Menu(master)
		master.config(menu=menu)
		acquisition = Menu(menu)
		menu.add_cascade(label='Acquisition', menu=acquisition)
		acquisition.add_command(label='DD.exe')
		acquisition.add_command(label='DumpIT')
		acquisition.add_command(label='Exit', command=master.quit)

		analysis= Menu(menu)
		menu.add_cascade(label='Analysis', menu=analysis)
		analysis.add_command(label='Photorec')
		analysis.add_command(label='Volatality')
		analysis.add_separator()


		helpmenu = Menu(menu)
		menu.add_cascade(label='Help', menu=helpmenu)
		helpmenu.add_command(label='About')
		helpmenu.add_command(label='Contact')
		
		
		self.label1=Label(self.master,text='Volatality Dump Analyser ',font="Times 16 bold italic",fg="blue").grid(row=0,column=1)
		
		self.label1=Label(self.master,text="", fg='red').grid(row=2,column=0)
		self.label1=Label(self.master,text="Enter Your Dump File", fg='red').grid(row=3,column=0,sticky=W)
		self.label1=Label(self.master,text="Click Your Image Info", fg='red').grid(row=4,column=0,sticky=W)
		self.label1=Label(self.master,text="Select Your OS Version ", fg='red').grid(row=6,column=0,sticky=W)
		
		self.buttonSubmit = Button(master, text = "Browse", command = self.browsefile, width = 17,height=1).grid(row=3,column=1,sticky=W)
		self.buttonSubmit = Button(master, text = "ImageInfo", width = 17,height=1,command=self.imageOS).grid(row=4,column=1,sticky=W)
		
		
		self.options=["Select An Option", "Win10x64_10586","Win10x64","Win10x86","Win81U1x64","Win81U1x86","Win8SP1x64","Win8SP1x86","Win7SP1x64","Win7SP1x86","WinXPSP3x86","WinXPSP3x64","WinXPSP2x86","WinXPSP2x64"]
		self.selectoption= StringVar()
		self.selectoption.set(self.options[0])
		self.imageinfo= OptionMenu(master, self.selectoption,*self.options,command=self.runoption).grid(row=6,column=1,sticky=W)
		
		self.label1=Label(self.master,text="").grid(row=7,column=0)
		self.button1=Button(self.master,text='Start Process Scan',fg='blue', width =17,height=1,command=self.startscan).grid(row=8,column=1,columnspan=1,rowspan=1,sticky=W)
		self.button1=Button(self.master,text='Start Process List',fg='blue', width =17,height=1,command=self.processlist).grid(row=8,column=1,columnspan=2,rowspan=1)
		self.button1=Button(self.master,text='Start Process Tree',fg='blue', width =17,height=1,command=self.pstree).grid(row=9,column=1,columnspan=1,rowspan=1,sticky=W)
		self.button1=Button(self.master,text='Start Dll List Scan',fg='blue', width =17,height=1,command=self.dlllist).grid(row=9,column=1,columnspan=2,rowspan=1)
		self.button1=Button(self.master,text='Start KDBG Scan',fg='blue', width =17,height=1,command=self.kdbgscan).grid(row=10,column=1,columnspan=1,rowspan=1,sticky=W)
		self.button1=Button(self.master,text='Start KPCR Scan',fg='blue', width =17,height=1,command=self.kpcrscan).grid(row=10,column=1,columnspan=2,rowspan=1)
		self.label1=Label(self.master,text="        ", fg='red').grid(row=11,column=0)
		self.buttonSubmit = Button(master,text='Quit',fg='red',height = 1, width = 17,command=self.myquit).grid(row=10,column=1,sticky=E)
		self.label1=Label(self.master,text="        ", fg='red').grid(row=13,column=0)
		
		
		self.button=Button(self.master,text='Start Net Scan',fg='blue', width =17,height=1,command=self.netscan).grid(row=7,column=1,columnspan=2,rowspan=1)
		self.button=Button(self.master,text='Start Hive Scan',fg='blue', width =17,height=1,command=self.hivescan).grid(row=6,column=1,columnspan=2,rowspan=1)
		self.button=Button(self.master,text='Start MFT Parser',fg='blue', width =17,height=1,command=self.mftparser).grid(row=5,column=1,columnspan=2,rowspan=1)
		
	#	self.label1=Label(self.master,text="1. Select the Dump File ", fg='black').grid(row=3,column=2,sticky=W)
	#	self.label1=Label(self.master,text="2. Click on ImageInfo to find the operating system ", fg='black').grid(row=4,column=2,sticky=W)
	#	self.label1=Label(self.master,text="3. Check Your Operating System Details  in ImageInfo", fg='black').grid(row=5,column=2,sticky=W)
	#	self.label1=Label(self.master,text="4. Select Your Operating System in Dropdown List", fg='black').grid(row=6,column=2,sticky=W)
	#	self.label1=Label(self.master,text="5. Click on Any Operation", fg='black').grid(row=7,column=2,sticky=W)
		
		self.textbox = Text(master,width=150)
		self.textbox.grid(row=12,column=1)
		
		self.buttonSubmit = Button(master,text='Save',fg='red',height = 1, width = 17,command=self.save_file).grid(row=9,column=1,sticky=E)
	
	###################### Functions ########################
	
	def browsefile(self):
		self.filename = askopenfilename(title="Select File",filetypes=(("Memory Dump Files","*.raw"),("All Files","*.*")))
		print (self.filename)
		
	def runoption(self,value):
		self.value=value
		print (self.value)
		
	def startscan(self):
		cmd3='volatality -f "%s" --profile=%s psscan' %(self.filename,self.value)
		print (cmd3)
		p3=subprocess.Popen(cmd3,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p3.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END)
		self.textbox.insert(END,sout)
		
	def imageOS(self):
		cmd='volatality -f "%s" imageinfo' %(self.filename)
		print (cmd)
		p = subprocess.Popen(cmd,stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		out,err = p.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END) 
		self.textbox.insert(END,sout)
		
	def processlist(self):
		cmd5='volatality -f "%s" --profile=%s pslist' %(self.filename,self.value)
		print (cmd5)
		p5=subprocess.Popen(cmd5,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p5.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END)
		self.textbox.insert(END,sout)
	
	def kdbgscan(self):
		cmd6='volatality -f "%s" --profile=%s kdbgscan' %(self.filename,self.value)
		print (cmd6)
		p6=subprocess.Popen(cmd6,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p6.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END)
		self.textbox.insert(END,sout)
		
	def kpcrscan(self):
		cmd7='volatality -f "%s" --profile=%s kpcrscan' %(self.filename,self.value)
		print (cmd7)
		p7=subprocess.Popen(cmd7,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p7.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END)
		self.textbox.insert(END,sout)		

		
	def pstree(self):
		cmd8='volatality -f "%s" --profile=%s pstree' %(self.filename,self.value)
		print (cmd8)
		p8=subprocess.Popen(cmd8,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p8.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END)
		self.textbox.insert(END,sout)			
		
	def dlllist(self):
		cmd9='volatality -f "%s" --profile=%s dlllist' %(self.filename,self.value)
		print (cmd9)
		p9=subprocess.Popen(cmd9,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p9.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END)
		self.textbox.insert(END,sout)	

	def netscan(self):
		cmd9='volatality -f "%s" --profile=%s netscan' %(self.filename,self.value)
		print (cmd9)
		p9=subprocess.Popen(cmd9,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p9.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END)
		self.textbox.insert(END,sout)	

	def hivescan(self):
		cmd9='volatality -f "%s" --profile=%s hivescan' %(self.filename,self.value)
		print (cmd9)
		p9=subprocess.Popen(cmd9,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p9.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END)
		self.textbox.insert(END,sout)	
		
	def mftparser(self):
		cmd9='volatality -f "%s" --profile=%s mftparser' %(self.filename,self.value)
		print (cmd9)
		p9=subprocess.Popen(cmd9,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p9.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END)
		self.textbox.insert(END,sout)	

	def timeline(self):
		cmd9='volatality -f "%s" --profile=%s timeline' %(self.filename,self.value)
		print (cmd9)
		p9=subprocess.Popen(cmd9,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
		out,err = p9.communicate()
		sout = out.decode('utf8')
		self.textbox.delete(1.0,END)
		self.textbox.insert(END,sout)	
			
	def save_file(self):
		self.savefile = asksaveasfilename(defaultextension='.txt',filetypes=(("Text Files","*.txt"),("All Files","*.*")))
		f = open(self.savefile, 'w')
		f.write(self.textbox.get('1.0','end'))
		f.close()
		
	def myquit(self):
		self.master.destroy()

def main():

	root=Tk()
	myGUIWelcome=Welcome(root)
	root.mainloop()
	
if __name__=='__main__':
	main()