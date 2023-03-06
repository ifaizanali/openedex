from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import redirect
from .serializers import GreetingSerializer
from .permissions import IsAuthenticated
from .models import Greeting


def is_home():
    return len(Greeting.objects.filter(greetings_text__exact='hello')) == 0


# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def home(request, greet=None):
    if request.method == "GET":
        print("Greeting Received: ", greet)
        serializer = GreetingSerializer(data={"greetings_text": greet})
        if greet == "hello" and serializer.is_valid() and is_home():
            serializer.save()
            return redirect('http://127.0.0.1:8000/greetings/goodbye')
        elif greet == "goodbye" and serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': "Cannot greet more."}, status=status.HTTP_400_BAD_REQUEST)
