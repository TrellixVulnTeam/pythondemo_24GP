import sched, time
def print_time(msg = 'default'):
    print("当前时间", time.time(), msg)

s = sched.scheduler(time.time, time.sleep)
print(time.time())
s.enter(5, 1, print_time, argument = ('延迟五秒，优先级1',))
s.enter(3, 4, print_time, argument = ('延迟3秒，优先级4',))
s.enter(3, 3, print_time, argument = ('延迟3秒，优先级3',))
s.run()
print(time.time())