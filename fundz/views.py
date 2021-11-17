from django.http import HttpResponse
from django.shortcuts import render
import joblib
from fundz.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECERT_KEY
import razorpay
from django.contrib.auth. forms import UserCreationForm


def home(request):
    return render(request, 'home.html')


def education(request):
    return render(request, 'education.html')


def health(request):
    return render(request, 'health.html')


def sports(request):
    return render(request, 'sports.html')


def startup(request):
    return render(request, 'startup.html')


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECERT_KEY))


def pay(request):
    order_amount = 100000
    order_currency = 'INR'
    payment_order = client.order.create(
        dict(amount=order_amount, currency=order_currency, payment_capture=1))
    payment_order_id = payment_order['id']
    context = {
        'amount': order_amount, 'api_key': RAZORPAY_API_KEY, 'order_id': payment_order_id
    }
    return render(request, 'pay.html', context)
