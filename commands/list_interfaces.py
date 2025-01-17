# commands/list_interfaces.py
import subprocess
import json
from logger import NetmancerLogger

def get_network_interfaces():
    try:
        """
            List available network interfaces using nmcli command
            Skip loopback and p2p interface.
            Return:
                str: A JSON-formatted list of interface with there status and type
        """
        logger = NetmancerLogger()
        logger.log_info("Listing network interfaces...")
        result = subprocess.run(['nmcli', 'device', 'status'], capture_output=True, text=True)
        interfaces = []
        for line in result.stdout.split('\n')[1:]:
            if line:
                parts = line.split()
                if len(parts) >= 3:
                    interface = parts[0]
                    status = parts[2]
                    if interface != 'lo' and interface != 'p2p':
                        interface_type = parts[1]
                        interfaces.append({"interface": interface, "status": status, "type": interface_type})
        logger.log_info(f"Network interfaces: {interfaces}")
        return json.dumps(interfaces)
    except Exception as e:
        logger.log_error(f"Error listing network interfaces: {e}")
        return {"error": f"Error listing network interfaces: {e}"}
