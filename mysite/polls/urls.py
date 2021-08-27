from django.urls import path
from . import views
from . import views2

urlpatterns = [
    path('1', views.index, name='index'),
    path('2', views.index3, name='index3'),
    path('3', views2.index2, name='index2'),
    
]#O próximo passo é apontar na raiz da URLconf para o módulo polls.urls. No arquivo mysite/urls.py,
# adicione uma importação de django.urls.include e insira um include() na lista urlpatterns, de forma que você tenha:

