from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

client = RemoteAPIClient()

sim = client.getObject("sim")

#Handle do Robo
robotHandle = sim.getObject("/Manta")
steerHandle = sim.getObject("/Manta/steer_joint")
motorHandle = sim.getObject("/Manta/motor_joint")

#Definindo torque e velocidade do motor do Robo
motorTorque = 60
motorVelocity = 12
sim.setJointForce(motorHandle, motorTorque)
sim.setJointTargetVelocity(motorHandle, motorVelocity)

robotPos = sim.getObjectPosition(robotHandle, -1)

# Definindo o ângulo máximo que o meu volante consegue virar
maxSteer = np.deg2rad(5)

sim.startSimulation()

while (t := sim.getSimulationTime()) < 20:

    # Obtendo a posição do robo na cena
    robotPos = sim.getObjectPosition(robotHandle, -1)
    
    # Entrada de Controle
    u =  maxSteer

    # se o Robô passou da linha, vire para o outro lado
    if robotPos[1] > 0:
        u = -maxSteer

    sim.setJointTargetPosition(steerHandle, u)

sim.stopSimulation()