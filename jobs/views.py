from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import re, operator

from .models import Codedjob
from .targetwords import *
from .funky import *


def submit(request):
    if request.method == 'POST':
        if request.POST['job_text']:
            job = Codedjob()
            text = request.POST['job_text']
            textlist = text_to_list(text)
            job.job_text = text
            job.submit_time = timezone.datetime.now()
            job.total_words = len(textlist)

            masclist = gender_word_list(textlist, mascwords) + gender_exact_word_list(textlist, mascexactwords)
            a = list_of_words_to_dict(masclist)
            b = phrase_in_text(text, mascphrases)
            mascdict = {**a, **b}
            mascitems = dictcount(mascdict)
            job.masc_words = mascdict
            job.total_masc_words = mascitems
            job.masc_word_proportion = (mascitems/len(textlist))*100

            femlist = gender_word_list(textlist, femwords) + gender_exact_word_list(textlist, femexactwords)
            x = list_of_words_to_dict(femlist)
            y = phrase_in_text(text, femphrases)
            femdict = {**x, **y}
            femitems = dictcount(femdict)
            job.fem_words = femdict
            job.total_fem_words = femitems
            job.fem_word_proportion = (femitems/len(textlist))*100

            gender_balance = len(masclist) - len(femlist)
            if gender_balance > 0:
                job.result = 'Masculine'
            elif gender_balance == 0:
                job.result = 'Neutral'
            else:
                job.result = 'Feminine'
            job.save()
            return redirect('result/' + int_str(job.id, keyspace))
        else:
            return render(request, 'jobs/submit.html',{'error': 'Please add the job text'})
    else:
        return render(request, 'jobs/submit.html')


def result(request, unique_id):
    job_id = str_int(unique_id, keyspace)
    job = get_object_or_404(Codedjob, pk=job_id)
    text = job.job_text
    textlist = text_to_list(text)

    # Created sorted dictionary with masc words found in the text
    masclist = gender_word_list(textlist, mascwords) + gender_exact_word_list(textlist, mascexactwords)
    a = list_of_words_to_dict(masclist)
    b = phrase_in_text(text, mascphrases)
    mascdict = {**a, **b}
    mascdictsorted = sorted(mascdict.items(), key=operator.itemgetter(1), reverse=True)

    # Create sorted dictionary with fem words found in text
    femlist = gender_word_list(textlist, femwords) + gender_exact_word_list(textlist, femexactwords)
    x = list_of_words_to_dict(femlist)
    y = phrase_in_text(text, femphrases)
    femdict = {**x, **y}
    femdictsorted = sorted(femdict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'jobs/result.html', {'job':job, 'mascdictsorted':mascdictsorted, 'femdictsorted':femdictsorted})
