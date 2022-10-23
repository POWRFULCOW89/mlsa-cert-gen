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
COLLEGE_EMAIL_DOMAIN = "ucc.mx"

"""
Dummy array when using the --dry-run flag.
"""
TEST_ATTENDEES = [["Your Name", "email@email.email"]]

"""
Event name used in the certificate and email, without quotes.
"""
EVENT_NAME = "Creación de aplicaciones web en la nube"

"""
Name of the MLSA student that organized the event.
"""
HOST_NAME = "Diego Melo"

"""
Subject of the email sent to each attendee.
"""
EMAIL_SUBJECT = 'MLSA - Certificado de participación'

"""
Body of the email sent to each attendee.
"""
EMAIL_BODY = f"""Excelente día:

Hago entrega del certificado de participación en el evento "Creación de aplicaciones web en la nube" el jueves 20 de octubre a las 9 de la mañana. Muchas gracias por acompañarnos durante la hora, esperando verte en el siguiente ;)

Saludos,

{HOST_NAME}
Alpha Microsoft Learn Student Ambassador
+52 229 242 5177
GitHub: POWRFULCOW89
LinkedIn: diego-melo-mx

"""
