from django.shortcuts import render
from django.views.generic import *
from .models import Election, HouSyuanRen
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django import forms

# Create your views here.

# 首頁，列出所有選舉
class ListElections(ListView):
    model = Election


# 創建選舉
class CreateElection(LoginRequiredMixin, CreateView):
    model = Election
    fields = ['name', 'content', 'date_start']
    success_url = '../'

    def get_form(self): # 讓用戶輸入日期
        form = super().get_form()
        form.fields['date_start'].widget = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        return form


# 刪除選舉
class DeleteElection(LoginRequiredMixin, DeleteView):
    model = Election
    success_url = reverse_lazy('mainpage')


# 列出單一選舉的所有候選人
class DetailElection(DetailView):
    model = Election

    def get_context_data(self, **kwargs):
        super_dict = super().get_context_data(**kwargs)
        super_dict['HouSyuanRen'] = HouSyuanRen.objects.filter(election_id = self.object.id)
        return super_dict


# 查看特定候選人的選舉公報
class ElectionBulletin(DetailView):
    model = HouSyuanRen


# 參選
class RunElection(CreateView):
    model = HouSyuanRen
    fields = ['first_name', 'name', 'birth', 
    'gender', 'party', 'academy', 'seniority', 'politics', 'pic']


    def get_form(self): # 讓用戶輸入日期
        form = super().get_form()
        form.fields['birth'].widget = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        return form
    
    def form_valid(self, form): # 表單驗證
        form.instance.election_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return "../candidate" + str(self.object.id) + "/"


# 編輯選舉公報
class EditElectionBulletin(LoginRequiredMixin, UpdateView):
    model = HouSyuanRen
    fields = ['first_name', 'name', 'birth', 
    'gender', 'party', 'academy', 'seniority', 'politics', 'pic']
    success_url = "../"

    def get_form(self): # 輸入日期
        form = super().get_form()
        form.fields['birth'].widget = forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        return form


# 退選
class WithdrawElection(LoginRequiredMixin, DeleteView):
    model = HouSyuanRen
    success_url = reverse_lazy('detail_ele')


# 投票
class Vote(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return '../'