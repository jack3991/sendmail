import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header


class SendMail():
    def __init__(self):
        with open(r'/home/jack/桌面/first_project/content', 'rb') as fp:
            self.s = fp.read()

    def sendnail_3(self,mail):
        # Define these once; use them twice!
        strFrom = 'jack@globalsocial.net'
        strTo = mail

        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'test message'
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        #msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        # msgText = MIMEText('This is the alternative plain text message.')
        # msgAlternative.attach(msgText)

        # We reference the image in the IMG SRC attribute by the ID we give it below
        msgText = MIMEText(self.s.decode(), 'html')
        msgAlternative.attach(msgText)

        # This example assumes the image is in the current directory
        with open(r'/home/jack/桌面/news/TVB.png', 'rb') as fp1:
            msgImage1 = MIMEImage(fp1.read())

        with open(r'/home/jack/桌面/news/safe_image.jpg', 'rb') as fp2:
            msgImage2 = MIMEImage(fp2.read())

        # Define the image's ID as referenced above
        msgImage1.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage1)

        msgImage2.add_header('Content-ID', '<image2>')
        msgRoot.attach(msgImage2)

        # Send the email (this example assumes SMTP authentication is required)
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # smtp.connect('smtp.example.com')
        smtp.login('jack@globalsocial.net', 'jack0953563780')
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        smtp.quit()

        return 'send mail ready'
