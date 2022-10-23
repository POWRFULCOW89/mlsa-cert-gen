# MLSA Certificate Generator

A tool to generate & distribute event certificates for your attendees!

## Installation

1. Clone the repository

```bash
gh repo clone POWRFULCOW89/mlsa-cert-gen
```

2. Create and activate a virtual environment

```bash
python -m venv env
```

3. Install the dependencies

```bash
pip install requirements.txt
```

## Setup & Usage

You can generate certificates for your attendees by running the script:

```bash
python app.py [--dry-run] [--from-txt]
```

By default, the tool will generate certificates for all the attendees in a file called `attendees.csv` (available from the Teams attendance report) with the following structure:

```csv
1. Summary
Meeting title	Title
Attended participants	10
Start time	21/10/22 12:00:00
End time	21/10/22 03:00:00
Meeting duration	3h 0m 0s
Average attendance time	3h 0m 0s

2. Participants
Name	First join	Last leave	In-meeting duration	Email	Participant ID (UPN)	Role
...

3. In-Meeting activities
Name	Join time	Leave time	Duration	Email	Role
...
```

or from an `attendees.txt` file, with a simpler format for in-person events:

```txt
Full Name 10001
...
```

where the number represents the student ID, used for later sending the certificates via email.

A number of configuration options are available in the [`config.py`](config.py) file, including some path variables and the email template.

After successfully retrieving a list of names and emails from any of the previous sources, the tool will generate a certificate for each attendee and save it in the `certificates` folder by default.

An SMTP server is then used to send the certificates to the attendees via email, with the credentials provided in the `.env` file.

Always verify the output before sending the emails to your attendees using the `--dry-run` flag to avoid spam.

## Todo

- [Email verification](https://gitea.ksol.io/karolyi/py3-validate-email)
- More ways to load attendee data
- Tests (especially for mass email sending)
