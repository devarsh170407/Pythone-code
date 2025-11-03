import smtplib
from email.mime.text import MIMEText

# Your email credentials
sender_email = "devarsh.bhatt128171@marwadiuniversity.ac.in"
password = "Yokm@652"

# List of recipient emails
recipients = [
    "devarshbhatt1747@gmail.com"
    "kenil.parekh131653@marwadiuniversity.ac.in"
]


# Email content
subject = "Hello from Python!"
body = "Hi, this is a test email sent from Python."

# Set up the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

# Send mail to all recipients
for email in recipients:
    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject

    server.sendmail(sender_email, email, msg.as_string())
    print(f"✅ Email sent to {email}")

server.quit()
print("🎉 All emails sent successfully!")
