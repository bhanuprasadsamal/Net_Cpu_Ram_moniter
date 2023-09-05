import speedtest

st = speedtest.Speedtest()

download_speed = st.download() / 10**6  # in Mbps
upload_speed = st.upload() / 10**6      # in Mbps

print(f"Download Speed: {download_speed:.2f} Mbps")
print(f"Upload Speed: {upload_speed:.2f} Mbps")
