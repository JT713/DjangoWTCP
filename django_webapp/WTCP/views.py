from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def links(request):
    return render(request, 'WTCP/links.html', {'title' : 'Links'})

def details(request):
    return render(request, 'WTCP/studentDetails.html', {'title' : 'Student Details'})

def monthlyAssessment(request):
    return render(request, 'WTCP/monthlyAssessment.html', {'title' : 'MonthlyAssessment'})

def exitInterview(request):
    return render(request, 'WTCP/exitInterview.html', {'title' : 'Exit Interview'})

def tanfFamilyIncome(request):
    return render(request, 'WTCP/TANFfamilyIncome.html', {'title' : 'TANF FAMILY INCOME'})

def tanfFamilyMember(request):
    return render(request, 'WTCP/TANFfamilyMember.html', {'title' : 'TANF FAMILY MEMBERS'})

def tanfPublicBenefits(request):
    return render(request, 'WTCP/TANFpublicBenefits.html', {'title' : 'TANF PUBLIC BENEFITS'})
