import socket  # Import the networking library to handle TCP/IP connections

# Define a class to organize our scanner's data and logic
class PortScanner:
    def __init__(self, target_ip):
        # Store the target IP address in a private-style variable
        self._target_ip = target_ip
        # Initialize an empty list to keep track of any open ports found
        self.found_ports = []

    def scan_port(self, port):
        """Attempts to 'knock' on a specific port to see if it answers."""
        
        # Create a new socket object
        # AF_INET = Use IPv4 addresses
        # SOCK_STREAM = Use TCP protocol (connection-oriented)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout of 0.5 seconds so the script doesn't wait forever on closed ports
        s.settimeout(0.5)
        
        # connect_ex tries to connect; it returns 0 for success and an error code for failure
        # We pass a tuple containing the target IP and the current port number
        result = s.connect_ex((self._target_ip, port))
        
        # If the result is 0, the port responded to the handshake (it's OPEN)
        if result == 0:
            print(f"[!] Port {port} is OPEN")
            self.found_ports.append(port) # Save the open port to our list
        
        # Close the socket connection to free up system resources
        s.close()

    def run_scan(self, start_port, end_port):
        """Triggers a loop to scan a range of ports defined by the user."""
        print(f"--- Starting Scan on {self._target_ip} ---")
        
        # Loop through every number from the start_port to the end_port
        for port in range(start_port, end_port + 1):
            self.scan_port(port) # Run the scan logic for this specific port
            
        print("--- Scan Complete ---")

# This block ensures the scanner only runs if the script is executed directly
if __name__ == "__main__":
    # 127.0.0.1 is the 'Loopback' address (your own computer)
    target = "127.0.0.1" 
    
    # Create an instance (object) of the PortScanner class
    scanner = PortScanner(target)
    
    # Start the scan on a specific range (e.g., ports 75 through 85)
    scanner.run_scan(75, 85)