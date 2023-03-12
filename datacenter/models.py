from django.db import models

from django.utils import timezone
import datetime as dt



class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    """Вернет длительность нахождения для визита хранилища"""
    visitor_entered_time = visit.entered_at
    now_time = dt.datetime.now(timezone.utc)
    delta_time = now_time - visitor_entered_time

    return delta_time


def format_duration(duration):
    """Откидывает от длительности нахождения миллисекунды"""
    formatted_duration = str(duration).split('.')[0]
    return formatted_duration

