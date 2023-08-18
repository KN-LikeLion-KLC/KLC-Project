from django.shortcuts import render, redirect
from django.http import HttpResponse
 
# Create your views here.
def redirect_main(request):
    return redirect('/main')

def main(request):
    return render(request, 'main.html')

def appGuide(request):
    return render(request, 'app_guide.html')

def kioskGuide(request):
    return render(request, 'kiosk_guide.html')

def emailGuide(request):
    return render(request, 'email_guide.html')

def mobilenotificationGuide(request):
    context = {'img': list(range(1, 16))}
    return render(request, 'mobile_notification_guide.html', context)

def quiz(request):
    return render(request, 'quiz.html')

def quiz_ans(request):
    return render(request, 'quiz_ans.html')