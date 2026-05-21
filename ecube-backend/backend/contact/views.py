from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from mailjet_rest import Client
import os

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
                # Mailjet API credentials (loaded from .env or server environment variables)
                MAILJET_API_KEY = os.environ.get("MAILJET_API_KEY")
                MAILJET_API_SECRET = os.environ.get("MAILJET_API_SECRET")
                
                if not MAILJET_API_KEY or not MAILJET_API_SECRET:
                    return Response({'error': 'Server missing Mailjet API keys.'}, status=500)
                
                # The sender email MUST be verified in your Mailjet account!
                # Replace this with the email you verified on Mailjet.
                MAILJET_SENDER_EMAIL = "gopallalit2000@gmail.com" 

                mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_API_SECRET), version='v3.1')
                
                payload = {
                    "Messages": [
                        {
                            "From": {
                                "Email": MAILJET_SENDER_EMAIL,
                                "Name": "Ecube Website"
                            },
                            "To": [
                                {
                                    "Email": "gopallalit2000@gmail.com",
                                    "Name": "Admin"
                                }
                            ],
                            "ReplyTo": {
                                "Email": email,
                                "Name": name
                            },
                            "Subject": "New Contact Form Submission",
                            "TextPart": full_message
                        }
                    ]
                }

                result = mailjet.send.create(data=payload)

                if result.status_code == 200:
                    return Response({'message': 'Your message has been sent successfully!'}, status=200)
                else:
                    print("Mailjet Error:", result.json())
                    return Response({'error': 'Failed to send message via Mailjet.'}, status=500)
            except Exception as e:
                print("Exception:", str(e))
                return Response({'error': 'Failed to send message. Please try again later.'}, status=500)
            
            

