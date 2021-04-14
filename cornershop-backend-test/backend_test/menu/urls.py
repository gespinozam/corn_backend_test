from django.urls import path

# Import views class to set path's
from .views import (
    ListLunch,
    DetailLunch,
    CreateLunch,
    UpdateLunch,
    OrderLunch,
    MyOrdersLunch,
    DeleteLunch,
)

from .security import AuthMethods

auth = AuthMethods()

urlpatterns = [
    path("menu/", ListLunch.as_view(template_name="lunch/index.html"), name="list"),
    path(
        "menu/details/<uuid:pk>",
        DetailLunch.as_view(template_name="lunch/details.html"),
        name="details",
    ),
    path(
        "menu/create",
        CreateLunch.as_view(template_name="lunch/create.html"),
        name="create",
    ),
    path(
        "menu/edit/<uuid:pk>",
        UpdateLunch.as_view(template_name="lunch/update.html"),
        name="update",
    ),
    path(
        "menu/order/",
        OrderLunch.as_view(template_name="lunch/order.html"),
        name="order",
    ),
    path(
        "menu/my_orders/",
        MyOrdersLunch.as_view(template_name="lunch/my_orders.html"),
        name="my_orders",
    ),
    path("menu/delete/<uuid:pk>", DeleteLunch.as_view(), name="delete"),
    path("signup/", auth.signup_view, name="signup"),
    path("login/", auth.login_view, name="login"),
    path("logout/", auth.logout_view, name="logout"),
]
