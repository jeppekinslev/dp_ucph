# import packages used
import numpy as np
import scipy.optimize as optimize

def solve_consumption_grid_search(par):
     # initialize solution class
    class sol: pass
    sol.C = np.zeros(par.num_W)
    sol.V = np.zeros(par.num_W)
    
    # consumption grid as a share of available resources
    grid_C = np.linspace(0.0,1.0,par.num_C) 
    
    # Resource grid
    grid_W = par.grid_W

    # Init for VFI
    delta = 1000 #difference between V_next and V_now
    it = 0  #iteration counter 
    
    while (par.max_iter>= it and par.tol<delta):
        it = it+1
        V_next = sol.V.copy()
        for iw,w in enumerate(grid_W):  # enumerate automaticcaly unpack w
                           
            # Fill in  
            # Find possible consumption choices given the size of the cake w
            c = grid_C * w  
            # Calculate cake left after consumption
            w_c = w - c                    # Hint: For each w create a consumption grid, c, using grid_C.                          
            
            V_next_interp = np.interp(w_c,grid_W,V_next)                   # Use c to calculate V_guess using interpolation
            V_guess = np.sqrt(c)+par.beta*V_next_interp
            index = np.argmax(V_guess)
            sol.C[iw] = c[index]
            sol.V[iw] = np.amax(V_guess)
                                        #       In order to interpolate use:  np.interp
                                        #       Proceed as in Exercise_2.py
      
        delta = np.amax(np.abs(sol.V - V_next))
    
    return sol