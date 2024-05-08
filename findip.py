<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Blackhat-python</title>
<style>
/* Define animation */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Apply animation to element */
.animate-fadeIn {
  animation: fadeIn 1s ease-in-out;
}

/* Style for the button */
.button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

/* Style for the loading spinner */
.spinner {
  border: 4px solid #f3f3f3; /* Light grey */
  border-top: 4px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
  display: none; /* Initially hide spinner */
}

/* Spinner animation */
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
</head>
<body>

<!-- Button to trigger animation -->
<button id="githubButton" class="button">Fetch Data</button>
<!-- Loading spinner -->
<div id="spinner" class="spinner"></div>

<script>
document.getElementById('githubButton').addEventListener('click', function() {
  // Show loading spinner
  document.getElementById('spinner').style.display = 'inline-block';
  // Simulate fetching data from GitHub (replace this with your actual code)
  setTimeout(function() {
    // Hide loading spinner after a delay (replace 2000 with however long your operation takes)
    document.getElementById('spinner').style.display = 'none';
    // Simulate displaying fetched data (replace this with your actual code)
    alert('Data fetched from GitHub!');
  }, 2000);
});
</script>

</body>
</html>


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
