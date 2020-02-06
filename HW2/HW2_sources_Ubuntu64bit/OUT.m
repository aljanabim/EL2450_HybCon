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

