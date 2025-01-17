import argparse
from logger import NetmancerLogger
from commands.list_interfaces import get_network_interfaces
from commands.scan_wireless_devices import scan_wireless_devices

def help_menu():
    print("Network Configuration Utility")
    print("Usage: python3 netmancer.py [options]")
    print("Options:")
    print("  --list-interfaces  List available network interfaces")
    print("  --scan-wireless-devices   Scan for wireless devices")
    print("  --H                     Display this help menu")

def main():
    parser = argparse.ArgumentParser(description="Network Configuration Utility", allow_abbrev=False)
    
    # Argument for listing network interfaces
    parser.add_argument("--list-interfaces", action="store_true", help="List available network interfaces")
    # Argument for displaying help menu
    parser.add_argument("--H", action="store_true", help="Display help menu")
    # Argument for scanning for wireless devices
    parser.add_argument("--scan-wireless-devices", action="store_true", help="Scan for wireless devices")

    args = parser.parse_args()
    
    try:
        # Check if the --list-interfaces argument is provided
        if args.list_interfaces:
            # Call the function to list network interfaces
            interfaces = get_network_interfaces()
            if interfaces:
                print(interfaces)
        elif args.scan_wireless_devices:
            # Call the function to scan for wireless devices
            devices = scan_wireless_devices()
            if devices:
                print(devices)
        elif args.H:
            # Display the help menu
            help_menu()

    except Exception as e:
        logger.log_error(f"Error: {e}")
    
if __name__ == "__main__":
    # Create an instance of the NetmancerLogger class
    logger = NetmancerLogger()
    main()