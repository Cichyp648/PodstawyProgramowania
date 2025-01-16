import queue

people = queue.Queue() # FIFO

people.put('Michael')
people.put('Charlotte')
people.put('Olivia')

## prints number of elements of the queue
print('Number of queue elements:', people.qsize())

# gets and prints items from the queue
while not people.empty():
    person = people.get()
    print(person)