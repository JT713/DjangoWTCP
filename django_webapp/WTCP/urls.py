from django.urls import path
from . import views

urlpatterns = [
    path('', views.links, name='links'),
    path('details/', views.details, name='studentDetails'),
    path('monthlyAssessment/', views.monthlyAssessment, name='monthlyAssessment'),
    path('exitInterview/', views.exitInterview, name='exitInterview'),
    path('TANFfamilyIncome/', views.tanfFamilyIncome, name= 'tanfFamilyIncome'),
    path('TANFfamilyMember/', views.tanfFamilyMember, name='tanfFamilyMember'),
    path('TANFpublicBenefits/', views.tanfPublicBenefits, name='tanfPublicBenefits'),
]
