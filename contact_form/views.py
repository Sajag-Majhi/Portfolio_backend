from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from .serializers import ContactSerializer
from django.conf import settings

@api_view(['POST'])
def send_contact_email(request):
    serializer = ContactSerializer(data=request.data)
    
    if serializer.is_valid():
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        message = serializer.validated_data['message']

        subject = f"New Contact Form Message from {name}"      # Name as subject
        content = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            content,
            settings.EMAIL_HOST_USER,  
            [settings.EMAIL_HOST_USER],         # your receiving mail
        )

        return Response({"success": "Email sent!"})

    return Response(serializer.errors, status=400)
