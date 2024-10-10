from .services.email_service import EmailService
from config.celery import app


@app.task
def send_activation_code_celery(username, email, activation_code):
    EmailService.send_activation_code(username, email, activation_code)


@app.task
def send_password_celery(username, email, activation_code):
    EmailService.send_password_recovery(username, email, activation_code)
