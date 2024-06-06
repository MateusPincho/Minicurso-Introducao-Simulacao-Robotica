from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

client = RemoteAPIClient()
sim = client.getObject("sim")

# Função de normalização dos ângulos ao intervalo [-pi, pi)
def normalizeAngle(angle):
    return np.mod(angle+np.pi, 2*np.pi) - np.pi

# Handle do P3DX

# Handle dos motores

# Dados do robo P3DX
L = 0.381
r = 0.0975
maxv = 1.0
maxw = np.deg2rad(45)

# Definir o meu Goal -> array (x, y, theta)

#rho inicia muito grande
rho = np.inf 

sim.startSimulation()

# Enquanto meu robô estiver a uma distância maior que 5cm do goal, execute: 
while rho > 0.05:
    # Obter posição e orientação atual do robô

    # calculo do erro em x, y e theta
    
    # variaveis de estado atual (alpha, beta e rho) -> usar equações do slide

    # definir valores de constante proporcial

    kr = 4 / 20
    ka = 8 / 20
    kb = -1.5 / 20

    # checar se o goal está na frente do robô -> | alpha | > 90° ? 
    # se sim, a velocidade linear deve ser negativa
    # se sim, alpha e beta devem ser normalizados para o intervalo

    # calculo da velocidade linear e angular

    # lembre-se de limitar as velocidades ao valor maximo do robo

    # calculo de WL e WR a partir de v e w

    # definir a velocidade dos motores do P3DX


# Parar o robô

# Finalizar simulação
sim.stopSimulation()
