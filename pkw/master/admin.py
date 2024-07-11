from django.contrib import admin
from .models import Pengunjung, PrediksiPengunjung

class PengunjungAdmin(admin.ModelAdmin):
    list_display = ['date', 'jumlah']

class PrediksiPengunjungAdmin(admin.ModelAdmin):
    list_display = ['date', 'dewasa', 'anak']

# Register your models here.
admin.site.register(Pengunjung, PengunjungAdmin)
#admin.site.register(PrediksiPengunjung, PrediksiPengunjungAdmin)