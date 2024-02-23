from django.contrib import admin

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
    
