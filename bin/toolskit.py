
class EmailSender:
    def __init__(self, __email_from, __password):
        self.__email_from = __email_from
        self.__password = __password

    def send_mail(self, rcpt_to, subject, content):
        from email.message import EmailMessage
        import ssl
        import smtplib

        emailMessage = EmailMessage()
        emailMessage['From'] = self.__email_from
        emailMessage['To'] = rcpt_to
        emailMessage['Subject'] = subject
        emailMessage.set_content(content)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail,com', 465, context=context) as smtp:
            smtp.login(self.__email_from, self.__password)
            smtp.sendmail(self.__email_from, rcpt_to, emailMessage.as_string())
