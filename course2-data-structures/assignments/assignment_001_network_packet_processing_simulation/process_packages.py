#!/usr/bin/python3

from sys import stdin

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

    def __repr__(self):
        return ('[' + str(self.arrival_time) + ', ' +
            str(self.process_time) + ']')

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

    def __repr__(self):
        return '[' + str(self.dropped) + ', ' + str(self.start_time) + ']'

class Buffer:
    """
    You are given a series of incoming network packets, and your task is to
    simulate their processing. Packets arrive in some order. For each packet
    number i, you know the time when it arrived Ai and the time it takes the
    processor to process it Pi (both in milliseconds). There is only one
    processor, and it processes the incoming packets in the order of their
    arrival. If the processor started to process some packet, it doesn’t
    interrupt or stop until it finishes the processing of this packet, and
    the processing of packet i takes exactly Pi milliseconds.

    The computer processing the packets has a network buffer of fixed size S.
    When packets arrive, they are stored in the buffer before being processed.
    However, if the buffer is full when a packet arrives (there are S packets
    which have arrived before this packet, and the computer hasn’t finished
    processing any of them), it is dropped and won’t be processed at all. If
    several packets arrive at the same time, they are first all stored in the
    buffer (some of them may be dropped because of that — those which are
    described later in the input). The computer processes the packets in the
    order of their arrival, and it starts processing the next available packet
    from the buffer as soon as it finishes processing the previous one. If at
    some point the computer is not busy, and there are no packets in the
    buffer, the computer just waits for the next packet to arrive. Note that
    a packet leaves the buffer and frees the space in the buffer as soon as
    the computer finishes processing it.

    One possible solution is to store in the list or queue finish_times
    the times when the computer will finish processing the packets which
    are currently stored in the network buffer, in increasing order. When
    a new packet arrives, you will first need to pop from the front of
    finish_times all the packets which are already processed by the time
    new packet arrives. Then you try to add the finish time for the new
    packet to finish_times. If the buffer is full (there are already S
    (the buffer's size) finish times in finish_times), the packet is
    dropped. Otherwise, its processing finish time is added to
    finish_times.

    If finish_times is empty when a new packet arrives, computer will
    start processing the new packet immediately as soon as it arrives.
    Otherwise, computer will start processing the new packet as soon as
    it finishes to process the last of the packets currently in
    finish_times (here is when you need to access the last element of
    finish_times to determine when the computer will start to process
    the new packet). You will also need to compute the processing finish
    time by adding Pi to the processing start time and push it to the
    back of finish time.
    """

    def __init__(self, size):
        self.size = size
        self.finish_times = []

    def process(self, request):
        index = 0
        for i, time in enumerate(self.finish_times):
            if time <= request.arrival_time:
                index += 1
            elif time > request.arrival_time:
                break
        if index != 0:
            self.finish_times = self.finish_times[index:]

        if len(self.finish_times) == self.size:
            return Response(True, -1)
        else:
            start_time = -1
            if len(self.finish_times) == 0:
                start_time = request.arrival_time
            else:
                start_time = self.finish_times[-1]

            self.finish_times.append(start_time + request.process_time)

            return Response(False, start_time)

def _check_input(size, requests):
    assert(1 <= size)
    assert(0 <= len(requests))

    previous_arrival_time = 0
    for r in requests:
        assert(0 <= r.arrival_time)
        assert(0 <= r.process_time)

        assert(previous_arrival_time <= r.arrival_time)
        previous_arrival_time = r.arrival_time

def read_requests(count, stream):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int,
            stream.readline().strip().split())
        requests.append(Request(arrival_time, process_time))

    return requests

def process_requests(requests, buffer):
    _check_input(buffer.size, requests)

    responses = []
    for request in requests:
        responses.append(buffer.process(request))

    return responses

def print_responses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = read_requests(count, stdin)

    buffer = Buffer(size)
    responses = process_requests(requests, buffer)

    print_responses(responses)
