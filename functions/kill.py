import os




def kill():
    pid = os.getpid()
    os.kill(pid, 9)
    return