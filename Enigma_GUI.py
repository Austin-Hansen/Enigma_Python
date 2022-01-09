import tkinter as tk
from tkinter import *
from Enigma_Branch import EnigmaSim


class Enigma_GUI:

	def __init__(self):
		self.root = tk.Tk()
		self.root.attributes('-fullscreen', True)
		self.root.configure(background='#838B8B')
		self.fullScreenState = False
		self.root.bind("<F11>", self.toggleFullScreen)
		self.root.bind("<Escape>", self.quitFullScreen)
		self.root.title('Enigma Sim - Alpha 0.1')
		self.EnigmaVersion = StringVar(value="A")

		self.EnigmaMachine = EnigmaSim()

		temp1=[]
		temp2=[]

		self.rotor_alphabets_var = []
		self.rotors_order_var=[]

		#Unfortunately, it was impossible to cleanly update the letters for the individual rotors, had to make these new 
		#arrays
		print(len(self.EnigmaMachine.rotor_alphabets))
		print(len(self.EnigmaMachine.rotors_order))

		for i in range(0,len(self.EnigmaMachine.rotor_alphabets)-1):
			for j in range(0,len(self.EnigmaMachine.alphabet)):

				temp1.append(StringVar(value=self.EnigmaMachine.rotor_alphabets[i][j]))
				temp2.append(StringVar(value=self.EnigmaMachine.rotors_order[i][j]))
				#print(temp2[j].get())
			#print(i)
			#print()

			self.rotor_alphabets_var.append(temp1)
			self.rotors_order_var.append(temp2)

			temp1=[]
			temp2=[]

		#Project title 
		Label(self.root, text='Enigma - Alpha Version 0.1', bg='#838B8B', font=('arial', 12, 'normal'),borderwidth=1, relief="solid").grid(row=0,column=0,columnspan=6,sticky='nwse')
		
		#Plug Setting, input, Machine Version, and reset button (Row 1)
		Label(self.root, text='Plugboard Settings', bg='#838B8B', font=('arial', 12, 'normal'),borderwidth=1, relief="solid").grid(row=1,column=0,sticky='nwse')
		self.PlugInput = Entry(self.root).grid(row=1,column=1,columnspan=3,sticky='we')
		self.resetFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid").grid(row=1,column=5,columnspan=1,sticky='nwse')
		self.reset = Button(self.resetFrame, text = 'Reset', bd = '5',justify='center').grid(row=1,column=5,columnspan=1,sticky='nwse')
		self.FileToggleFrame = Frame(self.root)
		self.FileToggleFrame.grid(row=1,column=4,columnspan=1,sticky='nswe')

		#File Toggle maker
		self.filelabel = Label(self.FileToggleFrame, text='Output Type', bg='#838B8B', font=('arial', 12, 'normal'),borderwidth=1, relief="solid").grid(row=0,column=0,columnspan=2,sticky='nwse')
		self.OutputLineButton = Button(self.FileToggleFrame, text = 'Line', bd = '5').grid(row=1,column=0,columnspan=1,sticky='nwse')
		self.FileButton = Button(self.FileToggleFrame, text = 'File', bd = '5').grid(row=1,column=1,columnspan=1,sticky='nwse')

		#Ring settings, positions(0-25)x3, Enigma Version: (ver)
		self.PositionFrames = Frame(self.root)
		self.PositionFrames.grid(row=2,column=1,columnspan=3,sticky='nswe')

		Label(self.root, text='Ring Settings', bg='#838B8B', font=('arial', 12, 'normal'),borderwidth=1, relief="solid").grid(row=2,column=0,columnspan=1,sticky='nwse')
		self.Position1 = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.Position1.grid(row=2,column=1,columnspan=1,sticky='nswe')
		self.Position2 = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.Position2.grid(row=2,column=2,columnspan=1,sticky='nswe')
		self.Position3 = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.Position3.grid(row=2,column=3,columnspan=1,sticky='nswe')
		self.EnigmaVersionFrame = Frame(self.root,bg='white',borderwidth=1, relief="solid")
		self.EnigmaVersionFrame.grid(row=2,column=4,columnspan=2,sticky='nswe')
		self.EnigmaVersionFrame.columnconfigure(0,weight=0)
		self.EnigmaVersionFrame.columnconfigure(1,weight=1)


		#put the enigma rotor position labels in the proper order
		Label(self.Position1, text='Position:', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0,column=0,columnspan=1,sticky='nwes')
		Label(self.Position2, text='Position:', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0,column=0,columnspan=1,sticky='nwes')
		Label(self.Position3, text='Position:', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0,column=0,columnspan=1,sticky='nwes')

		self.alpha_position=Label(self.Position1, text='0', bg='#838B8B', font=('arial', 12, 'normal'),).grid(row=0,column=1,columnspan=1,sticky='nwes')
		self.beta_position = Label(self.Position2, text='0', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0,column=1,columnspan=1,sticky='nwes')
		self.gamma_position = Label(self.Position3, text='0', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0,column=1,columnspan=1,sticky='nwes')

		#Enigma Version
		Label(self.EnigmaVersionFrame, text='Enigma Machine Version: ', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid").grid(row=0,column=0,columnspan=1,sticky='nwes')
		Label(self.EnigmaVersionFrame, textvariable=self.EnigmaVersion, bg='#838B8B', font=('arial', 12, 'normal'),relief="solid").grid(row=0,column=1,columnspan=2,sticky='nwes')


		self.UKWFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.UKWFrame.columnconfigure(0,weight=0)
		self.UKWFrame.columnconfigure(1,weight=2)
		self.UKWFrame.grid(row=3,column=0,columnspan=1,sticky='nswe')

		Label(self.UKWFrame, text='UKW', bg='#838B8B', font=('arial', 12, 'normal'),width=3).grid(row=0,column=0,columnspan=3,sticky='nwes')
		Button(self.UKWFrame, text='<<', font=('arial', 12, 'normal'),width=3).grid(row=1,column=0,columnspan=1,sticky='nwes')
		Label(self.UKWFrame, text='A', bg='#838B8B', font=('arial', 12, 'normal'),width=3).grid(row=1,column=1,columnspan=1,sticky='nwes')
		Button(self.UKWFrame, text='>>', font=('arial', 12, 'normal'),width=3).grid(row=1,column=2,columnspan=1,sticky='nwes')

		#Alpha Rotor
		self.AlphaFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.AlphaFrame.grid(row=3,column=1,columnspan=1,sticky='nswe')

		self.AlphaFrame.columnconfigure(1,weight=2)

		Label(self.AlphaFrame, text='Alpha Rotor', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid",width=3).grid(row=0,column=0,columnspan=3,sticky='nwes')
		Button(self.AlphaFrame, text='<<', font=('arial', 12, 'normal'),relief="solid",width=3).grid(row=1,column=0,columnspan=1,sticky='nwes')
		Label(self.AlphaFrame, text='I', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid",width=3).grid(row=1,column=1,columnspan=1,sticky='nwes')
		Button(self.AlphaFrame, text='>>', font=('arial', 12, 'normal'),relief="solid",width=3).grid(row=1,column=2,columnspan=1,sticky='nwes')

		#Beta Rotor
		self.BetaFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.BetaFrame.grid(row=3,column=2,columnspan=1,sticky='nswe')

		self.BetaFrame.columnconfigure(1,weight=2)

		Label(self.BetaFrame, text='Beta Rotor', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid",width=3).grid(row=0,column=0,columnspan=3,sticky='nwes')
		Button(self.BetaFrame, text='<<', width=3, font=('arial', 12, 'normal'),relief="solid").grid(row=1,column=0,columnspan=1,sticky='nwes')
		Label(self.BetaFrame, text='II', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid",width=3).grid(row=1,column=1,columnspan=1,sticky='nwes')
		Button(self.BetaFrame, text='>>', width=3, font=('arial', 12, 'normal'),relief="solid").grid(row=1,column=2,columnspan=1,sticky='nwes')

		#Gamma Rotor
		self.GammaFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.GammaFrame.grid(row=3,column=3,columnspan=1,sticky='nswe')

		self.GammaFrame.columnconfigure(1,weight=2)

		Label(self.GammaFrame, text='Gamma Rotor', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid",width=3).grid(row=0,column=0,columnspan=3,sticky='nwes')
		Button(self.GammaFrame, text='<<', font=('arial', 12, 'normal'),relief="solid",width=3).grid(row=1,column=0,columnspan=1,sticky='nwes')
		Label(self.GammaFrame, text='III', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid",width=3).grid(row=1,column=1,columnspan=1,sticky='nwes')
		Button(self.GammaFrame, text='>>', font=('arial', 12, 'normal'),relief="solid",width=3).grid(row=1,column=2,columnspan=1,sticky='nwes')


		Label(self.root, text='ETW', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid",width=9).grid(row=3,column=4,columnspan=1,sticky='nwes')
		Label(self.root, text='PlugBoard', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid",width=15).grid(row=3,column=5,columnspan=1,sticky='nwes')

		#Frames for the rotors themselves
		self.UKWFullFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.UKWFullFrame.grid(row=4,column=0,columnspan=1,sticky='nswe')

		self.AlphaFullFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.AlphaFullFrame.grid(row=4,column=1,columnspan=1,sticky='nswe')

		self.BetaFullFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.BetaFullFrame.grid(row=4,column=2,columnspan=1,sticky='nswe')

		self.GammaFullFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.GammaFullFrame.grid(row=4,column=3,columnspan=1,sticky='nswe')


		self.ETWFullFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.ETWFullFrame.grid(row=4,column=4,columnspan=1,sticky='nswe')
		
		self.PlugBoardFullFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.PlugBoardFullFrame.grid(row=4,column=5,columnspan=1,sticky='nswe')

		#rotor columns, update via textvariable
		for i in range(len(self.EnigmaMachine.alphabet),0,-1):

			Label(self.UKWFullFrame, textvariable=self.rotors_order_var[0][i-1], bg='#838B8B', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=0,columnspan=1,sticky='nwes')
			self.UKWFullFrame.columnconfigure(1,weight=2)
			Label(self.UKWFullFrame, text='', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0+i,column=1,columnspan=1,sticky='nwes')
			Label(self.UKWFullFrame, textvariable=self.rotor_alphabets_var[0][i-1], bg='#838B8B', font=('arial', 12, 'normal'),relief="raised",anchor='w').grid(row=0+i,column=2,columnspan=1,sticky='nwes')

			Label(self.AlphaFullFrame, textvariable=self.rotors_order_var[1][i-1], bg='red', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=0,columnspan=1,sticky='nwes')
			self.AlphaFullFrame.columnconfigure(1,weight=2)
			Label(self.AlphaFullFrame, text='', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0+i,column=1,columnspan=1,sticky='nwes')
			Label(self.AlphaFullFrame, textvariable=self.rotor_alphabets_var[1][i-1], bg='blue', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=2,columnspan=1,sticky='nwes')

			Label(self.BetaFullFrame, textvariable=self.rotors_order_var[2][i-1], bg='#838B8B', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=0,columnspan=1,sticky='nwes')
			self.BetaFullFrame.columnconfigure(1,weight=2)
			Label(self.BetaFullFrame, text='', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0+i,column=1,columnspan=1,sticky='nwes')
			Label(self.BetaFullFrame, textvariable=self.rotor_alphabets_var[2][i-1], bg='#838B8B', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=2,columnspan=1,sticky='nwes')

			Label(self.GammaFullFrame, textvariable=self.rotors_order_var[3][i-1], bg='#838B8B', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=0,columnspan=1,sticky='nwes')
			self.GammaFullFrame.columnconfigure(1,weight=2)
			Label(self.GammaFullFrame, text='', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0+i,column=1,columnspan=1,sticky='nwes')
			Label(self.GammaFullFrame, textvariable=self.rotor_alphabets_var[3][i-1], bg='#838B8B', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=2,columnspan=1,sticky='nwes')

			Label(self.ETWFullFrame, text=self.EnigmaMachine.rotors_order[4][i-1], bg='#838B8B', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=0,columnspan=1,sticky='nwes')
			self.ETWFullFrame.columnconfigure(1,weight=2)
			Label(self.ETWFullFrame, text='', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0+i,column=1,columnspan=1,sticky='nwes')
			Label(self.ETWFullFrame, text=self.EnigmaMachine.rotor_alphabets[4][i-1], bg='#838B8B', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=2,columnspan=1,sticky='nwes')

			Label(self.PlugBoardFullFrame, text=self.EnigmaMachine.rotors_order[5][i-1], bg='#838B8B', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=0,columnspan=1,sticky='nwes')
			self.PlugBoardFullFrame.columnconfigure(1,weight=2)
			Label(self.PlugBoardFullFrame, text='', bg='#838B8B', font=('arial', 12, 'normal')).grid(row=0+i,column=1,columnspan=1,sticky='nwes')
			Label(self.PlugBoardFullFrame, text=self.EnigmaMachine.rotor_alphabets[5][i-1], bg='#838B8B', font=('arial', 12, 'normal'),relief="raised").grid(row=0+i,column=2,columnspan=1,sticky='nwes')

		#Position of Letters Frames
		self.UKWLetterFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.UKWLetterFrame.grid(row=5,column=0,columnspan=1,sticky='nswe')
		self.AlphaLetterFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.AlphaLetterFrame.grid(row=5,column=1,columnspan=1,sticky='nswe')
		self.BetaLetterFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.BetaLetterFrame.grid(row=5,column=2,columnspan=1,sticky='nswe')
		self.GammaLetterFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.GammaLetterFrame.grid(row=5,column=3,columnspan=1,sticky='nswe')


		#Position Selector for letter rotor
		self.UKWLetterFrame.columnconfigure(1,weight=2)
		Button(self.UKWLetterFrame, text='<<', font=('arial', 12, 'normal'),relief="solid").grid(row=1,column=0,columnspan=1,sticky='nwes')
		Label(self.UKWLetterFrame, textvariable=self.rotor_alphabets_var[0][0], bg='#838B8B', font=('arial', 12, 'normal'),relief="solid").grid(row=1,column=1,columnspan=1,sticky='nwes')
		Button(self.UKWLetterFrame, text='>>', font=('arial', 12, 'normal'),relief="solid").grid(row=1,column=2,columnspan=1,sticky='nwes')

		self.AlphaLetterFrame.columnconfigure(1,weight=2)
		Button(self.AlphaLetterFrame, text='<<', font=('arial', 12, 'normal'),relief="solid",command=lambda: self.move_rotor(1,1)).grid(row=1,column=0,columnspan=1,sticky='nwes')
		Label(self.AlphaLetterFrame, textvariable=self.rotor_alphabets_var[1][0], bg='#838B8B', font=('arial', 12, 'normal'),relief="solid").grid(row=1,column=1,columnspan=1,sticky='nwes')
		Button(self.AlphaLetterFrame, text='>>', font=('arial', 12, 'normal'),relief="solid",command=lambda: self.move_rotor(1,3)).grid(row=1,column=2,columnspan=1,sticky='nwes')

		self.BetaLetterFrame.columnconfigure(1,weight=2)
		Button(self.BetaLetterFrame, text='<<', font=('arial', 12, 'normal'),relief="solid",command=lambda: self.move_rotor(2,1)).grid(row=1,column=0,columnspan=1,sticky='nwes')
		Label(self.BetaLetterFrame, textvariable=self.rotor_alphabets_var[2][0], bg='#838B8B', font=('arial', 12, 'normal'),relief="solid").grid(row=1,column=1,columnspan=1,sticky='nwes')
		Button(self.BetaLetterFrame, text='>>', font=('arial', 12, 'normal'),relief="solid",command=lambda: self.move_rotor(2,3)).grid(row=1,column=2,columnspan=1,sticky='nwes')

		self.GammaLetterFrame.columnconfigure(1,weight=2)
		Button(self.GammaLetterFrame, text='<<', font=('arial', 12, 'normal'),relief="solid",command=lambda: self.move_rotor(3,1)).grid(row=1,column=0,columnspan=1,sticky='nwes')
		Label(self.GammaLetterFrame, textvariable=self.rotor_alphabets_var[3][0], bg='#838B8B', font=('arial', 12, 'normal'),relief="solid").grid(row=1,column=1,columnspan=1,sticky='nwes')
		Button(self.GammaLetterFrame, text='>>', font=('arial', 12, 'normal'),relief="solid",command=lambda: self.move_rotor(3,3)).grid(row=1,column=2,columnspan=1,sticky='nwes')


		#set up the main input line
		Label(self.root, text='Input', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid").grid(row=6,column=0,columnspan=1,sticky='nwes')
		self.TInput=Entry(self.root)
		self.TInput.bind('<Return>',self.encrypt_input)
		self.TInput.grid(row=6,column=1,columnspan=3,sticky='nwes')

		#Set up Output line
		Label(self.root, text='Output', bg='#838B8B', font=('arial', 12, 'normal'),relief="solid").grid(row=7,column=0,columnspan=1,sticky='nwes')
		self.dynamic = StringVar()
		self.dynamic = ""
		self.Output = Entry(self.root)
		self.Output.grid(row=7,column=1,columnspan=3,sticky='nwes')

		#Selection for the different machines
		self.MachineSelecionFrame = Frame(self.root,bg='#838B8B',borderwidth=1, relief="solid")
		self.MachineSelecionFrame.grid(row=8,column=0,columnspan=6,sticky='nswe')
		Label(self.MachineSelecionFrame, text='Machine Selection', bg='#838B8B', font=('arial', 12, 'normal')).pack(side='left')
		Button(self.MachineSelecionFrame, text='A/B', font=('arial', 12, 'normal'),relief="solid",command=lambda:self.update_enigma_machine_presets('A/B')).pack(side='left',expand='true')
		Button(self.MachineSelecionFrame, text='C', font=('arial', 12, 'normal'),relief="solid",command=lambda:self.update_enigma_machine_presets('C')).pack(side='left',expand='true')
		Button(self.MachineSelecionFrame, text='Enigma I', font=('arial', 12, 'normal'),relief="solid",command=lambda:self.update_enigma_machine_presets('Enigma I')).pack(side='left',expand='true')
		Button(self.MachineSelecionFrame, text='Swiss K', font=('arial', 12, 'normal'),relief="solid",command=lambda:self.update_enigma_machine_presets('Swiss K')).pack(side='left',expand='true')
		Button(self.MachineSelecionFrame, text='Rail', font=('arial', 12, 'normal'),relief="solid",command=lambda:self.update_enigma_machine_presets('Rail')).pack(side='left',expand='true')
		Button(self.MachineSelecionFrame, text='M3 Army', font=('arial', 12, 'normal'),relief="solid",command=lambda:self.update_enigma_machine_presets('M3 Army')).pack(side='left',expand='true')



		# Create a Button
		btn = Button(self.root, text = 'Exit', bd = '5',command = self.root.destroy)
		# Set the position of button on the top of rootw
		btn.grid(row=6,column=5)

		self.root.mainloop()

	def toggleFullScreen(self, event):
		self.fullScreenState = not self.fullScreenState
		self.root.attributes("-fullscreen", self.fullScreenState)

	def quitFullScreen(self, event):
		self.fullScreenState = False
		self.root.attributes("-fullscreen", self.fullScreenState)

	#Encryption and Entry handling here
	def returnEntry(self,event=None):
		userInput = self.TInput.get()
		print("Function input")
		print(userInput)
		self.Output.delete(0,END)
		return userInput

	def encrypt_input(self,event=None):
		result = self.returnEntry()
		result = self.EnigmaMachine.encrypt(result)
		self.Output.insert(0,result)

		for i in range(0,4):
			for j in range(len(self.EnigmaMachine.alphabet)):
				self.rotor_alphabets_var[i][j].set(self.EnigmaMachine.rotor_alphabets[i][j])			
				self.rotors_order_var[i][j].set(self.EnigmaMachine.rotors_order[i][j])

	def update_enigma_machine_presets(self,EnigmaModel):
		self.EnigmaVersion.set(EnigmaModel)

		


	def move_rotor(self,rotnum,update_type):
		#Only the 'Alphabet' rotor has been updated (this behaves like we rewired it)
		if(update_type==0):
			print(self.EnigmaMachine.rotor_alphabets[rotnum])
			self.EnigmaMachine.rotor_down_one(self.EnigmaMachine.rotor_alphabets[rotnum])
			print(self.EnigmaMachine.rotor_alphabets[rotnum])

			for i in range(len(self.EnigmaMachine.alphabet)):
				self.rotor_alphabets_var[rotnum][i].set(self.EnigmaMachine.rotor_alphabets[rotnum][i])
		#Full rotor movement, both alphabets step once
		if(update_type==1):
			print(self.EnigmaMachine.rotors_order[rotnum])
			self.EnigmaMachine.rotor_down_one(self.EnigmaMachine.rotor_alphabets[rotnum])
			self.EnigmaMachine.rotor_down_one(self.EnigmaMachine.rotors_order[rotnum])
			print(self.EnigmaMachine.rotors_order[rotnum])

			for i in range(len(self.EnigmaMachine.alphabet)):
				self.rotor_alphabets_var[rotnum][i].set(self.EnigmaMachine.rotor_alphabets[rotnum][i])			
				self.rotors_order_var[rotnum][i].set(self.EnigmaMachine.rotors_order[rotnum][i])

		if(update_type == 2):
			self.EnigmaMachine.rotor_up_one(self.EnigmaMachine.rotor_alphabets[rotnum])

			for i in range(len(self.EnigmaMachine.alphabet)):
				self.rotor_alphabets_var[rotnum][i].set(self.EnigmaMachine.rotor_alphabets[rotnum][i])

		if(update_type==3):
			self.EnigmaMachine.rotor_up_one(self.EnigmaMachine.rotor_alphabets[rotnum])
			self.EnigmaMachine.rotor_up_one(self.EnigmaMachine.rotors_order[rotnum])

			for i in range(len(self.EnigmaMachine.alphabet)):
				self.rotor_alphabets_var[rotnum][i].set(self.EnigmaMachine.rotor_alphabets[rotnum][i])			
				self.rotors_order_var[rotnum][i].set(self.EnigmaMachine.rotors_order[rotnum][i])

if __name__ == '__main__':
	app = Enigma_GUI()    
