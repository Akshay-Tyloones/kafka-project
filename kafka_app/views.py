from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .producer import kafka_producer



def home(request):
    return HttpResponse("hello from home")



def send_message(request):
    produce_message = kafka_producer()
    produce_message('Hello, Kafka! from akshay kumravat')
    return JsonResponse({'status': 'Message sent'})


