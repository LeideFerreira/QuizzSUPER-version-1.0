from django.urls import path
from .views import index, resultado, showquizz, save_ans

urlpatterns = [
    path('', index, name="index"),
    path('showquizz', showquizz, name="showquizz"),
    path('save_ans/', save_ans, name="saveans"),
    path('resultado', resultado, name="resultado"),
]
