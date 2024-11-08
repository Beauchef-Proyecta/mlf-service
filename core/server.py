import math
import struct
from flask import Flask, request, Response, Blueprint, make_response
import cv2
import os
from serial_wrapper.mk2_serial import MK2Serial

offset_str = os.getenv("OFFSETS", '0,0,0,0')
offset_list = [int(num) for num in offset_str.split(',')]

print(offset_list)
app = Flask(__name__)
mk2_serial = MK2Serial()

@app.route("/")
def home():
    return "Hello, World!"


@app.route("/connect")
def connect():
    return f"Connected! offsets: {offset_list}"


@app.route("/move")
def move_xyz():
    return "No disponible por el momento ¯\_(ツ)_/¯"


@app.route("/set_joints")
def set_joints():
    q0 = request.args.get("q0")
    q1 = request.args.get("q1")
    q2 = request.args.get("q2")
    q3 = request.args.get("q3")

    s0 = (int(float(q0)) + offset_list[0]) & 0xFF
    s1 = (int(float(q1)) + offset_list[1]) & 0xFF
    s2 = (int(float(q2)) + offset_list[2]) & 0xFF
    s3 = (int(float(q3)) + offset_list[3]) & 0xFF

    mk2_serial.set_joints([s0, s1, s2, s3])
    return f"Mi nueva pose es: (q0={q0}, q1={q1}, q2={q2}, q3={q3})"

@app.route("/set_relay_status", methods=["GET"])
def set_relay_status():
    state = request.args.get("state")
    relay = request.args.get("n_relay")
    s = int(state) & 0xFF 
    n = int(relay)
    mk2_serial.set_relay_status([s], n)
    return f"Estado del relay {n}: {state}"

@app.route("/set_extra_servo", methods=["GET"])
def set_extra_servo():
    q = request.args.get("q")
    s = int(q) & 0xFF
    mk2_serial.set_extra_servo([s])
    return f"Estado del extra: {q}"


@app.route("/set_gripper_servo", methods=["GET"])
def set_gripper_servo():
    q = request.args.get("q")
    s = int(q) & 0xFF
    mk2_serial.set_gripper_servo([s])
    return f"Estado del gripper: {q}"

@app.route("/get_weight", methods=["GET"])
def get_weight():
    data  = mk2_serial.get_weight()[:4]
    weight = struct.unpack('f', data)
    return {'weight': weight}
    
@app.route('/capture', methods=["GET"])
def capture_image():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        return Response("Camera is closed", status=503)
    
    ret, frame = camera.read()
    ret, jpeg = cv2.imencode('.jpg', frame)

    image = jpeg.tobytes()
    if image is None:
        return Response("Camera not available", status=503)
    
    return Response(image, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
