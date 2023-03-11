import time


def RunTime():
    """
    运行时长
    """
    start = time.time()
    while True:
        time.sleep(1)
        elapsed = time.time() - start
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        print(f"\r运行时间: {hours:02d}:{minutes:02d}:{seconds:02d}", end="")


if __name__ == "__main__":
    RunTime()
