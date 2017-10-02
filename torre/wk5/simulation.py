from Request import Request
from Server import Server
from Queue import Queue
import sys

def main(in_file) :
    #for i in range(24):
        simulateOneServer(24, 5,in_file)

def simulateOneServer(num_seconds, file_per_minute,in_file):
    server = Server(file_per_minute)
    print_queue = Queue()
    waiting_times = []

    with open(in_file) as lines:
        for line in lines:
            data = line.split(',')
            request = Request(int(data[0].strip()), data[1],int(data[2].strip()))
            print_queue.enqueue(request)
            #print(str(request.wait_time()))
    #print (data)
    for current_second in range(num_seconds):

        if (not server.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time())
            server.start_next(next_task)

        server.tick()
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." %(average_wait, print_queue.size()))


if __name__ == "__main__": main(sys.argv[1])

