from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.core.checks import messages
from .models import Student, Teacher
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import path
from .forms import CSVUploadForm
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'nama', 'gender', 'kelas', 'voted')
    list_filter = ('kelas', 'voted')
    seacrh_fields = ('user', 'nama', 'voted')
    def add_student_view(self, request):
        form = CSVUploadForm
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                delimiter = form.cleaned_data['delimiter']
                csv_delimiter = ",;|"
                if delimiter not in csv_delimiter:
                    return redirect('admin:index')
                csv_file = form.cleaned_data['csv_file']
                if not csv_file.name.endswith('.csv'):
                    messages.warning(request, 'The File Format is Wrong!')
                    return redirect('admin:add_student')
                data = csv_file.read().decode('utf-8')
                csv_data = data.split('\n')
                for data in csv_data[1:]:
                    if len(data) <= 2:
                        continue
                    fields = data.split(delimiter)
                    print(fields)
                    user = User.objects.update_or_create(
                        username = str(fields[1].strip(' "')),
                        defaults= {
                            'password' : 'TestPassword!'
                        }
                    )
                    cur_user = User.objects.get(username = str(fields[1].strip(' "')))
                    cur_user.set_password(str(fields[2].strip(' "')))
                    cur_user.save()
                    student = Student.objects.update_or_create(
                        user = User.objects.get(username = fields[1].strip(' "')),
                        defaults= {
                            'nama' : fields[3].strip(' "'),
                            'gender' : fields[4].strip(' "'),
                            'kelas' : int(fields[7].strip(' "'))
                        }
                        
                    )
                return redirect('admin:index')
        return render(request, 'admin/add_student.html', {'form':form})

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('add_student', self.add_student_view),
        ]
        return my_urls + urls

class TeacherAdmin(ModelAdmin):
    list_display = ('user', 'nama', 'gender', 'mengajar', 'voted')
    list_filter = ('voted',)
    seacrh_fields = ('user', 'nama', 'voted')

    def add_teacher_view(self, request):
        form = CSVUploadForm
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                delimiter = form.cleaned_data['delimiter']
                csv_delimiter = ",;|"
                if delimiter not in csv_delimiter:
                    return redirect('admin:index')
                csv_file = form.cleaned_data['csv_file']
                if not csv_file.name.endswith('.csv'):
                    messages.warning(request, 'The File Format is Wrong!')
                    return redirect('admin:add_teacher')
                data = csv_file.read().decode('utf-8')
                csv_data = data.split('\n')
                for data in csv_data[1:]:
                    if len(data) <= 2:
                        continue
                    fields = data.split(delimiter)
                    print(fields)
                    user = User.objects.update_or_create(
                        username = str(fields[1].strip(' "')),
                        defaults= {
                            'password' : 'TestPassword!'
                        }
                    )
                    cur_user = User.objects.get(username = str(fields[1].strip(' "')))
                    cur_user.set_password(str(fields[2].strip(' "')))
                    cur_user.save()
                    teacher = Teacher.objects.update_or_create(
                        user = User.objects.get(username = fields[1].strip(' "')),
                        defaults= {
                            'nama' : fields[3].strip(' "'),
                            'gender' : fields[4].strip(' "'),
                            'mengajar' : fields[5].strip(' "')
                        }
                    )
                return redirect('admin:index')
        return render(request, 'admin/add_student.html', {'form':form})

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('add_teacher', self.add_teacher_view),
        ]
        return my_urls + urls

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)