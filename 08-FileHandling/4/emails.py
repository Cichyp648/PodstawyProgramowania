import re

def email_sender(emailContents):
    pattern = r'^From:\s.+<(.+)>'
    output = re.findall(pattern, emailContents, re.MULTILINE)
    return output

def email_recipient(emailContents):
    pattern = r'^To:\s.+<(.+)>'
    output = re.findall(pattern, emailContents, re.MULTILINE)
    return output

def email_subject(emailContents):
    pattern = r'^Subject:\s(.+)'
    output = re.findall(pattern, emailContents, re.MULTILINE)
    return output

def email_body(emailContents):
    pattern = r'\n\n(.*)$'  # Capture everything after two newlines (end of headers)
    output = re.findall(pattern, emailContents, re.DOTALL)  # DOTALL allows '.' to match newlines
    return output