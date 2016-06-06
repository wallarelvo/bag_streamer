
import roshelper


n = roshelper.Node("bag_streamer", anonymous=False)


@n.entry_point()
class Republisher(object):

    def __init__(self):
        self.message_queue = list()

    def add_message(self, msg):
        self.message_queue.append(msg)
        return self

    def publish(self, msg):
        pass

    @n.main_loop(frequency=100)
    def run(self):
        mq = self.message_queue[:]
        for msg in mq:
            self.publish(msg)
