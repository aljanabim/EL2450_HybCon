%%
p = plot(ANGLES.Time, ANGLES.Data,'LineWidth',3)
set(p, {'color'}, {[0 0 1]; [0 1 0]; [1 0 0]});
legend('Pendilum 1','Pendilum 2','Pendilum 3')
grid()
xlabel('Time, t')
ylabel('Angles, \theta')

%%
p = plot(tout, Schedule.signals.values,'LineWidth',3)
set(p, {'color'}, {[0 0 1]; [0 1 0]; [1 0 0]});
legend('Pendilum 1','Pendilum 2','Pendilum 3')
grid()
xlabel('Time, t')
xlim([0.023 0.09])
ylabel('Schedule')

%%
% After running inv_pend_delay
hold on
plot(d_0_02.TIME, d_0_02.DATA,'LineWidth',2)
plot(d_0_03.TIME, d_0_03.DATA,'LineWidth',2)
plot(d_0_04.TIME, d_0_04.DATA,'LineWidth',2)
plot(d_0_041.TIME, d_0_041.DATA,'LineWidth',2)
plot(d_0_05.TIME, d_0_05.DATA,'LineWidth',2)


% plot(d_0_08.TIME, d_0_08.DATA,'LineWidth',2)

legend('\tau=0.02','\tau=0.03','\tau=0.04','\tau=0.041','\tau=0.05')
grid()
xlabel('Time, t')
ylabel('\Theta')