%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Hybrid and Embedded control systems
% Homework 1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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
[b_cont,a_cont] = tfdata(G);
[A_cont,B_cont,C_cont,D_cont] = tf2ss(cell2mat(b_cont), cell2mat(a_cont));
Ts = 4; % Sampling time
Fd = c2d(G, Ts, 'ZOH');
[b,a] = tfdata(Fd);
% Discretize the continous state space system, save it in state space form
[Phi,Gamma,C,D] = tf2ss(cell2mat(b),cell2mat(a));

% Observability and reachability
Wc = [Gamma Phi*Gamma]
Wo = [C ;C*Phi]

% State feedback controller gain
L = 1;
% observer gain
K = 1;
% reference gain
lr = 1;

% augmented system matrices
Aa = 1;
Ba = 1;
