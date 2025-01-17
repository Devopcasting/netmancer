import argparse
from logger import NetmancerLogger
from commands.list_interfaces import get_network_interfaces

def help_menu():
    print("Network Configuration Utility")
    print("Usage: python3 network_config.py [options]")
    print("Options:")
    print("  --list-interfaces   List available network interfaces")
    print("  --help              Display this help menu")

def main():
    # Create an instance of the NetmancerLogger class
    logger = NetmancerLogger()

    parser = argparse.ArgumentParser(description="Network Configuration Utility", allow_abbrev=False)
    
    # Argument for listing network interfaces
    parser.add_argument("--list-interfaces", action="store_true", help="List available network interfaces")
    args = parser.parse_args()
    
    try:
        # Check if the --list-interfaces argument is provided
        if args.list_interfaces:
            # Call the function to list network interfaces
            interfaces = get_network_interfaces()
            if interfaces:
                print(interfaces)
    except Exception as e:
        logger.log_error(f"Error: {e}")
    
if __name__ == "__main__":
    main()