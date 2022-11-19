def send_msg(msg_queue, sent_msgs):
    while msg_queue:
        msgs = msg_queue.pop()
        sent_msgs.append(msgs)

msg_queue = ['hello', 'how r u?', 'where r u from?']
sent_msgs = []
q = msg_queue[:]

send_msg(q, sent_msgs)
print(f'messages in the queue: {q}')
print(f'sent msg: {sent_msgs}')