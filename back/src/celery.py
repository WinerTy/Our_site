from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from celery import Celery
from jinja2 import Environment, FileSystemLoader

from .config.config import settings


class CeleryService:
    def __init__(
        self,
        broker_url,
        backend_url,
        smtp_server,
        smtp_port,
        smtp_username,
        smtp_password,
    ):
        self.env = Environment(loader=FileSystemLoader("templates/email"))
        self.celery_app = Celery(
            "tasks",
            broker=broker_url,
            backend=backend_url,
        )
        self.celery_app.conf.update(
            task_serializer="json",
            accept_content=["json"],
            result_serializer="json",
            timezone="UTC",
            enable_utc=True,
        )
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def send_email(self, to_email, subject, template_name, context):
        template = self.env.get_template(template_name)
        html_content = template.render(context)

        msg = MIMEMultipart()
        msg["From"] = self.smtp_username
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(html_content, "html"))

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.smtp_username, to_email, msg.as_string())

    def create_task(self, task_name, task_func):
        setattr(self.celery_app, task_name, self.celery_app.task(task_func))


celery_service = CeleryService(
    broker_url=settings.CELERY_BROKER_URL,
    backend_url=settings.CELERY_RESULT_BACKEND,
    smtp_server=settings.SMTP_HOST,
    smtp_port=settings.SMTP_PORT,
    smtp_username=settings.SMTP_USER,
    smtp_password=settings.SMTP_PASSWORD,
)

celery_service.create_task("send_email", celery_service.send_email)
