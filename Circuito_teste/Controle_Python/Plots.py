# coding: utf-8

import numpy as np
from OpenDSS_Functions import *
from mpl_toolkits.mplot3d import Axes3D

from Princ import *

matplotlib.rc('font', family='Arial', )
matplotlib.rcParams.update({'font.size': 30})



def Comp_Tensao_Desq_Uma_Barra(Final_Tensoes_Dia_S_VV, Final_DSQ_Dia_S_VV, Final_Tensoes_Dia_C_VV, Final_DSQ_Dia_C_VV,
                                            Barra, Nomes_Barras):


    Bus_Name = str(Barra)

    # Acha o indice do nome da barra
    Position_Bus = 0
    for Bus in Nomes_Barras:
        if Bus == Bus_Name:
            Position_Bus = Position_Bus
            break
        else:
            Position_Bus = Position_Bus + 1

    plt.figure(1)
    subplot(221)##########################################################################



    # Create an vector to save de voltage of this bus
    Bus_Voltage_Daily = []
    for Bus_Voltage in Final_Tensoes_Dia_S_VV:
        Bus_Voltage_Daily.append(Bus_Voltage[Position_Bus])

    # Create the function to plot
    puVmag_1 = []
    puVmag_2 = []
    puVmag_3 = []

    for Tensao in Bus_Voltage_Daily:
        puVmag_1.append(Tensao[0])
        puVmag_2.append(Tensao[1])
        puVmag_3.append(Tensao[2])

    barWidth = 0.25
    r1 = np.arange(len(puVmag_1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
    plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
    plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')


    plt.ylabel(u'Tensões (pu)')
    plt.grid()
    plt.legend(loc='upper right', fontsize=24)
    plt.ylim(0.91, 1.08)


    subplot(222) #####################################################################################

    # Create an vector to save de voltage of this bus
    Bus_Voltage_Daily = []
    for Bus_Voltage in Final_Tensoes_Dia_C_VV:
        Bus_Voltage_Daily.append(Bus_Voltage[Position_Bus])

    # Create the function to plot
    puVmag_1 = []
    puVmag_2 = []
    puVmag_3 = []

    for Tensao in Bus_Voltage_Daily:
        puVmag_1.append(Tensao[0])
        puVmag_2.append(Tensao[1])
        puVmag_3.append(Tensao[2])

    barWidth = 0.25
    r1 = np.arange(len(puVmag_1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
    plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
    plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')

    plt.grid()
    plt.legend(loc='upper right', fontsize=24)
    plt.ylim(0.91, 1.08)

    subplot(223) #####################################################################################

    # Create an vector to save de UNBALANCE of this bus
    Bus_DSQ_Daily = []
    for Bus_DSQ in Final_DSQ_Dia_S_VV:
        Bus_DSQ_Daily.append(Bus_DSQ[Position_Bus])

    X = []
    [X.append(i) for i in range(len(Bus_DSQ_Daily))]
    plt.bar(X, Bus_DSQ_Daily, color='#6A5ACD', width=barWidth, label='Barra')
    plt.ylabel(u'Desq Tensão ')
    plt.xlabel(u'(A) HC sem VV ')
    plt.grid()
    plt.legend(loc='upper right', fontsize=24)
    plt.ylim(0, 3)

    subplot(224) #####################################################################################

    # Create an vector to save de UNBALANCE of this bus
    Bus_DSQ_Daily = []
    for Bus_DSQ in Final_DSQ_Dia_C_VV:
        Bus_DSQ_Daily.append(Bus_DSQ[Position_Bus])

    X = []
    [X.append(i) for i in range(len(Bus_DSQ_Daily))]
    plt.bar(X, Bus_DSQ_Daily, color='#6A5ACD', width=barWidth, label='Barra')
    plt.xlabel(u'(B) HC com VV ')
    plt.grid()
    plt.legend(loc='upper right', fontsize=24)
    plt.ylim(0, 3)

    plt.suptitle(u' Dados da Barra ' + str(Bus_Name.upper()) + ' do Sistema ', fontsize=40, weight='bold')



def Comp_Pot(Final_P_GDs_por_Snap_S_VV, Final_Q_GDs_por_Snap_S_VV, Final_P_GDs_por_Snap_C_VV, Final_Q_GDs_por_Snap_C_VV,
                 Barra, Nomes_Barras):

    Bus_Name = str(Barra)

    # Acha o indice do nome da barra
    Position_Bus = 0
    for Bus in Nomes_Barras:
        if Bus == Bus_Name:
            Position_Bus = Position_Bus
            break
        else:
            Position_Bus = Position_Bus + 1



    plt.figure(2)
    subplot(221) #####################################################################################

    # Create the function to plot
    GD_1 = []
    GD_2 = []
    GD_3 = []
    GD_4 = []
    GD_5 = []
    GD_6 = []

    for Tensao in Final_P_GDs_por_Snap_S_VV:
        GD_1.append(Tensao[0])
        GD_2.append(Tensao[1])
        GD_3.append(Tensao[2])
        GD_4.append(Tensao[3])
        GD_5.append(Tensao[4])
        GD_6.append(Tensao[5])

    plt.plot(GD_1, linewidth=4, label=u'GD 1')
    plt.plot(GD_2, linewidth=4, label=u'GD 2')
    plt.plot(GD_3, linewidth=4, label=u'GD 3')
    plt.plot(GD_4, linewidth=4, label=u'GD 4')
    plt.plot(GD_5, linewidth=4, label=u'GD 5')
    plt.plot(GD_6, linewidth=4, label=u'GD 6')

    plt.ylabel(U' Pot. GD (kW) ')
    plt.grid()
    plt.ylim(0, 31)

    subplot(222) #####################################################################################

    # Create the function to plot
    GD_1 = []
    GD_2 = []
    GD_3 = []
    GD_4 = []
    GD_5 = []
    GD_6 = []

    for Tensao in Final_P_GDs_por_Snap_C_VV:
        GD_1.append(Tensao[0])
        GD_2.append(Tensao[1])
        GD_3.append(Tensao[2])
        GD_4.append(Tensao[3])
        GD_5.append(Tensao[4])
        GD_6.append(Tensao[5])

    plt.plot(GD_1, linewidth=4, label=u'GD 1')
    plt.plot(GD_2, linewidth=4, label=u'GD 2')
    plt.plot(GD_3, linewidth=4, label=u'GD 3')
    plt.plot(GD_4, linewidth=4, label=u'GD 4')
    plt.plot(GD_5, linewidth=4, label=u'GD 5')
    plt.plot(GD_6, linewidth=4, label=u'GD 6')
    plt.grid()
    #plt.legend(loc='upper right', fontsize=24)
    plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left', borderaxespad=0., fontsize=24)
    plt.ylim(0, 31)

    subplot(223) #####################################################################################

    # Create the function to plot
    GD_1 = []
    GD_2 = []
    GD_3 = []
    GD_4 = []
    GD_5 = []
    GD_6 = []

    for Tensao in Final_Q_GDs_por_Snap_S_VV:
        GD_1.append(Tensao[0])
        GD_2.append(Tensao[1])
        GD_3.append(Tensao[2])
        GD_4.append(Tensao[3])
        GD_5.append(Tensao[4])
        GD_6.append(Tensao[5])

    plt.plot(GD_1, linewidth=4, label=u'GD 1')
    plt.plot(GD_2, linewidth=4, label=u'GD 2')
    plt.plot(GD_3, linewidth=4, label=u'GD 3')
    plt.plot(GD_4, linewidth=4, label=u'GD 4')
    plt.plot(GD_5, linewidth=4, label=u'GD 5')
    plt.plot(GD_6, linewidth=4, label=u'GD 6')

    plt.xlabel(u'(A) HC sem VV ')
    plt.ylabel(U' Pot. GD (kVAr) ')
    plt.grid()

    plt.ylim(-16, 20)

    subplot(224) #####################################################################################

    # Create the function to plot
    GD_1 = []
    GD_2 = []
    GD_3 = []
    GD_4 = []
    GD_5 = []
    GD_6 = []

    for Tensao in Final_Q_GDs_por_Snap_C_VV:
        GD_1.append(Tensao[0])
        GD_2.append(Tensao[1])
        GD_3.append(Tensao[2])
        GD_4.append(Tensao[3])
        GD_5.append(Tensao[4])
        GD_6.append(Tensao[5])

    plt.plot(GD_1, linewidth=4, label=u'GD 1')
    plt.plot(GD_2, linewidth=4, label=u'GD 2')
    plt.plot(GD_3, linewidth=4, label=u'GD 3')
    plt.plot(GD_4, linewidth=4, label=u'GD 4')
    plt.plot(GD_5, linewidth=4, label=u'GD 5')
    plt.plot(GD_6, linewidth=4, label=u'GD 6')
    plt.grid()
    plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left', borderaxespad=0., fontsize=24)
    plt.xlabel(u'(B) HC com VV ')
    plt.ylim(-16, 20)


    plt.suptitle(u' Dados das GDs Inseridas ', fontsize=40, weight='bold')

    plt.figure(5)
    subplot(121) #####################################################################################
    barWidth = 1


    SomaHC = []
    X = []
    [SomaHC.append(sum(PotSnap)) for PotSnap in Final_P_GDs_por_Snap_S_VV]
    [X.append(i) for i in range(len(SomaHC))]
    plt.bar(X, SomaHC, color='#6A5ACD', width=barWidth, label='HC')
    plt.xlabel(u'(A) HC sem VV ')
    plt.ylabel(U' HC (kW) ')
    plt.grid()
    plt.legend(loc='upper right')
    plt.ylim(0, 152)
    from FunctionsSecond import find
    plt.annotate(u' HC : ' + str(round(max(SomaHC), 2)),
                xy=((X[find(SomaHC, max(SomaHC))]), max(SomaHC)),
                xycoords='data',
                xytext=(0, 100),
                textcoords='data',
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

    subplot(122) #####################################################################################

    SomaHC = []
    X = []
    [SomaHC.append(sum(PotSnap)) for PotSnap in Final_P_GDs_por_Snap_C_VV]
    [X.append(i) for i in range(len(SomaHC))]
    plt.bar(X, SomaHC, color='#6A5ACD', width=barWidth, label='HC')
    plt.xlabel(u'(B) HC com VV ')
    plt.grid()
    plt.legend(loc='upper right')
    plt.ylim(0, 152)
    plt.annotate(u' HC : ' + str(round(max(SomaHC), 2)),
                xy=((X[find(SomaHC, max(SomaHC))]), max(SomaHC)),
                xycoords='data',
                xytext=(0, 80),
                textcoords='data',
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

    plt.suptitle(u' Variação Hosting Capacity Durante o Dia ', fontsize=40, weight='bold')

def Comp_Pot_Sub(Final_Power_Sub, Final_Power_Sub_VV):




    plt.figure(3)

    # Create the function to plot
    P_A = []
    P_B = []
    P_C = []
    Q_A = []
    Q_B = []
    Q_C = []

    for Tensao in Final_Power_Sub:
        P_A.append(Tensao[0])
        P_B.append(Tensao[2])
        P_C.append(Tensao[4])
        Q_A.append(Tensao[1])
        Q_B.append(Tensao[3])
        Q_C.append(Tensao[5])

    subplot(221)  #####################################################################################

    plt.plot(P_A, linewidth=4, label=u'P(a)')
    plt.plot(P_B, linewidth=4, label=u'P(b)')
    plt.plot(P_C, linewidth=4, label=u'P(c)')
    plt.ylabel(U' Pot. Ativa (kW)')
    plt.grid()
    plt.ylim(-15, 25)
    #plt.xlim(0, 48)

    subplot(223)  #####################################################################################

    plt.plot(Q_A, linewidth=4, label=u'Q(a)')
    plt.plot(Q_B, linewidth=4, label=u'Q(b)')
    plt.plot(Q_C, linewidth=4, label=u'Q(c)')
    plt.xlabel(u'(A) HC sem VV ')
    plt.ylabel(U' Pot. Reativa (kVAr)')
    plt.grid()

    plt.ylim(-15, 25)
    #plt.xlim(0, 48)



    # Create the function to plot
    P_A = []
    P_B = []
    P_C = []
    Q_A = []
    Q_B = []
    Q_C = []

    for Tensao in Final_Power_Sub_VV:
        P_A.append(Tensao[0])
        P_B.append(Tensao[2])
        P_C.append(Tensao[4])
        Q_A.append(Tensao[1])
        Q_B.append(Tensao[3])
        Q_C.append(Tensao[5])

    subplot(222)  #####################################################################################

    plt.plot(P_A, linewidth=4, label=u'P(a)')
    plt.plot(P_B, linewidth=4, label=u'P(b)')
    plt.plot(P_C, linewidth=4, label=u'P(c)')
    plt.grid()
    plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left', borderaxespad=0., fontsize=24)
    plt.ylim(-15, 25)
    plt.xlim(0, 48)

    subplot(224)  #####################################################################################

    plt.plot(Q_A, linewidth=4, label=u'Q(a)')
    plt.plot(Q_B, linewidth=4, label=u'Q(b)')
    plt.plot(Q_C, linewidth=4, label=u'Q(c)')
    plt.xlabel(u'(b) HC com VV ')
    plt.grid()
    plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left', borderaxespad=0., fontsize=24)
    plt.ylim(-15, 25)
    plt.xlim(0, 48)

    plt.suptitle(u'Potência no Transformador de Entrada do Sistema', fontsize=40, weight='bold')

def Comp_HC_EXT(Final_Variables_Power_Sub, Final_Variables_Power_Sub_VV):

    LoopExterno_HC = []
    for LoopExterno in Final_Variables_Power_Sub:
        SomaHC = []
        [SomaHC.append(sum(PotSnap)) for PotSnap in LoopExterno]
        LoopExterno_HC.append(max(SomaHC))

    LoopExterno_HC_Media = ones(len(LoopExterno_HC)) * average(LoopExterno_HC)

    LoopExterno_HC_VV = []

    for LoopExterno in Final_Variables_Power_Sub_VV:
        SomaHC = []
        [SomaHC.append(sum(PotSnap)) for PotSnap in LoopExterno]
        LoopExterno_HC_VV.append(max(SomaHC))

    LoopExterno_HC_Media_VV = ones(len(LoopExterno_HC_VV)) * average(LoopExterno_HC_VV)

    plt.figure(4)
    barWidth = 0.5


    subplot(121)  #####################################################################################
    X = []
    [X.append(i) for i in range(len(LoopExterno_HC))]
    plt.bar(X, LoopExterno_HC, color='#6A5ACD', width=barWidth, label='HC')
    plt.plot(X, LoopExterno_HC_Media, linewidth=6, label=u'Avg HC', color='red')

    plt.xlabel(u'(a) HC sem VV ')
    plt.ylabel(U'HC (kW)')
    plt.grid()
    plt.legend(loc='upper right')
    plt.ylim(0, 200)
    plt.xlim(0, len(LoopExterno_HC_VV ) - 1)
    plt.annotate(u'Avg HC : ' + str(round(LoopExterno_HC_Media[0], 2)),
                xy=(((float(len(LoopExterno_HC)-1))/2), LoopExterno_HC_Media[0]),
                xycoords='data',
                xytext=(0.1*(len(LoopExterno_HC) - 1), 160),
                textcoords='data',
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

    subplot(122)  #####################################################################################
    X = []
    [X.append(i) for i in range(len(LoopExterno_HC_VV))]
    plt.bar(X, LoopExterno_HC_VV, color='#6A5ACD', width=barWidth, label='HC')
    plt.plot(X, LoopExterno_HC_Media_VV, linewidth=6, label=u'Avg HC', color='red')

    plt.xlabel(u'(b) HC com VV ')
    plt.grid()
    plt.legend(loc='upper right')
    plt.ylim(0, 200)
    plt.xlim(0, len(LoopExterno_HC_VV ) - 1)
    plt.annotate(u'Avg HC : ' + str(round(LoopExterno_HC_Media_VV[0], 2)),
                xy=(((float(len(LoopExterno_HC_VV)-1))/2), LoopExterno_HC_Media_VV[0]),
                xycoords='data',
                xytext=(0.1*(len(LoopExterno_HC_VV) - 1), 160),
                textcoords='data',
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))


    plt.suptitle(u'Média da Variação do Hosting Capacity', fontsize=40, weight='bold')

    plt.show()
def Plota_Nivel_Tensao(Tensoes):
    puVmag_1 = []
    puVmag_2 = []
    puVmag_3 = []

    for Tensao in Tensoes:
        puVmag_1.append(Tensao[0])
        puVmag_2.append(Tensao[1])
        puVmag_3.append(Tensao[2])

    barWidth = 0.25
    r1 = np.arange(len(puVmag_1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
    plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
    plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')

    plt.xlabel('Barras')
    # Bus_Name = Plot.Leitura_Nome_Barras(self)
    plt.xticks([r + barWidth for r in range(len(Tensoes))])
    plt.ylabel('puVoltages')
    plt.title(u'Tensões nas barras')

    plt.grid()
    plt.legend()
    plt.ylim(0.8, 1.10)
    plt.show()

class Plot(DSS):

    def Plota_Nivel_Tensao(self, Tensoes):

        puVmag_1 = []
        puVmag_2 = []
        puVmag_3 = []

        for Tensao in Tensoes:
                puVmag_1.append(Tensao[0])
                puVmag_2.append(Tensao[1])
                puVmag_3.append(Tensao[2])

        barWidth = 0.25
        r1 = np.arange(len(puVmag_1))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
        plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
        plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')

        plt.xlabel('Barras')
        #Bus_Name = Plot.Leitura_Nome_Barras(self)
        plt.xticks([r + barWidth for r in range(len(Tensoes))])
        plt.ylabel('puVoltages')
        plt.title(u'Tensões nas barras')

        plt.grid()
        plt.legend()
        plt.ylim(0.8, 1.10)
        plt.show()

    def Plot_Pot_Dia(self, Powers):

        P_W_A = []
        P_Q_A = []
        P_W_B = []
        P_Q_B = []
        P_W_C = []
        P_Q_C = []

        for Power in Powers:
            P_W_A.append(Power[0])
            P_Q_A.append(Power[1])
            P_W_B.append(Power[2])
            P_Q_B.append(Power[3])
            P_W_C.append(Power[4])
            P_Q_C.append(Power[5])
        x = range(len(P_W_A))

        subplot(121)
        plt.plot(x, P_W_A, x, P_W_B, x, P_W_C)
        subplot(122)
        plt.plot(x, P_Q_A, x, P_Q_B, x, P_Q_C)

        plt.show()

    def Plot_Tensao_Dia_Uma_Barra(self, All_Buses, Name_Bus):

        Bus_Name = str(Name_Bus)

        # Acha o indice do nome da barra
        Position_Bus = 0
        for Bus in DSS.Leitura_Nome_Barras(self):
            if Bus == Bus_Name:
                Position_Bus = Position_Bus
                break
            else:
                Position_Bus = Position_Bus + 1

        # Create an vector to save de voltage of this bus
        Bus_Voltage_Daily = []
        for Bus_Voltage in All_Buses:
            Bus_Voltage_Daily.append(Bus_Voltage[Position_Bus])

        #Create the function to plot
        puVmag_1 = []
        puVmag_2 = []
        puVmag_3 = []

        for Tensao in Bus_Voltage_Daily:
            puVmag_1.append(Tensao[0])
            puVmag_2.append(Tensao[1])
            puVmag_3.append(Tensao[2])

        barWidth = 0.25
        r1 = np.arange(len(puVmag_1))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
        plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
        plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')

        plt.xlabel('Barra ' + str(Bus_Name))
        plt.ylabel('puVoltages')
        plt.title(u'Tensões nas barras')

        plt.grid()
        plt.legend()
        plt.ylim(0.8, 1.10)
        plt.show()

    def Plot_Teste_2(self, Tensoes, Powers, Tensoes_Dia_VV, Powers_Dia_VV, Name_Bus):

        plt.subplot(321)#######################################################
        Bus_Name = str(Name_Bus)

        # Acha o indice do nome da barra
        Position_Bus = 0
        for Bus in DSS.Leitura_Nome_Barras(self):
            if Bus == Bus_Name:
                Position_Bus = Position_Bus
                break
            else:
                Position_Bus = Position_Bus + 1

        # Create an vector to save de voltage of this bus
        Bus_Voltage_Daily = []
        for Bus_Voltage in Tensoes:
            Bus_Voltage_Daily.append(Bus_Voltage[Position_Bus])

        # Create the function to plot
        puVmag_1 = []
        puVmag_2 = []
        puVmag_3 = []

        for Tensao in Bus_Voltage_Daily:
            puVmag_1.append(Tensao[0])
            puVmag_2.append(Tensao[1])
            puVmag_3.append(Tensao[2])

        barWidth = 0.25
        r1 = np.arange(len(puVmag_1))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
        plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
        plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')

        plt.xlabel('Barra ' + str(Bus_Name))
        plt.ylabel('puVoltages')
        plt.title(u'Tensões nas barras')

        plt.grid()
        plt.legend()
        plt.ylim(0.97, 1.03)

        plt.subplot(322)###################################################################
        Bus_Name = str(Name_Bus)

        # Acha o indice do nome da barra
        Position_Bus = 0
        for Bus in DSS.Leitura_Nome_Barras(self):
            if Bus == Bus_Name:
                Position_Bus = Position_Bus
                break
            else:
                Position_Bus = Position_Bus + 1

        # Create an vector to save de voltage of this bus
        Bus_Voltage_Daily = []
        for Bus_Voltage in Tensoes_Dia_VV:
            Bus_Voltage_Daily.append(Bus_Voltage[Position_Bus])

        # Create the function to plot
        puVmag_1 = []
        puVmag_2 = []
        puVmag_3 = []

        for Tensao in Bus_Voltage_Daily:
            puVmag_1.append(Tensao[0])
            puVmag_2.append(Tensao[1])
            puVmag_3.append(Tensao[2])

        barWidth = 0.25
        r1 = np.arange(len(puVmag_1))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
        plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
        plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')

        plt.xlabel('Barra ' + str(Bus_Name))
        plt.ylabel('puVoltages')
        plt.title(u'Tensões nas barras')

        plt.grid()
        plt.ylim(0.97, 1.03)

        plt.subplot(323)  ###################################################################
        P_A = []
        P_B = []
        P_C = []

        for fase in Powers:
            P_A.append(Powers[0])
            P_B.append(Powers[2])
            P_C.append(Powers[4])

        plt.plot(P_A)
        plt.plot(P_B)
        plt.plot(P_C)

        plt.subplot(324)  ###################################################################

        P_A = []
        P_B = []
        P_C = []

        for fase in Powers_Dia_VV:
            P_A.append(Powers[0])
            P_B.append(Powers[2])
            P_C.append(Powers[4])

        plt.plot(P_A)
        plt.plot(P_B)
        plt.plot(P_C)

        plt.subplot(325)  ###################################################################
        Q_A = []
        Q_B = []
        Q_C = []

        for fase in Powers:
            Q_A.append(Powers[1])
            Q_B.append(Powers[3])
            Q_C.append(Powers[5])

        plt.plot(Q_A)
        plt.plot(Q_B)
        plt.plot(Q_C)

        plt.subplot(326)  ###################################################################
        Q_A = []
        Q_B = []
        Q_C = []

        for fase in Powers_Dia_VV:
            Q_A.append(Powers[1])
            Q_B.append(Powers[3])
            Q_C.append(Powers[5])

        plt.plot(Q_A)
        plt.plot(Q_B)
        plt.plot(Q_C)

        plt.show()

    def Plot_Tensao_Reativo_Volt_Var(self, All_Buses, Reativo_GDs, Name_Bus):

        plt.subplot(311)
        Bus_Name = str(Name_Bus)

        # Acha o indice do nome da barra
        Position_Bus = 0
        for Bus in DSS.Leitura_Nome_Barras(self):
            if Bus == Bus_Name:
                Position_Bus = Position_Bus
                break
            else:
                Position_Bus = Position_Bus + 1

        # Create an vector to save de voltage of this bus
        Bus_Voltage_Daily = []
        for Bus_Voltage in All_Buses:
            Bus_Voltage_Daily.append(Bus_Voltage[Position_Bus])

        # Create the function to plot
        puVmag_1 = []
        puVmag_2 = []
        puVmag_3 = []

        for Tensao in Bus_Voltage_Daily:
            puVmag_1.append(Tensao[0])
            puVmag_2.append(Tensao[1])
            puVmag_3.append(Tensao[2])

        barWidth = 0.25
        r1 = np.arange(len(puVmag_1))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
        plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
        plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')

        plt.xlabel('Barra ' + str(Bus_Name))
        plt.ylabel('puVoltages')
        plt.title(u'Tensões nas barras')

        plt.grid()
        #plt.legend()
        plt.ylim(0.97, 1.03)

        plt.subplot(312)
        Index_GD = DSS.Retorna_GD_da_Barra(self, Name_Bus)

        plt.plot(Reativo_GDs[Index_GD])
        plt.xlabel('Barra ' + str(Bus_Name))
        plt.ylabel('kVAr')
        plt.grid()

        plt.subplot(313)
        Max = 1.08
        Min = 0.92

        Vector_X = [Min]
        for itera in range(int((Max-Min) * 100)):
            Vector_X.append(Vector_X[itera] + 0.01)

        from FunctionsSecond import Verifica_Fase
        Vector_Y = Verifica_Fase(Vector_X)

        Vet_X = []
        for X in Vector_X:
            Vet_X.append(X)


        plt.plot(Vet_X, Vector_Y)
        plt.grid()
        plt.xlabel('puVoltages')
        plt.ylabel('pukVAr')

        plt.show()

    def Plot_Pot_CC(self, Pout_GDs, Qout_GDs, Powers_Sub, Powers_Loads):

        Pl = []
        Ql = []

        subplot(321)
        plt.plot(Pout_GDs)
        plt.ylabel('kW')
        plt.title(u'Somatório potência ativa GDs (Pgd)')
        plt.grid()

        subplot(322)
        plt.plot(Qout_GDs)
        plt.ylabel('kVAr')
        plt.title(u'Somatório potência reativa GDs (Qgd)')
        plt.grid()

        from FunctionsSecond import PCC_QCC_Vet
        Pcc, Qcc = PCC_QCC_Vet(Powers_Sub)

        subplot(323)
        plt.plot(Pcc)
        plt.ylabel('kW')
        plt.title(u'Potência ativa Pcc')
        plt.grid()
        subplot(324)
        plt.plot(Qcc)
        plt.ylabel('kVAr')
        plt.title(u' Potência reativa Qcc')
        plt.grid()

        for i in range(len(Pcc)):
            Pl.append(Pcc[i] + Pout_GDs[i])
            Ql.append(Qcc[i] + Qout_GDs[i])

        subplot(325)
        plt.plot(Pl)
        plt.ylabel('kW')
        plt.title(u' PCC + Pgd')
        plt.grid()
        subplot(326)
        plt.plot(Ql)
        plt.ylabel('kVAr')
        plt.title(u' Qcc + Qgd')
        plt.grid()

        plt.show()

    def Plot_Alfa_Beta(self, Alfa, Beta):

        subplot(121)
        plt.plot(Alfa)
        subplot(122)
        plt.plot(Beta)

        plt.show()

    def Plot(self, vet):

        plt.plot(vet)
        plt.show()

    def Plot_Pot_Volt_Var(self, kvar_GDs, kw_GDs):

        subplot(121)
        plt.plot(kvar_GDs[0])
        subplot(122)
        plt.plot(kw_GDs[0])

        plt.show()

# TESTES
    def Plot_Pot_CC_teste(self, Pout_GDs, Qout_GDs, Powers_Sub, Powers_Loads, P_A, P_B, P_C):

        P_W_A = []
        P_Q_A = []
        P_W_B = []
        P_Q_B = []
        P_W_C = []
        P_Q_C = []

        Pcc = []
        Qcc = []

        Pl = []
        Ql = []

        P_teste = []
        Q_teste = []

        subplot(421)
        plt.plot(Pout_GDs)
        plt.ylabel('kW')
        plt.title(u'Somatório potência ativa GDs (Pgd)')
        plt.grid()

        subplot(422)
        plt.plot(Qout_GDs)
        plt.ylabel('kVAr')
        plt.title(u'Somatório potência reativa GDs (Qgd)')
        plt.grid()

        for Power in Powers_Sub:
            P_W_A.append(Power[0])
            P_Q_A.append(Power[1])
            P_W_B.append(Power[2])
            P_Q_B.append(Power[3])
            P_W_C.append(Power[4])
            P_Q_C.append(Power[5])
        x = range(len(P_W_A))

        for i in range(len(P_W_C)):
            Pcc.append(P_W_A[i] + P_W_B[i] + P_W_C[i])
            Qcc.append(P_Q_A[i] + P_Q_B[i] + P_Q_C[i])

        subplot(423)
        plt.plot(Pcc)
        plt.ylabel('kW')
        plt.title(u'Potência ativa Pcc')
        plt.grid()
        subplot(424)
        plt.plot(Qcc)
        plt.ylabel('kVAr')
        plt.title(u' Potência reativa Qcc')
        plt.grid()

        for i in range(len(Pcc)):
            Pl.append(Pcc[i] + Pout_GDs[i])
            Ql.append(Qcc[i] + Qout_GDs[i])


        subplot(425)
        plt.plot(Pl)
        plt.ylabel('kW')
        plt.title(u' PCC + Pgd')
        plt.grid()
        subplot(426)
        plt.plot(Ql)
        plt.ylabel('kVAr')
        plt.title(u' Qcc + Qgd')
        plt.grid()

        subplot(427)
        plt.plot(Powers_Loads)
        plt.ylabel('kW')
        plt.title(u' Pot Ativa Loads')
        plt.grid()

        for i in range(len(Pcc)):
            P_teste.append(Powers_Loads[i] - Pout_GDs[i])
            Q_teste.append(Powers_Loads[i] - Qout_GDs[i])

        subplot(428)
        plt.plot(P_teste)
        plt.ylabel('kW')
        plt.title(u' Pot Ativa Loads')
        plt.grid()


        plt.show()

    def Plot_Teste(self, P_A, P_B, P_C, P_A_GD, P_B_GD, P_C_GD, Powers):

        P_W_A = []
        P_Q_A = []
        P_W_B = []
        P_Q_B = []
        P_W_C = []
        P_Q_C = []

        P1 = []
        P2 = []
        P3 = []
        Q1 = []
        Q2 = []
        Q3 = []

        for Power in Powers:
            P_W_A.append(Power[0])
            P_Q_A.append(Power[1])
            P_W_B.append(Power[2])
            P_Q_B.append(Power[3])
            P_W_C.append(Power[4])
            P_Q_C.append(Power[5])

        for i in range(len(P_W_A)):
            P1.append(P_W_A[i] + P_A_GD[i])
            #Q1.append(Q_A[i] + Q_A_GD[i])

            P2.append(P_W_B[i] + P_B_GD[i])
            #Q2.append(Q_B[i] + Q_B_GD[i])

            P3.append(P_W_C[i] + P_C_GD[i])
            #Q3.append(Q_C[i] + Q_C_GD[i])

        subplot(3,4,1)
        plt.plot(P_W_A)
        subplot(3,4,2)
        plt.plot(P_A_GD)
        subplot(3,4,3)
        plt.plot(P1)
        subplot(3,4,4)
        plt.plot(P_A)

        subplot(3,4,5)
        plt.plot(P_W_B)
        subplot(3,4,6)
        plt.plot(P_B_GD)
        subplot(3,4,7)
        plt.plot(P2)
        subplot(3,4,8)
        plt.plot(P_B)

        subplot(3,4,9)
        plt.plot(P_W_C)
        subplot(3,4,10)
        plt.plot(P_C_GD)
        subplot(3,4,11)
        plt.plot(P3)
        subplot(3,4,12)
        plt.plot(P_C)

        plt.show()

    def Plot_Efeito_VV_GDs(self, Nome_Barra):

        # def Plot_Efeito_VV_GDs(self, Tensoes_Dia, Tensoes_Dia_VV, Nome_Barra, Powers_Dia, Powers_Dia_VV, Pot_Ativa_GDs_por_snap,
        #                              Pot_Reativa_GDs_por_snap, Pot_Ativa_GDs_por_snap_VV, Pot_Reativa_GDs_por_snap_VV):

        Tensoes_Dia = self.Tensoes_Dia
        Tensoes_Dia_VV = self.Tensoes_Dia_VV
        Pot_Ativa_GDs_por_snap = Func.Pot_Ativa_GDs_por_snap
        Pot_Reativa_GDs_por_snap = self.Pot_Reativa_GDs_por_snap
        Pot_Ativa_GDs_por_snap_VV = self.Pot_Ativa_GDs_por_snap_VV
        Pot_Reativa_GDs_por_snap_VV = self.Pot_Reativa_GDs_por_snap_VV

        GD = DSS.Acha_GD_da_Bara_retorna_o_indice(self, Nome_Barra)
        print GD

        subplot(321)
        Vet_Valor = []
        for pot_gds in Pot_Ativa_GDs_por_snap:
            Vet_Valor.append(pot_gds[GD])
        plt.plot(Vet_Valor)
        plt.ylim(0, 4)
        plt.grid()

        subplot(322)
        Vet_Valor = []
        for pot_gds in Pot_Ativa_GDs_por_snap_VV:
            Vet_Valor.append(pot_gds[GD])
        plt.plot(Vet_Valor)
        plt.ylim(0, 4)
        plt.grid()

        subplot(323)
        Vet_Valor = []
        for pot_gds in Pot_Reativa_GDs_por_snap:
            Vet_Valor.append(pot_gds[GD])
        plt.plot(Vet_Valor)
        plt.ylim(0, 5)
        plt.grid()

        subplot(324)
        Vet_Valor = []
        for pot_gds in Pot_Reativa_GDs_por_snap_VV:
            Vet_Valor.append(pot_gds[GD])
        plt.plot(Vet_Valor)
        plt.ylim(0, 5)
        plt.grid()

        subplot(325)

        Bus_Voltage_Daily = []
        for Bus_Voltage in Tensoes_Dia:
            Bus_Voltage_Daily.append(Bus_Voltage[2])

        # Create the function to plot
        puVmag_1 = []
        puVmag_2 = []
        puVmag_3 = []

        for Tensao in Bus_Voltage_Daily:
            puVmag_1.append(Tensao[0])
            puVmag_2.append(Tensao[1])
            puVmag_3.append(Tensao[2])

        barWidth = 0.25
        r1 = np.arange(len(puVmag_1))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
        plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
        plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')

        plt.ylabel('puVoltages')
        plt.title(u'Tensões nas barras')

        # plt.legend()
        plt.ylim(0.98, 1.01)
        plt.grid()

        subplot(326)

        Bus_Voltage_Daily = []
        for Bus_Voltage in Tensoes_Dia_VV:
            Bus_Voltage_Daily.append(Bus_Voltage[2])

        # Create the function to plot
        puVmag_1 = []
        puVmag_2 = []
        puVmag_3 = []

        for Tensao in Bus_Voltage_Daily:
            puVmag_1.append(Tensao[0])
            puVmag_2.append(Tensao[1])
            puVmag_3.append(Tensao[2])

        barWidth = 0.25
        r1 = np.arange(len(puVmag_1))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
        plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
        plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')


        plt.ylabel('puVoltages')
        plt.title(u'Tensões nas barras')
        #plt.legend()
        plt.ylim(0.98, 1.01)
        plt.grid()

        plt.show()

    def Plot_Efeito_VV_Storages(self, Name_Bus, Tensoes_Dia):

        Bus_Name = str(Name_Bus)

        # Acha o indice do nome da barra
        Position_Bus = 0
        for Bus in DSS.Leitura_Nome_Barras(self):
            if Bus == Bus_Name:
                Position_Bus = Position_Bus
                break
            else:
                Position_Bus = Position_Bus + 1

        plt.figure(1)
        subplot(111)

        Bus_Voltage_Daily = []
        for Bus_Voltage in Tensoes_Dia:
            Bus_Voltage_Daily.append(Bus_Voltage[Position_Bus])

        # Create the function to plot
        puVmag_1 = []
        puVmag_2 = []
        puVmag_3 = []

        for Tensao in Bus_Voltage_Daily:
            puVmag_1.append(Tensao[0])
            puVmag_2.append(Tensao[1])
            puVmag_3.append(Tensao[2])

        barWidth = 0.25
        r1 = np.arange(len(puVmag_1))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        plt.bar(r1, puVmag_1, color='#6A5ACD', width=barWidth, label='A')
        plt.bar(r2, puVmag_2, color='#6495ED', width=barWidth, label='B')
        plt.bar(r3, puVmag_3, color='#00BFFF', width=barWidth, label='C')

        plt.ylabel('puVoltages')
        plt.xlabel(str(Bus_Name))
        plt.title(u'Tensões nas barras')

        # plt.legend()
        plt.ylim(0.98, 1.01)
        plt.grid()

        plt.show()

    # Trava o PC
    def Plot_Tensoes_Dia(self, Tensoes_Dia):

        fig = plt.figure()
        ax1 = fig.add_subplot(111, projection='3d')

        zpos = np.ones(len(Tensoes_Dia[0])) * 0.9  # start point, tem que ser zero
        dx = np.ones(len(Tensoes_Dia[0])) / 4
        dy = np.ones(len(Tensoes_Dia[0])) / 4

        barWidth = 0.25
        ypos1 = np.arange(len(zpos))
        ypos2 = [x + barWidth for x in ypos1]
        ypos3 = [x + barWidth for x in ypos2]

        for Min in range(len(Tensoes_Dia)):
            print Min
            xpos = np.ones(len(Tensoes_Dia[0])) * (Min + 1)
            dz1 = []
            dz2 = []
            dz3 = []
            for Barra in range(len(zpos)):
                if (Tensoes_Dia[Min][Barra][0] == 0):
                    dz1.append(Tensoes_Dia[Min][Barra][0])
                else:
                    dz1.append(Tensoes_Dia[Min][Barra][0] - 0.9)
                if (Tensoes_Dia[Min][Barra][1] == 0):
                    dz2.append(Tensoes_Dia[Min][Barra][1])
                else:
                    dz2.append(Tensoes_Dia[Min][Barra][1] - 0.9)
                if (Tensoes_Dia[Min][Barra][2] == 0):
                    dz3.append(Tensoes_Dia[Min][Barra][2])
                else:
                    dz3.append(Tensoes_Dia[Min][Barra][2] - 0.9)

            ax1.bar3d(xpos, ypos1, zpos, dx, dy, dz1, color='#6A5ACD', label='A', shade=True)
            ax1.bar3d(xpos, ypos2, zpos, dx, dy, dz2, color='#6495ED', label='B', shade=True)
            ax1.bar3d(xpos, ypos3, zpos, dx, dy, dz3, color='#00BFFF', label='C', shade=True)

        plt.xlabel('X_Min')
        plt.ylabel('Y_Barra')
        #plt.xlim(0, 24)
        #plt.ylim(0, 16)
        ax1.set_zlim3d(0.9, 1.075)
        ax1.set_xlim(0, 24)
        ax1.set_ylim(0, 16)

        plt.show() #











