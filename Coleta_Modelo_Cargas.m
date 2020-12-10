
% Salvar em um arquivo excel

% Load 1
Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_A = -P_Load_1_A/Dados.Load.Load_1.P(1); clear P_Load_1_A;

AuxStart = (length(Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_A)/10) - 1440
%length(Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_A(1:10:(end-AuxStart)))
length(Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_A(1:length(Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_A)/1440:(end)))

length(Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_A) 

%csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_1_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_B = -P_Load_1_B/Dados.Load.Load_1.P(2); clear P_Load_1_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_1_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_C = -P_Load_1_C/Dados.Load.Load_1.P(3); clear P_Load_1_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_1_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.Q_A = -Q_Load_1_A/Dados.Load.Load_1.Q(1); clear Q_Load_1_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_1_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.Q_B = -Q_Load_1_B/Dados.Load.Load_1.Q(2); clear Q_Load_1_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_1_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.Q_C = -Q_Load_1_C/Dados.Load.Load_1.Q(3); clear Q_Load_1_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_1_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.Q_C(Ajuste_Dados:end));

% Load 3
Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.P_A = -P_Load_3_A/Dados.Load.Load_3.P(1); clear P_Load_3_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_3_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.P_B = -P_Load_3_B/Dados.Load.Load_3.P(2); clear P_Load_3_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_3_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.P_C = -P_Load_3_C/Dados.Load.Load_3.P(3); clear P_Load_3_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_3_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.Q_A = -Q_Load_3_A/Dados.Load.Load_3.Q(1); clear Q_Load_3_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_3_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.Q_B = -Q_Load_3_B/Dados.Load.Load_3.Q(2); clear Q_Load_3_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_3_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.Q_C = -Q_Load_3_C/Dados.Load.Load_3.Q(3); clear Q_Load_3_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_3_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_3.Q_C(Ajuste_Dados:end));

% Load 4
Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.P_A = -P_Load_4_A/Dados.Load.Load_4.P(1); clear P_Load_4_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_4_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.P_B = -P_Load_4_B/Dados.Load.Load_4.P(2); clear P_Load_4_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_4_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.P_C = -P_Load_4_C/Dados.Load.Load_4.P(3); clear P_Load_4_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_4_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.Q_A = -Q_Load_4_A/Dados.Load.Load_4.Q(1); clear Q_Load_4_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_4_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.Q_B = -Q_Load_4_B/Dados.Load.Load_4.Q(2); clear Q_Load_4_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_4_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.Q_C = -Q_Load_4_C/Dados.Load.Load_4.Q(3); clear Q_Load_4_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_4_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_4.Q_C(Ajuste_Dados:end));

% Load 5
Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.P_A = -P_Load_5_A/Dados.Load.Load_5.P(1); clear P_Load_5_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_5_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.P_B = -P_Load_5_B/Dados.Load.Load_5.P(2); clear P_Load_5_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_5_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.P_C = -P_Load_5_C/Dados.Load.Load_5.P(3); clear P_Load_5_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_5_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.Q_A = -Q_Load_5_A/Dados.Load.Load_5.Q(1); clear Q_Load_5_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_5_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.Q_B = -Q_Load_5_B/Dados.Load.Load_5.Q(2); clear Q_Load_5_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_5_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.Q_C = -Q_Load_5_C/Dados.Load.Load_5.Q(3); clear Q_Load_5_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_5_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_5.Q_C(Ajuste_Dados:end));

% Load 6
Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.P_A = -P_Load_6_A/Dados.Load.Load_6.P(1); clear P_Load_6_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_6_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.P_B = -P_Load_6_B/Dados.Load.Load_6.P(2); clear P_Load_6_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_6_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.P_C = -P_Load_6_C/Dados.Load.Load_6.P(3); clear P_Load_6_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_6_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.Q_A = -Q_Load_6_A/Dados.Load.Load_6.Q(1); clear Q_Load_6_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_6_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.Q_B = -Q_Load_6_B/Dados.Load.Load_6.Q(2); clear Q_Load_6_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_6_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.Q_C = -Q_Load_6_C/Dados.Load.Load_6.Q(3); clear Q_Load_6_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_6_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_6.Q_C(Ajuste_Dados:end));

% Load 8
Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.P_A = -P_Load_8_A/Dados.Load.Load_8.P(1); clear P_Load_8_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_8_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.P_B = -P_Load_8_B/Dados.Load.Load_8.P(2); clear P_Load_8_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_8_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.P_C = -P_Load_8_C/Dados.Load.Load_8.P(3); clear P_Load_8_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_8_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.Q_A = -Q_Load_8_A/Dados.Load.Load_8.Q(1); clear Q_Load_8_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_8_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.Q_B = -Q_Load_8_B/Dados.Load.Load_8.Q(2); clear Q_Load_8_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_8_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.Q_C = -Q_Load_8_C/Dados.Load.Load_8.Q(3); clear Q_Load_8_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_8_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_8.Q_C(Ajuste_Dados:end));

% Load 9
Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.P_A = -P_Load_9_A/Dados.Load.Load_9.P(1); clear P_Load_9_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_9_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.P_B = -P_Load_9_B/Dados.Load.Load_9.P(2); clear P_Load_9_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_9_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.P_C = -P_Load_9_C/Dados.Load.Load_9.P(3); clear P_Load_9_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_9_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.Q_A = -Q_Load_9_A/Dados.Load.Load_9.Q(1); clear Q_Load_9_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_9_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.Q_B = -Q_Load_9_B/Dados.Load.Load_9.Q(2); clear Q_Load_9_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_9_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.Q_C = -Q_Load_9_C/Dados.Load.Load_9.Q(3); clear Q_Load_9_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_9_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_9.Q_C(Ajuste_Dados:end));

% Load 10
Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.P_A = -P_Load_10_A/Dados.Load.Load_10.P(1); clear P_Load_10_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_10_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.P_B = -P_Load_10_B/Dados.Load.Load_10.P(2); clear P_Load_10_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_10_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.P_C = -P_Load_10_C/Dados.Load.Load_10.P(3); clear P_Load_10_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_10_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.Q_A = -Q_Load_10_A/Dados.Load.Load_10.Q(1); clear Q_Load_10_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_10_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.Q_B = -Q_Load_10_B/Dados.Load.Load_10.Q(2); clear Q_Load_10_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_10_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.Q_C = -Q_Load_10_C/Dados.Load.Load_10.Q(3); clear Q_Load_10_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_10_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_10.Q_C(Ajuste_Dados:end));

% Load 11
Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.P_A = -P_Load_11_A/Dados.Load.Load_11.P(1); clear P_Load_11_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_11_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.P_B = -P_Load_11_B/Dados.Load.Load_11.P(2); clear P_Load_11_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_11_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.P_C = -P_Load_11_C/Dados.Load.Load_11.P(3); clear P_Load_11_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_11_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.Q_A = -Q_Load_11_A/Dados.Load.Load_11.Q(1); clear Q_Load_11_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_11_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.Q_B = -Q_Load_11_B/Dados.Load.Load_11.Q(2); clear Q_Load_11_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_11_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.Q_C = -Q_Load_11_C/Dados.Load.Load_11.Q(3); clear Q_Load_11_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_11_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_11.Q_C(Ajuste_Dados:end));

% Load 13
Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.P_A = -P_Load_13_A/Dados.Load.Load_13.P(1); clear P_Load_13_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_13_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.P_B = -P_Load_13_B/Dados.Load.Load_13.P(2); clear P_Load_13_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_13_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.P_C = -P_Load_13_C/Dados.Load.Load_13.P(3); clear P_Load_13_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_13_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.Q_A = -Q_Load_13_A/Dados.Load.Load_13.Q(1); clear Q_Load_13_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_13_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.Q_B = -Q_Load_13_B/Dados.Load.Load_13.Q(2); clear Q_Load_13_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_13_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.Q_C = -Q_Load_13_C/Dados.Load.Load_13.Q(3); clear Q_Load_13_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_13_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_13.Q_C(Ajuste_Dados:end));

% Load 14
Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.P_A = -P_Load_14_A/Dados.Load.Load_14.P(1); clear P_Load_14_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_14_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.P_B = -P_Load_14_B/Dados.Load.Load_14.P(2); clear P_Load_14_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_14_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.P_C = -P_Load_14_C/Dados.Load.Load_14.P(3); clear P_Load_14_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_14_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.Q_A = -Q_Load_14_A/Dados.Load.Load_14.Q(1); clear Q_Load_14_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_14_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.Q_B = -Q_Load_14_B/Dados.Load.Load_14.Q(2); clear Q_Load_14_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_14_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.Q_C = -Q_Load_14_C/Dados.Load.Load_14.Q(3); clear Q_Load_14_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_14_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_14.Q_C(Ajuste_Dados:end));

% Load 15
Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.P_A = -P_Load_15_A/Dados.Load.Load_15.P(1); clear P_Load_15_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_15_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.P_B = -P_Load_15_B/Dados.Load.Load_15.P(2); clear P_Load_15_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_15_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.P_C = -P_Load_15_C/Dados.Load.Load_15.P(3); clear P_Load_15_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_15_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.Q_A = -Q_Load_15_A/Dados.Load.Load_15.Q(1); clear Q_Load_15_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_15_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.Q_B = -Q_Load_15_B/Dados.Load.Load_15.Q(2); clear Q_Load_15_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_15_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.Q_C = -Q_Load_15_C/Dados.Load.Load_15.Q(3); clear Q_Load_15_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_15_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_15.Q_C(Ajuste_Dados:end));

% Load 16
Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.P_A = -P_Load_16_A/Dados.Load.Load_16.P(1); clear P_Load_16_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_16_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.P_B = -P_Load_16_B/Dados.Load.Load_16.P(2); clear P_Load_16_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_16_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.P_C = -P_Load_16_C/Dados.Load.Load_16.P(3); clear P_Load_16_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_16_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.Q_A = -Q_Load_16_A/Dados.Load.Load_16.Q(1); clear Q_Load_16_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_16_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.Q_B = -Q_Load_16_B/Dados.Load.Load_16.Q(2); clear Q_Load_16_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_16_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.Q_C = -Q_Load_16_C/Dados.Load.Load_16.Q(3); clear Q_Load_16_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_16_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_16.Q_C(Ajuste_Dados:end));

% Load 17
Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.P_A = -P_Load_17_A/Dados.Load.Load_17.P(1); clear P_Load_17_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_17_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.P_B = -P_Load_17_B/Dados.Load.Load_17.P(2); clear P_Load_17_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_17_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.P_C = -P_Load_17_C/Dados.Load.Load_17.P(3); clear P_Load_17_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_17_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.Q_A = -Q_Load_17_A/Dados.Load.Load_17.Q(1); clear Q_Load_17_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_17_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.Q_B = -Q_Load_17_B/Dados.Load.Load_17.Q(2); clear Q_Load_17_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_17_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.Q_C = -Q_Load_17_C/Dados.Load.Load_17.Q(3); clear Q_Load_17_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_17_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_17.Q_C(Ajuste_Dados:end));

% Load 18
Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.P_A = -P_Load_18_A/Dados.Load.Load_18.P(1); clear P_Load_18_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_18_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.P_B = -P_Load_18_B/Dados.Load.Load_18.P(2); clear P_Load_18_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_18_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.P_C = -P_Load_18_C/Dados.Load.Load_18.P(3); clear P_Load_18_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_18_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.Q_A = -Q_Load_18_A/Dados.Load.Load_18.Q(1); clear Q_Load_18_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_18_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.Q_B = -Q_Load_18_B/Dados.Load.Load_18.Q(2); clear Q_Load_18_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_18_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.Q_C = -Q_Load_18_C/Dados.Load.Load_18.Q(3); clear Q_Load_18_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_18_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_18.Q_C(Ajuste_Dados:end));

% Load 19
Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.P_A = -P_Load_19_A/Dados.Load.Load_19.P(1); clear P_Load_19_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_19_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.P_B = -P_Load_19_B/Dados.Load.Load_19.P(2); clear P_Load_19_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_19_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.P_C = -P_Load_19_C/Dados.Load.Load_19.P(3); clear P_Load_19_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_19_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.Q_A = -Q_Load_19_A/Dados.Load.Load_19.Q(1); clear Q_Load_19_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_19_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.Q_B = -Q_Load_19_B/Dados.Load.Load_19.Q(2); clear Q_Load_19_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_19_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.Q_C = -Q_Load_19_C/Dados.Load.Load_19.Q(3); clear Q_Load_19_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_19_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_19.Q_C(Ajuste_Dados:end));

% Load 21
Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.P_A = -P_Load_21_A/Dados.Load.Load_21.P(1); clear P_Load_21_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_21_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.P_B = -P_Load_21_B/Dados.Load.Load_21.P(2); clear P_Load_21_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_21_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.P_C = -P_Load_21_C/Dados.Load.Load_21.P(3); clear P_Load_21_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_21_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.Q_A = -Q_Load_21_A/Dados.Load.Load_21.Q(1); clear Q_Load_21_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_21_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.Q_B = -Q_Load_21_B/Dados.Load.Load_21.Q(2); clear Q_Load_21_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_21_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.Q_C = -Q_Load_21_C/Dados.Load.Load_21.Q(3); clear Q_Load_21_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_21_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_21.Q_C(Ajuste_Dados:end));

% Load 23
Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.P_A = -P_Load_23_A/Dados.Load.Load_23.P(1); clear P_Load_23_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_23_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.P_B = -P_Load_23_B/Dados.Load.Load_23.P(2); clear P_Load_23_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_23_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.P_C = -P_Load_23_C/Dados.Load.Load_23.P(3); clear P_Load_23_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_23_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.Q_A = -Q_Load_23_A/Dados.Load.Load_23.Q(1); clear Q_Load_23_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_23_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.Q_B = -Q_Load_23_B/Dados.Load.Load_23.Q(2); clear Q_Load_23_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_23_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.Q_C = -Q_Load_23_C/Dados.Load.Load_23.Q(3); clear Q_Load_23_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_23_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_23.Q_C(Ajuste_Dados:end));

% Load 25
Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.P_A = -P_Load_25_A/Dados.Load.Load_25.P(1); clear P_Load_25_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_25_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.P_B = -P_Load_25_B/Dados.Load.Load_25.P(2); clear P_Load_25_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_25_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.P_C = -P_Load_25_C/Dados.Load.Load_25.P(3); clear P_Load_25_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_25_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.Q_A = -Q_Load_25_A/Dados.Load.Load_25.Q(1); clear Q_Load_25_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_25_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.Q_B = -Q_Load_25_B/Dados.Load.Load_25.Q(2); clear Q_Load_25_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_25_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.Q_C = -Q_Load_25_C/Dados.Load.Load_25.Q(3); clear Q_Load_25_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_25_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_25.Q_C(Ajuste_Dados:end));

% Load 26
Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.P_A = -P_Load_26_A/Dados.Load.Load_26.P(1); clear P_Load_26_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_26_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.P_B = -P_Load_26_B/Dados.Load.Load_26.P(2); clear P_Load_26_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_26_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.P_C = -P_Load_26_C/Dados.Load.Load_26.P(3); clear P_Load_26_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_26_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.Q_A = -Q_Load_26_A/Dados.Load.Load_26.Q(1); clear Q_Load_26_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_26_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.Q_B = -Q_Load_26_B/Dados.Load.Load_26.Q(2); clear Q_Load_26_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_26_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.Q_C = -Q_Load_26_C/Dados.Load.Load_26.Q(3); clear Q_Load_26_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_26_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_26.Q_C(Ajuste_Dados:end));

% Load 29
Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.P_A = -P_Load_29_A/Dados.Load.Load_29.P(1); clear P_Load_29_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_29_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.P_B = -P_Load_29_B/Dados.Load.Load_29.P(2); clear P_Load_29_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_29_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.P_C = -P_Load_29_C/Dados.Load.Load_29.P(3); clear P_Load_29_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_29_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.Q_A = -Q_Load_29_A/Dados.Load.Load_29.Q(1); clear Q_Load_29_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_29_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.Q_B = -Q_Load_29_B/Dados.Load.Load_29.Q(2); clear Q_Load_29_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_29_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.Q_C = -Q_Load_29_C/Dados.Load.Load_29.Q(3); clear Q_Load_29_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_29_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_29.Q_C(Ajuste_Dados:end));

% Load 31
Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.P_A = -P_Load_31_A/Dados.Load.Load_31.P(1); clear P_Load_31_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_31_P_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.P_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.P_B = -P_Load_31_B/Dados.Load.Load_31.P(2); clear P_Load_31_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_31_P_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.P_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.P_C = -P_Load_31_C/Dados.Load.Load_31.P(3); clear P_Load_31_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_31_P_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.P_C(Ajuste_Dados:end));

Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.Q_A = -Q_Load_31_A/Dados.Load.Load_31.Q(1); clear Q_Load_31_A; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_31_Q_A.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.Q_A(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.Q_B = -Q_Load_31_B/Dados.Load.Load_31.Q(2); clear Q_Load_31_B; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_31_Q_B.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.Q_B(Ajuste_Dados:end));
Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.Q_C = -Q_Load_31_C/Dados.Load.Load_31.Q(3); clear Q_Load_31_C; %csvwrite("C:\Users\hugo1\Desktop\Projeto\Circuito_teste\Circuito_OpenDSS\LoadShapes\Load_31_Q_C.csv",Coleta_Dados_OpenDSS.Perfil_Carga.Load_31.Q_C(Ajuste_Dados:end));



% plot(Coleta_Dados_OpenDSS.Perfil_Carga.Load_1.P_A)
