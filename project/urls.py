from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.index),
    path('test/', core.views.test),
]
