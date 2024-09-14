from django.urls import path, include

urlpatterns = [
    # Djoser автоматически создаст набор необходимых эндпоинтов.
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
] 

