import aiosmtpd
from email.message import EmailMessage

from celery import Celery
from config import SMTP_USER,SMTP_PASSWORD

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')

def get_email_template_dashboard(username:str):
    email = EmailMessage()
    email["Subject"] ="Trade report dashbort "
    email["From"] = SMTP_USER
    email["To"] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://avatars.dzeninfra.ru/get-zen_doc/1900274/pub_64c11c71c146cc22fb193cc7_64c11c9ecef63a68ef64b88e/scale_1200'
        '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
        '-mobile-free-vector.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report_dashboard(username:str):
    email = get_email_template_dashboard(username)
    with aiosmtpd.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)