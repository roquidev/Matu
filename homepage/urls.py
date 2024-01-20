# External modules
from django.urls import path

# Local modules
from .views import home, profile
# from .views import signup, signout, signin,  blog#, demo,


urlpatterns = [
    path('', home, name="home"),
    path('accounts/profile/', profile, name="profile"),
    # Ejemplos
    # path('accounts/signup/', signup, name="signup"),
    # path('accounts/logout/', signout, name="logout"),
    # path('accounts/signin/', signin, name="signin"),
    # path('blog/', blog, name="blog"),
    # path('demo/', demo, name="demo"),
]
