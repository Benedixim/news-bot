import subprocess
import time

commands = [

    ["py", "-m", "uvicorn", "api.app:app", "--reload"],

    ["py", "-m", "bot.bot"],

    ["py", "-m", "services.parser_service"],

    ["py", "-m", "services.ai_service"],

    ["py", "-m", "services.notification_service"]

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