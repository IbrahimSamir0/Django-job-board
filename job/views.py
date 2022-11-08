from multiprocessing import context
from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm ,JobForm 
from django.shortcuts import redirect , render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.
def job_list(request):
    job_list=Job.objects.all()
        
    #filters
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs
    
    paginator = Paginator(job_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={'jobs' :page_obj,'myfilter':myfilter}#template name
    return render(request,'job/job_list.html',context)


def job_details(request,slug):
    job_details=Job.objects.get(slug=slug)
    if request.method =='POST':
    
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.job=job_details
            myform.save()

    else :
        form = ApplyForm()

    context ={'job':job_details, 'form':form}
    return render(request,'job/job_details.html',context)


@login_required
def add_job(request):
    if request.method =='POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    context={'form':form}
    return render(request,'job/add_job.html',context)
