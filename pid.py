import psutil

def get_pid(name):
    res = []
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if str.upper(name) in p.name() or str.lower(name) in p.name():
            res.append(pid)

    return res
