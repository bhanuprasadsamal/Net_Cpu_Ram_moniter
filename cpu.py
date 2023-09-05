import psutil   #used for test the Cpu and Ram 
import speedtest    #used for test the speed of your net 

# CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)  # Returns CPU usage percentage in the last 1 second
print(f"CPU Usage: {cpu_usage}%")

# RAM Usage
ram = psutil.virtual_memory()
print(f"Total RAM: {ram.total / (1024**3):.2f} GB")
print(f"Available RAM: {ram.available / (1024**3):.2f} GB")
print(f"Used RAM: {ram.used / (1024**3):.2f} GB")
print(f"RAM Usage Percentage: {ram.percent}%")

# Below all the code is required for the test the speed of you net
st = speedtest.Speedtest()

download_speed = st.download() / 10**6  # in Mbps
upload_speed = st.upload() / 10**6      # in Mbps

print(f"Download Speed: {download_speed:.2f} Mbps")
print(f"Upload Speed: {upload_speed:.2f} Mbps")
