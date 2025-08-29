from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import FoodDonation
from .forms import FoodDonationForm, DeliveryConfirmationForm

# Home Page
def home_view(request):
    return render(request, 'home.html')


# Smart redirect for yellow "Get Started" button
def get_started(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('signup')  # Change to your signup URL name if different

    role = getattr(user, 'role', None)

    if role == 'restaurant':
        return redirect('donate_food')  # URL name for donate_food_view
    elif role == 'ngo':
        return redirect('available_donations')  # URL name for available_donations_view

    return redirect('home')


# Restaurant Dashboard
@login_required
def restaurant_dashboard(request):
    my_donations = FoodDonation.objects.filter(restaurant=request.user).order_by('-expiry_time')
    return render(request, 'dashboards/restaurant_dashboard.html', {
        'my_donations': my_donations
    })


# NGO Dashboard
@login_required
def ngo_dashboard(request):
    delivered_donations = FoodDonation.objects.filter(
        claimed_by=request.user,
        is_claimed=True,
        delivered=True,
        delivery_photo__isnull=False
    ).order_by('-delivered_at')
    return render(request, 'dashboards/ngo_dashboard.html', {
        'delivered_donations': delivered_donations
    })


# Optional: General User Dashboard
@login_required
def user_dashboard(request):
    return render(request, 'dashboards/user_dashboard.html')


# Donation Form View (for Restaurant)
@login_required
def donate_food_view(request):
    if request.method == 'POST':
        form = FoodDonationForm(request.POST, request.FILES)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.restaurant = request.user
            donation.save()
            return redirect('restaurant_dashboard')
    else:
        form = FoodDonationForm()
    return render(request, 'main/donate_food.html', {'form': form})


# Available Donations List (for NGO)
@login_required
def available_donations_view(request):
    donations = FoodDonation.objects.filter(
        is_claimed=False,
        expiry_time__gt=timezone.now()
    ).order_by('-added_at')
    return render(request, 'main/available_donations.html', {'donations': donations})


# Claim Donation (NGO)
@login_required
def claim_donation_view(request, donation_id):
    donation = get_object_or_404(FoodDonation, id=donation_id)

    if not donation.is_claimed and donation.expiry_time > timezone.now():
        donation.is_claimed = True
        donation.claimed_by = request.user
        donation.save()
        messages.success(request, "You have successfully claimed the food.")
    else:
        messages.error(request, "This donation is no longer available.")

    return redirect('available_donations')


# My Claims Page (NGO)
@login_required
def my_claims_view(request):
    claimed_donations = FoodDonation.objects.filter(
        claimed_by=request.user
    ).order_by('-expiry_time')
    return render(request, 'main/my_claims.html', {
        'claimed_donations': claimed_donations
    })


# Verify Pickup (NGO)
@login_required
def verify_pickup_view(request, donation_id):
    donation = get_object_or_404(FoodDonation, id=donation_id)

    if donation.claimed_by:
        donation.is_claimed = True
        donation.save()
        messages.success(request, "Pickup successfully verified!")
    else:
        messages.error(request, "This donation hasn't been claimed yet.")

    return redirect('ngo_dashboard')


# Mark As Delivered (upload photo)
@login_required
def mark_as_delivered_view(request, donation_id):
    donation = get_object_or_404(FoodDonation, id=donation_id, claimed_by=request.user)

    if request.method == 'POST':
        form = DeliveryConfirmationForm(request.POST, request.FILES, instance=donation)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.delivered = True
            donation.delivered_at = timezone.now()
            donation.save()
            messages.success(request, "Marked as delivered successfully.")
            return redirect('my-claims')
    else:
        form = DeliveryConfirmationForm(instance=donation)

    return render(request, 'main/mark_as_delivered.html', {
        'form': form,
        'donation': donation
    })
