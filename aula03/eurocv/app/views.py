from django.shortcuts import render
from app.models import Cv, Person, Address, Email, Contact, Position, Activity, Employer


# Create your views here.
def eurocv(request, id_num):
    cv = Cv.objects.get(id=id_num)
    person = Person.objects.get(id=cv.person_id)
    position = Position.objects.get(id=cv.position_id)
    personAddress = Address.objects.get(id=person.address_id)
    personContact = Contact.objects.get(person_id=cv.person_id)
    personEmails = Email.objects.filter(contact_id=personContact.id)
    employer = Employer.objects.get(id=position.employer_id)
    activities = Activity.objects.filter(position_id=position.id)

    context = {
        'cv': cv,
        'person': person,
        'position': position,
        'personAddress': personAddress,
        'personContact': personContact,
        'personEmails': personEmails,
        'employer': employer,
        'activities': activities,
    }
    return render(request, 'eurocv.html', context)
