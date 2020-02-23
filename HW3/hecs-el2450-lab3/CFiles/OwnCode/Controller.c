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
    // rotation
    Serial.print("Engage orientation controller!");
    xdelta = xg - x;
    ydelta = yg - y;
    w = k_psi * (theta_goal - theta);

    // translation
    xdelta = x0 - x;
    ydelta = y0 - y;
    d0 = cos(theta * PI / 180) * xdelta + sin(theta * PI / 180) * ydelta;
    vel = k_w * d0;

    if (abs(theta_goal_full - theta_full) < angle_threshold)
    {
        controller = 1;
        w = 0;
        vel = 0;
    }
    break;

case 1: // Go-to-goal controller
    // translation
    if (sqrt(pow(xg - x, 2) + pow(yg - y, 2)) > distance_threshold)
    {

        Serial.print("Engage Go-to-Goal controller!");
    }
    else
    {
        Serial.print("Reached goal!");
        send_done();
    }

    k_w_g2g = 10;
    xdelta = xg - x;
    ydelta = yg - y;
    d0 = cos(theta_goal * PI / 180) * xdelta + sin(theta_goal * PI / 180) * ydelta;
    vel = k_w_g2g * d0;

    xdelta = (x + p * cos(theta * PI / 180) - x0) * sin(theta_goal * PI / 180);
    ydelta = (y + p * sin(theta * PI / 180) - y0) * cos(theta_goal * PI / 180);
    w = k_psi_g2g * (xdelta - ydelta);

    break;
}

left = vel - w / 2;
right = vel + w / 2;