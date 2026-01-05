import socket

@app.route("/health")
def health():
    return "OK", 200

@app.route("/")
def hello():
    return f"Hello from LightApp 🚀\nHostname: {socket.gethostname()}\n"
