# coding: utf-8
import win32com.client
import sys

from pylab import *

from OpenDSS_Functions import *
from Functions import *
from Plots import *

objeto = DSS("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Master.dss")
AuxFunc = Func(objeto)
PlotFunc = Plot(objeto)

if __name__ == "__main__":
    print u"""Autor: Hugo Torquato \nData: 24/01/2020 \nE-mail: hugortorquato@gmail.com \n"""

    # Compila o codigo do sistema
    objeto.compila_DSS()

    ## Configurações do sistema
    Entrar_com_GDs = 0
    Entrar_com_Baterias = 1

    Entrar_com_VV_GDs = 0
    Entrar_com_VV_Storages = 1

    print sqrt(11)

    ## Declaração dos Elementos
    objeto.Declaracao_Elementos(Entrar_com_GDs, Entrar_com_Baterias)

    ## Snapshot de um dia, minuto a minuto
    if Entrar_com_VV_GDs == 1:
        Tensoes_Dia, Tensoes_Dia_VV, Powers_Dia, Powers_Dia_VV, Pot_Ativa_GDs_por_snapW, \
        Pot_Reativa_GDs_por_snap, Pot_Ativa_GDs_por_snap_VV, Pot_Reativa_GDs_por_snap_VV = objeto.Solve_Hora_por_Hora(
            Entrar_com_GDs, Entrar_com_Baterias, Entrar_com_VV_GDs, Entrar_com_VV_Storages)

        PlotFunc.Plot_Efeito_VV_GDs(Tensoes_Dia, Tensoes_Dia_VV, 'n03', Powers_Dia, Powers_Dia_VV,
                                    Pot_Ativa_GDs_por_snapW,
                                    Pot_Reativa_GDs_por_snap, Pot_Ativa_GDs_por_snap_VV, Pot_Reativa_GDs_por_snap_VV)

    if Entrar_com_VV_Storages == 1:
        Tensoes_Dia = objeto.Solve_Hora_por_Hora(
            Entrar_com_GDs, Entrar_com_Baterias, Entrar_com_VV_GDs, Entrar_com_VV_Storages)

        PlotFunc.Plot_Efeito_VV_Storages(Tensoes_Dia, 'n03')


    #Tensoes, Powers, kvar_GDs, kw_GDs, Stored_Capacit, Power_Storage, Pout_GDs, Qout_GDs, Powers_Loads, \
    #P_A, P_B, P_C, P_A_GD, P_B_GD, P_C_GD = objeto.Solve_Hora_por_Hora(Entrar_com_GDs, Entrar_com_Baterias)


    #PlotFunc.Plot(Powers_Loads)


    ##### MSOTRAR DANILO
    # Volt Var GD
    #PlotFunc.Plot_Teste_2(Tensoes, Powers, Tensoes_Dia_VV, Powers_Dia_VV, 'n03')
    #PlotFunc.Plot_Tensao_Reativo_Volt_Var(Tensoes, kvar_GDs, 'n03')



    # Volt Var Storage

    # PBC ( c/GD G1 / s/GD )




















    # PLot Volt Var
    #PlotFunc.Plot_Tensao_Reativo_Volt_Var(Tensoes, kvar_GDs, 'n03')
    #PlotFunc.Plot_Pot_Volt_Var(kvar_GDs, kw_GDs)

    # Storage
    #objeto.Plot_Storages_Monitors()
    #PlotFunc.Plot(Stored_Capacit)

    # CC
    #PlotFunc.Plot_Pot_CC(Pout_GDs, Qout_GDs, Powers, Powers_Loads) # ALTERAR O PLOT E BUSCAR VARIÁVEIS DA FUNÇÃO, E NÃO CALCULAR
    #PlotFunc.Plot_Alfa_Beta(Alfa, Beta)



## TESTES ANTIGOS

    #PlotFunc.Plot_Pot_CC(Pout_GDs, Qout_GDs, Powers, Powers_Loads)
    #PlotFunc.Plot_Teste(P_A, P_B, P_C, P_A_GD, P_B_GD, P_C_GD, Powers)  # ERRO

    #PlotFunc.Plot_Tensao_Dia_Uma_Barra(Tensoes, 'n03')
    #PlotFunc.Plot_Tensao_Dia_Uma_Barra(Tensoes, 'n01')



    #PlotFunc.Plot_Pot_Dia(Powers)

    #print (objeto.Leitura_Nome_Barras())
    #objeto.get_resultados_potencia()
    #objeto.LoadShapes_Teste()
    #objeto.Plot_Monitors()

    #print objeto.Leitura_Nome_Barras()
    #print objeto.Leitura_Nome_Linhas()
    #print objeto.Leitura_Nome_Swt()

    #print objeto.Leitura_Nome_Barras()
    #print AuxFunc.Tensao_Barras()


    # TESTE para abertura das chaves
    #objeto.Abre_Chave('S1')
    #objeto.Abre_Chave('S2')
    #objeto.Abre_Chave('S3')
    #objeto.solve()

    #print AuxFunc.Tensao_Barras()
    #PlotFunc.Plota_Nivel_Tensao(AuxFunc.Tensao_Barras())






