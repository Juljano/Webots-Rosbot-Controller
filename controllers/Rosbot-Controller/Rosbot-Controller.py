from controller import Robot, Camera, Motor
import numpy as np
import cv2

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


def take_photos(camera_name):
    try:
        width = camera_name.getWeight()
        height = camera_name.getHeight()
        image = camera_name.getImage()
        img_array = np.frombuffer(image, dtype=np.uint8).reshape((height, width, 4))
        save_image = cv2.cvtColor(img_array, cv2.COLOR_RGBA2BGR)
        cv2.imwrite("aufnahme.png", save_image)
    except Exception as e:
        print(F"Es konnte kein Foto aufgenommen werden. Kamera:{camera_name} - Fehler:{e}")




if __name__ == '__main__':

    controller = Controller()
    camera_depth = controller.enableSensors("camera depth")
    camera_rgb = controller.enableSensors("camera rgb")
    fl_motor = controller.enableMotors("fl_wheel_joint")
    fr_motor = controller.enableMotors("fr_wheel_joint")
    rl_motor = controller.enableMotors("rl_wheel_joint")
    rri_motor = controller.enableMotors("rr_wheel_joint")


while controller.step(controller.timestep) != -1:
        fl_motor.setVelocity(5)     # links vorne  (langsamer)
        fr_motor.setVelocity(15)    # rechts vorne (schneller)

        rl_motor.setVelocity(5)     # links hinten  (langsamer)
        rri_motor.setVelocity(15)   # rechts hinten (schneller)

        #take_photos(camera_depth)

