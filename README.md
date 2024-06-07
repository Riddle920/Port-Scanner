# Port-Scanner

Port Scanner which accepts IP address or URL as argument. Returns output showcasing open ports.
- Attempts to establish a connection to Ports 22, 25, 53, 80, 443.
- If no connection can be established within the timeout time (0.1s), then the port is considered closed.

# Future Work

Future features that may potentially be added include:
- Scanning of all ports, not just hard-coded ports.
- Ability to designate a specific port or a range of ports to scan.