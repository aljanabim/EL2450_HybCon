#include <math.h>
theta_goal = atan2(ygoal, xgoal) * 180 / PI;
controller = 10;
angle_threshold = 1;
w = 0;
distance_threshold = 5;

if (abs(theta_goal - theta) > angle_threshold)
{
    controller = 0;
}
else if (sqrt(pow(xg - x, 2) + pow(yg - y, 2)) > distance_threshold)
{
    controller = 1;
}

switch (controller)
{
case 0: // rotational conttroller
    k_psi = 5;
    k_w = 5;

    xgoal = (xg - x) / 100;
    ygoal = yg - y;
    // w = k_psi * (theta_goal - theta);

    xdelta = x0 - x;
    ydelta = y0 - y;
    d0 = cos(theta * PI / 180) * xdelta + sin(theta * PI / 180) * ydelta;
    vel = k_w * d0;

case 1:

    break;

default:
    vel = 0;
    w = 0;
    break;
}

left = vel - w / 2;
right = vel + w / 2;

Serial.print("Theta error: ");
Serial.print(theta_goal - theta);
Serial.print(" | xdelta: ");
Serial.print(xdelta);
Serial.print(" | ydelta: ");
Serial.print(ydelta);
Serial.print(" | d0: ");
Serial.print(d0);
Serial.print(" | x ");
Serial.print(x);
Serial.print(" | x0 ");
Serial.print(x0);
Serial.print(" | xg ");
Serial.print(xg);