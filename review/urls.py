from django.urls import path
import review.views


urlpatterns = [
    path('review/', review.views.ReviewList.as_view()),
    path('review/<int:pk>/', review.views.ReviewDetail.as_view()),
]
