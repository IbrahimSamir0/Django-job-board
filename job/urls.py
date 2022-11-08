from django.urls import path , include
from. import  views, api
app_name='job' 

urlpatterns = [
    path('',views.job_list,name = 'job_list'),
    path('add',views.add_job,name ='add_job'),
    path('<str:slug>',views.job_details,name ='job_details'),
    
    # API
    path('api/jobs',api.job_list_api,name ='job_list_api'),
    path('api/jobs/<int:id>',api.job_details_api,name ='job_details_api'),
    
    
    #geniric class(class based viwes)
    
    path('api/v2/jobs',api.JobListApi.as_view(),name ='job_list_api'),
    path('api/v2/jobs/<int:id>',api.JobDetaill.as_view(),name ='job_details_api'),
] 