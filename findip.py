import time
from colorama import init, Fore
import pyfiglet

def animate_tool_name(tool_name):
    init()  # initialize colorama
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    figlet_text = pyfiglet.figlet_format(tool_name)  # convert tool name to ASCII art
    
    for color in colors:
        for line in figlet_text.split('\n'):
            print(color + line)
            time.sleep(0.1)  # adjust the delay to change animation speed
        time.sleep(0.5)  # pause between color changes

if __name__ == "__main__":
    tool_name = "BLACKHAT_PYTHON"
    animate_tool_name(tool_name)



import socket

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return "Unable to resolve hostname"

# Example usage
website_url = input("Enter Website URL : ")
ip_address = get_ip_address(website_url)
print("IP Address of ", website_url, ":", ip_address)
