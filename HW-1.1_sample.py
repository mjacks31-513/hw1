## This is my first attempt at homework 1.1

import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as pyplot

'''
function ode_demo()

    %% Forward Euler
    dt = 0.01;

    t = 0;
    x(1) = 1;
    y(1) = 1;
    Nsteps = 100;

    fprintf('t\tx\ty\n')
    for i = 1:Nsteps-1
        fprintf('%.1f\t%.1f\t%.1f\n',t(i),x(i),y(i));
        x(i+1) = x(i) + dt*x(i);
        y(i+1) = y(i) - dt*y(i);
        t(i+1) = t(i) + dt;
    end

    plot(x,y);
    hold on;
    xlabel('x')
    ylabel('y')
    title('$dx/dt=x; dy/dt=-y$; x(0)=y(0)=1','Interpreter','Latex');

    %% Runge-Kutta


    function ret = dXdt(t, X)
        % For MATLAB ODE functions, must specify code that computes right-hand
        % side of differential equations. Here we have
        % dx/dt = x
        % dy/dt = -y
        %
        % Defining X = [x, y], in matrix notation
        %   dX/dt = [x; -y]
        ret = [X(1); -X(2)];
    end    

    [t, X] = ode45(@dXdt, [0, 1], [1, 1]);

    plot(X(:,1),X(:,2),'r-');

    legend('Forward Euler', 'Runge-Kutta 4-5');
end
'''


dt = 0.01
nSteps = 100

t = np.zeros((101,))
x = np.empty((101,))
y = np.empty((101,))

x[0] = 1
y[0] = 1

for iii in range(nSteps):
    x[iii+1] = x[iii] + dt*x[iii]
    y[iii+1] = y[iii] - dt*y[iii]
    t[iii+1] = t[iii] + dt

# E_field = kq * ((x-x_p) + (y-y_p) + (z-z_p))/(((x-x_p)**2 + (y-y_p)**2 + (y-y_p)**2)**(3/2))

def dXdt(t, X):
    return np.array([X[0], 0-X[1]])

output = spint.solve_ivp(dXdt,[0,1],[1,1],t_eval=np.linspace(0,1,101))


