from django.shortcuts import render
from django.http import HttpResponse

from .models import BioDrug

def select_drug(request):
    if request.method == 'POST':
        drugs_id = request.POST.get('drugs')
        drugs_id_list = drugs_id.strip().split(' ')
        return HttpResponse(','.join(drugs_id_list))
    else:
        drugs = BioDrug.objects.filter(inputer__isnull=True)
        return render(request,'exam2014/index.html',{'drugs': drugs})