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



wr = np.deg2rad(270)
wl = np.deg2rad(180)

sim.setJointTargetVelocity(roda_direita, wr)
sim.setJointTargetVelocity(roda_esquerda, wl)

sim.startSimulation()

while (t := sim.getSimulationTime()) < 10:

    pos = sim.getObjectPosition(handle_robo, -1)
    print(pos)



sim.stopSimulation()
