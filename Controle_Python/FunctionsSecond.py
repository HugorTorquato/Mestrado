# coding: utf-8

def find(str, ch):
    indice = 0
    while indice < len(str):
        if str[indice] == ch:
            return indice
        indice = indice + 1
    return -1

def Verify_Phases(Phases):

    if len(Phases) > 3 or len(Phases) == 0:
        print " Phases incorretas"
        return 0
    elif len(Phases) == 1:
        if Phases == 'A' or Phases == 'B' or Phases == 'C':
            return 1
        else:
            print " Phases incorretas"
            return 0
    elif len(Phases) == 2:
        if Phases == "AB" or Phases == "BA":
            return 1
        elif Phases == "AC" or Phases == "CA":
            return 1
        elif Phases == "BC" or Phases == "CB":
            return 1
        else:
            print " Phases incorretas"
            return 0
    elif len(Phases) == 3:
        if Phases == "ABC" or Phases == "BCA" or Phases == "CBA" or Phases == "BAC":
            return 1
        else:
            print " Phases incorretas"
            return 0
    else:
        print " Phases incorretas"
        return 0

def Identify_Phases(Phases):

    Num_Phases = ""
    for Phase in Phases:
        if Phase == "A":
            Num_Phases = Num_Phases + ".1"
        elif Phase == "B":
            Num_Phases = Num_Phases + ".2"
        elif Phase == "C":
            Num_Phases = Num_Phases + ".3"
    return Num_Phases

def Agrega_Fase_Tensao(AllVoltages):

    Fase_A = []
    Fase_B = []
    Fase_C = []
    Fase_Media = []
    A = 0
    B = 1
    C = 2

    for Tensao in range(len(AllVoltages)/3):
        Fase_A.append(AllVoltages[A])
        Fase_B.append(AllVoltages[B])
        Fase_C.append(AllVoltages[C])
        A = A + 3
        B = B + 3
        C = C + 3
        Fase_Media.append((Fase_A[-1] + Fase_B[-1] + Fase_C[-1])/3)

    return Fase_A, Fase_B, Fase_C, Fase_Media

def Create_Vector_Volt_Var(index, Fases):

    ## Cria um vetor com as tensões na barra escolhida
    Tensao_Fase = []
    Tensao_Media_Fase = []

    ## Vol/Var - Para cada fase
    #for i in range(len(Fases[0:3])):
    #    Tensao_Fase.append(Fases[i][index])
    ##Vector_Y = Verifica_Fase(Tensao_Fase)

    ## Vol/Var - Valor Médio entre as fases
    Tensao_Media_Fase.append(Fases[3][index])
    from FunctionsSecond import Verifica_Fase
    Vector_Y = Verifica_Fase(Tensao_Media_Fase)

    return Vector_Y

def Calc_Param_Func_1_Ordem(X1, Y1, X2, Y2):

    A = ((Y2 - Y1) / (X2 - X1))
    B = Y1 - A*X1
    return A, B

def Verifica_Fase(Tensao_Fase):

    Vector_Y = []

    V_Max  = 1.08
    DB_Max = 1.02
    DB_Min = 0.98
    V_Min  = 0.92

    V_Max  = 1.08
    DB_Max = 1.02
    DB_Min = 1.01
    V_Min  = 0.99

    V_Max  = 1.05
    DB_Max = 1
    DB_Min = 0.999
    V_Min  = 0.990

    from FunctionsSecond import Verifica_Fase
    A1, B1 = Calc_Param_Func_1_Ordem(V_Min, 1, DB_Min, 0)
    A2, B2 = Calc_Param_Func_1_Ordem(V_Max, -1, DB_Max, 0)

    for Fase in Tensao_Fase:
        if Fase >= DB_Min and Fase <= DB_Max:
            Vector_Y.append(0)
        elif Fase > DB_Max and Fase <= V_Max:
            Vector_Y.append((((A2 * Fase + B2))))
        elif Fase < DB_Min and Fase >= V_Min:
            Vector_Y.append((((A1 * Fase + B1))))
        elif Fase > V_Max:
            Vector_Y.append(-1)
        elif Fase < V_Min:
            Vector_Y.append(1)
        else:
            print "ERRO MEDIÇÃO FASE"
            break
    return Vector_Y

def Verifica_Fase_BKP(Tensao_Fase):

    Vector_Y = []

    V_Max  = 1.08
    DB_Max = 1.02
    DB_Min = 0.98
    V_Min  = 0.92

    V_Max  = 1.03
    DB_Max = 1.02
    DB_Min = 1
    V_Min  = 0.99

    from FunctionsSecond import Verifica_Fase
    A1, B1 = Calc_Param_Func_1_Ordem(V_Min, 1, DB_Min, 0)
    A2, B2 = Calc_Param_Func_1_Ordem(V_Max, -1, DB_Max, 0)

    for Fase in Tensao_Fase:
        if Fase >= DB_Min and Fase <= DB_Max:
            Vector_Y.append(0)
        elif Fase > DB_Max and Fase <= V_Max:
            Vector_Y.append((((A2 * Fase + B2))))
        elif Fase < DB_Min and Fase >= V_Min:
            Vector_Y.append((((A1 * Fase + B1))))
        elif Fase > V_Max:
            Vector_Y.append(1)
        elif Fase < V_Min:
            Vector_Y.append(-1)
        else:
            print "ERRO MEDIÇÃO FASE"
            break
    return Vector_Y

def Hora_2_Min(Var):
    return Var * 60

## CC

def PCC_QCC(Powers):

    P_W_A = []
    P_Q_A = []
    P_W_B = []
    P_Q_B = []
    P_W_C = []
    P_Q_C = []

    Pcc = []
    Qcc = []

    P_W_A.append(Powers[0])
    P_Q_A.append(Powers[1])
    P_W_B.append(Powers[2])
    P_Q_B.append(Powers[3])
    P_W_C.append(Powers[4])
    P_Q_C.append(Powers[5])

    for i in range(len(P_W_C)):
        Pcc.append(float(P_W_A[i] + P_W_B[i] + P_W_C[i]))
        Qcc.append(float(P_Q_A[i] + P_Q_B[i] + P_Q_C[i]))

    return Pcc, Qcc

def PCC_QCC_Vet(Powers):

    # Usado no Plot ( tem de compilar o vetor inteiro )

    P_W_A = []
    P_Q_A = []
    P_W_B = []
    P_Q_B = []
    P_W_C = []
    P_Q_C = []

    Pcc = []
    Qcc = []

    for Power in Powers:
        P_W_A.append(Power[0])
        P_Q_A.append(Power[1])
        P_W_B.append(Power[2])
        P_Q_B.append(Power[3])
        P_W_C.append(Power[4])
        P_Q_C.append(Power[5])

    for i in range(len(P_W_C)):
        Pcc.append(float(P_W_A[i] + P_W_B[i] + P_W_C[i]))
        Qcc.append(float(P_Q_A[i] + P_Q_B[i] + P_Q_C[i]))

    return Pcc, Qcc

##

def Leitura_kvar_GDs():
    arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\Pot_Reativa.txt', 'r')
    Pot_Reativa = []
    for linha in arquivo:
        Pot_Reativa.append(linha.rstrip())
    arquivo.close()
    return Pot_Reativa

def Leitura_kW_GDs():
    arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\Pot_Geradores\Pot_Ativa.txt', 'r')
    Pot_Ativa = []
    for linha in arquivo:
        Pot_Ativa.append(linha.rstrip())
    arquivo.close()
    return Pot_Ativa

def Leitura(Nome_Arquivo):
    arquivo = open(Nome_Arquivo, 'r')
    Vet = []
    for linha in arquivo:
        Vet.append(linha.rstrip())
    arquivo.close()
    return Vet

def Acha_Index_LoadShape_GD(Nome_GD, Names_Loadshapes):

    index = 0
    for Loadshape in Names_Loadshapes:
        if str(Loadshape) == Nome_GD:
            return index
        elif Loadshape != Nome_GD:
            index = index + 1
        elif index == (len(Names_Loadshapes) - 1):
            index = 0
            print " NÃO ENCONTROU LOADSHAPE"
            break

def Leitura_pmult(Nome):

    Nome_GD = ("\P" + str(Nome.upper()))
    arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores' + str(Nome_GD) + '.txt', 'r')
    pmult = []
    for linha in arquivo:
        pmult.append(linha.rstrip())
    arquivo.close()
    return pmult

def Leitura_qmult(Nome):

    Nome_GD = ("\Q" + str(Nome.upper()))
    arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores' + str(Nome_GD) + '.txt', 'r')
    qmult = []
    for linha in arquivo:
        qmult.append(linha.rstrip())
    arquivo.close()
    return qmult

def Escreve_pmult(Nome, pmult):

    Nome_GD = ("\P" + str(Nome.upper()))
    arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores' + str(Nome_GD) + '.txt', 'w')
    for mult in pmult:
        arquivo.write((mult) + "\n")
    arquivo.close()

def Escreve_qmult(Nome, qmult):

    Nome_GD = ("\Q" + str(Nome.upper()))
    arquivo = open('C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Geradores' + str(Nome_GD) + '.txt', 'r')
    for mult in qmult:
        arquivo.write(str(mult) + "\n")
    arquivo.close()

def Soma_Elementos_Vetor(Vetor):

    i = 0
    for Elemento in Vetor:
        i = i + float(Elemento)
    return i

##### Colocar no Principal #############################################################################################
def Salva_Arquivo(self, Var, nome):

        for GD in self.dssGenerators.AllNames:
            Nome_GD = (str(GD.upper()))
            arquivo = open('C:\Users\hugo1\Desktop\Projeto\Testes\Sistema_Menor\Testes\_' + str(
                Nome_GD) + "_" + str(nome) + '.txt', 'w')
            for Uni_Var in Var:
                arquivo.write(str(Uni_Var) + "\n")
            arquivo.close()

