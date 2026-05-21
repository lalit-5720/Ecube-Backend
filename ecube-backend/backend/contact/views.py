from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.core.mail import send_mail

# Create your views here.
class ContactView(ViewSet):
    def create(self,request):
        print("API Called")
        if request.method == 'POST':
            name =request.data.get('name')
            email =request.data.get('email')
            phone =request.data.get('phone')
            event_type = request.data.get('event')
            event_date = request.data.get('date')
            event_message = request.data.get('message')

            if not all([name, email, phone, event_type, event_date, event_message]):
                return Response({'error': 'Please fill out all the fields before submitting.'}, status=400)

            full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nEvent Type: {event_type}\nEvent Date: {event_date}\nEvent Message: {event_message}"

            try:
                send_mail(
                    subject='New Contact Form Submission',
                    message=full_message,
                    from_email=email,
                    recipient_list=['lalitchandran2004@gmail.com'],
                )
                return Response({'message': 'Your message has been sent successfully!'}, status=200)
            except Exception as e:
                return Response({'error': 'Failed to send message. Please try again later.'}, status=500)
            
            

