from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(44)
queue.popleft()
print(queue)

# Problem: Printer Job Queue
# You are building a printer system that handles print jobs in the order they are received.
# Requirements:
# Users can send documents to the printer → add them to the queue.
# The printer prints the first document in the queue → remove it from the front.
# Always show the current queue after each operation

printer_queue = deque([])

def send_document(doc):
    printer_queue.append(doc)
    print("Queque",list(printer_queue))

def print_document():
    if printer_queue:
        doc = printer_queue.popleft()
        print("printing",doc)
        print("Queue:", list(printer_queue))

    else:
        print("No documents to print.")




send_document("Document1")
send_document("Document2")
print_document()