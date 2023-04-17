from datacenter.models import Visit
from datacenter.models import get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    visitors_in_vault = Visit.objects.filter(leaved_at__isnull=True)
    visitors_not_leaved_vault = []

    for visit in visitors_in_vault:
        visit_time = visit.entered_at
        visitor_name = visit.passcard.owner_name
        duration_in_vault = get_duration(visit)
        formatted_duration = format_duration(duration_in_vault)
        non_closed_visits = {
            'who_entered': visitor_name,
            'entered_at': str(visit_time.strftime('%d-%m-%Y %H:%M')),
            'duration': formatted_duration,
            }
        visitors_not_leaved_vault.append(non_closed_visits)

    context = {
        'non_closed_visits': visitors_not_leaved_vault,
    }
    return render(request, 'storage_information.html', context)
