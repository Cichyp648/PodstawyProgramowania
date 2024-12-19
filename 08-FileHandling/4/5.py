# Get email data
import emails

with open('email.txt', 'r') as file:
    data = file.read()

sender = str(emails.email_sender(data))[2:-2]
recipient = str(emails.email_recipient(data))[2:-2]
subject = str(emails.email_subject(data))[2:-2]
body = str(emails.email_body(data))[2:-2]

body = body.split(r'\n')

print('Email sender: ', sender)
print('Email recipient: ', recipient)
print('Email subject: ', subject)
print('Email body: ')
for line in body:
    print(line)
