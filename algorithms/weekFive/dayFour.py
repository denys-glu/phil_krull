# Circular Queues
# ------------------------------------------------------------------------
# When Queue’s tail or head approaches ‘size’, wrap around to [0] and continue. We cannot let tail and head meet – one can’t “lap” the other. Instead, enqueue(val) should fail: Queue is full. Ditto dequeue() if Queue is empty. Constructor requires a size argument. Starting there, let’s create a circular queue implementation!

def CirQueue():
    def __init__(self, cap):
        self.head = 0
        self.tail = 0
        self.capacity = cap
        self.data = [None]*cap

# Enqueue
# ------------------------------------------------------------------------
# Create enqueue(val) that adds val to our circular queue. Return false on fail. Wrap if needed!

# Front
# ------------------------------------------------------------------------
# Return (not remove) the queue’s front value.

# Is Empty
# ------------------------------------------------------------------------
# Return whether queue is empty.

# Is Full
# ------------------------------------------------------------------------
# Return whether queue is full.

# Dequeue
# ------------------------------------------------------------------------
# Create cirQueue method dequeue() that removes and returns the front value. Return null on fail.

# Contains
# ------------------------------------------------------------------------
# Return whether given val is within the queue.

# Size
# ------------------------------------------------------------------------
# Return number of queued vals (not capacity).