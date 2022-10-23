
import codecs
from config import *
from docxtpl import DocxTemplate
from dotenv import load_dotenv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from importlib.metadata import PackageNotFoundError
import smtplib
import os

load_dotenv()


def generate_certificate(attendee_name: str, EVENT_NAME: str, host_name: str):
    try:
        params = {'attendee_name': attendee_name,
                  "EVENT_NAME": EVENT_NAME, "host_name": host_name}

        filename = f"MLSA - {EVENT_NAME} - {attendee_name}.docx"
        filepath = f"{CERTIFICATES_DIRECTORY}/{filename}"

        doc = DocxTemplate(TEMPLATE_FILE)
        doc.render(params)
        doc.save(filepath)

        return filename
    except PackageNotFoundError as e:
        print("Couldn't open template file: " + e.msg)
        return None


def get_attendees_from_csv(filename: str):
    skip_lines = 10  # Skips the overview of the meeting
    counter = 0
    attendees = []
    # reader = csv.reader(open('./attendance.csv', encoding="utf-16"),
    #                     delimiter='\t')

    with codecs.open(filename, "r", "utf-16") as f:
        lines = f.readlines()

        for line in lines:

            counter += 1

            # Skipping the first section (overview)
            if counter <= skip_lines:
                continue

            # Skipping the third section (activities)
            if "activities" in line:
                break

            data = line.split("\t")

            # Trimming the last blank row and attendees without email
            if len(data) < 2 or data[4] == "":
                continue

            name = data[0].title().split("(")[0].strip()
            email = data[4]

            attendees.append([name, email])

    return attendees


def get_attendees_from_txt(filename: str):
    attendees = []

    with codecs.open(filename, "r", "utf-8") as f:
        lines = f.readlines()

        for line in lines:
            data = line.split(" ")
            name = " ".join(data[:-1])
            email = f"{data[-1].strip()}@{COLLEGE_EMAIL_DOMAIN}"
            attendees.append([name, email])

    return attendees


def send_email(subject: str, address_from: str, address_to: str, content: str, attachment: str):

    msg = MIMEMultipart()

    msg['Subject'] = subject
    msg['From'] = address_from
    msg['To'] = address_to
    msg.attach(MIMEText(content))

    # attach an image
    with open(attachment, 'rb') as f:

        part = MIMEBase("application", "octet-stream")

        part.set_payload(f.read())

        encoders.encode_base64(part)

        part.add_header("Content-Disposition",
                        "attachment", filename=attachment)

        msg.attach(part)

    email = ""
    password = ""

    try:
        email = os.environ["email"]
        password = os.environ["password"]
    except:
        print("Missing credentials from .env file")
        return

    # Consider using SSL
    # with smtplib.SMTP_SSL('smtp-mail.outlook.com', 465) as server:
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:

        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(email, password)
        server.send_message(msg)
        server.quit()


def indent_text(text: str, indent: int):
    return "\n".join(["  " * indent + line for line in text.splitlines()])
