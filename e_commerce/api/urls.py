from django.urls import path

from .views import CategoryApiView


urlpatterns = [
    # path('recipes/',RecipeApiView.as_view(),name='recipes_api'),
    # path('recipes/<int:pk>/',RecipeReadUpdateDeleteView.as_view(),name='recipe_api'),
    path('categories/',CategoryApiView.as_view(),name='categories_api'),

]