from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryListView, QuestionListView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView, \
    AnswerViewSet

router = DefaultRouter()
router.register('answers', AnswerViewSet)

urlpatterns = [
    # path('categories-list/', category_list),
    # path('category-list/', CategoryView.as_view()),
    path('category-list/', CategoryListView.as_view()),
    path('questions-list/', QuestionListView.as_view()),
    path('questions-create/', QuestionCreateView.as_view()),
    path('questions-update/<int:pk>/', QuestionUpdateView.as_view()),
    path('questions-delete/<int:pk>/', QuestionDeleteView.as_view()),
    path('', include(router.urls)),
]