import np as numpy

class MiControlador(Motor):
    def __init__(self):
        self.stop()
        super().__init__()
        self.Kp=0
        self.Ki=0
        self.Kd=0
        self.error=0
        self.error_anterior=0
        self.error_acumulado=0
        self.error_derivativo=0
        self.t_ant=0.0000001
        self.t=list()
        self.theta=list()

    def control (self,theta,t):
        self.t.append(t)
        self.theta.append(np.rad2deg(theta))
        if t>5:
            theta_ref=np.radians(90)
        else:
            theta_ref = np.radians(90)

        self.error=theta_ref-theta
        delta_t=t-self.t_ant
        self.error_derivativo=(self.error-self.error_anterior)/delta_t
        self.error_acumulado+=self.error

        PWM=self.Kp*self.error + self.Kd*self.error_derivativo + self.Ki*self.error_acumulado*delta_t

        self.t_ant=t
        self.error_anterior=self.error

        if t >=10:
            self.stop()



