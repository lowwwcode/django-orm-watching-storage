from datacenter.models import Passcard, Visit, get_duration, is_visit_suspect, format_duration

from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_person_visits = Visit.objects.filter(passcard=passcard)
    final_visits_list = []
    for visit in all_person_visits:
        duration_in_vault = get_duration(visit)
        formatted_duration = format_duration(duration_in_vault)
        suspension_check = is_visit_suspect(duration_in_vault, 60)
        this_passcard_visits = {
                'entered_at': visit.entered_at,
                'duration': formatted_duration,
                'is_strange': suspension_check
            }
        final_visits_list.append(this_passcard_visits)
    context = {
        'passcard': passcard,
        'this_passcard_visits': final_visits_list
    }
    return render(request, 'passcard_info.html', context)
