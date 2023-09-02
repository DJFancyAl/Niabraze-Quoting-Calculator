from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .serializers import QuoteSerializer
from .models import Quote

# Create your views here.
class QuotesView(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = QuoteSerializer

    def get(self, request, *args, **kwargs):
        quotes = Quote.objects.all()
        serializer = self.serializer_class(quotes, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuoteDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuoteSerializer

    # Get one Quote by ID
    def get(self, request, id, *args, **kwargs):
        try:
            quote = Quote.objects.get(id=id)
        except Quote.DoesNotExist:
            raise NotFound("Quote not found with the specified ID.")
        
        serializer = QuoteSerializer(quote)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Delete one Quote by ID
    def delete(self, request, id, *args, **kwargs):
        try:
            quote = Quote.objects.get(id=id)
        except Quote.DoesNotExist:
            raise NotFound("Quote not found with the specified ID.")
        
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)