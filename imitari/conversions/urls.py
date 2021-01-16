from django.conf.urls import url

from conversions.views import (
   ConversionView,
)

urlpatterns = [
   url(r'^convert/$', ConversionView.as_view(), name='convert_image'),
]