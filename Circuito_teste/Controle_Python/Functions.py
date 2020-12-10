# coding: utf-8
from OpenDSS_Functions import *
from Plots import *
import cmath

class Func(DSS):

    #################### Desequilibrio de Tensão
    def Chama_IEC(self, Tensoes, Angulos):

        Deseq = []
        for i in range(len(Tensoes)):
            Deseq.append(Func.IEC(self, Tensoes[i][0], Tensoes[i][1], Tensoes[i][2], Angulos[i][0], Angulos[i][1], Angulos[i][2],))
        return Deseq

    def IEC(self, Tensao1, Tensao2, Tensao3, Angle1, Angle2, Angle3):  # Limite de 3%

        alfa = complex(-0.5, 0.866025403784)
        inv_alfa = complex(-0.5, -0.866025403784)

        if Tensao1 != 0 and Tensao2 != 0 and Tensao3 != 0:
            Positiva = 0.333333 * (
                    (cmath.rect(Tensao1, np.deg2rad(Angle1))) + (alfa * cmath.rect(Tensao2, np.deg2rad(Angle2))) + (
                    inv_alfa * cmath.rect(Tensao3, np.deg2rad(Angle3))))
            Negativa = 0.333333 * ((cmath.rect(Tensao1, np.deg2rad(Angle1))) + (
                    inv_alfa * cmath.rect(Tensao2, np.deg2rad(Angle2))) + (
                                           alfa * cmath.rect(Tensao3, np.deg2rad(Angle3))))
            return (abs(Negativa) / abs(Positiva)) * 100
        else:
            return 0

    def IEEE(self, Tensao1, Tensao2, Tensao3, max, min):

        invsqrt3 = 1 / (3 ** (0.5))

        # Utiliza tensões de fase
        return (3 * 100 * (max - min)) / (Tensao1 + Tensao2 + Tensao3)

    def NEMA(self, Vmedio, Vmax):

        return ((Vmax - Vmedio) / Vmedio) * 100

    def Max_Min(self, Tensao1, Tensao2, Tensao3):

        Vet_Max_Min = [Tensao1, Tensao2, Tensao3]

        if Tensao1 != 0 and Tensao2 != 0 and Tensao3 != 0:
            max_Tensao = max(Vet_Max_Min)
            min_Tensao = min(Vet_Max_Min)
            return max_Tensao, min_Tensao

        elif Tensao1 == 0 and Tensao2 != 0 and Tensao3 != 0:

            max_Tensao = max(Vet_Max_Min)
            if Tensao2 > Tensao3:
                min_Tensao = Tensao3
                return max_Tensao, min_Tensao
            else:
                min_Tensao = Tensao3
                return max_Tensao, min_Tensao

        elif Tensao1 != 0 and Tensao2 == 0 and Tensao3 != 0:

            max_Tensao = max(Vet_Max_Min)
            if Tensao1 > Tensao3:
                min_Tensao = Tensao3
                return max_Tensao, min_Tensao
            else:
                min_Tensao = Tensao1
                return max_Tensao, min_Tensao

        elif Tensao1 != 0 and Tensao2 != 0 and Tensao3 == 0:

            max_Tensao = max(Vet_Max_Min)
            if Tensao1 > Tensao2:
                min_Tensao = Tensao2
                return max_Tensao, min_Tensao
            else:
                min_Tensao = Tensao1
                return max_Tensao, min_Tensao

        else:
            max_Tensao = max(Vet_Max_Min)
            min_Tensao = max_Tensao
            return max_Tensao, min_Tensao

    #################### Nível de Tensão

    def Tensao_Barras(self):

        puVmag_Buses = []
        angle_Buses = []
        Bus_Names = Func.Leitura_Nome_Barras(self)

        for Barra in Bus_Names:

            puVmag = []
            angle = []
            Func.ativa_barra(self, Barra)  # Ativa a barra
            VmagAngle = Func.puVmagAngle(self)
            # print " Cromossomo puVmag " + str(VmagAngle)

            if len(VmagAngle) == 6:
                puVmag.append(VmagAngle[0])
                puVmag.append(VmagAngle[2])
                puVmag.append(VmagAngle[4])
            elif len(VmagAngle) == 4:
                puVmag.append(VmagAngle[0])
                puVmag.append(VmagAngle[2])
                puVmag.append(0)
            elif len(VmagAngle) == 2:
                puVmag.append(VmagAngle[0])
                puVmag.append(0)
                puVmag.append(0)

            if len(VmagAngle) == 6:
                angle.append(VmagAngle[1])
                angle.append(VmagAngle[3])
                angle.append(VmagAngle[5])
            elif len(VmagAngle) == 4:
                angle.append(VmagAngle[1])
                angle.append(VmagAngle[3])
                angle.append(0)
            elif len(VmagAngle) == 2:
                angle.append(VmagAngle[1])
                angle.append(0)
                angle.append(0)

            puVmag_Buses.append(puVmag)
            angle_Buses.append(angle)

        return puVmag_Buses, angle_Buses

    def Pot_Sub_entrada(self):

        All_Elements_Names = self.dssCircuit.AllElementNames
        for Element in All_Elements_Names:
            if Element == 'Transformer.sub':
                Func.Ativa_Elemento(self, Element)
                return self.dssCktElement.Powers

    def Pot_Loads(self):

        # Retorna Pot trifásica
        All_Elements_Names = self.dssCircuit.AllElementNames
        Power_P = 0
        Power_Q = 0
        for Element in All_Elements_Names:
            if Element[0:4] == 'Load':
                Func.Ativa_Elemento(self, Element)
                Power = self.dssCktElement.Powers
                Power_P = Power_P + Power[0]
                Power_Q = Power_Q + Power[1]
        return Power_P

    def Pot_Loads_Fase(self):

        # Retorna Pot trifásica
        All_Elements_Names = self.dssCircuit.AllElementNames

        P_A = 0
        Q_A = 0
        P_B = 0
        Q_B = 0
        P_C = 0
        Q_C = 0

        for Element in All_Elements_Names:
            Func.Ativa_Elemento(self, Element)
            Power = self.dssCktElement.Powers
            if Element[0:4] == 'Load':
                if Element[-1] == 'a':
                    P_A = P_A + Power[0]
                    Q_A = Q_A + Power[1]
                elif Element[-1] == 'b':
                    P_B = P_B + Power[0]
                    Q_B = Q_B + Power[1]
                elif Element[-1] == 'c':
                    P_C = P_C + Power[0]
                    Q_C = Q_C + Power[1]

        return P_A, Q_A, P_B, Q_B, P_C, Q_C

    def Pot_GD_Fase(self):
        # Não consegui identificar o erro, está computando mais potÊncia do que deveria


        P_A = 0
        Q_A = 0
        P_B = 0
        Q_B = 0
        P_C = 0
        Q_C = 0

        arquivo = open('C:\Users\hugo1\Desktop\Projeto_Final_Microrredes_Copia_Copia\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\Fases_GDs.txt', 'r')
        Fases_GD =[]
        for linha in arquivo:
            Fases_GD.append(linha.rstrip())
        arquivo.close()

        for GD in self.dssGenerators.AllNames:

            self.dssGenerators.Name = str(GD)
            if self.dssGenerators.Phases == 1:
                if Fases_GD[int(GD[-1])-1] == "A":
                    P_A = P_A + self.dssGenerators.kW
                    Q_A = Q_A + self.dssGenerators.kvar
                elif Fases_GD[int(GD[-1])-1] == 'B':
                    P_B = P_B + self.dssGenerators.kW
                    Q_B = Q_B + self.dssGenerators.kvar
                elif Fases_GD[int(GD[-1])-1] == 'C':
                    P_C = P_C + self.dssGenerators.kW
                    Q_C = Q_C + self.dssGenerators.kvar
            elif self.dssGenerators.Phases == 2:
                for No in Fases_GD[int(GD[-1])-1]:
                    if No == "A":
                        P_A = P_A + self.dssGenerators.kW/2
                        Q_A = Q_A + self.dssGenerators.kvar/2
                    elif No == 'B':
                        P_B = P_B + self.dssGenerators.kW/2
                        Q_B = Q_B + self.dssGenerators.kvar/2
                    elif No == 'C':
                        P_C = P_C + self.dssGenerators.kW/2
                        Q_C = Q_C + self.dssGenerators.kvar/2
            elif self.dssGenerators.Phases == 3:
                for No in Fases_GD[int(GD[-1])-1]:
                    if No == "A":
                        P_A = P_A + self.dssGenerators.kW/3
                        Q_A = Q_A + self.dssGenerators.kvar/3
                    elif No == 'B':
                        P_B = P_B + self.dssGenerators.kW/3
                        Q_B = Q_B + self.dssGenerators.kvar/3
                    elif No == 'C':
                        P_C = P_C + self.dssGenerators.kW/3
                        Q_C = Q_C + self.dssGenerators.kvar/3

        return P_A, Q_A, P_B, Q_B, P_C, Q_C

    #################### Controle Central

    def CC(self, Powers, P_max):

        ## Potência no ponto de acoplamento
        from FunctionsSecond import PCC_QCC
        Pcc, Qcc = PCC_QCC(Powers)

        ## Potência GDs
        Pout, Qout = Func.Powers_GDs(self)

        ## Total Absorvido pelo Acoplamento da MG
        P_L = Pcc[0] + Pout
        Q_L = Qcc[0] + Qout

        ## Capacidade de potência dos conversores
        from FunctionsSecond import Leitura_kW_GDs
        Pot_Ativa = Leitura_kW_GDs()

        from FunctionsSecond import Leitura_kvar_GDs
        Pot_Reativa = Leitura_kvar_GDs()

        from FunctionsSecond import Soma_Elementos_Vetor
        Sum_Pot_Ativa = Soma_Elementos_Vetor(Pot_Ativa)
        Sum_Pot_Reativa = Soma_Elementos_Vetor(Pot_Reativa)

        A_gt = sqrt((Sum_Pot_Ativa**2) + (Sum_Pot_Reativa**2))

        ## Potência máxima e minima

        # Primeiro Teste

        P_max = 30
        P_0 = Pcc[-1]

        Q_max = 30
        Q_0 = Qcc[-1]


        ## Alfa e Beta
        Alfa = (P_L - P_0) / P_max
        Beta = (Q_L - Q_0) / Q_max

        if Alfa >= 1:
            Alfa = 1
        elif Alfa <= 0:
            Alfa = 0

        if Beta >= 1:
            Beta = 1
        elif Beta <= -1:
            Beta = -1


        Beta = 0


        return Alfa, Beta

    def Powers_GDs(self):

        Pout = 0
        Qout = 0

        for GD in self.dssGenerators.AllNames:
            self.dssGenerators.Name = str(GD)

            if self.dssGenerators.Phases == 1:
                kW = self.dssGenerators.kW
                kVAr = self.dssGenerators.kVAr
            elif self.dssGenerators.Phases == 2:
                kW = self.dssGenerators.kW/2
                kVAr = self.dssGenerators.kVAr/2
            elif self.dssGenerators.Phases == 3:
                kW = self.dssGenerators.kW/3
                kVAr = self.dssGenerators.kVAr/3

            Pout = Pout + kW
            Qout = Qout + kVAr

        return Pout, Qout


    ################# VIOLACAO MICRORREDES

    def Viola(self, Tensao_Itera, IEC_Itera):

        from FunctionsSecond import Pertinencia_Trapezoid, Pertinencia_Triang


        # Conferir Tensões
        for Barra in range(len(Tensao_Itera)):
            for Fase in Tensao_Itera[Barra]:
                if Fase > 1.05 or Fase < 0.92:
                    print Tensao_Itera[Barra]
                    return 1

        # Confere Desequilibrio
        Violacao_D = 0
        for Barra in IEC_Itera:
            if Barra >= 3:
                return 1

        return 0

