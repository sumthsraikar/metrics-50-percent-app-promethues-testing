from prometheus_client import start_http_server, Gauge
import time

cpu_usage = Gauge('app_cpu_usage_percent', 'Fake CPU usage percent')

def collect_metrics():
    while True:
        cpu_usage.set(50)
        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    collect_metrics()
