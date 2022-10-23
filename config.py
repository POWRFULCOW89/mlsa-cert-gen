"""
The directory where the certificates are stored.
"""
CERTIFICATES_DIRECTORY = "certificates"

"""
The template file for the certificates.
"""
TEMPLATE_FILE = "./template.docx"

"""
The domain used for sending emails when using a text file.
"""
COLLEGE_EMAIL_DOMAIN = "college.com"

"""
Dummy array when using the --dry-run flag.
"""
TEST_ATTENDEES = [["Your Name", "email@domain.com"]]

"""
Event name used in the certificate and email, without quotes.
"""
EVENT_NAME = "My Event Name"

"""
Name of the MLSA student that organized the event.
"""
HOST_NAME = "John Doe"

"""
Subject of the email sent to each attendee.
"""
EMAIL_SUBJECT = 'MLSA - Attendance certificate'

"""
Body of the email sent to each attendee.
"""
EMAIL_BODY = f"""Excelent day:

Find attached your participation certificate from the event {EVENT_NAME} on October 20th. Thanks again for joining us during the event, hoping to see you again in the next one! ;)

Greetings,

{HOST_NAME}
Alpha Microsoft Learn Student Ambassador
+52 123 456 7890
GitHub: john-doe
LinkedIn: john-doe

"""
