# 🐍🚢🛂 Py-Port-Scaner - Simple Network Port Scanner

Py-Port-Scaner is a Python program that functions as a network port scanner. 
A port scanner is a tool used to discover open ports on a network host, which can help identify potential vulnerabilities.

# 📔 Project Plan
- ✍️ **User Input**
  - Prompt the user to enter a target IP address or hostname to scan.
- 🚢 **Port Range**
  - Ask the user for a range of ports to scan.
  - You can choose to scan a specific range (e.g., 1-1000)
  - You can provide a list of common ports to scan.
- 👓 **Port Scanning Logic**
  - Implement a port scanning logic that checks if a port is open or closed on the target host. 
  - TIP: use Python's socket library to establish a connection to the target IP and port.
- 📺 **Output**
  - Display the results to the user, indicating which ports are open and which are closed.
- ⁉️ **Error Handling**
  - Handle exceptions that may occur during the scanning process, such as connection timeouts or errors.
- 🚁 **Optimization**
  - Consider implementing multithreading to speed up the scanning process by scanning multiple ports simultaneously.
- 🧪 **Testing Environment**
  - Add config for Vagrant or Docker container where you can use PyPortScaner to demonstrate the program

# 🔑 Security Considerations
Make sure to follow ethical guidelines and use this tool only on networks you have permission to scan. Unwanted or unauthorized port scanning can be considered malicious.

# 🪖 Disclaimer
The main idea of this project is to gain hands-on experience in network scanning techniques and further understand how to identify potential entry points for attackers. As with great power comes greate responsibility make sure to use this knowledge responsibly and for educational purposes.
