import time


class TooSoonError(Exception): pass


def once_per_minute(f):
    most_recent = 0
    pause_time = 60

    def inside(*args, **kwargs):
        nonlocal most_recent
        current_time = time.time()
        if current_time - most_recent < pause_time:
            wait_until = most_recent + pause_time
            wait_time = wait_until - current_time
            raise TooSoonError("Wait another {} seconds".format(wait_time))
        most_recent = current_time
        return f(*args, **kwargs)
    return inside

@once_per_minute
def hello(name):
    return "Hello, {}".format(name)

for i in range(30):
    print(i)
    try:
        time.sleep(3)
        print(hello("attempt {}".format(i)))
    except TooSoonError as e:
        print("Too soon: {}".format(e))

