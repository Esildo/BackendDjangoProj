import datetime
def application(environ, start_response):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = f"Hello, World! The current time is {current_time}\n".encode('utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
