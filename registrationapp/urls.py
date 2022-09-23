from django.urls import path
from . import views

urlpatterns = [
    path('register',views.registeradmin,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('addbook',views.addbook,name='addbook'),
    path('addbookval',views.addbookval,name='addbookval'),
    path('updsrch',views.updatesearch,name='updsrch'),
    path('updval',views.update_val,name='updval'),
    path('updsubmit',views.update_submit,name='updsubmit'),
    path('studentview',views.studview,name='studentview'),
    path('bookview/<str:bkid>',views.bookview,name='bookview'),
    path('delsrch',views.delsrch,name='delsrch'),
    path('delval',views.delval,name='delval'),
    path('issuebook',views.issuebook,name='issuebook'),
    path('issueval',views.issueval,name='issueval'),
    path('returnsrch',views.returnsrch,name='returnsrch'),
    path('returnview',views.returnview,name='returnview'),
    path('returnval',views.returnval,name='returnval'),
]