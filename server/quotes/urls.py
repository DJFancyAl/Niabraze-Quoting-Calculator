from django.urls import path
from .views import QuotesView, QuoteDetailView

urlpatterns = [
    path('', QuotesView.as_view(), name='quotes-view'),
    path('<int:id>', QuoteDetailView.as_view(), name='quote-detail'),
]