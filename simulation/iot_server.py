"""
Secure IoT Network for Smart Campus
IoT Device Simulation

This program simulates three smart-campus IoT devices:
1. Temperature Sensor
2. Smart Lighting
3. Smart Door Lock

The server provides a simple interface for authorized
security testing in a controlled laboratory environment.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


HOST = "127.0.0.1"
PORT = 8080


# Simulated IoT devices
IOT_DEVICES = {
    "temperature": {
        "device_name": "Campus Temperature Sensor",
        "status": "online",
        "temperature": "27°C"
    },
    "lighting": {
        "device_name": "Smart Classroom Lighting",
        "status": "online",
        "state": "ON"
    },
    "door_lock": {
        "device_name": "Main Building Smart Door Lock",
        "status": "online",
        "state": "LOCKED"
    }
}


class IoTRequestHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status_code=200):
        response = json.dumps(data).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)

    def do_GET(self):

        if self.path == "/":
            self.send_json({
                "project": "Secure IoT Network for Smart Campus",
                "server": "IoT Simulation Server",
                "status": "running"
            })

        elif self.path == "/devices":
            self.send_json(IOT_DEVICES)

        elif self.path == "/temperature":
            self.send_json(IOT_DEVICES["temperature"])

        elif self.path == "/lighting":
            self.send_json(IOT_DEVICES["lighting"])

        elif self.path == "/door":
            self.send_json(IOT_DEVICES["door_lock"])

        else:
            self.send_json({
                "error": "Unknown endpoint"
            }, 404)

    def log_message(self, format, *args):
        print("[IoT LOG]", format % args)


def start_server():

    server = HTTPServer((HOST, PORT), IoTRequestHandler)

    print("=" * 50)
    print(" SMART CAMPUS IoT SIMULATION")
    print("=" * 50)
    print(f"Server running on http://{HOST}:{PORT}")
    print()
    print("Available IoT endpoints:")
    print("  /devices")
    print("  /temperature")
    print("  /lighting")
    print("  /door")
    print()
    print("Press CTRL+C to stop the server.")
    print("=" * 50)

    server.serve_forever()


if __name__ == "__main__":
    start_server()
