
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signupPage,name="signupPage"),
    path('loginPage/',views.loginPage,name="loginPage"),
    path('homePage/',views.homePage,name="homePage"),
    path('addPage/',views.addPage,name="addPage"),
    path('updatePage/<str:id>',views.updatePage,name="updatePage"),
    path('deletePage/<str:id>',views.deletePage,name="deletePage"),

    # path('show/', views.s, name='s'),
    # path('delete/<int:x>', views.d),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)