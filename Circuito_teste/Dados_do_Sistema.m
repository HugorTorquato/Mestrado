%% Dados Gerais

Dados.Freq = 60;

Dados.Tensao.va=[8000*sqrt(2) 0];        % [vpeak angle] - Alterar depois
Dados.Tensao.vb=[8000*sqrt(2) -120];
Dados.Tensao.vc=[8000*sqrt(2) 120];





%% Dados de linha [ R(omh) L(H) ]


Dados.Linha.Linha_01_02 = [0.032  31.1e-6  ];
Dados.Linha.Linha_02_04 = [0.0206  19.98e-6];
Dados.Linha.Linha_04_03 = [0.0037  5.46e-6 ];
Dados.Linha.Linha_04_05 = [0.0001  0.14e-6 ];
Dados.Linha.Linha_05_06 = [0.0278  27.04e-6];
Dados.Linha.Linha_06_08 = [0.0378  36.7e-6 ];
Dados.Linha.Linha_08_11 = [0.0234  2.69e-6 ];
Dados.Linha.Linha_11_09 = [0.006  5.79e-6  ];
Dados.Linha.Linha_11_12 = [0.0123  11.94e-6];
Dados.Linha.Linha_12_14 = [0.0345  33.52e-6];
Dados.Linha.Linha_11_13 = [0.0126  12.25e-6];
Dados.Linha.Linha_13_18 = [0.03  26.16e-6  ];
Dados.Linha.Linha_18_22 = [0.0285  27.7e-6 ];
Dados.Linha.Linha_22_24 = [0.0202  19.61e-6];
Dados.Linha.Linha_24_25 = [0.0056  8.13e-6 ];
Dados.Linha.Linha_25_26 = [0.0354  34.36e-6];
Dados.Linha.Linha_24_23 = [0.0015  2.24e-6 ];
Dados.Linha.Linha_23_21 = [0.0221  32.21e-6];
Dados.Linha.Linha_21_20 = [0.0206  30.04e-6];
Dados.Linha.Linha_20_19 = [0.0073  10.59e-6];
Dados.Linha.Linha_19_17 = [0.0129  18.75e-6];
Dados.Linha.Linha_17_15 = [0.0188  27.47e-6];
Dados.Linha.Linha_19_16 = [0.0125  18.25e-6];
Dados.Linha.Linha_16_10 = [0.0188  27.48e-6];
Dados.Linha.Linha_10_07 = [0.0172  25.06e-6];
Dados.Linha.Linha_07_04 = [0.0084  12.21e-6];

%% Dados GDs

Dados.GDs.GD_1.P = 5000;
Dados.GDs.GD_1.Q = 5000;

Dados.GDs.GD_2.P = 7000;
Dados.GDs.GD_2.Q = 7000;

Dados.GDs.GD_3.P = 5000;
Dados.GDs.GD_3.Q = 5000;

Dados.GDs.GD_4.P = 10000;
Dados.GDs.GD_4.Q = 10000;

Dados.GDs.GD_5.P = 9000;
Dados.GDs.GD_5.Q = 9000;

Dados.GDs.GD_6.P = 9000;
Dados.GDs.GD_6.Q = 9000;

%% Dados de Carga 

Dados.Load.Load_1.P = [560.64 280.32 280.32];  % Barra 1
Dados.Load.Load_1.Q = [237.6 118.8 118.8];     % Barra 1

Dados.Load.Load_2.P = [0 93.44 0];  % Barra 2
Dados.Load.Load_2.Q = [0 39.6 0];   % Barra 2

Dados.Load.Load_3.P = [0 1027.84 1027.84];  % Barra 3
Dados.Load.Load_3.Q = [0 435.6 435.6];    % Barra 3

Dados.Load.Load_4.P = [560.64 280.32 280.32];  % Barra 4
Dados.Load.Load_4.Q = [237.6 118.8 118.8];    % Barra 4

Dados.Load.Load_5.P = [0 373.76 373.76];  % Barra 5
Dados.Load.Load_5.Q = [0 158.4 158.4];    % Barra 5

Dados.Load.Load_6.P = [467.2 467.2 280.32];  % Barra 6
Dados.Load.Load_6.Q = [198 198 118.8];    % Barra 6

Dados.Load.Load_8.P = [186.88 747.52 747.52];  % Barra 7
Dados.Load.Load_8.Q = [79.2 316.8 316.8];    % Barra 7

Dados.Load.Load_9.P = [467.2 467.2 280.32];  % Barra 8
Dados.Load.Load_9.Q = [198 198 118.8];    % Barra 8

Dados.Load.Load_10.P = [467.2 467.2 467.2];  % Barra 9
Dados.Load.Load_10.Q = [198 198 198];    % Barra 9

Dados.Load.Load_11.P = [1401.6 747.52 467.2];  % Barra 10
Dados.Load.Load_11.Q = [594 316.8 198];    % Barra 10

Dados.Load.Load_13.P = [280.32 373.76 654.08];  % Barra 12
Dados.Load.Load_13.Q = [118.8 158.4 277.2];    % Barra 12

Dados.Load.Load_14.P = [373.76 280.32 840.96];  % Barra 13
Dados.Load.Load_14.Q = [158.4 118.8 356.4];    % Barra 13

Dados.Load.Load_15.P = [560.64 280.32 93.44];  % Barra 14
Dados.Load.Load_15.Q = [237.6 118.8 39.6];    % Barra 14

Dados.Load.Load_16.P = [93.44 373.76 373.76];  % Barra 15
Dados.Load.Load_16.Q = [39.6 158.4 158.4];    % Barra 15

Dados.Load.Load_17.P = [186.88 467.2 373.76];  % Barra 16
Dados.Load.Load_17.Q = [79.2 198 158.4];    % Barra 16

Dados.Load.Load_18.P = [747.52 934.4 280.32];  % Barra 17
Dados.Load.Load_18.Q = [316.8 396 118.8];    % Barra 17

Dados.Load.Load_19.P = [560.64 934.4 1308.16];  % Barra 18
Dados.Load.Load_19.Q = [237.6 396 554.4];    % Barra 18

Dados.Load.Load_21.P = [0 1121.28 280.32];  % Barra 26
Dados.Load.Load_21.Q = [0 475.2 118.8];    % Barra 26

Dados.Load.Load_23.P = [2055.7 1401.6 1495.04];  % Barra 26
Dados.Load.Load_23.Q = [871.2 594 633.6];    % Barra 26

Dados.Load.Load_25.P = [654.08 560.64 560.64];  % Barra 22
Dados.Load.Load_25.Q = [277.2 237.6 237.6];    % Barra 22

Dados.Load.Load_26.P = [280.32 373.76 186.88];  % Barra 23
Dados.Load.Load_26.Q = [188.8 158.4 79.2];    % Barra 23

Dados.Load.Load_29.P = [840.96 840.96 356.4];  % Barra 25
Dados.Load.Load_29.Q = [356.4 356.4 158.4];    % Barra 25
 
Dados.Load.Load_31.P = [186.88 560.64 467.2];  % Barra 26
Dados.Load.Load_31.Q = [79.2 237.6 198];    % Barra 26













