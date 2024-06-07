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
maxSteer = np.deg2rad(20)

# Definindo o meu set point do eixo y
setPoint = 0

# Iniciando as variaveis de erro
error = 0
lastError = 0
cumError = 0

sim.startSimulation()

while (t := sim.getSimulationTime()) < 20:

    # dt = Passo da simulação
    dt = sim.getSimulationTimeStep()

    # Obtendo a posição do robô na cena
    robotPos = sim.getObjectPosition(robotHandle, -1)
    
    # Error        
    error = setPoint - robotPos[1]

    # Derivada do erro
    dError = (error - lastError) / dt

    # Integral do erro
    cumError += error * dt
    
    # kp = .095 kd = .95 ki = .0001 -> valores testados para o controlador

    # Proporcional
    kp = .1
    up = kp*error
        
    # Derivativo
    kd = .95
    ud = kd*dError
        
    # Integral
    ki = .0001
    ui = ki*cumError

    # Controller
    u = up + ud + ui 
    
    # Limitando o valor para +/- max
    u = max(min(u, maxSteer), -maxSteer)
    
    sim.setJointTargetPosition(steerHandle, u)
    
    lastError = error    

sim.stopSimulation()