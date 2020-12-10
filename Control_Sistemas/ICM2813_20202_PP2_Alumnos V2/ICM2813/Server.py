
import time
# import cv2
import functools
import numpy as np

#from controller_GT import Controller, Controlador
import random
import sys

from ICM2813 import b0RemoteApi

from functools import reduce 
import threading
import datetime




class LineFollower:

    def __init__(self, Controlador):


        # Cliente B0
        self.channel = "b0RemoteApi"
        self.node = "b0RemoteApi_pythonClient"
        self.client = b0RemoteApi.RemoteApiClient(self.node , self.channel)
       
        self.client.doNextStep=True
        self.simTime = 0
        self.__running = True
        self._wasPaused = False

        # VARIABLES DEL ROBOT.
        self._jointNames = ['RightWheel', 'LeftWheel']
        self._sensorNames = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']
        self._endSensor = ['EndSensor']
        
        self._ref = 3500.
        self._linepos_prev = 0.
        self._lineSensors = [False for i in np.arange(0, 8)]
        self._mean_sum = 0
        self._sum = 0
        
        

        print("Inicializando seguidor de linea")

        if self.client._clientId != -1:
            self.client.runInSynchronousMode = True
            self.client.simxSynchronous(True)

            self._joinHandles = [self.client.simxGetObjectHandle(joint , self.client.simxServiceCall())[1] for joint in self._jointNames]
            self._sensorHandles = [self.client.simxGetObjectHandle(joint , self.client.simxServiceCall())[1] for joint in self._sensorNames]
            self._endSensorHandles = [self.client.simxGetObjectHandle(joint , self.client.simxServiceCall())[1] for joint in self._endSensor]
            self._botHandle = self.client.simxGetObjectHandle('Base_dyn' , self.client.simxServiceCall())[1]

        
        else:
            raise Exception()

        # Debemos guardar la posicion inicial del robot.

        _, self._lastPose = self.client.simxGetObjectPosition(self._botHandle, -1, self.client.simxServiceCall())
        
        


        self.stopSim = False

        # Aca definimos nuestro cotrolador.
        
        self.controller = Controlador

    


    def running(self):
        return self.__running

    def stop(self):
        self.__running = False

    def checkEndFlag(self):
        result = [self.client.simxReadProximitySensor(sensorHandle, self.client.simxServiceCall() ) for sensorHandle in self._endSensorHandles][0]
        return result[1]

    def simulationStepStarted(self, msg):
        simTime=msg[1][b'simulationTime']
        # print('Simulation step started at simulation time: ',simTime)
        
    def simulationStepDone(self, msg):
        simTime=msg[1][b'simulationTime']
        # print('Simulation step done at simulation time: ',simTime)
        self.simTime = simTime
        self.client.doNextStep=True


        
    def medirS1(self, msg):
        if msg[0]:
            lis = np.array(np.frombuffer(msg[2], dtype=np.uint8), dtype=np.uint8)

            im = np.mean(np.resize(lis, msg[1]))
            
            
            self._mean_sum += im
            self._sum += 0*im
            self._lineSensors[0] = True

  

    def medirS2(self, msg):
        if msg[0]:
            lis = np.array(np.frombuffer(msg[2], dtype=np.uint8), dtype=np.uint8)

            im = np.mean(np.resize(lis, msg[1]))
            self._mean_sum += im
            self._sum += 1000*im
            self._lineSensors[1] = True
    

    def medirS3(self, msg):
        if msg[0]:
            lis = np.array(np.frombuffer(msg[2], dtype=np.uint8), dtype=np.uint8)

            im = np.mean(np.resize(lis, msg[1]))
            self._mean_sum += im
            self._sum += 2000*im
            self._lineSensors[2] = True
            

        
    def medirS4(self, msg):
        if msg[0]:
            lis = np.array(np.frombuffer(msg[2], dtype=np.uint8), dtype=np.uint8)

            im = np.mean(np.resize(lis, msg[1]))
            self._mean_sum += im
            self._sum += 3000*im
            self._lineSensors[3] = True

            
    def medirS5(self, msg):
        if msg[0]:
            lis = np.array(np.frombuffer(msg[2], dtype=np.uint8), dtype=np.uint8)

            im = np.mean(np.resize(lis, msg[1]))
            self._mean_sum += im
            self._sum += 4000*im
            self._lineSensors[4] = True
            

    def medirS6(self, msg):
        if msg[0]:
            lis = np.array(np.frombuffer(msg[2], dtype=np.uint8), dtype=np.uint8)

            im = np.mean(np.resize(lis, msg[1]))
            self._mean_sum += im
            self._sum += 5000*im
            self._lineSensors[5] = True

            
            

    def medirS7(self, msg):
        if msg[0]:
            lis = np.array(np.frombuffer(msg[2], dtype=np.uint8), dtype=np.uint8)

            im = np.mean(np.resize(lis, msg[1]))
            self._mean_sum += im
            self._sum += 6000*im
            self._lineSensors[6] = True
          

    def medirS8(self, msg):
        if msg[0]:
            lis = np.array(np.frombuffer(msg[2], dtype=np.uint8), dtype=np.uint8)

            im = np.mean(np.resize(lis, msg[1]))
            self._mean_sum += im
            self._sum += 7000*im
            self._lineSensors[7] = True
           
        
    def measure(self, verbose=False):
        if reduce(lambda x, y : x and y , self._lineSensors):
            self._lineSensors = [False for i in np.arange(0, 8)]
            if(verbose):
                print("self._mean_sum = {}".format(self._mean_sum))
                print("self._sum = {}".format(self._sum))
            if self._sum > 0 : 
                linepos = self._sum / self._mean_sum 
                linepos += random.randint(-300, 300)
            else:
                linepos = self._linepos_prev
            
            self._linepos_prev = linepos
            
            self._sum = 0
            self._mean_sum = 0

            return linepos
        else:
            return self._linepos_prev

    

    def exitHandler(self):
        _, state = self.client.simxGetSimulationState(self.client.simxServiceCall())
        if state != 0:
            self.client.simxStopSimulation(self.client.simxServiceCall())
        self.client.__exit__()


    def run(self):
        #self.client.simxStartSimulation(self.client.simxServiceCall())
        self.client.simxGetSimulationStepStarted(self.client.simxDefaultSubscriber(self.simulationStepStarted))
        self.client.simxGetSimulationStepDone(self.client.simxDefaultSubscriber(self.simulationStepDone))
        #self.client.simxStartSimulation(self.client.simxServiceCall())

        # Agregado:

        self.client.simxGetVisionSensorImage(self._sensorHandles[0], True, self.client.simxDefaultSubscriber(self.medirS1) )
        self.client.simxGetVisionSensorImage(self._sensorHandles[1], True, self.client.simxDefaultSubscriber(self.medirS2) )
        self.client.simxGetVisionSensorImage(self._sensorHandles[2], True, self.client.simxDefaultSubscriber(self.medirS3) )
        self.client.simxGetVisionSensorImage(self._sensorHandles[3], True, self.client.simxDefaultSubscriber(self.medirS4) )
        self.client.simxGetVisionSensorImage(self._sensorHandles[4], True, self.client.simxDefaultSubscriber(self.medirS5) )
        self.client.simxGetVisionSensorImage(self._sensorHandles[5], True, self.client.simxDefaultSubscriber(self.medirS6) )
        self.client.simxGetVisionSensorImage(self._sensorHandles[6], True, self.client.simxDefaultSubscriber(self.medirS7) )
        self.client.simxGetVisionSensorImage(self._sensorHandles[7], True, self.client.simxDefaultSubscriber(self.medirS8) )
        # ------------------------ #

        
        counts = 0
        # Obtenemos el estado de la simulacion 
        #_, state = self.client.simxGetSimulationState(self.client.simxServiceCall())
        while self.running():
            
                
                #self.client.simxStopSimulation(self.client.simxServiceCall())
                #self.client.__exit__()
                #self.stop()
                #break

            
            _, state = self.client.simxGetSimulationState(self.client.simxServiceCall())

            
            
            if self.client.runInSynchronousMode and state == 16:
                while not self.client.doNextStep: 
                    
                    if self.checkEndFlag() == 1 and state == 16:
                        self.stop()
                        break

                    #if(state == 16):
                    # Obtenemos el valor del sensor de linea.
                    print("Procesando!")
                    linepos = self.measure()

                    # Calculamos el valor de la señal de entrada u
                    error = self._ref - linepos 
                    dt = 0.05
                    
                    
                    w_derecha, w_izquierda = self.controller.calculate(error, dt)

                    # Cambiamos el valor de las velocidades de las ruedas.

                    self.client.simxSetJointTargetVelocity(self._joinHandles[0], w_derecha, self.client.simxDefaultPublisher())
                    self.client.simxSetJointTargetVelocity(self._joinHandles[1], w_izquierda , self.client.simxDefaultPublisher())
                        
                        

                    self.client.simxSpinOnce()

                self.client.doNextStep=False
                self.client.simxSynchronousTrigger()
            else:
                if state ==0:
                    self.controller.__init__()
                

            if self.checkEndFlag() == 1 and state == 16:
                self.stop()
                #print("Simulacion terminada ...")
                break

            
            counts += 1
            print("counts : {}".format(counts))
            


        print("# --- SIMULACION TERMINADA --- #")
        converted = datetime.timedelta(seconds=self.simTime)
        print("H : M : S")
        print("Su Robot se ha demorado ", converted, "en completar la simulacion.")
        print("Segundos : {}".format(self.simTime))
        
        
     
    

