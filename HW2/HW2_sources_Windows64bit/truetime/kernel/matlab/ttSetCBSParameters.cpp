/*
 * Copyright (c) 2016 Lund University
 *
 * Written by Anton Cervin, Dan Henriksson and Martin Ohlin,
 * Department of Automatic Control LTH, Lund University, Sweden.
 *   
 * This file is part of TrueTime 2.0.
 *
 * TrueTime 2.0 is free software: you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * TrueTime 2.0 is distributed in the hope that it will be useful, but
 * without any warranty; without even the implied warranty of
 * merchantability or fitness for a particular purpose. See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with TrueTime 2.0. If not, see <http://www.gnu.org/licenses/>
 */

#define KERNEL_MATLAB
#include "../ttkernel.h" 

#include "../setcbsparameters.cpp"
#include "getrtsys.cpp"
#include "../checkinputargs.cpp"

void mexFunction( int nlhs, mxArray *plhs[],
                  int nrhs, const mxArray *prhs[] )
{
  rtsys = getrtsys() ; // Get pointer to rtsys 

  if (rtsys==NULL) {
    return;
  }

  /* Check and parse input arguments */

  char name[MAXCHARS];
  double Qs, Ts;

  if (checkinputargs(nrhs,prhs,TT_STRING,TT_SCALAR,TT_SCALAR)) {

    mxGetString(prhs[0], name, MAXCHARS);
    Qs = *mxGetPr(prhs[1]);
    Ts = *mxGetPr(prhs[2]);

  } else {
    
    TT_MEX_ERROR("ttSetCBSParameters: Wrong input arguments!\n"
		 "Usage: ttSetCBSParameters(name, Qs, Ts)");
    return;
  }

  ttSetCBSParameters(name, Qs, Ts);
}
