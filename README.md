# PyNet-Scanner 🛡️

A lightweight TCP Port Scanner written in Python. This tool is designed for network reconnaissance and security auditing, allowing users to identify open "attack surfaces" on a target host.

## ⚙️ Core Logic
The scanner utilizes a **TCP Connect Scan** method. It attempts to complete the three-way handshake (SYN, SYN-ACK, ACK) with the target. If the kernel returns a success code (0), the port is identified as active and listening.

## ✨ Features
*   **Object-Oriented Architecture:** Uses a `PortScanner` class for clean and modular code.
*   **Performance Optimized:** Implements a 0.5s timeout per connection to ensure rapid scanning without hanging.
*   **Target Flexibility:** Easily switch between `localhost` testing and external IP auditing.

## 🚀 How to Use
1. Ensure Python is installed.
2. Clone the repository and navigate to the folder.
3. Run the script:
   ```bash
   python scanner.py
