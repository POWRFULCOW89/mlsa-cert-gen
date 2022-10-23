from generator import *
import sys
import os

if __name__ == "__main__":

    dry_run = "--dry-run" in sys.argv
    from_txt = "--from-txt" in sys.argv

    print(
        f"-- {'(Dry Run) ' if dry_run else ''}MLSA Certificate Generator & Email Sender --")

    # 1. We get all names and emails from the csv report -> ["Name", "email"]
    if dry_run:
        attendees = TEST_ATTENDEES
    if from_txt:
        attendees = get_attendees_from_txt("attendance.txt")
    else:
        attendees = get_attendees_from_csv("attendance.csv")

    print(f"-- Total Attendees: {len(attendees)} --")

    print("-- Email template --")
    print(f"Subject: {EMAIL_SUBJECT}")
    print(f'From: {os.environ["email"]}')
    print(f"Content: \n{indent_text(EMAIL_BODY, 1)}")

    if "n" in input("Do you wish to continue? [y/n]: ").lower():
        exit()

    for attendee in attendees:
        name = attendee[0]
        email = attendee[1]

        # 2. We generate a certificate for each person -> "MLSA - Event Name - Name"
        if not dry_run:
            generate_certificate(name, EVENT_NAME, HOST_NAME)

        print(f"{'(Dry Run) ' if dry_run else '' }Certificate generated: " + name)

    # TODO: a relative path gets sent as part of the file name, so we change dirs
    os.chdir(CERTIFICATES_DIRECTORY)

    for attendee in attendees:
        name = attendee[0]
        email = attendee[1]

        certificate_name = f"MLSA - {EVENT_NAME} - {name}.docx"

        total_sent = 0

        # 3. We send an email to each person with the certificate attached
        try:
            if not dry_run:
                send_email(
                    EMAIL_SUBJECT, os.environ["email"], email, EMAIL_BODY, certificate_name)

            total_sent += 1

            print(
                f"{'(Dry Run) ' if dry_run else '' }Email sent to: {email} | File: {certificate_name}")

        except Exception as e:
            print(f"Couldn't send email to: {name} | Error: {e}")

    print(f"-- Total sent {total_sent} --")
