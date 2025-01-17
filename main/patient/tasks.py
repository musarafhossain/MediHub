from django.shortcuts import render
from .models import Patient
from datetime import date, timedelta
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_next_visit_email_notification():
    # Fetch patients with a past visit date
    patients = Patient.objects.filter(visit_date__lt=date.today())
    count = 0

    for patient in patients:
        next_visit_date = patient.visit_date + timedelta(days=patient.next_visit)
        notification_date = next_visit_date - timedelta(days=1)
        if notification_date == date.today():
            # Prepare email content
            subject = 'Doctor Next Visit'
            context = {
                'next_visit': next_visit_date,
                'name': patient.name,
            }
            email_body = render_to_string('doctor/email-template.html', context)

            # Send email
            email = EmailMessage(
                subject=subject,
                body=email_body,
                from_email=settings.EMAIL_HOST_USER,
                to=[patient.email],
            )
            email.content_subtype = "html"  # Specify HTML content

            try:
                email.send()
                count += 1  # Increment count only if email sent successfully
            except Exception as e:
                # Log the error (optional, depending on your logging setup)
                print(f"Failed to send email to {patient.email}: {e}")

    print(count)