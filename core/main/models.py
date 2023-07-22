from django.db import models
from django.contrib import admin

# Create your models here.

class Header_Sidebar(models.Model):

    doc_title = models.CharField('Document Title', max_length=50)
    phone_number = models.CharField('Phone Number', max_length=20)
    open_times = models.CharField('Open Times', max_length=50)
    language1 = models.CharField('Language 1', max_length=5)
    language2 = models.CharField('Language 2', max_length=5)
    title = models.CharField('Title', max_length=50)
    path1 = models.CharField('Path 1', max_length=50)
    path2 = models.CharField('Path 2', max_length=50)
    path3 = models.CharField('Path 3', max_length=50)
    path4 = models.CharField('Path 4', max_length=50)
    path5 = models.CharField('Path 5', max_length=50)
    path6 = models.CharField('Path 6', max_length=50)
    path7 = models.CharField('Path 7', max_length=50)
    path8 = models.CharField('Path 8', max_length=50)
    btn_name = models.CharField('Button Name', max_length=50)

    class Meta:

        verbose_name = 'Header_Sidebar'
        verbose_name_plural = 'Header_Sidebar'

class Homepage(models.Model):

    background = models.ImageField('Background')
    title = models.CharField('Title', max_length=50)
    colored_title = models.CharField('Colored Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=70)
    btn_name1 = models.CharField('Button Name 1', max_length=40)
    btn_name2 = models.CharField('Button Name 2', max_length=40)

    class Meta:

        verbose_name = 'Homepage'
        verbose_name_plural = 'Homepage'

class About(models.Model):
    
    background = models.ImageField('Background')
    title = models.CharField('Title', max_length=200)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    img = models.ImageField('Image')

    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class AboutContent(models.Model):

    icon = models.CharField('Icon', max_length=50)
    text = models.TextField('Text')
        
    class Meta:

        verbose_name = 'About Content'
        verbose_name_plural = 'About Content'

class Title(models.Model):

    subtitle1 = models.CharField('Subtitle1', max_length=50)
    title1 = models.CharField('Title 1', max_length=80)
    subtitle2 = models.CharField('Subtitle2', max_length=50)
    title2 = models.CharField('Title 2', max_length=80)
    subtitle3 = models.CharField('Subtitle3', max_length=50)
    title3 = models.CharField('Title 3', max_length=80)
    subtitle4 = models.CharField('Subtitle4', max_length=50)
    title4 = models.CharField('Title 4', max_length=80)
    subtitle5 = models.CharField('Subtitle5', max_length=50)
    title5 = models.CharField('Title 5', max_length=80)
    subtitle6 = models.CharField('Subtitle6', max_length=50)
    title6 = models.CharField('Title 6', max_length=80)
    subtitle7 = models.CharField('Subtitle7', max_length=50)
    title7 = models.CharField('Title 7', max_length=80)
    subtitle8 = models.CharField('Subtitle8', max_length=50)
    title8 = models.CharField('Title 8', max_length=80)

class Reason(models.Model):

    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return self.title

class Menu(models.Model):

    category = models.CharField('category', max_length=50)

    class Meta:

        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self) -> str:
        return self.category

class MenuContent(models.Model):

    category = models.ForeignKey(Menu, on_delete=models.CASCADE)
    img = models.ImageField('Image')
    name = models.CharField('Name', max_length=60)
    recipe = models.TextField('Recipe')
    price = models.FloatField('Price')
    
    class Meta:

        verbose_name = 'Menu Content'
        verbose_name_plural = 'Menu Content'

    def __str__(self) -> str:
        return f'{self.name} - {self.category} - {self.price}'

class Special(models.Model):

    name = models.CharField('Name', max_length=50)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    img = models.ImageField('Image')

    def __str__(self) -> str:
        return self.name

class Event(models.Model):

    background = models.ImageField('Background')

class EventSlide(models.Model):

    img = models.ImageField('Image')
    title = models.CharField('Title', max_length=50)
    price = models.FloatField('Price')
    text1 = models.TextField('Text 1')
    offer1 = models.CharField('Offer 1', max_length=80)
    offer2 = models.CharField('Offer 2', max_length=80)
    offer3 = models.CharField('Offer 3', max_length=80)
    text2 = models.TextField('Text 2')
        
    class Meta:

        verbose_name = 'Event Slide'
        verbose_name_plural = 'Event Slides'

    def __str__(self) -> str:
        return f'{self.title} - {self.price}'
    
class ReservationContent(models.Model):

    placeholder1 = models.CharField('Input Placeholder 1', max_length=50)
    placeholder2 = models.CharField('Input Placeholder 2', max_length=50)
    placeholder3 = models.CharField('Input Placeholder 3', max_length=50)
    placeholder4 = models.CharField('Input Placeholder 4', max_length=50)
    placeholder5 = models.CharField('Input Placeholder 5', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)
            
    class Meta:

        verbose_name = 'Reservation Content'
        verbose_name_plural = 'Reservation Content'

class Reservation(models.Model):

    user_name = models.CharField('Name', max_length=50)
    user_email = models.EmailField('Email')
    user_phone = models.CharField('Phone Number', max_length=25)
    user_date = models.DateField('Date')
    user_time = models.TimeField('Time')
    user_count = models.IntegerField('Count')
    user_message = models.TextField('Message')

    def __str__(self) -> str:
        return f'{self.user_name} --------------------- {self.user_email} --------------------- {self.user_date} - {self.user_time} --------------------- {self.user_count}'
    
class Gallery(models.Model):

    img1 = models.ImageField('Image 1')
    img2 = models.ImageField('Image 2')
    img3 = models.ImageField('Image 3')
    img4 = models.ImageField('Image 4')
    img5 = models.ImageField('Image 5')
    img6 = models.ImageField('Image 6')
    img7 = models.ImageField('Image 7')
    img8 = models.ImageField('Image 8')
                
    class Meta:

        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'

class Chef(models.Model):

    img = models.ImageField('Image')
    name = models.CharField('Name', max_length=50)
    profession = models.CharField('Profession', max_length=50)
    social1 = models.CharField('Social Icon 1', max_length=50)
    social_url1 = models.URLField('Social Url 1')
    social2 = models.CharField('Social Icon 2', max_length=50)
    social_url2 = models.URLField('Social Url 2')
    social3 = models.CharField('Social Icon 3', max_length=50)
    social_url3 = models.URLField('Social Url 3')
    social4 = models.CharField('Social Icon 4', max_length=50)
    social_url4 = models.URLField('Social Url 4')

    def __str__(self) -> str:
        return f'{self.name} - {self.profession}'
    
class Contact(models.Model):

    google_map = models.TextField('Google Map')
    placeholder1 = models.CharField('Input Placeholder 1', max_length=50)
    placeholder2 = models.CharField('Input Placeholder 2', max_length=50)
    placeholder3 = models.CharField('Input Placeholder 3', max_length=50)
    placeholder4 = models.CharField('Input Placeholder 4', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)
                    
    class Meta:

        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

class ContactInfo(models.Model):

    icon = models.CharField('Icon', max_length=50)
    title = models.CharField('Title', max_length=40)
    info = models.CharField('Info', max_length=100)
                        
    class Meta:

        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'

    
    def __str__(self) -> str:
        return self.title
    
class ContactMessage(models.Model):

    user_name = models.CharField('Name', max_length=50)
    user_email = models.EmailField('Email')
    user_subject = models.CharField('Subject', max_length=60)
    user_message = models.TextField('Message')
                        
    class Meta:

        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self) -> str:
        return f'{self.user_name} ----------- {self.user_email} ----------- {self.user_subject}'
    
class Subscribe(models.Model):

    user_email = models.EmailField('User Email')

    def __str__(self) -> str:
        return self.user_email