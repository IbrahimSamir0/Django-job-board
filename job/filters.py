import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title =django_filters.CharFilter(lookup_expr='icontains')
    describtion =django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['category','title','describtion','experience','job_type']