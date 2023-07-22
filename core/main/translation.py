from .models import *
from modeltranslation.translator import register, TranslationOptions

@register(Header_Sidebar)
class Header_SidebarTranslationOptions(TranslationOptions):
    fields = ('open_times', 'language1', 'language2', 'path1', 'path2', 'path3', 'path4', 'path5', 'path6', 'path7', 'path8', 'btn_name',)

@register(Homepage)
class HomepageTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'btn_name1', 'btn_name2',)

@register(Title)
class TitleTranslationOptions(TranslationOptions):
    fields = ('title1', 'subtitle1', 'title2', 'subtitle2', 'title3', 'subtitle3', 'title4', 
              'subtitle4', 'title5', 'subtitle5', 'title6', 'subtitle6', 'title7', 'subtitle7', 'title8', 'subtitle8', )
    
@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('category',)
    
@register(MenuContent)
class MenuContentTranslationOptions(TranslationOptions):
    fields = ('name', 'recipe',)
    
@register(Special)
class SpecialTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(EventSlide)
class EventSlideTranslationOptions(TranslationOptions):
    fields = ('title',)
    
@register(ReservationContent)
class ReservationContentTranslationOptions(TranslationOptions):
    fields = ('placeholder1', 'placeholder2', 'placeholder3', 'placeholder4', 'placeholder5', 'btn_name',)
    
@register(Chef)
class ChefTranslationOptions(TranslationOptions):
    fields = ('name', 'profession',)
    
@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('placeholder1', 'placeholder2', 'placeholder3', 'placeholder4', 'btn_name',)
    
@register(ContactInfo)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ('title',)