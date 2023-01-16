
clc;clear;close all;
%two dimensional wave equation in a square section with constrained
%boundary

%(1/c^2)*utt=uxx+uyy;
%hyperbolic PDE;

%square section 0<x<1, 0<y<1;
%Initial condition  u(x,y,0) = sin(m*pi*x)*sin(n*pi*y) for entire square

%Boundary conditions
%u(x,0,t)=0 for t>0
%u(x,1,t)=0 for t>0
%u(0,y,t)=0 for t>0
%u(1,y,t)=0 for t>0

%initial condition is set later in the code

c = 1; %wave propagation speed

delta_x = 0.05;
delta_y = delta_x;


cfl = 0.3; %CFL number or courant number sets limit on time step 
dt = cfl*(delta_x/c);

t = 0:dt:3;
x = 0:delta_x:1;
y = 0:delta_y:1; 

u = zeros(length(x),length(y),length(t));

%setting the initial condition
Init=questdlg('Choose an initial condition:','Choice','sin(m*pi*x)*cos(n*pi*y)','radial exponential cos','radial exponential','sin(m*pi*x)*cos(n*pi*y)');
switch Init
    case 'sin(m*pi*x)*cos(n*pi*y)'
        answer=inputdlg({'Enter value of m:(default=2)','Enter value of n:(default=2)'},'In sin(m*pi*x)*cos(n*pi*y)',[1 60;1 60]);
        m=str2double(answer{1});
        n=str2double(answer{2});
        u(:,:,1) = transpose(sin(m.*pi.*x))*sin(n.*pi.*y); 
    case 'radial exponential'
        for i= 1:length(x)
            for j=1:length(y)
                r=sqrt(   ((x(i)-0.5)^2) +  ((y(j)-0.5)^2));
                
                u(i,j,1)=0.5*exp(-8*r);
            end
        end
        case 'radial exponential cos'
        for i= 1:length(x)
            for j=1:length(y)
                r=sqrt(   ((x(i)-0.5)^2) +  ((y(j)-0.5)^2));
                u(i,j,1)=0.5*cos(4*pi*r)*exp(-4*r);
                
            end
        end
    case []
        msgbox('Rerun code and choose properly')
        return;
end
%end of initial condition i.e, XY grid at t=0


for ii = 2:length(x)-1 
    
    for step = 2:length(y)-1
     
        u(ii,step,2) = (cfl^2)*((u(ii+1,step,1)-2*u(ii,step,1)+u(ii-1,step,1)) + (u(ii,step+1,1)-2*u(ii,step,1)+u(ii,step-1,1)))+2*u(ii,step,1) - u(ii,step,1); 
    
    end
    
end

%creates the XY grid for t(2) onwards using finite difference method 

for n=2:length(t)-1
    
    
    for ii=2:length(x)-1
        
        
        for step=2:length(y)-1
           
            u(ii,step,n+1)= (cfl^2)*((u(ii+1,step,n)-2*u(ii,step,n)+u(ii-1,step,n))+(u(ii,step+1,n)-2*u(ii,step,n)+u(ii,step-1,n))) + 2*u(ii,step,n) - u(ii,step,n-1);
        
        end
        
        
    end
    
end
%end of creation of xy grids for each time step

%visualisation

[X,Y] = meshgrid(x,y);

for step=1:length(t)
       
       plot = surf(X,Y,u(:,:,step)); 
       title(sprintf('Wave Equation at time = %1.3f,\n courant number = %1.2f',t(step),cfl));
       
       axis ([0 1 0 1 -1 1]);
       xlabel('x'); 
       ylabel('y');
       zlabel(sprintf('u(x,y,t = %1.3f)',t(step)));
       
       if step==2
           savefig('new1.fig');
       end
       if step==201
           savefig('new2.fig');
       end
       if step==48
           savefig('new3.fig');
       end
       if step==60
           savefig('new4.fig');
       end
       pause(0.001);
       hold on; 
       
       if(step~=length(t))
       
           delete(plot);

       end
end
%enf of visualisation