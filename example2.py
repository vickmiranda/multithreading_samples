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
    task = MyTasks(self.name, self.delay, 5)
    task.print_time()
    print 'exiting method1' + self.name
    task.log_info('my log')
    print 'exiting method2' + self.name


class MyTasks(object):
  def __init__(self, threadName, delay, counter):
    self.threadName =threadName
    self.delay = delay
    self.counter = counter

  def print_time(self):
    while self.counter:
      if exitFlag:
        self.threadName.exit()
      time.sleep(self.delay)
      print "%s: %s" % (self.threadName, time.ctime(time.time()))
      self.counter -= 1

  def log_info(self, message):
    for i in range(10):
      msg = '{}=>{}'.format(message, i)
      time.sleep(0.5)
      print 'my Name %s and %s=>' % (self.threadName, msg)


# Create new threads
thread1 = MyThread(1, "Thread-1", 0.5)
thread2 = MyThread(2, "Thread-2", 1)

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"
