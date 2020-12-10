# coding: utf-8
import win32com.client
import sys

from pylab import *

from OpenDSS_Functions import *
from Functions import *
from Plots import *

objeto = DSS("C:\Users\hugo1\Desktop\Projeto_Final_Microrredes_Copia_Copia\Circuito_teste\Circuito_OpenDSS\Master.dss")
AuxFunc = Func(objeto)

LI = Interno()

class PLOT_FINAL():

    def __init__(self):

        ### PLOT COMPARATIVO 1 SIMULAÇÃO
        self.Barra = []
        self.Final_Tensoes_Dia_S_VV = []
        self.Final_Tensoes_Dia_C_VV = []

        self.Final_DSQ_Dia_S_VV = []
        self.Final_DSQ_Dia_C_VV = []

        self.Final_P_GDs_por_Snap_S_VV = []
        self.Final_Q_GDs_por_Snap_S_VV = []

        self.Final_P_GDs_por_Snap_C_VV = []
        self.Final_Q_GDs_por_Snap_C_VV = []

        self.Final_Power_Sub = []
        self.Final_Power_Sub_VV = []



        ####### Simulação Temporal
        self.Final_Variables_Power_Sub = []
        self.Final_Variables_Power_Sub_VV = []

def Config_Sistema(Nome_Barras):

    ## Configurações dos elementos
    objeto.Entrar_com_GDs = 1
    #objeto.Entrar_com_Baterias = 0
    #objeto.Entrar_com_VV_GDs = 0
    #objeto.Entrar_com_VV_Storages = 0
    objeto.Variables_Positions = 0
    objeto.Pref_Pot_Ativa = 1
    objeto.Altera_GDs_sVV_cVV = 1

    LI.Num_GDs = 6                             # LIMITADO, pensar em uma forma de adicionar GDs iterativas
    objeto.Num_Fases_GDs = 3                 # 1 -> Monofásico   # 2 -> Trifásico # 3 -> Mix

    # Define os números máximos dos loops
    objeto.Loop_Externo = 100

    objeto.Loop_Interno = 1                   # Usado somente para print  ( CONTADOR )

    LI.Nome_Barras = Nome_Barras              # Usado em alguma função




if __name__ == "__main__":
    print u"""Autor: Hugo Torquato \nData: 06/10/2020 \nE-mail: hugortorquato@gmail.com \n"""

    Resultados = PLOT_FINAL()
    PlotFunc = Plot(objeto)

    # Compila o codigo do sistema
    objeto.compila_DSS()
    LI = Interno()
    LE = Externo()



    from FunctionsSecond import Leitura_pmult_reduzido, Leitura_pmult_reduzido_gdS
    # Usado para reduzir o tamanho dos multiplos -> Já estão reduzidos, não rodar de novo
    #print Leitura_pmult_reduzido()
    #Leitura_pmult_reduzido_gdS()


    Config_Sistema(objeto.Leitura_Nome_Barras())                                                # Salva as configurações do sistema na classe

    # Determina uma posição inicial para o teste de comparação simples
    if objeto.Variables_Positions == 0:
        objeto.Loop_Externo = 1
        LI.Determina_Locais_GDs()                                                               # Altera os locais de GD para cada confguração.
        LI.Determina_Fases(objeto.Num_Fases_GDs)

        objeto.Determina_Barras_GDs = LI.Barra_GD                                               # Altera os locais de GD para cada confguração.
        objeto.Determina_Fases_GDs = LI.Fase_GD
        #print LI.Fase_GD


    for Loop_Ext in range(objeto.Loop_Externo):                                            # Loop para levantamento de dados para análise

        if objeto.Variables_Positions == 1 and objeto.Altera_GDs_sVV_cVV == 0:  # Caso 1 -> Utilizado na simulação de análise estatistica

            LI.Determina_Locais_GDs()  # Altera os locais de GD para cada confguração.
            LI.Determina_Fases(objeto.Num_Fases_GDs)

            objeto.Determina_Barras_GDs = LI.Barra_GD  # Altera os locais de GD para cada confguração.
            objeto.Determina_Fases_GDs = LI.Fase_GD
            #print LI.Fase_GD

        for P in range(2):  # Loop para coletar a comparação dos resultados
            if P == 0:
                objeto.Entrar_com_VV_GDs = 0
            else:
                objeto.Entrar_com_VV_GDs = 1

            if objeto.Variables_Positions == 1 and objeto.Altera_GDs_sVV_cVV == 1:                                                # Caso 1 -> Utilizado na simulação de análise estatistica

                LI.Determina_Locais_GDs()                                                      # Altera os locais de GD para cada confguração.
                LI.Determina_Fases(objeto.Num_Fases_GDs)

                objeto.Determina_Barras_GDs = LI.Barra_GD                                      # Altera os locais de GD para cada confguração.
                objeto.Determina_Fases_GDs = LI.Fase_GD
                #print LI.Fase_GD

            print " "
            print "###########################################################################"
            print U" ########################## INFORMAÇÕES ##################################"
            print "###########################################################################"
            print " Loop Ext : " + str(Loop_Ext)
            if objeto.Entrar_com_VV_GDs == 1:
                print " Entra com VV ? SIM"
            else:
                print u" Entra com VV ? NÃO"
            print " Posicionamento das barras : " + str(LI.Barra_GD)
            print " Fase das barras : " + str(LI.Fase_GD)
            if objeto.Variables_Positions == 1:
                print " Disposição GDs random ? SIM"
            else:
                print u" Disposição GDs random ? NÃO"
            print "###########################################################################"
            print "###########################################################################"
            print ""

            objeto.kW_Init = 0
            objeto.Violacao = 0
            objeto.Loop_Interno = 0

            #### BUSCA UP
            while objeto.Violacao == 0:
                #print u"LOOP iNTERNO------------------------------------------------------ " + str(objeto.Loop_Interno)
                objeto.Loop_Interno += 1


                objeto.compila_DSS()

                objeto.Solve_Hora_por_Hora()
                #PlotFunc.Plot_Efeito_VV_GDs('n03')

                #print objeto.Violacao

                if objeto.Violacao == 1:
                    break
                objeto.kW_Init += 48

                #PlotFunc.Plot_Tensao_Dia_Uma_Barra(objeto.Tensoes_Dia, LI.Barra_GD[1])

            ### BUSCA DOWN
            if objeto.Violacao == 1:

                #for barra in LI.Barra_GD:
                    #PlotFunc.Plot_Tensao_Dia_Uma_Barra(objeto.Tensoes_Dia, barra)
                while objeto.Violacao == 1:

                    objeto.compila_DSS()
                    objeto.kW_Init -= 6
                    #print "LOADS : " + str(se.Pot_Loads())
                    #print "HC (KW) : " + str(objeto.kW_Init)

                    objeto.Solve_Hora_por_Hora()
                    #print "redução"
                    #print objeto.Violacao

                ######################################## SALVAR OS DADOS DO HC PARA A CONFIGURAÇÃO

                #PlotFunc.Plot_Tensao_Dia_Uma_Barra(objeto.Tensoes_Dia, 'n03')


            ######### SALVA DADOS OBTIDOS PARA PLOT

            if objeto.Variables_Positions == 0:                                           # Resultados de comparação 1 Compilação
                Resultados.Barra = LI.Barra_GD[0]
                if objeto.Entrar_com_VV_GDs == 0:
                    Resultados.Final_Tensoes_Dia_S_VV    = objeto.Tensoes_Dia
                    Resultados.Final_DSQ_Dia_S_VV        = objeto.Desq_Dia
                    Resultados.Final_P_GDs_por_Snap_S_VV = objeto.Pot_Ativa_GDs_por_snap
                    Resultados.Final_Q_GDs_por_Snap_S_VV = objeto.Pot_Reativa_GDs_por_snap
                    Resultados.Final_Power_Sub            = objeto.Power_Sub


                elif objeto.Entrar_com_VV_GDs == 1:
                    Resultados.Final_Tensoes_Dia_C_VV    = objeto.Tensoes_Dia_VV
                    Resultados.Final_DSQ_Dia_C_VV        = objeto.Desq_Dia_VV
                    Resultados.Final_P_GDs_por_Snap_C_VV = objeto.Pot_Ativa_GDs_por_snap_VV
                    Resultados.Final_Q_GDs_por_Snap_C_VV = objeto.Pot_Reativa_GDs_por_snap_VV
                    Resultados.Final_Power_Sub_VV        = objeto.Power_Sub_VV

            if objeto.Variables_Positions == 1:
                if objeto.Entrar_com_VV_GDs == 0:
                    Resultados.Final_Variables_Power_Sub.append(objeto.Pot_Ativa_GDs_por_snap)

                elif objeto.Entrar_com_VV_GDs == 1:
                    Resultados.Final_Variables_Power_Sub_VV.append(objeto.Pot_Ativa_GDs_por_snap_VV)

        ################# PLOTS

    if objeto.Variables_Positions == 0:
        from Plots import Comp_Tensao_Desq_Uma_Barra, Comp_Pot, Comp_Pot_Sub

        Comp_Tensao_Desq_Uma_Barra(Resultados.Final_Tensoes_Dia_S_VV, Resultados.Final_DSQ_Dia_S_VV,
                                            Resultados.Final_Tensoes_Dia_C_VV, Resultados.Final_DSQ_Dia_C_VV,
                                            Resultados.Barra, LI.Nome_Barras)

        Comp_Pot(Resultados.Final_P_GDs_por_Snap_S_VV, Resultados.Final_Q_GDs_por_Snap_S_VV,
                 Resultados.Final_P_GDs_por_Snap_C_VV, Resultados.Final_Q_GDs_por_Snap_C_VV,
                 Resultados.Barra, LI.Nome_Barras)

        Comp_Pot_Sub(Resultados.Final_Power_Sub, Resultados.Final_Power_Sub_VV)

    if objeto.Variables_Positions == 1:
        from Plots import Comp_HC_EXT
        Comp_HC_EXT(Resultados.Final_Variables_Power_Sub, Resultados.Final_Variables_Power_Sub_VV)


    plt.show()

    from FunctionsSecond import Armazena_Dados_Tensao, Armazena_Dados_Desq
    Armazena_Dados_Tensao(objeto.Tensoes_Dia)
    Armazena_Dados_Desq(objeto.Desq_Dia)