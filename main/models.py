from django.db import models
from ckeditor.fields import RichTextField
class Books(models.Model):
    name=models.CharField('Ad', max_length=200,unique=True)
    pdf=models.FileField('PDF', upload_to='media/')
    img=models.ImageField('Cover', upload_to='media/', default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kitab'
        verbose_name_plural = 'Kitablar'
class İnfo(models.Model):
    txt=RichTextField('Məlumat')
    def __str__(self):
        return self.txt
    class Meta:
        verbose_name = 'Məlumat'
        verbose_name_plural = 'Məlumat'