from controller import Robot, Camera, Motor

"""
fr_motor = fr_wheel_joint
fl_motor = fl_wheel_joint
rri_motor = rr_wheel_joint
rl_motor = rl_wheel_joint
camera = camera depth
"""


class Controller(Robot):
    def __init__(self):
        super(Controller, self).__init__()
        self.timestep = int(self.getBasicTimeStep())
        self.max_velocity = 26

    def enableSensors(self, sensor_name):
        try:
            sensor = self.getDevice(sensor_name)
            if sensor is not None:
                sensor.enable(self.timestep)
                print(F"Sensor {sensor_name} aktiviert")
                return sensor
        except Exception as e:
            print(f"Der Sensor {sensor_name} konnte nicht aktiviert oder gefunden werden")

    def enableMotors(self, motor_name):
        try:
            motor = self.getDevice(motor_name)
            if motor is not None:
                motor.setPosition(float('inf'))
                motor.setVelocity(0.0)
                print(F"Motor {motor_name} aktiviert")
                return motor
        except Exception as e:
            print(f"Der Motor {motor_name} konnte nicht aktiviert oder gefunden werden")


if __name__ == '__main__':

    controller = Controller()
    camera_depth = controller.enableSensors("camera depth")
    camera_rgb = controller.enableSensors("camera rgb")
    fl_motor = controller.enableMotors("fl_wheel_joint")
    fr_motor = controller.enableMotors("fr_wheel_joint")
    rl_motor = controller.enableMotors("rl_wheel_joint")
    rri_motor = controller.enableMotors("rr_wheel_joint")


while controller.step(controller.timestep) != -1:
        print("Starte Rosbot")
        fl_motor.setVelocity(25) #links
        fr_motor.setVelocity(0) #rechts
        rl_motor.setVelocity(15)
        rri_motor.setVelocity(15)

        image = camera_rgb.getImage()
