#include <math.h>
controller = 10;
distance_threshold = 5;
angle_threshold = 1;
theta_goal = atan2(yg, xg) * 180 / PI;
p = 2;

if (abs(theta_goal - theta) > 20)
{
    controller = 0;
}
else if (sqrt(pow(xg - x, 2) + pow(yg - y, 2)) > distance_threshold)
{
    controller = 1;
}
controller = 1;
switch (controller)
{
case 0: // rotational controller
    // rotation
    k_psi = 5;
    xdelta = xg - x;
    ydelta = yg - y;
    w = k_psi * (theta_goal - theta);

    // translation
    k_w = 5;
    xdelta = x0 - x;
    ydelta = y0 - y;
    d0 = cos(theta * PI / 180) * xdelta + sin(theta * PI / 180) * ydelta;
    vel = k_w * d0;
    break;

case 1: // Go-to-goal controller
    // translation
    k_w = 5;
    xdelta = xg - x;
    ydelta = yg - y;
    d0 = cos(theta_goal * PI / 180) * xdelta + sin(theta_goal * PI / 180) * ydelta;
    vel = k_w * d0;

    //Rotation
    p = sqrt(pow(xg - x, 2) + pow(yg - y, 2));
    if (20 < p)
    {
        k_g2g = 20;
    }
    else
    {
        k_g2g = p;
    }

    Serial.print(p);
    Serial.print(" k ");
    Serial.print(k_g2g);
    xdelta = (x + p * cos(theta * PI / 180) - x0) * sin(theta_goal * PI / 180);
    ydelta = (y + p * sin(theta * PI / 180) - y0) * cos(theta_goal * PI / 180);
    w = k_g2g * (xdelta - ydelta);

    break;

default:
    vel = 0;
    w = 0;
    Serial.print("No controller selected. All movement stopped!");
    break;
}

left = vel - w / 2;
right = vel + w / 2;

Serial.print(" Controller ");
Serial.print(controller);
// Serial.print(" | w: ");
// Serial.print(w);
// Serial.print(" | vel: ");
// Serial.print(vel);
// Serial.print(" | left: ");
// Serial.print(left);
// Serial.print(" | right: ");
// Serial.print(right);

// Serial.print("Theta error: ");
// Serial.print(theta_goal - theta);
// Serial.print(" | xdelta: ");
// Serial.print(xdelta);
// Serial.print(" | ydelta: ");
// Serial.print(ydelta);
// Serial.print(" | d0: ");
// Serial.print(d0);
// Serial.print(" | x ");
// Serial.print(x);
// Serial.print(" | x0 ");
// Serial.print(x0);
// Serial.print(" | xg ");
// Serial.print(xg);

// 0;0;-1.25;1.25
// -1.25;1.25;-0.75;1.25
// -0.75;1.25;-0.25;1.25
// -0.25;1.25;-0.25;0.75
// -0.25;0.75;0.25;0.75
// 0.25;0.75;0.25;0.25
