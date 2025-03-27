import json
import socket
import sys


from discord_message import Message

FILE = '/home/orin/discord-webhook/data.json'

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception as e:
        print(f"Error getting IP address: {e}")
        sys.exit(1)  # Exit with error code 1


def check_ip():
    # Open the JSON file
    with open(FILE, 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

    URL = data["url"]
    saved_ip = data["ip"]
    print(saved_ip)

   
    IPAddr = get_ip_address()
    print(IPAddr)

    if(IPAddr == saved_ip):
        print("IP has not changed")
        return

    m = Message()

    mail = "The IP Address has been changed to: "

    m.setURL(URL)
    m.send(mail + IPAddr)

    data["ip"] = IPAddr

    with open(FILE, 'w') as file: 
        json.dump(data, file, indent=4) 



check_ip()