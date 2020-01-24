%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Hybrid and Embedded control systems
% Homework 1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc, clear
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Initialization
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
init_tanks; 
g = 9.82; 
Tau = 1/alpha1*sqrt(2*tank_h10/g); 
k_tank = 60*beta*Tau; 
gamma_tank = alpha1^2/alpha2^2; 
uss = alpha2/beta*sqrt(2*g*tank_init_h2)*100/15; % steady state input yss = 40; % steady state output
yss = 40; % steady state output
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Continuous Control design
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
uppertank = tf([k_tank], [Tau 1]); % Transfer function for upper tank
lowertank = tf([gamma_tank],[gamma_tank*Tau 1]); % Transfer function for upper tank
G = uppertank*lowertank; % Transfer function from input to lower tank level

chi = 0.5;
omega0 = 0.2;
zeta = 0.8;
Gamma = gamma_tank;
K = k_tank;

% Calculate PID parameters
[K_pid,Ti,Td,N]=polePlacePID(chi,omega0,zeta,Tau,Gamma,K);
F = K_pid*tf([N*Td*Ti+Ti N*Ti+1 N], [Ti N*Ti 0]); % or 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Digital Control design
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Ts = 5; % Sampling time
Fd = c2d(F, Ts, 'ZOH');
[b,a] = tfdata(Fd);

% Discretize the continous controller, save it in state space form
[A_discretized,B_discretized,C_discretized,D_discretized] =tf2ss(cell2mat(b),cell2mat(a));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Discrete Control design
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% [b_cont,a_cont] = tfdata(G);
% [A_cont,B_cont,C_cont,D_cont] = tf2ss(cell2mat(b_cont), cell2mat(a_cont));

A = 1/Tau.*[-1 0; 1 -1/gamma_tank];
B = [k_tank/Tau; 0];
C = [0 1];
D = [0];

sys = ss(A,B,C,D);
Ts = 4; % Sampling time
Fd = c2d(sys, Ts, 'ZOH');
Phi = Fd.A;
Gamma = Fd.B;
C_disc = Fd.C;
% [b,a] = tfdata(Fd);   
% Discretize the continous state space system, save it in state space form
% [Phi,Gamma,C,D] = tf2ss(cell2mat(b_cont),cell2mat(a_cont));
% [Phi_,Gamma_,C_,D_] = tf2ss(cell2mat(b),cell2mat(a))

% Observability and reachability
Wc = [Gamma Phi*Gamma];
Wo = [C ;C*Phi];

closed_loop = minreal(G*F/(1+G*F));
p_cont = pole(closed_loop);
p_disc = exp(p_cont*Ts);
% State feedback controller gain

% observer gain
L = acker(Phi,Gamma,p_disc(3:4));
K = acker(Phi',C',p_disc(1:2))';
Aa = [Phi-Gamma*L Gamma*L;zeros(2,2) Phi-K*C_disc];
eig(Aa)
lr = 1/(C*(eye(2)-Phi+Gamma*L)^-1*Gamma);
Ba = [Gamma*lr; Gamma*lr]
% augmented system matrices

