from django.contrib import admin

# Register your models here.
from .models import *
from modeltranslation.admin import TranslationAdmin

class Header_SidebarAdmin(TranslationAdmin): 
    pass

class HomepageAdmin(TranslationAdmin):
    pass

class TitleAdmin(TranslationAdmin):
    pass

class MenuAdmin(TranslationAdmin):
    pass

class MenuContentAdmin(TranslationAdmin):
    pass

class SpecialContentAdmin(TranslationAdmin):
    pass

class EventSlideAdmin(TranslationAdmin):
    pass

class ReservationContentAdmin(TranslationAdmin):
    pass

class ChefAdmin(TranslationAdmin):
    pass

class ContAdmin(TranslationAdmin):
    pass

class ContInfo(TranslationAdmin):
    pass

admin.site.register(Header_Sidebar)
admin.site.register(Homepage)
admin.site.register(About)
admin.site.register(AboutContent)
admin.site.register(Title)
admin.site.register(Reason)
admin.site.register(Menu)
admin.site.register(MenuContent)
admin.site.register(Special)
admin.site.register(Event)
admin.site.register(EventSlide)
admin.site.register(ReservationContent)
admin.site.register(Reservation)
admin.site.register(Gallery)
admin.site.register(Chef)
admin.site.register(Contact)
admin.site.register(ContactInfo)
admin.site.register(ContactMessage)
admin.site.register(Subscribe)