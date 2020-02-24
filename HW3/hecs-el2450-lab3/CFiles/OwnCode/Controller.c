#include <math.h>

theta_rad = theta * PI / 180;
theta_goal_rad = atan2(yg - y0, xg - x0);
theta_goal = theta_goal_rad * 180 / PI;
theta_full = theta;
theta_goal_full = theta_goal;

if (theta_goal < 0)
{
    theta_goal_full = 360 + theta_goal;
}
if (theta < 0)
{
    theta_full = 360 + theta;
}

switch (controller)
{
case 0: // rotational controller
    if (abs(theta_goal_full - theta_full) > angle_threshold)
    {
        Serial.print("Engage orientation controller!");
    }
    else
    {
        Serial.print("Orientation good!");
        controller = 1;
        w = 0;
        vel = 0;
    }

    // rotation
    w = k_psi * (theta_goal - theta);

    // translation
    xdelta = x0 - x;
    ydelta = y0 - y;
    d0 = cos(theta_rad) * xdelta + sin(theta_rad) * ydelta;
    vel = k_w * d0;

    break;

case 1: // Go-to-goal controller
    if (sqrt(pow(xg - x, 2) + pow(yg - y, 2)) > distance_threshold)
    {
        Serial.print("Engage Go-to-Goal controller!");
    }
    else
    {
        Serial.print("Reached goal!");
        send_done();
    }

    // translation
    xdelta = xg - x;
    ydelta = yg - y;
    d0 = cos(theta_goal_rad) * xdelta + sin(theta_goal_rad) * ydelta;
    vel = k_w_g2g * d0;

    // rotation
    xdelta_rot = (x + p * cos(theta_rad) - x0) * sin(theta_goal_rad);
    ydelta_rot = (y + p * sin(theta_rad) - y0) * cos(theta_goal_rad);
    w = k_psi_g2g * (xdelta_rot - ydelta_rot);

    break;
}

left = vel - w / 2;
right = vel + w / 2;