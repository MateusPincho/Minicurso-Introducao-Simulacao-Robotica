from coppeliasim_zmqremoteapi_client import *
import numpy as np

client = RemoteAPIClient()
sim = client.getObject('sim')

handle_robo = sim.getObject('/PioneerP3DX')

roda_direita = sim.getObject('/PioneerP3DX/rightMotor')
roda_esquerda = sim.getObject('/PioneerP3DX/leftMotor')

# Dados do robo P3DX
L = 0.381
r = 0.0975

# Velocidades desejadas (linear e angular)
v= 1
w = np.deg2rad(36)

# Cinemática Inversa
w_direita = ((2.0*v) + (w*L))/(2.0*r)   
w_esquerda = ((2.0*v) - (w*L))/(2.0*r)    
u = np.array([w_direita, w_esquerda])

sim.setJointTargetVelocity(roda_direita, w_direita)
sim.setJointTargetVelocity(roda_esquerda, w_esquerda)

q = np.array([0, 0, 0])

sim.startSimulation()
last_t = 0

while (t:=sim.getSimulationTime()) < 10:
    
    dt = sim.getSimulationTimeStep()
    
    linear, angular = sim.getObjectVelocity(handle_robo)

sim.stopSimulation()