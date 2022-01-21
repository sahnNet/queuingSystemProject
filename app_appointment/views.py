from django.shortcuts import redirect
from django.urls import reverse

from app_hospital.models import Doctor
from .models import Appointment
from datetime import date
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def get_visiting_hours(turn_number: int, start_hours: int):
    time = start_hours * 60 + (turn_number - 1) * 10
    hours = int(time / 60)
    minutes = time % 60
    if hours < 10:
        hours = f'0{hours}'
    else:
        hours = f'{hours}'
    if minutes < 10:
        minutes = f'0{minutes}'
    else:
        minutes = f'{minutes}'

    return f'{hours}:{minutes}'


def set_appointment_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect((reverse('loginView')))

    MAX_TURN_NUMBER = 24
    doctor = Doctor.objects.filter(id=request.POST['d']).first()
    shift_en = request.POST['shift']
    user = request.user

    if shift_en == "morning":
        shift_fa = "صبح"
        start_hours = 8
    elif shift_en == "evening":
        shift_fa = "عصر"
        start_hours = 14
    else:
        shift_fa = "شب"
        start_hours = 20

    # Date tomorrow
    today = date.today()
    try:
        tomorrow = date(today.year, today.month, today.day + 1)
    except:
        if today.month < 12:
            tomorrow = date(today.year, today.month + 1, 1)
        else:
            tomorrow = date(today.year + 1, 1, 1)
    # /Date tomorrow

    if Appointment.objects.filter(user_id=user.id, date=tomorrow).exists():
        return redirect((reverse('homeView')))

    turn_number = len(Appointment.objects.filter(doctor_id=doctor.id, shift_en=shift_en, date=tomorrow)) + 1
    if turn_number > MAX_TURN_NUMBER:
        return redirect((reverse('homeView')))

    visiting_hours = get_visiting_hours(turn_number, start_hours)
    # Creat an object of Appointment
    Appointment.objects.create(user=user, doctor=doctor, turn_number=turn_number, shift_en=shift_en, shift_fa=shift_fa,
                               visiting_hours=visiting_hours, date=tomorrow)
    # /Creat an object of Appointment
    return redirect((reverse('accountView')))


def some_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect((reverse('loginView')))
    appointment = Appointment.objects.filter(id=kwargs['a']).first()
    if appointment.user.id != request.user.id:
        return redirect((reverse('homeView')))

    x = 40
    y = 700

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(x, y,
                 f"{appointment.user.first_name} {appointment.user.last_name} patient's appointment with national code {appointment.user.username} for {appointment.doctor.full_name_en}")
    p.drawString(x, y - 50, f'{appointment.doctor.specialty.name_en} specialty')
    p.drawString(x, y - 100, f'Turn number {appointment.turn_number}')
    p.drawString(x, y - 150, f'Shift {appointment.shift_en}')
    p.drawString(x, y - 200, f'Date of turn {appointment.get_date_en()}')
    p.drawString(x, y - 250, f'Visiting time {appointment.visiting_hours}')

    # Close the PDF object cleanly, and we're done.
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='appointment.pdf')
