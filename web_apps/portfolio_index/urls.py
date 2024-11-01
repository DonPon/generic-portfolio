# index/urls.py

from django.urls import path
from django.contrib.auth.views import LogoutView
from web_apps.portfolio_index.views import (PortfolioListView, ProjectDetailView, ContactFormView,
                                            PortfolioItemCreateView, PortfolioItemUpdateView, CustomLoginView,
                                            PersonalDetailsUpdateView, CoreSettingsView, PortfolioItemDeleteView)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='portfolio'), name='logout'),
    path('', CoreSettingsView.as_view(), name='portfolio'),
    path('personal/edit/', PersonalDetailsUpdateView.as_view(), name='personal_details_edit'),
    path('project/<uuid:id>/', ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('project/new/', PortfolioItemCreateView.as_view(), name='project_create'),  # Create project
    path('project/<uuid:id>/edit/', PortfolioItemUpdateView.as_view(), name='project_update'),  # Edit project
    path('project/<uuid:id>/delete/', PortfolioItemDeleteView.as_view(), name='project_delete'), # Delete project

]