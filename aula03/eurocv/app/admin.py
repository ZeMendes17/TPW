from django.contrib import admin
from app.models import Cv, Person, Address, Email, Contact, Position, Activity, Employer

# Register your models here.
admin.site.register(Cv)
admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Email)
admin.site.register(Contact)
admin.site.register(Position)
admin.site.register(Activity)
admin.site.register(Employer)