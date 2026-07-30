import subprocess
import time

import sys

#commands = [

#    ["py", "-m", "uvicorn", "api.app:app", "--reload"],

#    ["py", "-m", "bot.bot"],

#    ["py", "-m", "services.parser_service"],

#    ["py", "-m", "services.ai_service"],

#    ["py", "-m", "services.notification_service"]

#]

commands = [

    [
        sys.executable,
        "-m",
        "uvicorn",
        "api.app:app",
        "--host",
        "0.0.0.0",
        "--port",
        "10000"
    ],

    [
        sys.executable,
        "-m",
        "bot.bot"
    ],

    [
        sys.executable,
        "-m",
        "services.parser_service"
    ],

    [
        sys.executable,
        "-m",
        "services.ai_service"
    ],

    [
        sys.executable,
        "-m",
        "services.notification_service"
    ],

    [
        sys.executable, 
        "-m", 
        "services.keepalive_service"
    ]


]

processes = []

for command in commands:

    processes.append(
        subprocess.Popen(command)
    )

print("Все сервисы запущены.")


try:

    while True:
        time.sleep(1)

except KeyboardInterrupt:

    for process in processes:
        process.terminate()