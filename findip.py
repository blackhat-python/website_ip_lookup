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
