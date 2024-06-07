# Port-Scanner

Port Scanner which accepts IP address and URL as argument. Returns output showcasing open ports.
- Attempts to establish a connection to Ports 22, 25, 53, 80, 443.
- If no connection can be established within the timeout time (0.1s), then the port is considered closed.
