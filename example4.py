import Queue
import threading
import time


exitFlag = 0


class MyThread(threading.Thread):
  def __init__(self, threadId, name, queue):
    threading.Thread.__init__(self)
    self.threadId = threadId
    self.name = name
    self.queue = queue

  def run(self):
    print 'starting ' + self.name
    process_data(self.name, self.queue)
    print 'exiting ' + self.name


class DummyClass(object):
  def __init__(self):
    print 'dummy class'

  def do_some(self):
    print 'do something here'


def process_data(threadName, q):
  while not exitFlag:
    queueLock.acquire()
    if not workQueue.empty():
      data = q.get()
      if type(data) == type(DummyClass):
        dummy = data()
        dummy.do_some()
      queueLock.release()
      print "%s processing %s" % (threadName, data)
    else:
      queueLock.release()
    time.sleep(1)


threadList = ["thread-1", "thread-2", "thread-3"]
nameList = [1, 3, 4, 2, 10, "Eleven", "Fourteen", DummyClass]
queueLock = threading.Lock()
workQueue = Queue.Queue(len(nameList))
threads = []
threadId = 1


# Create new threads
for tName in threadList:
  thread = MyThread(threadId, tName, workQueue)
  thread.start()
  threads.append(thread)
  threadId += 1


# Fill the queue
queueLock.acquire()
for word in nameList:
  workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
  pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
  t.join()
print "Exiting Main Thread"



