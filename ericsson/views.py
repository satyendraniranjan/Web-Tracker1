from django.shortcuts import redirect
from ericsson.forms import EricssonPostComTrackerForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from ericsson.models import EricssonPostComTracker
from django.http import HttpResponse
import csv
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect




@login_required
def ericssontracker_list(request):

        latest_tracker_list = EricssonPostComTracker.objects.order_by('-created_date')
        context = {
            'latest_tracker_list': latest_tracker_list,
       }
        return render(request, 'ericsson/ericssontracker_list1.html', context)


@login_required
def ericssontracker_new(request):
    if request.method == "POST":
        form = EricssonPostComTrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('ericssontracker_list')
    else:
        form = EricssonPostComTrackerForm
    return render(request, 'ericsson/ericssontracker_edit.html', {'form': form})



@login_required
def ericssontracker_detail(request, pk):
    tracker = get_object_or_404(EricssonPostComTracker, pk=pk)
    return render(request, 'ericsson/ericssontracker_list.html', {'tracker': tracker})


@login_required
def ericssontracker_edit(request, pk):
    tracker = get_object_or_404(EricssonPostComTracker, pk=pk)
    if request.method == "POST":
        form = EricssonPostComTrackerForm(request.POST)
#        form = TrackerForm(request.POST, instance=tracker)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('ericssontracker_list')
    else:
        form = EricssonPostComTrackerForm(instance=tracker)
    return render(request, 'ericsson/ericssontracker_edit.html', {'form': form})

@login_required
def ericssontracker_edit1(request, pk):
    tracker = get_object_or_404(EricssonPostComTracker, pk=pk)
    if request.method == "POST":
        form = EricssonPostComTrackerForm(request.POST, instance=tracker)
#        form = TrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('ericssontracker_list')
    else:
        form = EricssonPostComTrackerForm(instance=tracker)
    return render(request, 'ericsson/ericssontracker_edit.html', {'form': form})


def ericssonexport(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Ericsson_Post_Com_Tracker.csv"'

    writer = csv.writer(response)
    writer.writerow(['System Date','User Date','User Name','Assignee','cascade','eNB','Technology', 'ENM','IP_OAM','Market','Volte_Soft','CSMS','FE_Name','Tech_Email','Tech_Contact','CIC_Airboss_Mail','RSD_Airboss_Mail','RSD_Manager_Mail','Construction_Manager_Mail','Activity','Activity_status','Site_Status_pre_Activity','Secondary_Fibre_check', 'Site_Status_post_Activity','Kpi_Profile','Remarks','Revisit_Required','Revisit','Site_Pre_Status','Site_Post_Status','OAR_Date','OAC_Date'])

    latest_tracker_list1 = EricssonPostComTracker.objects.order_by('-created_date')
    for item in latest_tracker_list1:
        writer.writerow([item.created_date,item.Date,item.admin,item.admin,item.cascade,item.eNB, item.Technology, item.ENM, item.IP_OAM, item.Market, item.Volte_Soft, item.CSMS, item.FE_Name, item.Tech_Email,item.Tech_Contact, item.CIC_Airboss_Mail,item.RSD_Airboss_Mail,item.Construction_Manager_Mail,item.Activity, item.Activity_status, item.Site_Status_pre_Activity, item.Secondary_Fibre_check, item.Site_Status_post_Activity,item.Kpi_Profile,item.Remarks,item.Revisit_Required,item.Revisit,item.Site_Pre_Status,item.Site_Post_Status,item.OAR_Date,item.OAC_Date])

    return response

@login_required
def ericssonpostcomsearch(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(cascade__icontains=query) | Q(admin__username__icontains=query)

            results = EricssonPostComTracker.objects.filter(lookups).distinct().order_by('-created_date')

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'ericsson/ericssonpostcomsearch.html', context)

        else:
            return render(request, 'ericsson/ericssonpostcomsearch.html')

    else:
        return render(request, 'ericsson/ericssonpostcomsearch.html')

