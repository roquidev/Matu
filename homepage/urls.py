# External modules
from django.urls import path

# Local modules
from .views import home, profile, signup, signout, signin,  blog#, demo,


urlpatterns = [
    path('', home, name="home"),
    # path('accounts/signup/', signup, name="signup"),
    # path('accounts/logout/', signout, name="logout"),
    # path('accounts/signin/', signin, name="signin"),
    path('accounts/profile/', profile, name="profile"),
    # path('blog/', blog, name="blog"),
    # path('demo/', demo, name="demo"),
]
