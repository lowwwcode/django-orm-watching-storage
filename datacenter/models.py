from django.db import models

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


def get_duration(visit_):
    """Вернет длительность нахождения для визита хранилища"""
    visitor_entered_time = visit_.entered_at
    visitor_leaved_at = visit_.leaved_at
    time_now = dt.datetime.now(dt.timezone.utc)
    if visitor_leaved_at is None:
        delta = time_now - visitor_entered_time
        return delta
    else:
        delta = visitor_leaved_at - visitor_entered_time
        return delta


def format_duration(duration_to_format):
    """Форматирует длительность в секундах в человекоподобный формат"""
    time_in_seconds = duration_to_format.total_seconds() * 24
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    return f'{int(hours)} ч {int(minutes)} мин'


def is_visit_suspect(visit_time_in_vault, mins):
    """Проверит визит на подозрительность и вернет подозрительный визит"""
    minutes_in_vault = visit_time_in_vault.total_seconds() // 60
    return minutes_in_vault > mins
