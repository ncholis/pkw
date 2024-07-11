from django.db import models
from statistics import mean 


class PengunjungQuerySet(models.QuerySet):
    def prediction_next_month(self):
        forecast = self.dataset_forecast()
        ret = sum(forecast) / len(forecast)
        return ret

    def dataset_date(self):
        if not self.exists():
            return []
        
        dd = [d.strftime('%Y-%m')  for d in self.values_list('date', flat=True)]
        return dd

    def dataset_actual(self):
        if not self.exists():
            return []
        return list(self.values_list('jumlah', flat=True))
    
    def dataset_forecast(self, cast=2):
        data_actual = self.dataset_actual()

        results = []
        for index, d in enumerate(data_actual, 1):
            if index <= cast:
                results.append(0)
                continue
            if index == 3:
                data = data_actual[:index]
            else:
                data = data_actual[index-3:index]
            v_average = sum(data) / len(data)
            results.append(v_average)
        
        return results
    
    def dataset_error(self):
        actual = self.dataset_actual()
        forecast = self.dataset_forecast()

        if len(actual) != len(forecast):
            return []

        result = []
        for x in range(len(actual)):
            r = actual[x] - forecast[x]
            result.append(r)
        return result


class PengunjungManager(models.Manager):
    def get_queryset(self):
        return PengunjungQuerySet(self.model, using=self._db)


class Pengunjung(models.Model):
    class Meta:
        verbose_name = 'Kunjungan'
        verbose_name_plural = 'Kunjungan'

    date = models.DateField()
    jumlah = models.PositiveIntegerField(default=0)
    objects = PengunjungManager()
    _already_clean = False

    def clean(self):
        self._already_clean = True

    def save(self, *args, **kwargs):
        if not self._already_clean:
            self.clean()
        ret = super().save(*args, **kwargs)
        return ret


class PrediksiPengunjung(models.Model):
    date = models.DateField()
    dewasa = models.PositiveIntegerField(default=0)
    anak = models.PositiveIntegerField(default=0)