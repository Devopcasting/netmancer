# commands/scan_wireless_devices.py
import subprocess
import json
from logger import NetmancerLogger
from commands.list_interfaces import get_network_interfaces

def scan_wireless_devices():
    try:
        """
            Scan for wireless devices using nmcli command
            Return:
                str: A JSON-formatted list of wireless devices
        """
        logger = NetmancerLogger()
        logger.log_info("Scanning for wireless devices...")
        
        # Check if wifi interface is available
        interfaces = json.loads(get_network_interfaces())
        wifi_interface = None
        for interface in interfaces:
            if interface['type'] == 'wifi':
                wifi_interface = interface['interface']
                break
        if wifi_interface is None:
            logger.log_error("No wifi interface found")
            return {"error": "No wifi interface found"}
        
        # Scan for wireless devices
        result = subprocess.run(
            ["nmcli", "-t", "-f", "BSSID,SSID,MODE,CHAN,RATE,SIGNAL,SECURITY", "dev", "wifi"],
            check=True,
            capture_output=True,
            text=True
        )
        wifi_list = []
        for line in result.stdout.strip().split("\n"):
            if line:
                fields = re.split(r'(?<!\\):', line)
                if len(fields) >= 7:
                    SSID = fields[1]
                    if SSID == "":
                        SSID = "Hidden Network"
                    wifi_list.append({
                        "BSSID": fields[0].replace("\\", ""),
                        "SSID": SSID,
                        "MODE": fields[2],
                        "CHAN": fields[3],
                        "RATE": fields[4],
                        "SIGNAL": fields[5],
                        "SECURITY": fields[6],
                    })
        logger.log_info(f"Wireless devices scanned successfully")
        return json.dumps(wifi_list, indent=4)
    except subprocess.CalledProcessError as e:
        logger.log_error(f"Error scanning for wireless devices: {e}")
        return {"error": f"Error scanning for wireless devices: {e}"}
    except Exception as e:
        logger.log_error(f"Error scanning for wireless devices: {e}")
        return {"error": f"Error scanning for wireless devices: {e}"}