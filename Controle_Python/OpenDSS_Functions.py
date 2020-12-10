# coding: utf-8
import win32com.client
from pylab import *

class Local():

    def __init__(self):
        self.Teste = []
        self.pot_Ativa_GDs_por_snap = []
        self.pot_Reativa_GDs_por_snap = []
        self.pot_Ativa_GDs_por_snap_VV = []
        self.pot_Reativa_GDs_por_snap_VV = []

        # Storages
        self.kW_Storages = []
        self.kVar_Storages = []

        # SEM CC
        self.tensoes_Dia = []
        self.powers_Dia = []
        self.tensoes_Dia_VV = []
        self.powers_Dia_VV = []
        self.powers_Loads = []
        self.kvar_GDs = []
        self. kw_GDs = []

        self.Power_Storage = []
        self.Stored_Capacit = []
        self.Pout_GDs = []
        self.Qout_GDs = []

        self.Alfa_Vet = []
        self.Beta_Vet = []
        self.P_Max_Vet = []

        self.P_GD_ref_Vet = []
        self.Q_GD_ref_Vet = []

        self.p_A = []
        self.Q_A = []
        self.p_B = []
        self.Q_B = []
        self.p_C = []
        self.Q_C = []

        self.p_A_GD = []
        self.Q_A_GD = []
        self.p_B_GD = []
        self.Q_B_GD = []
        self.p_C_GD = []
        self.Q_C_GD = []

        self.Power_GD = []

        # self.Desequilibrio_Dia_IEC = []
        # self.Desequilibrio_Dia_IEEE = []
        # self.Desequilibrio_Dia_NEMA = []

        # COM CC
        self.alfa_Vet = []
        self.beta_Vet = []

        self.tensoes_Dia_CC = []
        self.powers_CC = []
        self.powers_Dia_CC = []
        self.powers_Loads_CC = []

        self.p_A_CC = []
        self.q_A_CC = []
        self.p_B_CC = []
        self.q_B_CC = []
        self.p_C_CC = []
        self.q_C_CC = []




        self.kvar_GDs_CC = []
        self.kw_GDs_CC = []

        self.power_Storage_CC = []
        self.stored_Capacit_CC = []
        self.pout_GDs_CC = []
        self.qout_GDs_CC = []

        self.alfa_Vet = []
        self.beta_Vet = []
        self.p_Max_Vet = []

        self.power_Sto = []
        self.power_Sto_CC = []

class DSS():

    def __init__(self, Modelo_Barras):

        # Definicao_Atributos que serão utilizados

        # Controle do sistema
        self.Entrar_com_GDs = 0
        self.Entrar_com_Baterias= 0
        self.Entrar_com_VV_GDs = 0
        self.Entrar_com_VV_Storages = 0
        self.Entrar_com_CC = 0

        # Vetores de armazenamento de dados
            # Gerais
        self.Tensoes_Dia = []
        self.Powers_Dia  = []

            # VoltVar GDs
        self.Tensoes_Dia_VV = []
        self.Powers_Dia_VV = []
        self.Pot_Ativa_GDs_por_snapW = []
        self. Pot_Reativa_GDs_por_snap = []
        self.Pot_Ativa_GDs_por_snap_VV = []
        self.Pot_Reativa_GDs_por_snap_VV = []

            # CC
        self.Tensoes_Dia_CC = []
        self.Powers_Dia_CC  = []

        self.Power_Sto = []
        self.Power_Sto_CC = []




        # Armazena o caminho para o circuito .dss para ser aberto
        self.Modelo_Barras = Modelo_Barras

        # Criar a conexão entre Python e OpenDSS
        self.dssObj = win32com.client.Dispatch("OpenDSSEngine.DSS")

        # Iniciar o Objeto DSS
        if self.dssObj.Start(0) == False:
            print "Problemas em iniciar o OpenDSS"
        else:
            # Criar variáveis paras as principais interfaces
            self.dssText = self.dssObj.Text
            self.dssCircuit = self.dssObj.ActiveCircuit
            self.dssSolution = self.dssCircuit.Solution
            self.dssCktElement = self.dssCircuit.ActiveCktElement
            self.dssBus = self.dssCircuit.ActiveBus
            self.dssCapacitores = self.dssCircuit.Capacitors
            self.dssRegControls = self.dssCircuit.RegControls
            self.dssLoadShapes = self.dssCircuit.LoadShapes
            self.dssLoads = self.dssCircuit.Loads
            self.dssLines = self.dssCircuit.Lines
            self.dssSwtControls = self.dssCircuit.SwtControls
            self.dssGenerators = self.dssCircuit.Generators
            self.dssMonitors = self.dssCircuit.Monitors
            self.dssActiveClass = self.dssCircuit.ActiveClass
            self.dssPDElements = self.dssCircuit.PDElements

    def compila_DSS(self):

        # Limpar informações da ultima compilação
        self.dssObj.ClearALL()

        # Compilar o arquivo utilizando a interface texto
        # self.dssText.Command = "solve "
        self.dssText.Command = "compile " + self.Modelo_Barras

    def solve(self):
        self.dssText.Command = "solve"

    def Declaracao_Elementos(self):
        if self.Entrar_com_GDs == 1:
            DSS.Circuit_Generators(self)

        if self.Entrar_com_Baterias == 1:
            DSS.Circuit_Storage(self)

    def Solve_Hora_por_Hora(self):

        ## Declaração e inicialização de variáveis
        global itera
        DSS.Declaracao_Elementos(self)

        VetItera = Local()

        originalSteps = self.dssSolution.Number  # Número de soluções a se realizar
        self.dssSolution.Number = 1  # Determina que será realizado uma solução por vez

        for itera in range(0, originalSteps):

            print str(itera) + " --------------"

            from Main import AuxFunc

            ## Primeiro Solve
            if self.Entrar_com_Baterias == 1:
                # Definir estado inicial como IDLELING
                for storage in DSS.Get_Storage_Names(self):
                    DSS.Set_IDLING_State(self, storage)

            self.dssSolution.SolveSnap()

            ## Coleta de dados antesw Controle
            VetItera.tensoes_Dia.append(AuxFunc.Tensao_Barras())
            VetItera.power = AuxFunc.Pot_Sub_entrada()
            VetItera.powers_Dia.append(VetItera.power)
            VetItera.powers_Loads.append(AuxFunc.Pot_Loads())

            # Coleta Valores por Fase de Loads
            VetItera.pot_Loads = AuxFunc.Pot_Loads_Fase()
            VetItera.p_A.append(VetItera.pot_Loads[0])
            VetItera.p_B.append(VetItera.pot_Loads[2])
            VetItera.p_C.append(VetItera.pot_Loads[4])

            if self.Entrar_com_CC == 1:

                alfa, beta = AuxFunc.CC(VetItera.power, itera)
                print (alfa), (beta)
                VetItera.Alfa_Vet.append(alfa)
                VetItera.Beta_Vet.append(beta)

                ## atribuir valores para Storage
                for storage in DSS.Get_Storage_Names(self):
                    print storage

                    # Ativar elemento

                    DSS.Ativa_Elemento(self, storage)

                    VetItera.power_Sto.append((self.dssCktElement.Properties("KW").Val))

                    DSS.Atribui_CC(self, alfa, beta)
                    self.dssSolution.SolveSnap()
                    VetItera.power_Sto_CC.append((self.dssCktElement.Properties("KW").Val))


                    ## Coleta de dados antesw Controle
                    VetItera.tensoes_Dia_CC.append(AuxFunc.Tensao_Barras())
                    VetItera.powers_CC = AuxFunc.Pot_Sub_entrada()
                    VetItera.powers_Dia_CC.append(VetItera.powers_CC)
                    VetItera.powers_Loads_CC.append(AuxFunc.Pot_Loads())

                    # Coleta Valores por Fase de Loads
                    VetItera.pot_Loads_CC = AuxFunc.Pot_Loads_Fase()
                    VetItera.p_A_CC.append(VetItera.pot_Loads_CC[0])
                    VetItera.p_B_CC.append(VetItera.pot_Loads_CC[2])
                    VetItera.p_C_CC.append(VetItera.pot_Loads_CC[4])



                    #print DSS.kW_Storage(self, storage)
                    #print DSS.kVar_Storage(self, storage)



                ## Rodar o snao e coletar novos dados

                ## PLotar

            VetItera.pOT_GDs = AuxFunc.Pot_GD_Fase()
            VetItera.p_A_GD.append(VetItera.pOT_GDs[0])
            VetItera.p_B_GD.append(VetItera.pOT_GDs[2])
            VetItera.p_C_GD.append(VetItera.pOT_GDs[4])


            ## VOLT/VAR E STORAGES

            ## Volt_Var
            if self.Entrar_com_VV_GDs == 1:

                for i in range(len(self.dssGenerators.AllNames)):
                    VetItera.kw_GDs.append([])
                    VetItera.kvar_GDs.append([])
                    VetItera.kw_GDs_CC.append([])
                    VetItera.kvar_GDs_CC.append([])

                ## Coleta de dados antesw Controle
                VetItera.pot_Ativa, VetItera.pot_Reativa = DSS.Salva_Valores_Pot(self)
                print VetItera.pot_Ativa, VetItera.pot_Reativa
                VetItera.pot_Ativa_GDs_por_snap.append(VetItera.pot_Ativa)
                VetItera.pot_Reativa_GDs_por_snap.append(VetItera.pot_Reativa)

                # Coleta Valores por Fase de GDs
                VetItera.pOT_GDs = AuxFunc.Pot_GD_Fase()
                VetItera.p_A_GD.append(VetItera.pOT_GDs[0])
                VetItera.p_B_GD.append(VetItera.pOT_GDs[2])
                VetItera.p_C_GD.append(VetItera.pOT_GDs[4])

                #DSS.Volt_Var_Dados(self, kvar_GDs, kw_GDs)
                DSS.Volt_Var_Dados(self, self.Entrar_com_VV_GDs, self.Entrar_com_VV_Storages)
                self.dssSolution.SolveSnap()

                ## Coleta de dados depois Controle
                VetItera.tensoes_Dia_VV.append(AuxFunc.Tensao_Barras())
                VetItera.power = AuxFunc.Pot_Sub_entrada()
                powers_Dia_VV.append(VetItera.power)
                VetItera.pot_Ativa, VetItera.pot_Reativa = DSS.Salva_Valores_Pot(self)
                print VetItera.pot_Ativa, VetItera.pot_Reativa
                VetItera.pot_Ativa_GDs_por_snap_VV.append(VetItera.pot_Ativa)
                VetItera.pot_Reativa_GDs_por_snap_VV.append(VetItera.pot_Reativa)

                print " "

            ## Storage
            if self.Entrar_com_VV_Storages == 1:

                #print DSS.Get_Storage_Names(self)
                DSS.Get_Info_Storages(self, DSS.Get_Storage_Names(self))
                # Coloca todos os banco em estado de espera até realizar os calculos para ver se necessita e coleta
                # dados antes do VoltVar para cada GD
                for Storage in DSS.Get_Storage_Names(self):
                    VetItera.kW_Storages_Itera = []
                    VetItera.kVar_Storages_Itera = []
                    if self.dssCktElement.Properties("state").Val == "IDLING":
                        DSS.Set_CHARGING_State(self, Storage)
                    DSS.Volt_Var_por_Storage(self, Storage)           # Calc VoltVar

                    # salva valores de pot ativa e reativa
                    VetItera.kW_Storages_Itera.append(DSS.kW_Storage(self, Storage))
                    VetItera.kVar_Storages_Itera.append(DSS.kVar_Storage(self, Storage)) # Trocar para KVAR
                #print self.dssCktElement.Properties("state").Val
                VetItera.kW_Storages.append(VetItera.kW_Storages_Itera)
                VetItera.kVar_Storages.append(VetItera.kVar_Storages_Itera)

                # Calculo do VoltVar
                #DSS.Volt_Var_Dados(self, Entrar_com_VV_GDs, Entrar_com_VV_Storages)
                #self.dssSolution.SolveSnap()

                # Coleta resultados depois do VoltVar

            self.dssSolution.FinishTimeStep()
            print " "

        if self.Entrar_com_VV_GDs == 1:
            self.Tensoes_Dia                 = VetItera.tensoes_Dia
            self.Tensoes_Dia_VV              = VetItera.tensoes_Dia_VV
            self.Powers_Dia                  = VetItera.powers_Dia
            self.Powers_Dia_VV               = VetItera.powers_Dia_VV
            self.Pot_Ativa_GDs_por_snapW     = VetItera.pot_Ativa_GDs_por_snap
            self.Pot_Reativa_GDs_por_snap    = VetItera.pot_Reativa_GDs_por_snap
            self.Pot_Ativa_GDs_por_snap_VV   = VetItera.pot_Ativa_GDs_por_snap_VV
            self.Pot_Reativa_GDs_por_snap_VV = VetItera.pot_Reativa_GDs_por_snap_VV

            return

        if self.Entrar_com_VV_Storages == 1:
            self.Tensoes_Dia                 = VetItera.tensoes_Dia

            return

        if self.Entrar_com_CC == 1:
            self.Tensoes_Dia = VetItera.tensoes_Dia
            self.Powers_Dia = VetItera.powers_Dia
            self.Tensoes_Dia_CC = VetItera.tensoes_Dia_CC
            self.Powers_Dia_CC = VetItera.powers_Dia_CC
            self.Power_Sto = VetItera.power_Sto
            self.Power_Sto_CC = VetItera.power_Sto_CC

        if self.Entrar_com_GDs == 0:
            return VetItera.p_A, VetItera.p_B, VetItera.p_C

        return VetItera.p_A_GD, VetItera.p_B_GD, VetItera.p_C_GD


        #return Tensoes_Dia, Powers_Dia, kvar_GDs, kw_GDs, Stored_Capacit, Power_Storage, Pout_GDs, Qout_GDs, Powers_Loads, \
        #       P_A, P_B, P_C, P_A_GD, P_B_GD, P_C_GD, Tensoes_Dia_VV, Powers_Dia_VV#, Alfa_Vet, Beta_Vet #, Desequilibrio_Dia_IEC, Desequilibrio_Dia_IEEE, Desequilibrio_Dia_NEMA

# Storages -------------------------------------------------------------------------------------------------------------

    def Circuit_Storage(self):

        kWhrated = 15*6
        kWrated = 30
        kvar = 3.3166247903554

        from FunctionsSecond import Hora_2_Min
        DSS.Storage_Definer(self, kWrated, Hora_2_Min(kWhrated), 'n03')

        DSS.Salva_Dados_kWhrated_Storage(self, kWhrated)
        DSS.Salva_Dados_kWrated_Storage(self, kWrated)
        DSS.Salva_Dados_kVar_Storage(self, kvar)

    def Salva_Dados_kWhrated_Storage(self, kWhrated):

        #Ativa
        arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\kWhrated_Storage.txt', 'w')
        arquivo.write(str(kWhrated) + "\n")
        arquivo.close()

    def Salva_Dados_kWrated_Storage(self, kWrated):
        # Ativa
        arquivo = open(
            'C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\kWrated_Storage.txt',
            'w')
        arquivo.write(str(kWrated) + "\n")
        arquivo.close()

    def Salva_Dados_kVar_Storage(self, kvar):
        # Ativa
        arquivo = open(
            'C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\kvar_Storage.txt',
            'w')
        arquivo.write(str(kvar) + "\n")
        arquivo.close()

    def Storage_Definer(self, kWrated, kWhrated, Bus_Storage):

        # Entradas

        #kWrated = 100
        #kWhrated = 100000
        #Bus_Storage = 'n03'

        # Define o nome do banco
        Storage_Names = DSS.Get_Storage_Names(self)
        if len(Storage_Names) == 0:
            Num_Storage = 1
        else:
            Num_Storage = len(Storage_Names) + 1

        # Define the "kv" variable for the storage bus
        DSS.ativa_barra(self, Bus_Storage)
        kV = self.dssBus.kVBase

        self.dssText.Command = "New Storage.Battery_" + str(Num_Storage) + " phases=3 Bus1=" + str(Bus_Storage) + " kV="\
                               + str(kV) + " kWrated=" + str(kWrated) + "  kWhrated=" + str(kWhrated) +\
                               " model=1 state=dischar" + " pf=" + str(1) #+ " debugtrace=" + str('yes')

        self.dssText.Command = " New monitor.storage_power element=Storage.Battery_1 terminal=1 mode=1 ppolar=no"
        self.dssText.Command = " New monitor.storage_voltages element=Storage.Battery_1 terminal=1 mode=0"
        self.dssText.Command = " New monitor.storage_variables element=Storage.Battery_1 terminal=1 mode=3"

    def Get_Storage_Names(self):

        Storage_Names = []
        All_Elementes = self.dssCircuit.AllElementNames
        for Element in All_Elementes:
            if Element[0:7] == "Storage":
                Storage_Names.append(Element)
        return Storage_Names

    def Get_Info_Storages(self, Name_Storage):

        Stored = DSS.Storage_Stored(self, Name_Storage) # % Energia disponível

        #DSS.Set_CHARGING_State(self, Name_Storage)  # Seta bateria para Carregando

        #DSS.Set_IDLING_State(self, Name_Storage)  # Seta bateria para Em Espera

        #DSS.Set_DISCHARGING_State(self, Name_Storage)  # Seta bateria para Descarrregando

        kW = DSS.kW_Storage(self, Name_Storage) # Salva um arquivo .csv com debug do banco

        return Stored, kW

    def Storage_Stored(self, Name_Storage):

        # Retorna a porcentagem disponível na bateria. Tem limite inferior definido em 20%, mas pode ser alterado pela
        # variável (%reserve)

        All_Storages_Names = DSS.Get_Storage_Names(self)
        for Storage in All_Storages_Names:
            if Storage == Name_Storage:
                DSS.Ativa_Elemento(self, Storage)
                #print self.dssCktElement.Properties("%stored").Val
                return self.dssCktElement.Properties("%stored").Val

    def Set_IDLING_State(self, Name_Storage):

        # Seta o estado do banco para carregando. Se já estiver carregado vai para IDLING

        All_Storages_Names = DSS.Get_Storage_Names(self)
        for Storage in All_Storages_Names:
            if Storage == Name_Storage:
                DSS.Ativa_Elemento(self, Storage)
                self.dssCktElement.Properties("state").Val = 'IDLING'
                #print self.dssCktElement.Properties("state").Val
                return self.dssCktElement.Properties("state").Val

    def Set_CHARGING_State(self, Name_Storage):

        # Seta o estado do banco para carregando. Se já estiver carregado vai para IDLING

        All_Storages_Names = DSS.Get_Storage_Names(self)
        for Storage in All_Storages_Names:
            if Storage == Name_Storage:
                DSS.Ativa_Elemento(self, Storage)
                self.dssCktElement.Properties("state").Val = 'CHARGING'
                #print self.dssCktElement.Properties("state").Val
                return self.dssCktElement.Properties("state").Val

    def Set_DISCHARGING_State(self, Name_Storage):

        # Seta o estado do banco para descarregando. Se chegar no minimo entra no estado Em Espera sem carregar

        All_Storages_Names = DSS.Get_Storage_Names(self)
        for Storage in All_Storages_Names:
            if Storage == Name_Storage:
                DSS.Ativa_Elemento(self, Storage)
                self.dssCktElement.Properties("state").Val = 'DISCHARGING'
                #print self.dssCktElement.Properties("state").Val
                return self.dssCktElement.Properties("state").Val

    def kW_Storage(self, Name_Storage):

        # Salva um arquivo .csv com todas as informações do banco

        All_Storages_Names = DSS.Get_Storage_Names(self)
        for Storage in All_Storages_Names:
            if Storage == Name_Storage[0]:
                DSS.Ativa_Elemento(self, Storage)
                #self.dssCktElement.Properties("KW").Val = 3
                #print self.dssCktElement.Properties("KW").Val
                return self.dssCktElement.Properties("KW").Val

    def kVar_Storage(self, Name_Storage):

        # Salva um arquivo .csv com todas as informações do banco

        All_Storages_Names = DSS.Get_Storage_Names(self)
        for Storage in All_Storages_Names:
            if str(Storage) == str(Name_Storage):
                DSS.Ativa_Elemento(self, Storage)
                #self.dssCktElement.Properties("pf").Val = (' 0.5 ')
                #print self.dssCktElement.Properties("pf").Val
                #print self.dssCktElement.Properties("kvar").Val
                return self.dssCktElement.Properties("Kvar").Val

    def Atribui_CC(self, alfa, beta):

        if alfa > 0.01:
            self.dssCktElement.Properties("state").Val = 'DISCHARGING'
            self.dssCktElement.Properties("KW").Val = str(alfa * float(self.dssCktElement.Properties("kWrated").Val)/3)
            print self.dssCktElement.Properties("%stored").Val
            print self.dssCktElement.Properties("state").Val
            print self.dssCktElement.Properties("KW").Val
        else:
            self.dssCktElement.Properties("state").Val = 'IDLING'

            print self.dssCktElement.Properties("%stored").Val
            print self.dssCktElement.Properties("state").Val
            print self.dssCktElement.Properties("KW").Val

        # Definir o Reativo


    def teste(self):
        DSS.Set_DISCHARGING_State(self, DSS.Get_Storage_Names(self)[0])

        self.dssCktElement.Properties("%Discharge").Val = 50 # Define a saida de potÊncia por porcentagem 0~100%
        print self.dssCktElement.Properties("KW").Val
        #self.dssCktElement.Properties("KW").Val = 3
        print " Capacidade disponível"
        aaa = float(self.dssCktElement.Properties("%stored").Val)

# Volt/Var -------------------------------------------------------------------------------------------------------------

    def Volt_Var_Dados_Antigo(self, kvar, kw):

        i = 0
        for GD in self.dssGenerators.AllNames:
            self.dssGenerators.Name = str(GD)

            DSS.Volt_Var(self, GD)

            #print self.dssCktElement.Properties("kvar").Val
            #print self.dssGenerators.kw
            kvar[i].append(self.dssCktElement.Properties("kvar").Val)
            kw[i].append(self.dssGenerators.kw)


            if i == len(self.dssGenerators.AllNames) - 1:
                i = 0
            else:
                i = i + 1

        return kvar, kw

    def Volt_Var_Dados(self, Entrar_com_VV_GDs, Entrar_com_VV_Storages):

        if Entrar_com_VV_GDs == 1:
            i = 0
            for GD in self.dssGenerators.AllNames:
                self.dssGenerators.Name = str(GD)

                kw_mult, kvar_mult = DSS.Volt_Var_por_GD(self, GD)

                DSS.Atualiza_Multiplos_GDs(self, kw_mult, kvar_mult)

                if i == len(self.dssGenerators.AllNames) - 1:
                    i = 0
                else:
                    i = i + 1

        if Entrar_com_VV_Storages == 11:
            i = 0
            for Storage in DSS.Get_Storage_Names(self):
                DSS.Ativa_Elemento(self, Storage)
                kw_mult_S, kvar_mult_S = DSS.Volt_Var_por_Storage(self, Storage)


        if Entrar_com_VV_GDs == 1:
            return kw_mult, kvar_mult
        elif Entrar_com_VV_Storages == 1:
            return kw_mult_S, kvar_mult_S
        elif Entrar_com_VV_GDs == 1 and Entrar_com_VV_Storages == 1:
            return kw_mult, kvar_mult, kw_mult_S, kvar_mult_S

    def Atualiza_Multiplos_GDs(self, kw_mult, kvar_mult):


        All_load_shapes = self.dssLoadShapes.AllNames
        from FunctionsSecond import find
        GD = self.dssCktElement.Name
        shape = self.dssCktElement.Properties("daily").Val
        index = find(All_load_shapes, shape.lower())
        self.dssLoadShapes.Name = All_load_shapes[index]
        pmult = list(self.dssLoadShapes.Pmult)
        qmult = list(self.dssLoadShapes.Qmult)
        # Lembrar sempre de usar (itera -1) para os resultados baterem
        ##print pmult[itera-1]
        pmult[itera-1] = pmult[itera-1] * kw_mult
        qmult[itera - 1] = qmult[itera - 1] * kvar_mult
        self.dssLoadShapes.Pmult = pmult
        self.dssLoadShapes.Qmult = qmult
        #print pmult[itera-1]

    def Retorna_GD_da_Barra(self, Name_Bus):

        Buses = open(
            'C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\Bus_GDs.txt', 'r')
        Name_Buses = []
        for linha in Buses:
            Name_Buses.append(linha.rstrip())
        Buses.close()

        i = 0
        for Bus in Name_Buses:
            if Bus == Name_Bus.upper():
                #print i
                return i
            else:
                i = i + 1

    def Volt_Var_por_GD(self, GD):

        # Entrada
        #All_GD = self.dssGenerators.AllNames
        #GD = All_GD[0]

        # Pegar tensão na Barra da GD
        self.dssGenerators.Name = str(GD)
        Bus = self.dssCktElement.BusNames
        All_Buses = self.dssCircuit.AllBusNames
        Bus = Bus[0].split('.')[0]
        from FunctionsSecond import find
        index = find(All_Buses, Bus)

        ## Separa o vetor de fases para suas respectivas fases A, B e C
        from FunctionsSecond import Agrega_Fase_Tensao
        Fases = Agrega_Fase_Tensao(self.dssCircuit.AllBusVmagPu) # Fases = [ [A], [B], [C], [Média_ABC] ]

        ## Obtem o percentual de acrescimo ou decrescimo do reativo
        from FunctionsSecond import Create_Vector_Volt_Var
        Vector_Y = Create_Vector_Volt_Var(index, Fases)
            # Tem como retornar um vetor para valor Médio ou por fase ( Retornando Médio agora )

        ## Altera reativo da GD
        All_GDS = self.dssGenerators.AllNames
        from FunctionsSecond import find
        index_GD = find(All_GDS, GD)
        self.dssGenerators.Name = All_GDS[index_GD]

            ## Leitura dos parâmetros das GDs
        from FunctionsSecond import Leitura_kvar_GDs
        Pot_Reativa = Leitura_kvar_GDs()
        Pot_Reativa = float(Pot_Reativa[index_GD])

        from FunctionsSecond import Leitura_kW_GDs
        Pot_Ativa = Leitura_kW_GDs()
        Pot_Ativa = float(Pot_Ativa[index_GD])

        kW = self.dssGenerators.kw

            ## Calcula Potências
        Pot_Aparente = (((Pot_Ativa**2) + (Pot_Reativa**2))**0.5)
        Q_max = round(Pot_Aparente, 2)
        Q_VoltVar = round(Q_max * (Vector_Y[0]), 2)
        if float(sqrt((kW**2) + (Q_VoltVar**2))) >= Pot_Aparente:
            P_VoltVar = round(sqrt((Pot_Aparente**2) - (Q_VoltVar**2)), 2)
            #self.dssGenerators.kw = P_VoltVar
            if Pot_Ativa == 0:
                kw_mult = 0
            else:
                kw_mult = P_VoltVar / Pot_Ativa
        else:
            P_VoltVar = self.dssGenerators.kw
            #self.dssCktElement.Properties("kW").Val = P_VoltVar
            if Pot_Ativa == 0:
                kw_mult = 0
            else:
                kw_mult = Pot_Ativa / Pot_Ativa
                #kw_mult = P_VoltVar / Pot_Ativa

            ## Atribui Valores Para GD
        if itera == 800:
            print str(GD) + " Reativo " + str(Q_VoltVar) + " Ativa " + str(P_VoltVar) + " Aparente " + str(Pot_Aparente)
            print "Pot Aparente Calc = " + str(sqrt(Q_VoltVar**2 + P_VoltVar**2))


        #self.dssCktElement.Properties("kvar").Val = Q_VoltVar
        kvar_mult = Q_VoltVar * 1000
        #self.dssGenerators.kvar = Q_VoltVar

        return kw_mult, kvar_mult

    def Volt_Var_por_Storage(self, Storage):

        # Entrada
        #All_GD = self.dssGenerators.AllNames
        #GD = All_GD[0]

        # Pegar tensão na Barra da GD
        Bus = self.dssCktElement.BusNames
        All_Buses = self.dssCircuit.AllBusNames
        Bus = Bus[0].split('.')[0]
        from FunctionsSecond import find
        index = find(All_Buses, Bus)

        ## Separa o vetor de fases para suas respectivas fases A, B e C

             ###### MELHORIA - Não preciso fazer isso para todas as barras - Pode impactar para frente
        from FunctionsSecond import Agrega_Fase_Tensao
        Fases = Agrega_Fase_Tensao(self.dssCircuit.AllBusVmagPu) # Fases = [ [A], [B], [C], [Média_ABC] ]

        ## Obtem o percentual de acrescimo ou decrescimo do reativo
        from FunctionsSecond import Create_Vector_Volt_Var
        Vector_Y = Create_Vector_Volt_Var(index, Fases)
            # Tem como retornar um vetor para valor Médio ou por fase ( Retornando Médio agora )

        ## Altera reativo da GD

        Pot_Ativa, Q_max, Pot_Aparente, kWrated, Stored = DSS.Encontra_param_Storages(self, Storage)
        Q_VoltVar = round(Q_max * (Vector_Y[0]), 2)

        # Respeita limite de pot e fixa para máxima saída de pot ativa
        while ((Pot_Ativa**2 + Q_VoltVar**2)**0.5) >= Pot_Aparente:
            aa = ((Pot_Ativa**2 + Q_VoltVar**2)**0.5)
            if (Pot_Ativa**2 + Q_VoltVar**2) >= Pot_Aparente:
                if Q_VoltVar >= 0: Q_VoltVar = Q_VoltVar - 0.1
                else: Q_VoltVar = Q_VoltVar + 0.1

        #Calcula Fator de Pot
        if Pot_Ativa ==0 and Q_VoltVar == 0 : FP_Ajustado = 0
        elif Q_VoltVar >= 0: FP_Ajustado = Pot_Ativa / ((Pot_Ativa**2 + Q_VoltVar**2)**0.5)
        else: FP_Ajustado = -Pot_Ativa / ((Pot_Ativa**2 + Q_VoltVar**2)**0.5)


        # Saturador do FP
        if FP_Ajustado > 1: FP_Ajustado = 1
        elif FP_Ajustado < -1: FP_Ajustado = -1

        # Atribuir o valor do fator de potencia
        self.dssCktElement.Properties("pf").Val = (str(FP_Ajustado))

        teste1 = self.dssCktElement.Properties("KW").Val
        teste2 = self.dssCktElement.Properties("pf").Val
        teste3 = self.dssCktElement.Properties("kvar").Val

    def Encontra_param_Storages(self, Storage):

        All_Storages = DSS.Get_Storage_Names(self)
        from FunctionsSecond import find
        index_Storage = find(All_Storages, Storage)
        DSS.Ativa_Elemento(self, All_Storages[index_Storage])

            ## Leitura dos parâmetros das Storages
        from FunctionsSecond import Leitura
        kWhrated_Storage = Leitura('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\kWhrated_Storage.txt')
        kWhrated = float(kWhrated_Storage[index_Storage])
        kWrated_Storage = Leitura('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\kWrated_Storage.txt')
        kWrated = float(kWrated_Storage[index_Storage])
        kvar_Storage = Leitura('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\kvar_Storage.txt')
        kvar = float(kvar_Storage[index_Storage])

        Pot_Ativa = float(self.dssCktElement.Properties("KW").Val)

        ## Calcula VoltVar
        Pot_Aparente = (((kWrated**2) + (kvar**2))**0.5)
        Q_max = round(Pot_Aparente, 2)

        Stored = float(self.dssCktElement.Properties("%stored").Val)

        return Pot_Ativa, Q_max, Pot_Aparente, kWrated, Stored

# GDs ------------------------------------------------------------------------------------------------------------------

    def Circuit_Generators(self):

        # Read Generators shape
        self.dssText.Command = "New LoadShape._GD_1 npts=1440 sinterval=1 pmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\P_GD_1.txt) qmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\Q_GD_1.txt)"
        self.dssText.Command = "New LoadShape._GD_2 npts=1440 sinterval=1 pmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\P_GD_2.txt) qmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\Q_GD_2.txt)"
        self.dssText.Command = "New LoadShape._GD_3 npts=1440 sinterval=1 pmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\P_GD_3.txt) qmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\Q_GD_3.txt)"
        self.dssText.Command = "New LoadShape._GD_4 npts=1440 sinterval=1 pmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\P_GD_4.txt) qmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\Q_GD_4.txt)"
        self.dssText.Command = "New LoadShape._GD_5 npts=1440 sinterval=1 pmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\P_GD_5.txt) qmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\Q_GD_5.txt)"
        self.dssText.Command = "New LoadShape._GD_6 npts=1440 sinterval=1 pmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\P_GD_6.txt) qmult=(file=C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores\Q_GD_6.txt)"

        POWER_1 = [5, 0]
        POWER_2 = [7, 0]
        POWER_3 = [5, 0]
        POWER_4 = [10, 0]
        POWER_5 = [9, 0]
        POWER_6 = [9, 0]

        GD_1_Bus = 'N03'
        GD_2_Bus = 'N08'
        GD_3_Bus = 'N14'
        GD_4_Bus = 'N18'
        GD_5_Bus = 'N21'
        GD_6_Bus = 'N17'

        GD_1_Fase = 'BC'
        GD_2_Fase = 'C'
        GD_3_Fase = 'A'
        GD_4_Fase = 'AC'
        GD_5_Fase = 'AB'
        GD_6_Fase = 'B'

        DSS.Generator_Definer(self, GD_1_Bus, POWER_1[0], POWER_1[1],  GD_1_Fase, '_GD_1')
        DSS.Generator_Definer(self, GD_2_Bus, POWER_2[0], POWER_2[1],  GD_2_Fase, '_GD_2')
        DSS.Generator_Definer(self, GD_3_Bus, POWER_3[0], POWER_3[1],  GD_3_Fase, '_GD_3')
        DSS.Generator_Definer(self, GD_4_Bus, POWER_4[0], POWER_4[1],  GD_4_Fase, '_GD_4')
        DSS.Generator_Definer(self, GD_5_Bus, POWER_5[0], POWER_5[1],  GD_5_Fase, '_GD_5')
        DSS.Generator_Definer(self, GD_6_Bus, POWER_6[0], POWER_6[1],  GD_6_Fase, '_GD_6')

        DSS.Salva_Pot_GDs(self, POWER_1, POWER_2, POWER_3, POWER_4, POWER_5, POWER_6)
        DSS.Salva_Barras_GDs(self, GD_1_Bus, GD_2_Bus, GD_3_Bus, GD_4_Bus, GD_5_Bus, GD_6_Bus)
        DSS.Salva_Fase_GDs(self, GD_1_Fase, GD_2_Fase, GD_3_Fase, GD_4_Fase, GD_5_Fase, GD_6_Fase)

    def Salva_Pot_GDs(self, POWER_1, POWER_2, POWER_3, POWER_4, POWER_5, POWER_6):

        #Ativa
        arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\Pot_Ativa.txt', 'w')
        arquivo.write(str(POWER_1[0]) + "\n")
        arquivo.write(str(POWER_2[0]) + "\n")
        arquivo.write(str(POWER_3[0]) + "\n")
        arquivo.write(str(POWER_4[0]) + "\n")
        arquivo.write(str(POWER_5[0]) + "\n")
        arquivo.write(str(POWER_6[0]) + "\n")
        arquivo.close()

        #Reativa
        arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\Pot_Reativa.txt', 'w')
        arquivo.write(str(POWER_1[1]) + "\n")
        arquivo.write(str(POWER_2[1]) + "\n")
        arquivo.write(str(POWER_3[1]) + "\n")
        arquivo.write(str(POWER_4[1]) + "\n")
        arquivo.write(str(POWER_5[1]) + "\n")
        arquivo.write(str(POWER_6[1]) + "\n")
        arquivo.close()

    def Salva_Barras_GDs(self, GD_1_Bus, GD_2_Bus, GD_3_Bus, GD_4_Bus, GD_5_Bus, GD_6_Bus):

        arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\Bus_GDs.txt', 'w')
        arquivo.write(GD_1_Bus + "\n")
        arquivo.write(GD_2_Bus + "\n")
        arquivo.write(GD_3_Bus + "\n")
        arquivo.write(GD_4_Bus + "\n")
        arquivo.write(GD_5_Bus + "\n")
        arquivo.write(GD_6_Bus + "\n")
        arquivo.close()

    def Salva_Fase_GDs(self, GD_1_Fase, GD_2_Fase, GD_3_Fase, GD_4_Fase, GD_5_Fase, GD_6_Fase):

        arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\Fases_GDs.txt', 'w')
        arquivo.write(GD_1_Fase + "\n")
        arquivo.write(GD_2_Fase + "\n")
        arquivo.write(GD_3_Fase + "\n")
        arquivo.write(GD_4_Fase + "\n")
        arquivo.write(GD_5_Fase + "\n")
        arquivo.write(GD_6_Fase + "\n")
        arquivo.close()

    def Generator_Definer(self, BUS_GD, kw, kvar, Phases, Loadshape):
        # Tentar fazer uma função genérica, para adicionar um gerador na barra de acordo com um perfil multiplo

        # Entrada
        #BUS_GD = 'N17'
        #kw = 50
        #kvar = 0
        #Phases = 'bC'
        #Loadshape = '_1'

        # Defines the number of the generator
        Generators_Names = self.dssGenerators.AllNames
        if Generators_Names[0] == 'NONE':
            Num_Gerador = len(self.dssGenerators.AllNames)
        else:
            Num_Gerador = len(self.dssGenerators.AllNames) + 1

        # Define the "kv" variable for the generator bus
        Loads = self.dssLoads.AllNames
        self.dssLoads.Name = Loads[2]
        kv = self.dssLoads.kV

        # Define The Phases of the Generator
        from FunctionsSecond import Verify_Phases
        Verify = Verify_Phases(str(Phases.upper()))
        if Verify == 0:
            return 0    # Case the Phases have some mistake the program doesn't criate the generator
        from FunctionsSecond import Identify_Phases
        Phases_Number = Identify_Phases(Phases.upper())

        # Define the generator with the parameters
        #self.dssText.Command = "new generator.GD_" + str(Num_Gerador) + " phases=" + str(len(Phases)) + " bus1=" + \
        #                       str(BUS_GD) + str(Phases_Number) + " kv=" + str(kv) + " kW=" + str(kw) + " PF=" + \
        #                       str(1) + " model=4" + " daily=" + str(Loadshape)
        self.dssText.Command = "new generator.GD_" + str(Num_Gerador) + " phases=" + str(len(Phases)) + " bus1=" + \
                               str(BUS_GD) + str(Phases_Number) + " kv=" + str(kv) + " kW=" + str(kw) + " kVAr=" + \
                               str(0.001) + " model=1" + " daily=" + str(Loadshape)

    def Atualiza_Valores_GDs(self, Alfa, Beta):

        from FunctionsSecond import Acha_Index_LoadShape_GD, Leitura_pmult, Leitura_qmult, Escreve_pmult, Escreve_qmult

        Names_Loadshapes = self.dssLoadShapes.AllNames

        BKP_Pmult = []
        BKP_Qmult = []
        print " "
        print itera
        for GD in self.dssGenerators.AllNames:
            self.dssGenerators.Name = str(GD)

            # Acha indice do loadshap do gerador
            Nome_GD = ("_" + str(GD))
            i = Acha_Index_LoadShape_GD(Nome_GD, Names_Loadshapes)


            #self.dssLoadShapes.Name = str(Names_Loadshapes[i])
            #pmult = list(self.dssLoadShapes.Pmult)
            #qmult = list(self.dssLoadShapes.Qmult)

            pmult = list(Leitura_pmult(Nome_GD))
            qmult = list(Leitura_qmult(Nome_GD))
            BKP_Pmult.append(qmult[itera])
            BKP_Qmult.append(qmult[itera])

            print " testeeee 1 > " + str(pmult[itera]) + " kw > " + str(self.dssGenerators.kW)

            pmult[itera] = round(float(pmult[itera]), 4) * Alfa
            qmult[itera] = round(float(qmult[itera]), 4) * Alfa

            Escreve_pmult(Nome_GD, pmult)
            Escreve_qmult(Nome_GD, qmult)


            DSS.Atualza_LoadShape_GD(self, Nome_GD)
            self.dssSolution.SolveSnap()
            i = Acha_Index_LoadShape_GD(Nome_GD, Names_Loadshapes)
            self.dssLoadShapes.Name = str(Names_Loadshapes[i])
            pmult = list(self.dssLoadShapes.Pmult)
            qmult = list(self.dssLoadShapes.Qmult)

            print " testeeee 2 > " + str(pmult[itera]) + " kw > " + str(self.dssGenerators.kW)

        return BKP_Pmult, BKP_Qmult

    def Desatualiza_Valores_GDs(self, BKP_Pmult, BKP_Qmult):

        from FunctionsSecond import Acha_Index_LoadShape_GD, Leitura_pmult, Leitura_qmult

        Names_Loadshapes = self.dssLoadShapes.AllNames

        for GD in self.dssGenerators.AllNames:
            GDs = self.dssGenerators.AllNames
            self.dssGenerators.Name = str(GD)

            # Acha indice do loadshap do gerador
            Nome_GD = ("_" + str(GD))
            #i = Acha_Index_LoadShape_GD(Nome_GD, Names_Loadshapes)
            #self.dssLoadShapes.Name = str(Names_Loadshapes[i])
            #pmult = list(self.dssLoadShapes.Pmult)
            #qmult = list(self.dssLoadShapes.Qmult)



            pmult = list(Leitura_pmult(Nome_GD))
            qmult = list(Leitura_qmult(Nome_GD))
            print " testeeee 3 > " + str(pmult[itera]) + " kw > " + str(self.dssGenerators.kW)

            pmult[itera] = BKP_Pmult
            qmult[itera] = BKP_Qmult

            Escreve_pmult(Nome_GD, pmult)
            Escreve_qmult(Nome_GD, qmult)

            DSS.Atualza_LoadShape_GD(self, Nome_GD)
            self.dssSolution.SolveSnap()
            i = Acha_Index_LoadShape_GD(Nome_GD, Names_Loadshapes)
            self.dssLoadShapes.Name = str(Names_Loadshapes[i])
            pmult = list(self.dssLoadShapes.Pmult)
            qmult = list(self.dssLoadShapes.Qmult)


            print " testeeee 4 > " + str(pmult[itera]) + " kw > " + str(self.dssGenerators.kW)

    def Atualza_LoadShape_GD(self, Nome_GD):

        for GD in self.dssGenerators.AllNames:
            self.dssGenerators.Name = str(GD)
            self.dssCktElement.Properties("daily").Val = Nome_GD

    def Salva_Valores_Pot(self):

        Pot_Ativa = []
        Pot_Reativa = []

        for GD in self.dssGenerators.AllNames:
            self.dssGenerators.Name = str(GD.upper())
            Pot_Ativa.append(self.dssGenerators.kw)
            Pot_Reativa.append(self.dssGenerators.kvar)

        return Pot_Ativa, Pot_Reativa

    def Chave_GDs(self):
        return self.Entrar_com_GDs

# Auxiliares -----------------------------------------------------------------------------------------------------------

    def Leitura_Nome_Barras(self):

        All = self.dssCircuit.AllBusNames
        Bus_Names = []

        for bus in All:
            if bus[0] != 's':
                Bus_Names.append(bus)

        return Bus_Names

    def Leitura_Nome_Linhas(self):
        return self.dssLines.AllNames

    def Abre_Chave(self, Chave):

        self.dssLines.Name = Chave
        Bus = self.dssLines.Bus1
        from FunctionsSecond import find
        Index_Aux = find(Bus, '.')
        self.dssLines.Bus1 = str(Bus[0:Index_Aux] + ".11.22.33")

    def Leitura_Nome_Capacitores(self):
        return self.dssCapacitores.AllNames

    def Leitura_Nome_Reguladores(self):
        return self.dssRegControls.AllNames

    def get_resultados_potencia(self):
        self.dssText.Command = "Show power kva elements"
        self.dssText.Command = "Show Voltages LN Nodes"
        #self.dssText.Command = "Show Taps"
        #self.dssText.Command = "dump transformer.Sub debug"

    def LoadShapes_Teste(self):
        #print len(self.dssLoadShapes.AllNames)
        Names = self.dssLoadShapes.AllNames
        self.dssLoadShapes.Name = Names[1]
        print len(self.dssLoadShapes.pmult)
        print self.dssLoadShapes.pmult
        #print (self.dssLoadShapes.qmult)
        #print self.LoadShapes.Npts
        print self.dssLoads.AllNames

    def Plot_Monitors(self):

        self.dssText.Command = "Redirect Command_Monitores"

    def Plot_Storages_Monitors(self):

        #self.dssText.Command = "Visualize powers Storage.Battery_1"

        self.dssText.Command = "Plot monitor object=storage_power channels=(1 3 5)"
        self.dssText.Command = "Plot monitor object=storage_power channels=(2 4 6)"
        self.dssText.Command = "Plot monitor object=storage_voltages channels=(1 3 5)"
        self.dssText.Command = "Plot monitor object=storage_voltages channels=(2 4 6)"
        self.dssText.Command = "Plot monitor object=storage_variables channels=(1 3 5)"

    def puVmagAngle(self):
        return self.dssBus.puVmagAngle

    def ativa_barra(self, nome_barra):

        self.dssCircuit.SetActiveBus(nome_barra)

    def Ativa_Elemento(self, Nome_Elemento):

        self.dssCircuit.SetActiveElement(Nome_Elemento)

    def Acha_GD_da_Bara_retorna_o_indice(self, Nome_Barra):

        i = 0
        for GD in self.dssGenerators.AllNames:
            self.dssGenerators.Name = str(GD.upper())
            GD_Bus = self.dssCktElement.Properties("bus1").Val
            from FunctionsSecond import find
            index = find(GD_Bus, ".")
            Nome_Bus_GD = GD_Bus[0:index]
            if Nome_Barra.upper() == Nome_Bus_GD:
                return i
            i = i + 1

        # criar travamento para quando não tiver GD