import platform
import psutil
print(f"Sistema: {platform.system()}")
print(f"Sistema: {platform.release()}")

for i in range(10):
  print(f"\rUso de CPU: {psutil.cpu_percent(interval=1)}%", end="", flush=True)