import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt
import numpy as np

def membership_function(var,l1,l2,l3):
    return fuzz.trimf(var.universe,l1) , fuzz.trimf(var.universe,l2) , fuzz.trimf(var.universe,l3)

def rule(var1,var2):
    return ctrl.Rule(var1['W'],var2['W']) , ctrl.Rule(var1['M'],var2['M']) , ctrl.Rule(var1['S'],var2['S'])

def print_graphic_results(var1,var2):
    var1.view(sim=var2)
    plt.title(var1.label)
    plt.ylabel("Dégré d'appartenance à une classe")
    plt.xlabel("Valeur de la sortie pour cette option (Evaluée sur 100)")
    plt.show()

                    # Definition des parametres du systeme
#***********************************************************************************
# Definition des parametre d'entree du systeme (Correspondant aux quatre specialites disponibles)
sciences=ctrl.Antecedent(np.arange(0,21,1),'DSC')
security=ctrl.Antecedent(np.arange(0,21,1),'SEC')
program=ctrl.Antecedent(np.arange(0,21,1),'GLO')
network=ctrl.Antecedent(np.arange(0,21,1),'RTE')
# Definition de la sortie du systeme (Il s'agit ici de la reponse du systeme pour recommander une specialite)
orientation_dsc=ctrl.Consequent(np.arange(0,101,1),'Data Science')
orientation_sec=ctrl.Consequent(np.arange(0,101,1),'Securite et Cryptographie')
orientation_glo=ctrl.Consequent(np.arange(0,101,1),'Genie Logiciel')
orientation_rte=ctrl.Consequent(np.arange(0,101,1),'Reseaux et Telecommunications')


    # Definition des fonctions d'appartenance pour chacune des variables linguistiques
#******************************************************************************************
sciences['W'],sciences['M'],sciences['S'] = membership_function(sciences,[0,0,10],[8,15,15],[14,20,20])
security['W'],security['M'],security['S'] = membership_function(security,[0,0,10],[8,15,15],[14,20,20])
program['W'],program['M'],program['S'] = membership_function(program,[0,0,10],[8,15,15],[14,20,20])
network['W'],network['M'],network['S'] = membership_function(network,[0,0,10],[8,15,15],[14,20,20])

orientation_dsc['W'],orientation_dsc['M'],orientation_dsc['S'] = \
    membership_function(orientation_dsc,[0, 0, 35],[30, 70, 70],[65, 100, 100])
orientation_sec['W'],orientation_sec['M'],orientation_sec['S'] = \
    membership_function(orientation_sec,[0, 0, 35],[30, 70, 70],[65, 100, 100])
orientation_glo['W'],orientation_glo['M'],orientation_glo['S'] = \
    membership_function(orientation_glo,[0, 0, 35],[30, 70, 70],[65, 100, 100])
orientation_rte['W'],orientation_rte['M'],orientation_rte['S'] = \
    membership_function(orientation_rte,[0, 0, 35],[30, 70, 70],[65, 100, 100])


    # Definition des règles qui seront utilisées par le systeme pour faire une recommandation
#*************************************************************************************************
dsc_rule1,dsc_rule2,dsc_rule3=rule(sciences,orientation_dsc)
sec_rule1,sec_rule2,sec_rule3=rule(security,orientation_sec)
glo_rule1,glo_rule2,glo_rule3=rule(program,orientation_glo)
rte_rule1,rte_rule2,rte_rule3=rule(network,orientation_rte)


                        # Création du système de contrôle
#*****************************************************************************
dsc_advisor = ctrl.ControlSystem([dsc_rule1,dsc_rule2,dsc_rule3])
dsc_advisor_simulation = ctrl.ControlSystemSimulation(dsc_advisor)

sec_advisor = ctrl.ControlSystem([sec_rule1,sec_rule2,sec_rule3])
sec_advisor_simulation = ctrl.ControlSystemSimulation(sec_advisor)

glo_advisor = ctrl.ControlSystem([glo_rule1,glo_rule2,glo_rule3])
glo_advisor_simulation = ctrl.ControlSystemSimulation(glo_advisor)

rte_advisor = ctrl.ControlSystem([rte_rule1,rte_rule2,rte_rule3])
rte_advisor_simulation = ctrl.ControlSystemSimulation(rte_advisor)