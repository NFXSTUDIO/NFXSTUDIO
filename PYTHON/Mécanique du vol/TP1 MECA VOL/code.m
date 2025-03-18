



close all;
clear all;
%%Constant

S=34.84;
b=11.8;
A=4;
c_=3.29;
e=0.85;
g=9.81;

m=9926.7;
Ixx=18486.6;
Iyy=68965;
Izz=91599;
Ixz=3976.6;

H=0;
rho=1.225;
U_0=85;
M=0.25;
teta_0=11.2;

%% Constant Part 1
C_L_0=0.62;
C_D_0=0.072;

C_D_u=0.0105;
C_D_a=1.52;
C_L_u=0.04;
C_L_a=3.95;
C_L_pa=0;
C_L_q=0;
C_m_u=0.012;
C_m_a=-0.45;
C_m_pa=-0.7;
C_m_q=-3.8;

C_D_delta_e=0;
C_L_delta_e=0.6;
C_m_delta_e=-0.83;
C_D_delta_r=0;
C_L_delta_r=0;
C_m_delta_r=0;

%% Constant Part 2
C_gamma_beta=-0.88;
C_gamma_p=0;
C_gamma_r=0;
C_l_beta=-0.115;
C_l_p=-0.25;
C_l_r=0.18;
C_n_beta=0.105;
C_n_p=-0.01;
C_n_r=-0.34;

C_gamma_delta_a=-0.015;
C_l_delta_a=0.055;
C_n_delta_a=-0.002;
C_gamma_delta_r=0.23;
C_l_delta_r=0.007;
C_n_delta_r=-0.105;

%% Partie 1
q_=(1/2)*rho*(U_0^2);

X_u=-((q_*S)/(m*U_0))*(2*C_D_0+C_D_u);
Z_u=-((q_*S)/(m*U_0))*(2*C_L_0+C_L_u);
M_u=((q_*S*c_)/(Iyy*U_0))*C_m_u;

X_w=((q_*S)/(m*U_0))*(C_L_0*(1-(2/(pi*e*A))*C_L_a));
Z_w=-((q_*S)/(m*U_0))*(C_D_0+C_L_a);
M_w=((q_*S*c_)/(Iyy*U_0))*C_m_a;

Z_pw=((q_*S*c_)/(2*m*U_0^2))*(C_D_0+C_L_pa);
M_pw=((q_*S*c_^2)/(2*Iyy*U_0^2))*C_m_pa;

Z_q=((q_*S*c_)/(2*m*U_0))*C_L_q;
M_q=((q_*S*c_^2)/(2*Iyy*U_0))*C_m_q;


X_delta_r=((q_*S)/(m*U_0))*C_D_delta_r;
Z_delta_r=((q_*S)/(m*U_0))*C_L_delta_r;
M_delta_r=((q_*S*c_)/(Iyy*U_0))*C_m_delta_r;

X_delta_e=((q_*S)/(m*U_0))*C_D_delta_e;
Z_delta_e=((q_*S)/(m*U_0))*C_L_delta_e;
M_delta_e=((q_*S*c_)/(Iyy*U_0))*C_m_delta_e;



Aircraft_long=[[X_u X_w 0 -g*cos(deg2rad(teta_0))],
       [Z_u Z_w U_0 -g*sin(deg2rad(teta_0))],
       [M_u+Z_u*M_pw M_w+Z_w*M_pw M_q+U_0*M_pw 0],
       [0 0 1 0]];

Control_long=[[X_delta_e X_delta_r],
       [Z_delta_e Z_delta_r],
       [M_delta_e+Z_delta_e*M_pw M_delta_r+Z_delta_r*M_pw],
       [0 0]];

disp("Longitudinal Matrix:")
disp("Aircraft Matrix")
disp(Aircraft_long);
disp("Control Matrix")
disp(Control_long);

%% Partie 2

Y_nu=((q_*S)/(m*U_0))*C_gamma_beta;
L_nu=((q_*S*b)/(Ixx*U_0))*C_l_beta;
N_nu=((q_*S*b)/(Izz*U_0))*C_n_beta;

Y_p=((q_*S)/(2*m*U_0))*C_gamma_p;
L_p=((q_*S*b^2)/(2*Ixx*U_0))*C_l_p;
N_p=((q_*S*b^2)/(2*Izz*U_0))*C_n_p;

Y_r=((q_*S)/(2*m*U_0))*C_gamma_r;
L_r=((q_*S*b^2)/(2*Ixx*U_0))*C_l_r;
N_r=((q_*S*b^2)/(2*Izz*U_0))*C_n_r;

Y_delta_r=((q_*S)/(m*U_0))*C_gamma_delta_r;
L_delta_r=((q_*S*b)/(Ixx*U_0))*C_l_delta_r;
N_delta_r=((q_*S*b)/(Izz*U_0))*C_n_delta_r;

Y_delta_a=((q_*S)/(m*U_0))*C_gamma_delta_a;
L_delta_a=((q_*S*b)/(Ixx*U_0))*C_l_delta_a;
N_delta_a=((q_*S*b)/(Izz*U_0))*C_n_delta_a;

Aircraft_lat=[[Y_nu Y_p (Y_r-U_0) g*cos(deg2rad(teta_0))],
       [L_nu L_p L_r 0],
       [N_nu N_p N_r 0],
       [0 1 0 0]];

Control_lat=[[Y_delta_r Y_delta_a],
       [L_delta_r L_delta_a],
       [N_delta_r N_delta_a],
       [0 0]];
disp("Lateral Matrix:")
disp("Aircraft Matrix")
disp(Aircraft_lat);
disp("Control Matrix")
disp(Control_lat);

%% tutoriel 2 : 

lambda_long = eig(Aircraft_long);

omega1_long = sqrt(lambda_long(1) * lambda_long(2));
omega2_long = sqrt(lambda_long(3) * lambda_long(4));

ksi1_long = - (lambda_long(1) + lambda_long(2)) / (2 * omega1_long);
ksi2_long = - (lambda_long(3) + lambda_long(4)) / (2 * omega2_long);


%% tutoriel 3 : 

[V_long,lambda_long2] = eig(Aircraft_long);

""" Aircraft longitudinal """;
t = linspace(0,10,100);
delta_w = 0.85 * (V_long(2,1) * exp(lambda_long2(1,1) * t) + V_long(2,2) * exp(lambda_long2(2,2) * t));
delta_q = 0.1 * (V_long(3,1) * exp(lambda_long2(1,1) * t) + V_long(3,2) * exp(lambda_long2(2,2) * t));

figure();
subplot(2,1,1);
plot(t,delta_w);
xlabel('t (s)')
ylabel('delta_w(t)')
title('Delta w en fonction du temp')
grid();

subplot(2,1,2);
plot(t,delta_q);
xlabel('t (s)')
ylabel('delta_q(t)')
title('Delta q en fonction du temp')
grid();

""" Phugoid """;

t1 = linspace(0,2000,1000000);
delta_u = -8.5 * (abs(V_long(1,3)) * exp(lambda_long2(3,3) * t1) + abs(V_long(1,4)) * exp(lambda_long2(4,4) * t1));
delta_theta = -2 * (abs(V_long(4,3)) * exp(lambda_long2(3,3) * t1) + abs(V_long(4,4)) * exp(lambda_long2(4,4) * t1));

figure();
subplot(2,1,1);
plot(t1,delta_u);
xlabel('t (s)')
ylabel('delta_u(t)')
title('Delta u en fonction du temp')
grid();

subplot(2,1,2);
plot(t1,delta_theta);
xlabel('t (s)')
ylabel('delta_theta(t)')
title('Delta theta en fonction du temp')
grid();

""" Aircraft latteral-rolling""";

[V_lat,lambda_lat2] = eig(Aircraft_lat);

delta_v = 2 * (V_lat(1,1) * exp(lambda_lat2(1,1) * t));
delta_p = 0.1 * (V_lat(2,1) * exp(lambda_lat2(1,1) * t));
delta_r = 0.1 * (V_lat(3,1) * exp(lambda_lat2(1,1) * t));
delta_phy = 2 * (V_lat(4,1) * exp(lambda_lat2(1,1) * t));

figure();
subplot(4,1,1);
plot(t,delta_v);
xlabel('t (s)')
ylabel('delta_v(t)')
title('Delta v en fonction du temp')
grid();

subplot(4,1,2);
plot(t,delta_p);
xlabel('t (s)')
ylabel('delta_p(t)')
title('Delta p en fonction du temp')
grid();

subplot(4,1,3);
plot(t,delta_r);
xlabel('t (s)')
ylabel('delta_r(t)')
title('Delta r en fonction du temp')
grid();

subplot(4,1,4);
plot(t,delta_phy);
xlabel('t (s)')
ylabel('delta_phy(t)')
title('Delta phy en fonction du temp')
grid();

""" Aircraft latteral-spiral""";

t2 = linspace(0,100,1000);

delta_v_sp = 2 * (V_lat(1,4) * exp(lambda_lat2(4,4) * t2));
delta_p_sp = 0.1 * (V_lat(2,4) * exp(lambda_lat2(4,4) * t2));
delta_r_sp = 0.1 * (V_lat(3,4) * exp(lambda_lat2(4,4) * t2));
delta_phy_sp = 2 * (V_lat(4,4) * exp(lambda_lat2(4,4) * t2));

figure();
subplot(4,1,1);
plot(t2,delta_v_sp);
xlabel('t (s)')
ylabel('delta_v(t)')
title('Delta v en fonction du temp')
grid();

subplot(4,1,2);
plot(t2,delta_p_sp);
xlabel('t (s)')
ylabel('delta_p(t)')
title('Delta p en fonction du temp')
grid();

subplot(4,1,3);
plot(t2,delta_r_sp);
xlabel('t (s)')
ylabel('delta_r(t)')
title('Delta r en fonction du temp')
grid();

subplot(4,1,4);
plot(t2,delta_phy_sp);
xlabel('t (s)')
ylabel('delta_phy(t)')
title('Delta phy en fonction du temp')
grid();

""" Aircraft latteral-Dutch roll""";

delta_v_dr = 2 * (V_lat(1,3) * exp(lambda_lat2(3,3) * t2) + V_lat(1,4) * exp(lambda_lat2(4,4) * t2));
delta_p_dr = 0.1 * (V_lat(2,3) * exp(lambda_lat2(3,3) * t2) + V_lat(2,4) * exp(lambda_lat2(4,4) * t2));
delta_r_dr = 0.1 * (V_lat(3,3) * exp(lambda_lat2(3,3) * t2) + V_lat(3,4) * exp(lambda_lat2(4,4) * t2));
delta_phy_dr = 2 * (V_lat(4,3) * exp(lambda_lat2(3,3) * t2) + V_lat(4,4) * exp(lambda_lat2(4,4) * t2));

figure();
subplot(4,1,1);
plot(t2,delta_v_dr);
xlabel('t (s)')
ylabel('delta_v(t)')
title('Delta v en fonction du temp')
grid();

subplot(4,1,2);
plot(t2,delta_p_dr);
xlabel('t (s)')
ylabel('delta_p(t)')
title('Delta p en fonction du temp')
grid();

subplot(4,1,3);
plot(t2,delta_r_dr);
xlabel('t (s)')
ylabel('delta_r(t)')
title('Delta r en fonction du temp')
grid();

subplot(4,1,4);
plot(t2,delta_phy_dr);
xlabel('t (s)')
ylabel('delta_phy(t)')
title('Delta phy en fonction du temp')
grid();