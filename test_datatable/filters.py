import django_filters

from test_datatable import models


class StudiesFilter(django_filters.FilterSet):
    class Meta:
        model = models.Studies
        fields = '__all__'
