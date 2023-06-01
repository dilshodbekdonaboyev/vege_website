from django.urls import path
from apps.pages.views import (
    home, 
    about,
    shop,
    contact,
    blog,
    vagetables,
)
urlpatterns = [
    path('', home, name= 'home'),
    path('about/', about, name= 'about'),
    path('contact/', contact, name= 'contact'),
    path('shop/', shop, name= 'shop'),
    path('blog/', blog, name= 'blog'),
    path('vagetables/', vagetables, name= 'vagetables'),
    
]
