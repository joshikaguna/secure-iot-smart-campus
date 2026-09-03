"""
Secure IoT Network for Smart Campus
Authentication-enabled IoT Simulation
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import hashlib
import secrets
import os

HOST = "127.0.0.1"
PORT = 8080

# Demo credentials for the authorized laboratory environment.
USERNAME = os.getenv("IOT_USERNAME", "campus_admin")
PASSWORD = os.getenv("IOT_PASSWORD", "SmartCampus@2026")

# Store a password hash instead of the plaintext password.
PASSWORD_HASH = hashlib.sha256(
    PASSWORD.encode()
).hexdigest()

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


def verify_credentials(username, password):
    password_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    return (
        secrets.compare_digest(username, USERNAME)
        and secrets.compare_digest(password_hash, PASSWORD_HASH)
    )


class IoTRequestHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status_code=200):
        response = json.dumps(data).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)

    def authenticate(self):
        username = self.headers.get("X-IoT-Username")
        password = self.headers.get("X-IoT-Password")

        if not username or not password:
            self.send_json({
                "error": "Authentication required",
                "message": "Valid IoT credentials are required."
            }, 401)
            return False

        if not verify_credentials(username, password):
            self.send_json({
                "error": "Authentication failed",
                "message": "Invalid credentials."
            }, 403)
            return False

        return True

    def do_GET(self):

        # Public health-check endpoint
        if self.path == "/":
            self.send_json({
                "project": "Secure IoT Network for Smart Campus",
                "server": "IoT Simulation Server",
                "authentication": "enabled"
            })
            return

        # All IoT data endpoints require authentication
        if not self.authenticate():
            return

        if self.path == "/devices":
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

    server = HTTPServer(
        (HOST, PORT),
        IoTRequestHandler
    )

    print("=" * 55)
    print(" SECURE SMART CAMPUS IoT SIMULATION")
    print("=" * 55)
    print(f"Server running on http://{HOST}:{PORT}")
    print("Authentication: ENABLED")
    print()
    print("Protected endpoints:")
    print("  /devices")
    print("  /temperature")
    print("  /lighting")
    print("  /door")
    print()
    print("Press CTRL+C to stop the server.")
    print("=" * 55)

    server.serve_forever()


if __name__ == "__main__":
    start_server()
