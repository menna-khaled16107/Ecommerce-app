from django.urls import path 
from . import views


urlpatterns=[
    path('allproducts/',views.productlist,name='AllProduct'),
    path('category/<str:name>/',views.displayProducts,name='display_product'),
    path('',views.Home,name='Home'),
    path('search/',views.search,name='search_for_product'),
    path('addproduct/',views.addproduct,name='+AddProduct'),
    path('productDetails/<int:id>/',views.Product_Details,name='Details'),
    path('updatedpro/<int:id>/',views.Update_product,name='update_product'),
    path('deletedpro/<int:id>/',views.delete_product,name='deleted')
]