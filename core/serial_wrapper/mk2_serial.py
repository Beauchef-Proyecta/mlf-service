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
        self.serial.send_data(data)
        payload = 0
        for angle in angles:
            payload += angle
        return self.serial.recv_response(self.CMD_JOINT, payload % 256)

    def set_relay_status(self, state:list, n:int):
        if n == 1:
            cmd = self.CMD_RELAY_1
        else:
            cmd = self.CMD_RELAY_2
        data = self.build_serial_msg(cmd, state)
        self.serial.send_data(data)
        self.serial.recv_response(cmd, state)
    
    def set_extra_servo(self, angle: list):
        data = self.build_serial_msg(self.CMD_EXTRA, angle)
        self.serial.send_data(data)
        return self.serial.recv_response(self.CMD_EXTRA, angle)

    
    def set_gripper_servo(self, angle: list):
        data = self.build_serial_msg(self.CMD_GRIPPER, angle)
        self.serial.send_data(data)
        return self.serial.recv_response(self.CMD_GRIPPER, angle)

    def get_weight(self):
        data = self.build_serial_msg(self.CMD_WEIGHT, [])
        self.serial.send_data(data)
        return self.serial.recv_response(self.CMD_WEIGHT, 0) #payload = 0 porque no se envían datos