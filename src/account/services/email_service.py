from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailService:
    @staticmethod
    def send_email(subject, message, from_email, recipient_list, html_message=None):
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            html_message=html_message,
            fail_silently=False,
        )

    @staticmethod
    def send_activation_code(username, email, activation_code):
        context = {
            "text_detail": "Thank you for registering",
            "username": username,
            "email": email,
            "domain": "http://127.0.0.1",
            "activation_code": activation_code,
        }
        message_html = render_to_string("email_url.html", context)
        message = strip_tags(message_html)
        EmailService.send_email(
            "Activation account",
            message,
            "admin@gmail.com",
            [email],
            html_message=message_html,
        )

    @staticmethod
    def send_password_recovery(username, email, activation_code):
        context = {
            "text_detail": "Password recovery",
            "username": username,
            "email": email,
            "forgot_password_code": activation_code,
        }
        message_html = render_to_string("lose_password.html", context)
        message = strip_tags(message_html)
        EmailService.send_email(
            "Password recovery",
            message,
            "admin@gmail.com",
            [email],
            html_message=message_html,
        )
