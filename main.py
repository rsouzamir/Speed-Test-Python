import speedtest

test = speedtest.Speedtest()

print("Finding server list...")
test.get_servers()

print("Choosing best server...")
best = test.get_best_server()

print(f"Server name is : {best['name']}")
print(f"Found the server {best['host']} located in {best['country']}.")

print("Perfoming download speed test...")
download_result = test.download()

print("Perfoming upload speed test...")
upload_result = test.upload()

print("Perfoming ping test...")
ping_result = test.results.ping

print("Found the following results:")
print(f"Download Speed: {download_result / 1024 / 1024:.2f}Mbps")
print(f"Upload Speed: {upload_result / 1024 / 1024:.2f}Mbps")
print(f"Ping: {ping_result:.2f}ms")
