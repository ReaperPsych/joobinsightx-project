from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
    path('search-job', views.job_search, name='search_job'),
    path('view-job/<int:job_id>/', views.job_view, name ='view_job'),

    # paths for employee
    path('view-cv', views.cv_view, name= 'view_cv'),
    path('update-cv', views.cv_update, name ='update_cv'),
    path('save-job/<int:job_id>/', views.job_save, name ='save_job'),
    path('saved-jobs', views.jobs_saved, name ='saved_jobs'),
    path('applied-jobs', views.jobs_applied, name ='applied_jobs'),
    path('apply-job/<int:job_id>/', views.job_apply, name ='apply_job'),

    
    # paths for employer
    path('post-job', views.job_post, name = 'post_job'),
    path('view-dashboard', views.dashboard_view, name = 'view_dashboard'),
    path('view-applied-candidate/<int:job_id>/', views.applied_candidate_view, name = 'view_applied_candidate'),
    path('view-job-edit/<int:job_id>/', views.job_edit_view, name = 'view_job_edit'),
    path('view-job-delete/<int:job_id>/', views.job_delete_view, name = 'view_job_delete'),
    path('view-cv/<int:user_id>/', views.view_cv, name = 'cv_view'),
]
