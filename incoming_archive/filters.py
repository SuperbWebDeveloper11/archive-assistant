import django_filters
from .models import Mail


# we'll use this class to filter mails based on model attributes
class MailFilter(django_filters.FilterSet):
    class Meta:
        model = Mail
        fields = {
                'registration_number': ['exact', ],
                'reference_number': ['exact', ],
                'source__name': ['icontains', ],
                'title': ['icontains', ],
        }

