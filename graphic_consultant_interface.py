import tkinter as tk
import consultant
import re


fenetre=tk.Tk()
(LF,HF)=(fenetre.winfo_screenwidth(),fenetre.winfo_screenheight())

class Interface (tk.Frame) :
    def __init__ ( self , fenetre , ** kwargs ) :
        tk.Frame.__init__ ( self , fenetre , **kwargs )
        self.pack(fill='both')
        self.science_note=0
        self.security_note=0
        self.program_note=0
        self.network_note=0
        self.next1=False
        self.next2=False
        self.next3=False
        self.next4=False
        self.print_graphic_result=False
        self.user_name=tk.StringVar()
        self.question1=tk.StringVar()
        self.answer_to_question1=False
        self.question2=tk.StringVar()
        self.answer_to_question2=False
        self.question3=tk.StringVar()
        self.answer_to_question3=False
        self.question4=tk.StringVar()
        self.answer_to_question4=False
        self.question5=tk.StringVar()
        self.answer_to_question5=False
        self.question6=tk.StringVar()
        self.answer_to_question6=False
        self.question71=tk.IntVar()
        self.checked_case71=False
        self.question72=tk.IntVar()
        self.checked_case72=False
        self.question73=tk.IntVar()
        self.checked_case73=False
        self.question74=tk.IntVar()
        self.checked_case74=False
        self.question75=tk.IntVar()
        self.checked_case75=False
        self.question81=tk.IntVar()
        self.checked_case81=False
        self.question82=tk.IntVar()
        self.checked_case82=False
        self.question83=tk.IntVar()
        self.checked_case83=False
        self.question84=tk.IntVar()
        self.checked_case84=False
        self.question85=tk.IntVar()
        self.checked_case85=False
        self.question86=tk.IntVar()
        self.checked_case86=False
        self.question87=tk.IntVar()
        self.checked_case87=False
        self.question88=tk.IntVar()
        self.checked_case88=False
        self.question9=tk.StringVar()
        self.answer_to_question9=False
        

        # *************************   SECTION 1: Identification   *****************************
        # Definition et affichage du cadre representant cette section 
        self.name_area=tk.LabelFrame(self,width=LF,height=HF/13,borderwidth=5)
        self.name_area.pack(fill='x')
        # Definition et affichage des widgets contenus dans ce premier cadre
        self.label_name=tk.Label(self.name_area,text='Avant de commencer, veillez entrer ici votre nom,\
puis cliquer sur continuer1:')
        self.label_name.place(rely=0.3,relx=0.01,relwidth=0.5)
        self.input_name =tk.Entry( self.name_area , textvariable = self.user_name , width = 100 )
        self.input_name.place (rely=0.2,relx=0.55,relwidth=0.3,relheight=0.6)
        self.btn_next1=tk.Button(self.name_area,text='Continuer1',bg='blue',fg='white',\
                                command=self.click_on_btn_next1)
        self.btn_next1.place(rely=0.1,relx=0.9,relwidth=0.1,relheight=0.8)
        # *******************************************************************************************
        # ****************************   SECTION 2: Bienvenue   *******************************
        # Definition du cadre representant cette section
        self.welcome_area=tk.LabelFrame(self,width=LF/5,height=10*HF/13,borderwidth=5,bg='green')
        # Definition des widgets contenus dans ce  cadre
        self.label_welcome=tk.Label(self.welcome_area,text="")
        self.label_advice=tk.Label(self.welcome_area,text="Veillez a bien reflechir\navant de \
selectionner\n un option ou de cocher une case,\n car seule votre premier choix\n sera consideré.",fg='blue')
        self.label_continuer2=tk.Label(self.welcome_area,text='Pour passer a la suite,\n\
cliquez sur continuer2.',fg='red')
        self.btn_next2=tk.Button(self.welcome_area,text='Continuer2',bg='blue',fg='white',\
                                command=self.click_on_btn_next2)
        # *******************************************************************************************
        # ********************************   SECTION 3: Notes  *********************************   
        # Definition du cadre representant cette section
        self.orientation_area1=tk.LabelFrame(self,width=4*LF/5,height=3*HF/13,borderwidth=10,\
                                            text="Questions d'ordre academique")
        # Definition des widgets contenus dans ce  cadre
        self.label_question1=tk.Label(self.orientation_area1,text="1) Quelle note avez-vous \
obtenu en Algorithme et Programmation?")
        self.answer11=tk.Radiobutton(self.orientation_area1,text='Entre 0 et 10',value='a1',\
                                    variable=self.question1,command=self.check_buttonUE355)
        self.answer12=tk.Radiobutton(self.orientation_area1,text='Entre 10 et 15',value='a2',\
                                    variable=self.question1,command=self.check_buttonUE355)
        self.answer13=tk.Radiobutton(self.orientation_area1,text='Entre 15 et 20',value='a3',\
                                    variable=self.question1,command=self.check_buttonUE355)
        #                             <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>     
        self.label_question2=tk.Label(self.orientation_area1,text="2) Quelle note avez-vous \
obtenu en Signaux et Traitement du Signal?")
        self.answer21=tk.Radiobutton(self.orientation_area1,text='Entre 0 et 10',value='a1',\
                                    variable=self.question2,command=self.check_buttonUE325)
        self.answer22=tk.Radiobutton(self.orientation_area1,text='Entre 10 et 15',value='a2',\
                                    variable=self.question2,command=self.check_buttonUE325)
        self.answer23=tk.Radiobutton(self.orientation_area1,text='Entre 15 et 20',value='a3',\
                                    variable=self.question2,command=self.check_buttonUE325)
        #                             <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>     
        self.label_question3=tk.Label(self.orientation_area1,text="3) Quelle note avez-vous \
obtenu en Base de Donnees et Systemes d'Information?")
        self.answer31=tk.Radiobutton(self.orientation_area1,text='Entre 0 et 10',value='a1',\
                                    variable=self.question3,command=self.check_buttonUE335)
        self.answer32=tk.Radiobutton(self.orientation_area1,text='Entre 10 et 15',value='a2',\
                                    variable=self.question3,command=self.check_buttonUE335)
        self.answer33=tk.Radiobutton(self.orientation_area1,text='Entre 15 et 20',value='a3',\
                                    variable=self.question3,command=self.check_buttonUE335)
        #                             <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>     
        self.label_question4=tk.Label(self.orientation_area1,text="4) Quelle note avez-vous \
obtenu en Architecture des Ordis et Systemes d'Exploitation?")
        self.answer41=tk.Radiobutton(self.orientation_area1,text='Entre 0 et 10',value='a1',\
                                    variable=self.question4,command=self.check_buttonUE345)
        self.answer42=tk.Radiobutton(self.orientation_area1,text='Entre 10 et 15',value='a2',\
                                    variable=self.question4,command=self.check_buttonUE345)
        self.answer43=tk.Radiobutton(self.orientation_area1,text='Entre 15 et 20',value='a3',\
                                    variable=self.question4,command=self.check_buttonUE345)
        #                             <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>     
        self.label_question5=tk.Label(self.orientation_area1,text="5) Quelle note avez-vous \
obtenu en Admin Reseaux et Interconnexion?")
        self.answer51=tk.Radiobutton(self.orientation_area1,text='Entre 0 et 10',value='a1',\
                                    variable=self.question5,command=self.check_buttonUE315)
        self.answer52=tk.Radiobutton(self.orientation_area1,text='Entre 10 et 15',value='a2',\
                                    variable=self.question5,command=self.check_buttonUE315)
        self.answer53=tk.Radiobutton(self.orientation_area1,text='Entre 15 et 20',value='a3',\
                                    variable=self.question5,command=self.check_buttonUE315)
        #                             <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>     
        self.label_question6=tk.Label(self.orientation_area1,text="6) Quelle note avez-vous \
obtenu en Creation et Gestion d'Entreprise?")
        self.answer61=tk.Radiobutton(self.orientation_area1,text='Entre 0 et 10',value='a1',\
                                    variable=self.question6,command=self.check_buttonUE365)
        self.answer62=tk.Radiobutton(self.orientation_area1,text='Entre 10 et 15',value='a2',\
                                    variable=self.question6,command=self.check_buttonUE365)
        self.answer63=tk.Radiobutton(self.orientation_area1,text='Entre 15 et 20',value='a3',\
                                    variable=self.question6,command=self.check_buttonUE365)
        #                             <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>   
        self.label_continuer3=tk.Label(self.orientation_area1,text='Cliquez sur continuer3 \
pour passe a la suite.',fg='red')  
        self.btn_next3=tk.Button(self.orientation_area1,text='Continuer3',bg='blue',fg='white',\
                                command=self.click_on_btn_next3)
        # *******************************************************************************************
        # ********************************   SECTION 4: Personnalité  *********************************
        # Definition du cadre representant cette section
        self.orientation_area2=tk.LabelFrame(self,width=4*LF/5,height=5*HF/13,borderwidth=10,\
                                            text="Questions d'ordre personnelle")
        # Definition des widgets contenus dans ce  cadre
        self.label_question7=tk.Label(self.orientation_area2,text="A) Quelles sont vos plus grandes passions?",\
                                    fg='green')
        self.answer71=tk.Checkbutton(self.orientation_area2,text="Developper des programmes divers",\
                                    variable=self.question71,command=self.check_case)
        self.answer72=tk.Checkbutton(self.orientation_area2,text="Demonter et remonter des appareils\
 en vue de mieux comprendre comment ils fonctionnent.",variable=self.question72,command=self.check_case)
        self.answer73=tk.Checkbutton(self.orientation_area2,text="Rescencer des informations relatives\
 a differents sujets",variable=self.question73,command=self.check_case)
        self.answer74=tk.Checkbutton(self.orientation_area2,text="Analyser des situations et faire\
 des predications sur leur evolution",variable=self.question74,command=self.check_case)
        self.answer75=tk.Checkbutton(self.orientation_area2,text="Etudier et chercher a comprendre les \
les phenomenes physiques",variable=self.question75,command=self.check_case)
        #                             <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>  
        self.label_question8=tk.Label(self.orientation_area2,text="B) Qu'est-ce qui vous caracterise le plus?",\
                                    fg='green')   
        self.answer81=tk.Checkbutton(self.orientation_area2,text="Esprit d'equipe et de management",\
                                    variable=self.question81,command=self.check_case)
        self.answer82=tk.Checkbutton(self.orientation_area2,text="Bon esprit d'analyse.",\
                                    variable=self.question82,command=self.check_case)
        self.answer83=tk.Checkbutton(self.orientation_area2,text="Capacité à collecter efficacement des infos en \
rapport avec un sujet",variable=self.question83,command=self.check_case)
        self.answer84=tk.Checkbutton(self.orientation_area2,text="Precision et rigueur",\
                                    variable=self.question84,command=self.check_case)
        self.answer85=tk.Checkbutton(self.orientation_area2,text="Capacité d'apprentissage continu.",\
                                    variable=self.question85,command=self.check_case)
        self.answer86=tk.Checkbutton(self.orientation_area2,text="Esprit éveillé et curiosite",\
                                    variable=self.question86,command=self.check_case)
        self.answer87=tk.Checkbutton(self.orientation_area2,text="Esprit de creativite et d'innovation",\
                                    variable=self.question87,command=self.check_case)
        self.answer88=tk.Checkbutton(self.orientation_area2,text="Capacité à travailler sous pression",\
                                    variable=self.question88,command=self.check_case)
        #                             <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>     
        self.label_question9=tk.Label(self.orientation_area2,text="C) Avez-vous l'habitude de faire des \
projets individuellement ou en groupe?",fg='green')
        self.answer91=tk.Radiobutton(self.orientation_area2,text='OUI',value='o',\
                                    variable=self.question9,command=self.check_button)
        self.answer92=tk.Radiobutton(self.orientation_area2,text='NON',value='n',\
                                    variable=self.question9,command=self.check_button)
        #                             <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>   
        self.label_continuer4=tk.Label(self.orientation_area2,text='Vous avez a present terminer le test. \
Cliquez sur Continuer4 pour la suite.',fg='red')  
        self.btn_next4=tk.Button(self.orientation_area2,text='Continuer4',bg='blue',fg='white',\
                                command=self.click_on_btn_next4)
        # *******************************************************************************************
        # ****************************   SECTION 5: Resultats   *******************************
        # Definition du cadre representant cette section
        self.result_area=tk.LabelFrame(self,width=4*LF/5,height=2*HF/13,borderwidth=5)
        # Definition des widgets contenus dans ce  cadre
        self.label_security=tk.Label(self.result_area,text="")
        self.label_program=tk.Label(self.result_area,text="")
        self.label_network=tk.Label(self.result_area,text="")
        self.label_sciences=tk.Label(self.result_area,text="")
        self.btn_result=tk.Button(self.result_area,text='Cliquer pour voir les resultats graphiques',\
                                bg='blue',fg='white',command=self.click_on_btn_result)
        # *******************************************************************************************
        # ****************************   SECTION 6: Menu   *******************************
        # Definition et affichage du cadre representant cette section
        self.menu_area=tk.LabelFrame(self,width=LF,height=2*HF/13,borderwidth=5)
        self.menu_area.pack(fill='x',side='bottom')
        # Definition et affichage des widgets contenus dans ce  cadre
        self.btn_menu1=tk.Button(self.menu_area,text='Cliquer pour quitter',\
                                bg='blue',fg='white',command=self.quit)
        self.btn_menu1.pack()
        #self.btn_menu2=tk.Button(self.menu_area,text='Cliquer pour recommencer',bg='blue',fg='white',command=self.relaunch)
        #self.btn_menu2.pack(side='right')
        # *******************************************************************************************
    def click_on_btn_next1(self):
        if re.search(r"^[a-zA-Z][a-z A-Z]*$",self.user_name.get()) is None:
            self.label_name['text']='Entrer un nom valide'
        else:
            self.label_name['text']="Vous pouvez modifier votre nom d'utilisateur"
            # Modification du texte de bienvenue en fonction du nom entré par l'utilisateur
            self.label_welcome['text']="Bienvenu(e) a vous\n {}.\nVous allez maintenant\n\
subir notre test d'orientation.\nVeillez répondre de façon\n sincère pour une bonne\n\
orientation.".format(self.user_name.get().upper())
            self.next1=True
        if self.next1:
            # ****************************   SECTION 2: Bienvenue   *******************************
            # Affichage du cadre representant cette section
            self.welcome_area.pack(fill='y',side='left')  
            # Affichage des widgets contenus dans ce  cadre
            self.label_welcome.place(rely=0.1,relx=0,relwidth=1)
            self.label_advice.place(rely=0.4,relx=0.05,relwidth=0.9)
            self.label_continuer2.place(rely=0.7,relx=0.125,relwidth=0.75)
            self.btn_next2.place(rely=0.8,relx=0.1,relwidth=0.8,relheight=0.1)
            # *******************************************************************************************
    def click_on_btn_next2(self):
        self.next2=True
        if self.next2:
            # ********************************   SECTION 3: Notes  *********************************
            # Affichage du cadre representant cette section
            self.orientation_area1.pack(fill='x',side='top')      
            # Affichage des widgets contenus dans ce  cadre
            self.label_question1.place(rely=0,relx=0,relwidth=0.6)
            self.answer11.place(rely=0,relx=0.61,relwidth=0.12)
            self.answer12.place(rely=0,relx=0.74,relwidth=0.12)
            self.answer13.place(rely=0,relx=0.87,relwidth=0.12)
            #           <<<<<<<<<<<<<<>>>>>>>>>>>>>>
            self.label_question2.place(rely=0.12,relx=0,relwidth=0.6)
            self.answer21.place(rely=0.12,relx=0.61,relwidth=0.12)
            self.answer22.place(rely=0.12,relx=0.74,relwidth=0.12)
            self.answer23.place(rely=0.12,relx=0.87,relwidth=0.12)
            #           <<<<<<<<<<<<<<>>>>>>>>>>>>>>
            self.label_question3.place(rely=0.24,relx=0,relwidth=0.6)
            self.answer31.place(rely=0.24,relx=0.61,relwidth=0.12)
            self.answer32.place(rely=0.24,relx=0.74,relwidth=0.12)
            self.answer33.place(rely=0.24,relx=0.87,relwidth=0.12)
            #           <<<<<<<<<<<<<<>>>>>>>>>>>>>>
            self.label_question4.place(rely=0.36,relx=0,relwidth=0.6)
            self.answer41.place(rely=0.36,relx=0.61,relwidth=0.12)
            self.answer42.place(rely=0.36,relx=0.74,relwidth=0.12)
            self.answer43.place(rely=0.36,relx=0.87,relwidth=0.12)
            #           <<<<<<<<<<<<<<>>>>>>>>>>>>>>
            self.label_question5.place(rely=0.48,relx=0,relwidth=0.6)
            self.answer51.place(rely=0.48,relx=0.61,relwidth=0.12)
            self.answer52.place(rely=0.48,relx=0.74,relwidth=0.12)
            self.answer53.place(rely=0.48,relx=0.87,relwidth=0.12)
            #           <<<<<<<<<<<<<<>>>>>>>>>>>>>>
            self.label_question6.place(rely=0.60,relx=0,relwidth=0.6)
            self.answer61.place(rely=0.60,relx=0.61,relwidth=0.12)
            self.answer62.place(rely=0.60,relx=0.74,relwidth=0.12)
            self.answer63.place(rely=0.60,relx=0.87,relwidth=0.12)
            #           <<<<<<<<<<<<<<>>>>>>>>>>>>>>
            self.label_continuer3.place(rely=0.8,relx=0.1,relwidth=0.5)
            self.btn_next3.place(rely=0.75,relx=0.6,relwidth=0.3,relheight=0.2)
            # *******************************************************************************************
    def click_on_btn_next3(self):
        if self.answer_to_question1 and self.answer_to_question2 and self.answer_to_question3 and \
        self.answer_to_question4 and self.answer_to_question5 and self.answer_to_question6:
            self.label_continuer3['text']="Bien! Vous pouvons evoluer."
            self.next3=True
        else:
            self.label_continuer3['text']="Veillez d'abord repondre a toutes les questions pour pouvoir evoluer"
        if self.next3:
            # *************************   SECTION 4: Personnalité  ***************************
            # Affichage du cadre representant cette section
            self.orientation_area2.pack(fill='x',side='top')      
            # Affichage des widgets contenus dans ce  cadre
            self.label_question7.place(rely=0,relx=0.25,relwidth=0.5)
            self.answer71.place(rely=0.065,relx=0,relwidth=1)
            self.answer72.place(rely=2*0.065,relx=0,relwidth=1)
            self.answer73.place(rely=3*0.065,relx=0,relwidth=1)
            self.answer74.place(rely=4*0.065,relx=0,relwidth=1)
            self.answer75.place(rely=5*0.065,relx=0,relwidth=1)           
            #           <<<<<<<<<<<<<<>>>>>>>>>>>>>>
            self.label_question8.place(rely=6*0.065,relx=0.25,relwidth=0.5)
            self.answer81.place(rely=7*0.065,relx=0,relwidth=0.45)
            self.answer82.place(rely=7*0.065,relx=0.55,relwidth=0.45)
            self.answer83.place(rely=8*0.065,relx=0,relwidth=0.45)
            self.answer84.place(rely=8*0.065,relx=0.55,relwidth=0.45)
            self.answer85.place(rely=9*0.065,relx=0,relwidth=0.45)
            self.answer86.place(rely=9*0.065,relx=0.55,relwidth=0.45)
            self.answer87.place(rely=10*0.065,relx=0,relwidth=0.35)
            self.answer88.place(rely=10*0.065,relx=0.45,relwidth=0.5)
            #           <<<<<<<<<<<<<<>>>>>>>>>>>>>>
            self.label_question9.place(rely=11*0.065,relx=0.25,relwidth=0.5)
            self.answer91.place(rely=12*0.065,relx=0.3,relwidth=0.1)
            self.answer92.place(rely=12*0.065,relx=0.5,relwidth=0.1)
            #           <<<<<<<<<<<<<<>>>>>>>>>>>>>>
            self.label_continuer4.place(rely=14*0.065,relx=0.15,relwidth=0.5)
            self.btn_next4.place(rely=13.5*0.065,relx=0.7,relwidth=0.2,relheight=0.1)
            # *******************************************************************************************

    def click_on_btn_next4(self):
        # Attribution des valeurs trouvees aux differentes entrees representant les options
        consultant.dsc_advisor_simulation.input['DSC']=self.science_note
        consultant.sec_advisor_simulation.input['SEC']=self.security_note
        consultant.glo_advisor_simulation.input['GLO']=self.program_note
        consultant.rte_advisor_simulation.input['RTE']=self.network_note
        # Calcul de la sortie pour chaque entree
        consultant.dsc_advisor_simulation.compute()
        consultant.sec_advisor_simulation.compute()
        consultant.glo_advisor_simulation.compute()
        consultant.rte_advisor_simulation.compute()
        # definition des textes pour l'affichage des resultats
        self.label_security['text']="Orientation pour 'Securite et Cryptographie': {}%"\
            .format(consultant.sec_advisor_simulation.output['Securite et Cryptographie'])
        self.label_program['text']="Orientation pour 'Genie Logiciel': {}%"\
            .format(consultant.glo_advisor_simulation.output['Genie Logiciel'])
        self.label_network['text']="Orientation pour 'Reseaux et Telecommunications': {}%"\
            .format(consultant.rte_advisor_simulation.output['Reseaux et Telecommunications'])
        self.label_sciences['text']="Orientation pour 'Data Science': {}%"\
            .format(consultant.dsc_advisor_simulation.output['Data Science'])
        # Verification du secteur 4 avant decision d'affichage ou non du secteur 5
        if self.answer_to_question9:
            self.label_continuer4['text']="Bien! Vous pouvons evoluer."
            self.next4=True
        else:
            self.label_continuer4['text']="Vous ne pouvez continuer sans avoir repondu a la derniere question"
        if self.next4:
            # *************************   SECTION 5: Resultats  ***************************
            # Affichage du cadre representant cette section
            self.result_area.pack(fill='x',side='top')      
            # Affichage des widgets contenus dans ce  cadre
            self.label_security.place(rely=0,relx=0,relwidth=0.5)
            self.label_program.place(rely=0.25,relx=0,relwidth=0.5) 
            self.label_network.place(rely=0.5,relx=0,relwidth=0.5) 
            self.label_sciences.place(rely=0.75,relx=0,relwidth=0.5)           
            #           <<<<<<<<<<<<<<>>>>>>>>>>>>>>
            self.btn_result.place(rely=0,relx=0.6,relwidth=0.4,relheight=1)
            # *******************************************************************************************

    def click_on_btn_result(self):      # Pour l'affichage des resultats sous forme de graphes
        self.quit()
        self.print_graphic_result=True

    def relaunch(self):
        self.__init__(self)

    def check_buttonUE355(self):    # Algorithme et programation
        if self.answer_to_question1==False:
            if self.question1.get()=='a1':      # Si la note est faible
                self.network_note+=1
                self.science_note+=1
            elif self.question1.get()=='a2':    # Si la note est moyenne
                self.security_note+=1
                self.network_note+=1.5
                self.program_note+=1
                self.science_note+=2
            elif self.question1.get()=='a3':    # Si la note est forte
                self.security_note+=3
                self.network_note+=2
                self.program_note+=3
                self.science_note+=2
            self.answer_to_question1=True
    def check_buttonUE325(self):    # Signaux et systemes
        if self.answer_to_question2==False:
            if self.question2.get()=='a1':
                pass
            elif self.question2.get()=='a2':
                self.security_note+=1
                self.network_note+=1
                self.program_note+=1
                self.science_note+=1
            elif self.question2.get()=='a3':
                self.security_note+=2
                self.network_note+=3
                self.program_note+=2
                self.science_note+=2
            self.answer_to_question2=True
    def check_buttonUE335(self):    # Base de donnees
        if self.answer_to_question3==False:
            if self.question3.get()=='a1':
                pass
            elif self.question3.get()=='a2':
                self.security_note+=1
                self.network_note+=1
                self.program_note+=0.5
                self.science_note+=1
            elif self.question3.get()=='a3':
                self.security_note+=2.5
                self.network_note+=2.5
                self.program_note+=2.5
                self.science_note+=2.5
            self.answer_to_question3=True
    def check_buttonUE345(self):    # Architecture des Ordinateurs et SI
        if self.answer_to_question4==False:
            if self.question4.get()=='a1':
                self.network_note+=1
                self.science_note+=1
            elif self.question4.get()=='a2':
                self.security_note+=1
                self.network_note+=1.5
                self.program_note+=1
                self.science_note+=1.5
            elif self.question4.get()=='a3':
                self.security_note+=3
                self.network_note+=2
                self.program_note+=3
                self.science_note+=2
            self.answer_to_question4=True
    def check_buttonUE365(self):    # Entreprise
        if self.answer_to_question6==False:
            if self.question6.get()=='a1':
                self.security_note+=0.5
                self.network_note+=0.5
                self.program_note+=0.5
                self.science_note+=0.5
            elif self.question6.get()=='a2':
                self.security_note+=1.5
                self.network_note+=1.5
                self.program_note+=1.5
                self.science_note+=1.5
            elif self.question6.get()=='a3':
                self.security_note+=2.5
                self.network_note+=2.5
                self.program_note+=2.5
                self.science_note+=2.5
            self.answer_to_question6=True
    def check_buttonUE315(self): # Admin Reseaux locaux et Interconnexion
        if self.answer_to_question5==False:
            if self.question5.get()=='a1':
                self.program_note+=0.75
                self.science_note+=1
            elif self.question5.get()=='a2':
                self.security_note+=1
                self.network_note+=1
                self.program_note+=1.5
                self.science_note+=1.5
            elif self.question5.get()=='a3':
                self.security_note+=3
                self.network_note+=3
                self.program_note+=2
                self.science_note+=2
            self.answer_to_question5=True
    
    def check_case(self):
        if self.question71.get()==1 and self.checked_case71==False:
            self.security_note+=1
            self.program_note+=1
            self.checked_case71=True
        if self.question72.get()==1 and self.checked_case72==False:
            self.security_note+=1
            self.program_note+=1
            self.network_note+=1
            self.checked_case72=True
        if self.question73.get()==1 and self.checked_case73==False:
            self.science_note+=1
            self.checked_case73=True
        if self.question74.get()==1 and self.checked_case74==False:
            self.science_note+=1
            self.checked_case74=True
        if self.question75.get()==1 and self.checked_case75==False:
            self.network_note+=1
            self.checked_case75=True
        if self.question81.get()==1 and self.checked_case81==False:
            self.security_note+=0.75
            self.program_note+=1
            self.network_note+=0.75
            self.science_note+=0.5
            self.checked_case81=True
        if self.question82.get()==1 and self.checked_case82==False:
            self.security_note+=1
            self.program_note+=1
            self.network_note+=1
            self.science_note+=1.5
            self.checked_case82=True
        if self.question83.get()==1 and self.checked_case83==False:
            self.science_note+=1
            self.checked_case83=True
        if self.question84.get()==1 and self.checked_case84==False:
            self.network_note+=1
            self.checked_case84=True
        if self.question85.get()==1 and self.checked_case85==False:
            self.security_note+=1
            self.program_note+=1
            self.network_note+=0.75
            self.science_note+=0.5
            self.checked_case85=True
        if self.question86.get()==1 and self.checked_case86==False:
            self.security_note+=0.75
            self.program_note+=0.5
            self.network_note+=0.75
            self.science_note+=0.75
            self.checked_case86=True
        if self.question87.get()==1 and self.checked_case87==False:
            self.security_note+=0.5
            self.program_note+=1
            self.network_note+=1
            self.science_note+=0.5
            self.checked_case87=True
        if self.question88.get()==1 and self.checked_case88==False:
            self.security_note+=1
            self.program_note+=0.75
            self.network_note+=1
            self.science_note+=0.5
            self.checked_case88=True

    def check_button(self):
        if self.answer_to_question9==False:
            if self.question9.get()=='o':
                self.security_note+=1
                self.program_note+=1
                self.network_note+=1
                self.science_note+=1
            else : pass
            self.answer_to_question9=True

fenetre.geometry(str(LF)+'x'+str(HF))
fenetre.title("Conseiller d'Orientation")
interface=Interface(fenetre)


interface.mainloop()

if interface.print_graphic_result: # Pour l'affichage des resultats sous forme de graphes
    consultant.print_graphic_results(consultant.orientation_dsc,consultant.dsc_advisor_simulation)
    consultant.print_graphic_results(consultant.orientation_sec,consultant.sec_advisor_simulation)
    consultant.print_graphic_results(consultant.orientation_glo,consultant.glo_advisor_simulation)
    consultant.print_graphic_results(consultant.orientation_rte,consultant.rte_advisor_simulation)