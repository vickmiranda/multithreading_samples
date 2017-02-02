import threading
import time

exitFlag = 0

class MyThread(threading.Thread):
  def __init__(self, threadId, name, delay):
    threading.Thread.__init__(self)
    print 'new thread init %s' % (name)
    self.threadId = threadId
    self.name = name
    self.delay = delay

  def run(self):
    print 'starting %s with delay %0.2f\n' % (self.name, self.delay)
    print_time(self.name, self.delay, 5)
    print 'exiting method1' + self.name
    log_info(self.name, "loop")
    print 'exiting method2'


def print_time(threadName, delay, counter):
  while counter:
    if exitFlag:
      threadName.exit()
    time.sleep(delay)
    print "%s: %s" % (threadName, time.ctime(time.time()))
    counter -= 1


def log_info(threadName, message):
  for i in range(10):
    message = 'message=>{}'.format(i)
    time.sleep(0.5)
    print 'my Name %s and %s=>' % (threadName, message)
  # threadName.exit()


# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 1)

# Start new Threads
thread1.start()
thread2.start()



print "Exiting Main Thread"