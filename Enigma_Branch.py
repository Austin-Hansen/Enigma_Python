#!/usr/bin/python
#alpha, beta, and gamma rotors must be filled upon initialization
#delta applies only to an enigma machine that has 4 rotors and so can
#remain unfilled until the 4 rotor machine is selected
import copy
import sys

class EnigmaSim:

    def __init__(self):

        self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.settings = {'AB': {'I':"DMTWSILRUYQNKFEJCAZBPGXOHV", 'II':"HQZGPJTMOBLNCIFDYAWVEUSRKX", 'III':"UQNTLSZFMREHDPXKIBVYGJCWOA",'UKW':"ABCDEFGHIJKLMNOPQRSTUVWXYZ",'ETW':"ABCDEFGHIJKLMNOPQRSTUVWXYZ"},
        'Rail':{'I':"JGDQOXUSCAMIFRVTPNEWKBLZYH", 'II':"NTZPSFBOKMWRCJDIVLAEYUXHGQ", 'III':"JVIUBHTCDYAKEQZPOSGXNRMWFL", 'UKW':"QYHOGNECVPUZTFDJAXWMKISRBL", 'ETW':"QWERTZUIOASDFGHJKPYXCVBNML"},
        'Swiss':{'I':"PEZUOHXSCVFMTBGLRINQJWAYDK",'II':"ZOUESYDKFWPCIQXHMVBLGNJRAT",'III':"EHRVXGAOBQUSIMZFLYNWKTPDJC" ,'UKW':"IMETCGFRAYSQBZXWLHKDVUPOJN",'ETW':"QWERTZUIOASDFGHJKPYXCVBNML"},
        'EnigmaI':{'I':"EKMFLGDQVZNTOWYHXUSPAIBRCJ",'II':"AJDKSIRUXBLHWTMCQGZNPYFVOE",'III':"BDFHJLCPRTXVZNYEIWGAKMUSQO",'UKW':"EJMZALYXVBWFCRQUONTSPIKHGD",'ETW':"ABCDEFGHIJKLMNOPQRSTUVWXYZ"},
        'M3':{'I':"EKMFLGDQVZNTOWYHXUSPAIBRCJ",'II':"AJDKSIRUXBLHWTMCQGZNPYFVOE",'III':"BDFHJLCPRTXVZNYEIWGAKMUSQO",'IV':"ESOVPZJAYQUIRHXLNFTGKDCMWB",
        'V':"VZBRGITYUPSDNHLXAWMJQOFECK",'VI':"JPGVOUMFYQBENHZRDKASXLICTW",'VII':"JPGVOUMFYQBENHZRDKASXLICTW",'VIII':"FKQHTLXOCBJSPDZRAMEWNIUYGV",'UKW':"EJMZALYXVBWFCRQUONTSPIKHGD",
        'UKWB':"YRUHQSLDPXNGOKMIEBFZCWVJAT",'UKWC':"FVPJIAOYEDRZXWGCTKUQSBNMHL",'UKWBT':"ENKQAUYWJICOPBLMDXZVFTHRGS",'UKCT':"RDOBJNTKVEHMLFCWZAXGYIPSUQ",'ETW':"ABCDEFGHIJKLMNOPQRSTUVWXYZ"},
        'M4':{'I':"EKMFLGDQVZNTOWYHXUSPAIBRCJ",'II':"AJDKSIRUXBLHWTMCQGZNPYFVOE",'III':"BDFHJLCPRTXVZNYEIWGAKMUSQO",'IV':"ESOVPZJAYQUIRHXLNFTGKDCMWB",'V':"VZBRGITYUPSDNHLXAWMJQOFECK",
        'VI':"JPGVOUMFYQBENHZRDKASXLICTW",'VII':"JPGVOUMFYQBENHZRDKASXLICTW",'VIII':"FKQHTLXOCBJSPDZRAMEWNIUYGV", 'Beta': "LEYJVCNIXWPBQMDRTAKZGFUHOS",'Gamma':"FSOKANUERHMBTIYCWLQPZXVGJD",
        'UKW':"EJMZALYXVBWFCRQUONTSPIKHGD",'UKWB':"YRUHQSLDPXNGOKMIEBFZCWVJAT",'UKWC':"FVPJIAOYEDRZXWGCTKUQSBNMHL",'UKWBT':"ENKQAUYWJICOPBLMDXZVFTHRGS",'UKCT':"RDOBJNTKVEHMLFCWZAXGYIPSUQ",'ETW':"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}}


        #might be able to condense these settings to a collection, likely a list or dictionary
        self.alpha = list(self.settings['M3']['I'])
        self.beta = list(self.settings['M3']['II'])
        self.gamma = list(self.settings['M3']['III'])
        self.delta = []
        self.UKW = list(self.settings['M3']['UKWB'])
        #self.rUKW = self.UKW[::-1]
        self.ETW = list(self.settings['M3']['ETW'])
        self.Plugboard = copy.deepcopy(self.alphabet)
        self.machine ='M3'
        self.rotors_order = [copy.deepcopy(self.UKW),copy.deepcopy(self.alpha),copy.deepcopy(self.beta),copy.deepcopy(self.gamma),copy.deepcopy(self.ETW),copy.deepcopy(self.Plugboard)]
        #rotor alphabets is 1 larger than the default setting so that we can add a delta rotor more easily
        self.rotor_alphabets = [copy.deepcopy(self.alphabet),copy.deepcopy(self.alphabet),copy.deepcopy(self.alphabet),copy.deepcopy(self.alphabet),copy.deepcopy(self.alphabet),copy.deepcopy(self.alphabet),copy.deepcopy(self.alphabet)]
        self.rotor_alphabets_copy = copy.deepcopy(self.rotor_alphabets)
        self.debug_rotor_names = ["UKW","Alpha","Beta","Gamma","ETW","Plugboard"]

        self.positions = [0,0,0,0]
        self.permutations = 0

    def rotor_up_one(self, rotor):

        letter = rotor.pop(0)
        rotor.append(letter)

        return rotor

    def rotor_down_one(self, rotor):

        letter = rotor.pop()
        #print(letter)
        rotor.insert(0,letter)

        return rotor

    #try 3 case Enigma first
    def encrypt_letter(self,letter):

            #what is the index of the letter entered (A=0,B=1, etc...)
            index = self.Plugboard.index(letter)

            #ETW to Gamma

            for i in range(len(self.rotors_order)-1,-1,-1):

    
                #if not double stepping, step the gamma rotor, and once this rotor finishes step the beta rotor and so forth
                if(i== len(self.rotors_order)-3):

                    self.rotor_up_one(self.rotors_order[3])
                    self.rotor_up_one(self.rotor_alphabets[3])
                    self.positions[i-1]+1

                    #print(self.positions)

                    #from delta, step gamma
                    if(self.positions[3]==25):
                        self.rotor_up_one(self.rotors_order[4])
                        self.rotor_up_one(self.rotor_alphabets[4])
                        self.positions[2]+1
                        self.positions[3]=0
                        print(self.positions[2])

                    #from gamma, step beta
                    if(self.positions[2]==25):

                        self.rotor_up_one(self.rotors_order[2])
                        self.rotor_up_one(self.rotor_alphabets[2])
                        self.positions[1]+1
                        self.positions[2]=0
                        print(self.positions[1])

                    #from beta, step alpha
                    if(self.positions[1]==25):

                        self.rotor_up_one(self.rotors_order[1])
                        self.rotor_up_one(self.rotor_alphabets[1])
                        self.positions[0]+1
                        self.positions[1]=0

                    #alpha is maxed out, set to zero
                    if(self.positions[0]==25):

                        self.rotor_up_one(self.rotors_order[0])
                        self.rotor_up_one(self.rotor_alphabets[0])
                        self.positions[0]=0







                letter = self.rotors_order[i][index]

                #print("Name: "+ self.debug_rotor_names[i])
                #print("Letter: " + letter)
                #print("Rotor Alphabet equivalent: "+ self.rotor_alphabets[i][index])
                #print(self.rotor_alphabets[i])
                #print("Index: "+ str(index))

                index = self.rotor_alphabets[i].index(letter)
                #print()

            #print()
            #print("Second Half")
            #print()

            #going back the reverse direction, we don't have to worry about changing the rotors

            for i in range(1,len(self.rotors_order)):

                letter = self.rotor_alphabets[i][index]
                #print("Name: "+ self.debug_rotor_names[i])
                #print("Letter: " + letter)
                #print("Rotor Alphabet equivalent: "+ self.rotor_alphabets[i][index])
                #print(self.rotor_alphabets[i])
                index = self.rotors_order[i].index(letter)
                #print("Index: "+ str(index))
                #print()

            return letter

    #This will reset the machine to it's original default settings, it cannot go back to its previous state
    def change_machine_defaults(self,machine):

        self.alpha = list(self.settings[machine]['I'])
        self.beta = list(self.settings[machine]['II'])
        self.gamma = list(self.settings[machine]['III'])
        self.delta = None
        self.UKW = list(self.settings[machine]['UKW'])
        self.ETW = list(self.settings[machine]['ETW'])
        self.Plugboard = copy.deepcopy(self.alphabet)
        self.machine = machine
        self.rotors_order = [copy.deepcopy(self.UKW),copy.deepcopy(self.alpha),copy.deepcopy(self.beta),copy.deepcopy(self.gamma),copy.deepcopy(self.ETW),copy.deepcopy(self.Plugboard)]
        self.debug_rotor_names = ["UKW","Alpha","Beta","Gamma","ETW","Plugboard"]


        if((machine == 'M4') or (machine == "M4")):
            self.delta = list(self.settings[machine]['IV'])
            self.debug_rotor_names = ["UKW","Alpha","Beta","Gamma","Delta","ETW","Plugboard"]
            #print(self.debug_rotor_names)
            self.rotors_order = [copy.deepcopy(self.UKW),copy.deepcopy(self.alpha),copy.deepcopy(self.beta),copy.deepcopy(self.gamma),copy.deepcopy(self.delta),copy.deepcopy(self.ETW),copy.deepcopy(self.Plugboard)]

    #Add ability to change out rotors specific to a machine

    #Add ability to put message in .txt file and name it EnigmaOutput-<number>.txt or give it a custom name

    #Add the ability to adjust the Plugboard

    #Add the ability to scramble the Plugboard


    def encrypt(self,text):

        new_text = list(text.upper())
        encrypted_text = []
        self.change_machine_defaults('M4')


        for i in range(0,len(new_text)):

            if(new_text[i] != ' '):
                encrypted_text.append(self.encrypt_letter(new_text[i]))
            else:
                encrypted_text.append(' ')

        return "".join(encrypted_text)

    def get_alphabet(self):
        return self.alphabet

    def get_rotor_alphabet(self):
        return self.rotor_alphabets

    def get_rotor_order_alph(self):
        return self.rotors_order
  
EnigmaMachine = EnigmaSim()
print(EnigmaMachine.encrypt("DUCK"))
sys.stdout.write( "Hello Standard Output!\n" )
sys.stderr.write( "Hello Standard Error!\n" )

#return EnigmaMachine.encrypt("DUCK")