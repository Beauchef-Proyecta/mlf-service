from .serial_controller import SerialController


class MK2Serial:
    
    HEADER = 0xA0
    CMD_JOINT = 0x10
    CMD_BELT = 0x20
    CMD_GRIPPER = 0x30
    CMD_MAGNET = 0x40
    CMD_RELAY_1 = 0x50
    CMD_RELAY_2 = 0x60
    CMD_EXTRA = 0x70
    CMD_PROXIMITY = 0xA0
    CMD_LASER = 0xB0
    CMD_WEIGHT = 0x80

    
    def __init__(self, port="/dev/ttyUSB0"):
        self.serial = SerialController(port)
        self.serial.open()
    
    def build_serial_msg(self, cmd: int, params: list):
        data = [self.HEADER, len(params) + 1, cmd]
        for p in params:
            data.append(p)
        return bytearray(data)
    
    def set_joints(self, angles: list):
        data = self.build_serial_msg(self.CMD_JOINT, angles)
        return self.serial.send_data(data)

    def set_relay_status(self, state:list, n:int):
        if n == 1:
            data = self.build_serial_msg(self.CMD_RELAY_1, state)
        else:
            data = self.build_serial_msg(self.CMD_RELAY_2, state)
        return self.serial.send_data(data)
    
    def set_extra_servo(self, angle: list):
        data = self.build_serial_msg(self.CMD_EXTRA, angle)
        return self.serial.send_data(data)

    
    def set_gripper_servo(self, angle: list):
        data = self.build_serial_msg(self.CMD_GRIPPER, angle)
        return self.serial.send_data(data)

    def get_weight(self):
        #4 es len de la data recibida (4 por ser double en arduino)
        data = self.build_serial_msg(self.CMD_WEIGHT, [])
        return self.serial.recv_data(data, 4)   
