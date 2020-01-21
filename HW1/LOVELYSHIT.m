clf
figure(1)
hold on
plot(RESULTS_0_1.Time, RESULTS_0_1.Data)
plot(RESULTS_0_5.Time, RESULTS_0_5.Data)
plot(RESULTS_1.Time, RESULTS_1.Data)
plot(RESULTS_1_25.Time, RESULTS_1_25.Data)
plot(RESULTS_5.Time, RESULTS_5.Data)

legend('T=0.1', 'T=0.5','T=1','T=1.25', 'T=5')
title('Sampled step response')
xlabel('Time s')
ylabel('Tank 2 level [m]')
grid()
axis([0 150 38 58])
%%
clf
figure(2)

subplot(1,3,1)
hold on
plot(RESULTS_0_01.Time, RESULTS_0_01.Data)
plot(RESULTZ_0_01.Time, RESULTZ_0_01.Data)
legend('T=0.01 Continous', 'T=0.01 Discrete')
xlabel('Time s')
ylabel('Tank 2 level [m]')
grid()
axis([0 150 38 58])

subplot(1,3,2)
hold on
plot(RESULTS_1.Time, RESULTS_1.Data)
plot(RESULTZ_1.Time, RESULTZ_1.Data)
legend('T=1 Continous', 'T=1 Discrete')
xlabel('Time s')
ylabel('Tank 2 level [m]')
grid()
axis([0 150 38 58])


subplot(1,3,3)
hold on
plot(RESULTS_5.Time, RESULTS_5.Data)
plot(RESULTZ_5.Time, RESULTZ_5.Data)
legend('T=5 Continous', 'T=5 Discrete')
xlabel('Time s')
ylabel('Tank 2 level [m]')
grid()
axis([0 150 38 58])
