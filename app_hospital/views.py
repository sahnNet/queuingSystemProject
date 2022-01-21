from datetime import date
from jalali_date import date2jalali
from django.shortcuts import render
from .models import Doctor, Hospital
from django.utils.translation import gettext_lazy as _


def set_variable(variable):
    if variable is None:
        result = 0
    else:
        result = int(variable)
    return result


def appointment_view(request, *args, **kwargs):
    # Id's
    if request.GET.get('pc') is not None:
        province_id, city_id = request.GET.get('pc')
        province_id = int(province_id)
        city_id = int(city_id)
    else:
        province_id = set_variable(request.GET.get('p'))
        city_id = set_variable(request.GET.get('c'))
    hospital_id = set_variable(request.GET.get('h'))
    specialty_id = set_variable(request.GET.get('s'))
    doctor_id = set_variable(request.GET.get('d'))
    doctors_list = []
    doctors_select = []
    # /Id's

    # Date tomorrow
    today = date.today()
    try:
        tomorrow = date(today.year, today.month, today.day + 1)
    except:
        if today.month < 12:
            tomorrow = date(today.year, today.month + 1, 1)
        else:
            tomorrow = date(today.year + 1, 1, 1)

    tomorrow_en = tomorrow.strftime('%Y-%m-%d')
    tomorrow_fa = date2jalali(tomorrow).strftime('%Y-%m-%d')
    # /Date tomorrow

    # Doctors list
    if city_id == 0:
        if province_id == 0:
            hospitals_list = [a for a in Hospital.objects.all()]
        else:
            hospitals_list = [a for a in Hospital.objects.filter(city__province_id=province_id)]
    else:
        hospitals_list = [a for a in Hospital.objects.filter(city_id=city_id)]

    for h in hospitals_list:
        doctors_list += [a for a in Doctor.objects.filter(hospital_id=h.id)]
    doctors_list = list(set(doctors_list))
    # /Doctors list

    # Specialties list
    specialties_list = [a.specialty for a in doctors_list]
    specialties_list = list(set(specialties_list))
    # /Specialties list

    # Doctors select
    if doctor_id == 0:
        for d in doctors_list:
            if specialty_id == 0:
                if hospital_id == 0:
                    doctors_select.append(d)
                else:
                    if d.hospital.id == hospital_id:
                        doctors_select.append(d)
            else:
                if hospital_id == 0:
                    if d.specialty.id == specialty_id:
                        doctors_select.append(d)
                else:
                    if d.specialty.id == specialty_id and d.hospital.id == hospital_id:
                        doctors_select.append(d)
    else:
        a = Doctor.objects.filter(id=doctor_id).first()
        if a is not None:
            doctors_select = [a]
    # /Doctors select

    # Appointment page information's
    context = {
        'pc': f'{province_id}{city_id}',
        'h': hospital_id,
        's': specialty_id,
        'd': doctor_id,
        'hospitalsList': hospitals_list,
        'specialtiesList': specialties_list,
        'doctorsList': doctors_list,
        'doctorsSelect': doctors_select,
        'tomorrowEn': tomorrow_en,
        'tomorrowFa': tomorrow_fa,
        'hospitals': _('Hospitals'),
        'specialties': _('Specialties'),
        'doctors': _('Doctors'),
        'medicalCenter': _('Medical center'),
        'doctor': _('Doctor'),
        'borderText': _('Simply find the doctor, clinic, treatment center or hospital you are looking for'),
        'morningShift': _('Morning shift'),
        'eveningShift': _('Evening shift'),
        'nightShift': _('Night shift'),
        'readyToBook': _('Ready to book'),
    }

    return render(request, 'Apointment.html', context)


def doctor_page_view(request, *args, **kwargs):
    doctor = Doctor.objects.filter(id=kwargs['d']).first()
    shift = request.GET.get('shift')

    if shift is None:
        if doctor.is_morning_shift:
            shift = 'morning'
        elif doctor.is_evening_shift:
            shift = 'evening'
        else:
            shift = 'night'

    # Date tomorrow
    today = date.today()
    try:
        tomorrow = date(today.year, today.month, today.day + 1)
    except:
        if today.month < 12:
            tomorrow = date(today.year, today.month + 1, 1)
        else:
            tomorrow = date(today.year + 1, 1, 1)

    tomorrow_en = tomorrow.strftime('%A %d %B %Y')
    tomorrow_fa = date2jalali(tomorrow).strftime('%A %d %B %Y')
    # /Date tomorrow

    # Doctor page information's
    context = {
        'doctor': doctor,
        'tomorrowEn': tomorrow_en,
        'tomorrowFa': tomorrow_fa,
        'shift': shift,
        'specialties': _('Specialties'),
        'EducationAcademy': _('Education / Academy'),
        'honorsAndAwards': _('Honors and awards'),
        'physicianContactInformation': _('Physician contact information'),
        'yourPeaceAndHealthIsOurMainGoal': _('Your peace and health is our main goal'),
        'morning': _('Morning'),
        'evening': _('Evening'),
        'night': _('Night'),
        'ok': _('OK'),
        'cancel': _('Cancel'),
        'introductionOfOffices': _('Introduction of offices'),
        'hospital': _('Hospital'),
        'province': _('Province'),
        'city': _('City'),
        'telephoneNumber': _('Telephone number'),
        'ShowOnTheMap': _('Show on the map'),
    }

    return render(request, 'TheFirstDoctorPage.html', context)
