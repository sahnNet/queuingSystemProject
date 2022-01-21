from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from app_hospital.models import Doctor, Province, City, Hospital


def header_view(request, *args, **kwargs):
    # Header information's
    context = {
        'pant': _('Pant'),
        'home': _('Home'),
        'honors': _('Honors'),
        'services': _('Services'),
        'gallery': _('Gallery'),
        'physicians': _('Physicians'),
        'contactus': _('Contact us'),
        'account': _('Account'),
        'exit': _('Exit'),
        'login': _('Log in'),
        'register': _('Register'),
        'go': _('Go'),
    }
    return render(request, 'shared/Header.html', context)


def footer_view(request, *args, **kwargs):
    # Footer information's
    context = {
        'titleDescription': _('Schedule in the shortest time'),
        # 'description': _('Footer description'),
        'pages': _('Pages'),
        'home': _('Home'),
        'services': _('Services'),
        'gallery': _('Gallery'),
        'physicians': _('Physicians'),
        'contactus': _('Contact us'),
        'help': _('You want help?'),
        'support': _('Support'),
        'medicalAdvice': _('Medical advice'),
        'announcements': _('Announcements'),
        'aboutUs': _('About us'),
        'aboutUsDescriptions': _('Developers Amir Hossein Hekmat and Seyed Ali Hosseini Nasab'),
    }
    return render(request, 'shared/Footer.html', context)


def home_view(request, *args, **kwargs):
    provinces_list = Province.objects.all()
    cities_list = City.objects.all()
    hospitals_list = Hospital.objects.all()
    doctors_list = Doctor.objects.all()[:10]

    # Home page information's
    context = {
        'navbarTitle': _('Hospital appointments'),
        'navbarText': _('Scheduling offices / treatment centers / hospitals in the country online'),
        'navbarDescriptions': _('''
        In today's world we have learned to search the Internet for everything. 
        It's very common to choose services, especially medical services. 
        So, it is better to provide hospitalization for doctors and medical centers so that people can choose the doctor 
        they want more easily and with more information and make an appointment. Accordingly, our site provides online 
        appointments along with other appointment methods to the audience so that the managers of medical centers and 
        doctors can offer their services to patients in the best way.
        '''),
        'searchTitle': _('Search easily and quickly'),
        'search': _('Search'),
        'honors': _('Honors'),
        'topBadge': _('Top badge'),
        'healthBadge': _('Health badge'),
        'qualitativelySelected': _('Qualitatively selected'),
        'qualityService': _('The highest quality service'),
        'qualityServiceDescriptions': _('Easy scheduling in all of Iran'),
        'services': _('Services'),
        'serviceDescriptions': _('Part of our services'),
        'hygiene': _('Hygiene'),
        'experiencedDoctors': _('Experienced doctors'),
        'smartEquipment': _('Smart equipment'),
        'gallery': _('Gallery'),
        'all': _('All'),
        'partOne': _('Part One'),
        'partTwo': _('Part Two'),
        'partThree': _('Part Three'),
        'physicians': _('Physicians'),
        'getAppointment': _('Get an appointment'),
        'provinces': _('Provinces'),
        'cities': _('Cities'),
        'hospitals': _('Hospitals'),
        # Information doctors
        'provincesList': provinces_list,
        'citiesList': cities_list,
        'hospitalsList': hospitals_list,
        'doctorsList': doctors_list,
    }
    return render(request, 'index.html', context)
