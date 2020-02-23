#include <math.h>
theta_goal = atan2(ygoal, xgoal) * 180 / PI;
controller = 10;
angle_threshold = 1;
distance_threshold = 5;
vel = 0;
w = 0;

if (abs(theta_goal - theta) > angle_threshold)
{
    controller = 0;
}
else if (sqrt(pow(xg - x, 2) + pow(yg - y, 2)) > distance_threshold)
{
    controller = 1;
}

controller = 0;
switch (controller)
{
case 0: // rotational controller
    // rotation
    k_psi = 3;
    xdelta = xg - x;
    ydelta = yg - y;
    theta_goal = atan2(ydelta, xdelta) * 180 / PI;
    w = k_psi * (theta_goal - theta);
    vel = 0;
    // // translation
    // k_w = 5;
    // xdelta = x0 - x;
    // ydelta = y0 - y;
    // d0 = cos(theta * PI / 180) * xdelta + sin(theta * PI / 180) * ydelta;
    // vel = k_w * d0;
    break;

case 1: // Go-to-goal controller
    // translation
    k_w = 5;
    xdelta = xg - x;
    ydelta = yg - y;
    d0 = cos(theta_goal * PI / 180) * xdelta + sin(theta_goal * PI / 180) * ydelta;
    vel = k_w * d0;
    // rotation
    break;

default:
    vel = 0;
    w = 0;
    Serial.print("No controller selected. All movement stopped!");
    break;
}

left = vel - w / 2;
right = vel + w / 2;

Serial.print(" | w: ");
Serial.print(w);
Serial.print(" | vel: ");
Serial.print(vel);
Serial.print(" | left: ");
Serial.print(left);
Serial.print(" | right: ");
Serial.print(right);

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

// 0;0;-1.25;1.25
// -1.25;1.25;-0.75;1.25
// -0.75;1.25;-0.25;1.25
// -0.25;1.25;-0.25;0.75
// -0.25;0.75;0.25;0.75
// 0.25;0.75;0.25;0.25