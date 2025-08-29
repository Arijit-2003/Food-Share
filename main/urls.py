from django.urls import path
from . import views
from .views import (
    home_view,
    restaurant_dashboard,
    ngo_dashboard,
    user_dashboard,
    donate_food_view,
    available_donations_view,
    claim_donation_view,
    my_claims_view,
    verify_pickup_view,
    mark_as_delivered_view,
    get_started  # import added
)

urlpatterns = [
    path('', home_view, name='home'),

    # Dashboards
    path('restaurant/dashboard/', restaurant_dashboard, name='restaurant_dashboard'),
    path('ngo/dashboard/', ngo_dashboard, name='ngo_dashboard'),
    path('user/dashboard/', user_dashboard, name='user_dashboard'),

    # Donation actions
    path('donate/', donate_food_view, name='donate_food'),
    path('donations/', available_donations_view, name='available_donations'),
    path('claim/<int:donation_id>/', claim_donation_view, name='claim-donation'),
    path('my-claims/', my_claims_view, name='my-claims'),
    path('verify-pickup/<int:donation_id>/', verify_pickup_view, name='verify-pickup'),
    path('mark-delivered/<int:donation_id>/', mark_as_delivered_view, name='mark-as-delivered'),

    # Smart yellow button redirect view
    path('get-started/', get_started, name='get_started'),
]
