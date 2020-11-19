from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html')
def payment(request):
    if request.method == 'GET':
        amount = request.GET.get('amount')
        email = request.GET.get('email')
        content = f"Payment recevied of {amount}"
        send_mail("Payment Gateway Integration", content, "payxway.tect@gmail.com",[email])
        
        context={
            'amount': amount,
        }

    return render(request, 'payment.html', context)