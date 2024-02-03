from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .permission import user_is_employee, user_is_employer
from . models import cv, JobDetail, SavedJobs, AppliedJobs
from django.db.models import Q
from accounts.models import CustomUser
from django.contrib import messages



user = get_user_model
# Create your views here.

def home(request):
    return render(request, 'jobapp/home.html')



# def job_search(request):
#     if request.method == 'POST':
#         search_position = request.POST['position-search']
#         search_location = request.POST['location-search']

#         # search_job = JobDetail.objects.filter(name__icontains=search_position)

#         query = Q()
#         if search_position:
#             query != Q(position__icontains=search_position)
#         if search_location:
#             query != Q(address__icontains=search_location)

#         search_results = JobDetail.objects.filter(query)
#         print(search_results)

#         if search_results.exists():
#             context = {
#                 'search_results': search_results,
#                 'search_position':search_position,
#                 'search_location':search_location
#             }
#         else:
#             context = None
        
#         print(context)

#         return render (request, 'jobapp/search_job.html', context)

#     else:
#         # return render (request, 'jobapp/search_job.html')
#         return HttpResponse("Please Enter Job location and Job position")
    

def job_search(request):
    current_user = request.user
    if request.method == 'POST':
        search_position = request.POST['position-search']
        search_location = request.POST['location-search']

        query = Q()
        if search_position:
            query |= Q(position__icontains=search_position)
        if search_location:
            query |= Q(address__icontains=search_location)

        search_results = JobDetail.objects.filter(query).select_related('employer')
        # print(search_results)

        if search_results.exists():
            job_ids = list(search_results.values_list('id', flat=True))
            saved_job_ids = list(SavedJobs.objects.filter(user=current_user).values_list('job_id', flat=True))

            context = {
                'search_results': search_results,
                'search_position': search_position,
                'search_location': search_location,
                'current_user': current_user,
                'job_ids': job_ids,
                'saved_job_ids': saved_job_ids
            }
        else:
            context = None
        print(search_results)
        # print(current_user)
        # print(job_ids)
        # print(saved_job_ids)

        return render(request, 'jobapp/search_job.html', context)

    else:
        return HttpResponse("Please Enter Job location and Job position")





def job_view(request, job_id):
    current_user = request.user
    job_detail = get_object_or_404(JobDetail, id=job_id)
    employer = job_detail.employer
    user_account_type = current_user.account
    print(employer)

    saved_jobs = SavedJobs.objects.filter(user=current_user)
    saved_job_ids = list(saved_jobs.values_list('job_id', flat=True))

    applied_jobs = AppliedJobs.objects.filter(user=current_user)
    applied_job_ids = list(applied_jobs.values_list('job_id', flat=True))
    
    
    context = {
        'job_detail': job_detail,
        'employer':employer,
        'user_account_type':user_account_type,
        'saved_job_ids': saved_job_ids,
        'applied_job_ids': applied_job_ids
    }
    # print(user_account_type)
    # print(job_id)
    # print(saved_job_ids)
    # print(applied_job_ids)

    return render (request, 'jobapp/job_view_detail.html', context)



#employee views
@login_required
@user_is_employee
def cv_view(request):
    try:
        current_user = request.user
        current_user_account_type = request.user.account

        cv_instance = cv.objects.get(user=current_user)
    except cv.DoesNotExist:
        cv_instance = None

    return render(request, 'jobapp/employee/cv.html', {'cv_instance': cv_instance, 'current_user_account_type': current_user_account_type})



@login_required
@user_is_employee
def cv_update(request):
    try:
        current_user = request.user
        try:
            cv_instance = cv.objects.get(user=current_user)
        except cv.DoesNotExist:
            cv_instance = None

        if request.method == 'POST':
            form_data = request.POST
            photo = request.FILES.get('photo')
            try:
                if cv_instance:
                    cv_instance.full_name = form_data.get('full_name', '')
                    cv_instance.profession = form_data.get('profession', '')
                    cv_instance.gmail = form_data.get('gmail', '')
                    cv_instance.phone = form_data.get('phone', '')
                    cv_instance.linkedin = form_data.get('linkedin', '')
                    cv_instance.github = form_data.get('github', '')
                    cv_instance.description = form_data.get('description', '')
                    cv_instance.degree1 = form_data.get('degree1', '')
                    cv_instance.university1 = form_data.get('university1', '')
                    cv_instance.graduation_year1 = form_data.get('graduation_year1', '')
                    cv_instance.degree2 = form_data.get('degree2', '')
                    cv_instance.university2 = form_data.get('university2', '')
                    cv_instance.graduation_year2 = form_data.get('graduation_year2', '')
                    cv_instance.company1 = form_data.get('company1', '')
                    cv_instance.project1 = form_data.get('project1', '')
                    cv_instance.experience_description1 = form_data.get('experience_description1', '')
                    cv_instance.company2 = form_data.get('company2', '')
                    cv_instance.project2 = form_data.get('project2', '')
                    cv_instance.experience_description2 = form_data.get('experience_description2', '')
                    cv_instance.skill1 = form_data.get('skill1', '')
                    cv_instance.skill2 = form_data.get('skill2', '')
                    cv_instance.skill3 = form_data.get('skill3', '')
                    cv_instance.skill4 = form_data.get('skill4', '')
                    cv_instance.hobbies1 = form_data.get('hobbies1', '')
                    cv_instance.hobbies2 = form_data.get('hobbies2', '')
                    cv_instance.hobbies3 = form_data.get('hobbies3', '')
                    cv_instance.hobbies4 = form_data.get('hobbies4', '')
                    cv_instance.reference = form_data.get('reference', '')
                    if photo:
                        cv_instance.photo = photo
                    cv_instance.save()
                    messages.success(request, "CV updated successfully!")
                else:
                    cv_instance = cv(
                        user=current_user,
                        full_name=form_data.get('full_name', ''),
                        profession=form_data.get('profession', ''),
                        gmail=form_data.get('gmail', ''),
                        phone=form_data.get('phone', ''),
                        linkedin=form_data.get('linkedin', ''),
                        github=form_data.get('github', ''),
                        description=form_data.get('description', ''),
                        degree1=form_data.get('degree1', ''),
                        university1=form_data.get('university1', ''),
                        graduation_year1=form_data.get('graduation_year1', ''),
                        degree2=form_data.get('degree2', ''),
                        university2=form_data.get('university2', ''),
                        graduation_year2=form_data.get('graduation_year2', ''),
                        company1=form_data.get('company1', ''),
                        project1=form_data.get('project1', ''),
                        experience_description1=form_data.get('experience_description1', ''),
                        company2=form_data.get('company2', ''),
                        project2=form_data.get('project2', ''),
                        experience_description2=form_data.get('experience_description2', ''),
                        skill1=form_data.get('skill1', ''),
                        skill2=form_data.get('skill2', ''),
                        skill3=form_data.get('skill3', ''),
                        skill4=form_data.get('skill4', ''),
                        hobbies1=form_data.get('hobbies1', ''),
                        hobbies2=form_data.get('hobbies2', ''),
                        hobbies3=form_data.get('hobbies3', ''),
                        hobbies4=form_data.get('hobbies4', ''),
                        reference=form_data.get('reference', '')
                    )
                    if photo:
                        cv_instance.photo = photo
                    cv_instance.save()
                    messages.success(request, "CV created successfully")
            except Exception as e:
                print(e)
                # Handle exceptions if any
                return HttpResponse("An error occurred while processing your request.")

            return redirect('view_cv')

        else:
            return render(request, 'jobapp/employee/update_cv.html', {'cv_instance': cv_instance})
        
        

    except Exception as e:
        # Handle exceptions if any
        return HttpResponse("An error occurred while processing your request.")






@user_is_employee
def job_save(request, job_id):

    job = get_object_or_404(JobDetail, pk = job_id)
    saved_job = SavedJobs.objects.filter(user=request.user, job=job).first()
    if saved_job:
        saved_job.delete()
        messages.warning(request, "Bookmark removed")
    else:
        SavedJobs.objects.create(user=request.user, job=job)
        messages.success(request, "Bookmark added successfully")
    return redirect('saved_jobs')


@user_is_employee
def jobs_saved(request):
    current_user = request.user
    saved_jobs = SavedJobs.objects.filter(user=current_user)

    saved_job_ids = list(saved_jobs.values_list('job_id', flat=True))
    job_details = JobDetail.objects.filter(id__in=saved_job_ids)
    context={
        'search_results':job_details,
        'saved_job_ids': saved_job_ids
    }
    print(job_details)
    print(saved_job_ids)
    return render (request, 'jobapp/saved_jobs.html', context)


@user_is_employee
def job_apply(request, job_id):

    job = get_object_or_404(JobDetail, pk=job_id)
    AppliedJobs.objects.create(user=request.user, job=job)
    messages.success(request, "Job Applied Successfully")

    return redirect('home')



@user_is_employee
def jobs_applied(request):
    current_user = request.user
    
    applied_jobs = AppliedJobs.objects.filter(user=current_user)
    applied_job_ids = list(applied_jobs.values_list('job_id', flat=True))
    applied_job_details = JobDetail.objects.filter(id__in=applied_job_ids)
    saved_job_ids = list(SavedJobs.objects.filter(user=current_user).values_list('job_id', flat=True))
    
    context = {
        'applied_jobs': applied_jobs,
        'applied_job_details': applied_job_details,
        'saved_job_ids': saved_job_ids
    }
    # print(applied_job_details)
    # print(applied_jobs)
    
    return render(request, 'jobapp/jobs_applied.html', context)




# employeer views

@login_required
@user_is_employer
def job_post(request):
    # employer= request.user
    if request.method == 'POST':
        employer = request.user

        position = request.POST['position']
        location = request.POST['location']
        website = request.POST['website']
        description = request.POST['description']
        job_category = request.POST['job_category']
        job_level = request.POST['job_level']
        no_vac = request.POST['no_vac']
        emp_type = request.POST['emp_type']
        offered_salary = request.POST['offered_salary']
        apply_before = request.POST['apply_before']
        edu_level = request.POST['edu_level']
        exp_req = request.POST['exp_req']
        Professional_skill_req = request.POST['Professional_skill_req']
        job_desc1 = request.POST['job_desc1']
        job_desc2 = request.POST['job_desc2']
        job_desc3 = request.POST['job_desc3']
        job_desc4 = request.POST['job_desc4']
        job_desc5 = request.POST['job_desc5']
       
        other_spec1 = request.POST['other_spec1']
        other_spec2 = request.POST['other_spec2']
        other_spec3 = request.POST['other_spec3']
        other_spec4 = request.POST['other_spec4']
        other_spec5 = request.POST['other_spec5']

        job_detail = JobDetail.objects.create(
            employer=employer,
            position=position,
            website=website,
            address=location,
            description=description,
            category=job_category,
            level=job_level,
            number_vacancy=no_vac,
            emp_type = emp_type,
            salary=offered_salary,
            date=apply_before,
            edu_level=edu_level,
            exp_req=exp_req,
            skill_req=Professional_skill_req,
            job_desc1=job_desc1,
            job_desc2=job_desc2,
            job_desc3=job_desc3,
            job_desc4=job_desc4,
            job_desc5=job_desc5,
            other_spec1=other_spec1,
            other_spec2=other_spec2,
            other_spec3=other_spec3,
            other_spec4=other_spec4,
            other_spec5=other_spec5    
        )
        return redirect('view_dashboard')


    return render(request, 'jobapp/employer/post_job.html')


@login_required
@user_is_employer


def dashboard_view(request):
    current_user = request.user
    jobs = JobDetail.objects.filter(employer=current_user)
    
    context = {
        'jobs': jobs,
    }
    return render(request, 'jobapp/employer/dashboard.html', context)


@login_required
@user_is_employer
def applied_candidate_view(request, job_id):
    job = get_object_or_404(JobDetail, id=job_id)
    applied_users = CustomUser.objects.filter(appliedjobs__job=job)
    
    context = {
        'job': job,
        'job_position': job.position,
        'applied_users': applied_users
    }
    return render(request, 'jobapp/employer/applied_candidate.html', context)




@login_required
@user_is_employer
def job_edit_view(request, job_id):
    job_detail = get_object_or_404(JobDetail, id=job_id)

    if request.user == job_detail.employer:
        if request.method == 'POST':
            job_detail.position = request.POST['position']
            job_detail.address = request.POST['location']
            job_detail.website = request.POST['website']
            job_detail.description = request.POST['description']
            job_detail.category = request.POST['job_category']
            job_detail.level = request.POST['job_level']
            job_detail.number_vacancy = request.POST['no_vac']
            job_detail.emp_type = request.POST['emp_type']
            job_detail.salary = request.POST['offered_salary']
            job_detail.date = request.POST['apply_before']
            job_detail.edu_level = request.POST['edu_level']
            job_detail.exp_req = request.POST['exp_req']
            job_detail.skill_req = request.POST['Professional_skill_req']
            job_detail.job_desc1 = request.POST['job_desc1']
            job_detail.job_desc2 = request.POST['job_desc2']
            job_detail.job_desc3 = request.POST['job_desc3']
            job_detail.job_desc4 = request.POST['job_desc4']
            job_detail.job_desc5 = request.POST['job_desc5']
        
            job_detail.other_spec1 = request.POST['other_spec1']
            job_detail.other_spec2 = request.POST['other_spec2']
            job_detail.other_spec3 = request.POST['other_spec3']
            job_detail.other_spec4 = request.POST['other_spec4']
            job_detail.other_spec5 = request.POST['other_spec5']
            
            job_detail.save()
            
            return redirect('view_dashboard')
        else:
            show = 1
            context = {'job_detail': job_detail, 'show':show}
            return render(request, 'jobapp/employer/post_job.html', context)
    else:
        return HttpResponse("Unauthorized User")


@login_required
@user_is_employer
def job_delete_view(request, job_id ):
    job_detail = get_object_or_404(JobDetail, id=job_id)
    if request.user == job_detail.employer:
        job_detail.delete()

    return redirect('view_dashboard')



@user_is_employer
def view_cv(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    cv_instance = get_object_or_404(cv, user=user)
    current_user_account_type = request.user.account

    context = {
        'cv_instance': cv_instance,
        'current_user_account_type': current_user_account_type
    }
    print(current_user_account_type)
    
    return render(request, 'jobapp/employee/cv.html', context)