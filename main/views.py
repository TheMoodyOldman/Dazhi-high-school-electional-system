from django.shortcuts import render
from django.views.generic import *
from .models import Election, HouSyuanRen
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# 首頁，列出所有選舉
class ListElections(ListView):
    model = Election


# 創建選舉
class CreateElection(LoginRequiredMixin, CreateView):
    model = Election
    fields = ['name', 'content']
    # fields = ['name', 'content', 'date_start'] 日期不知道怎麼處理，先放著
    success_url = '../'


# 刪除選舉
class DeleteElection(LoginRequiredMixin, DeleteView):
    model = Election

    def get_redirect_url(self, *args, **kwargs):
        return '../../'


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
    'gender', 'party', 'academy', 'seniority', 'politics']

    def get_redirect_url(self, *args, **kwargs):
        return "../candidate" + self.id + "/"


# 編輯選舉公報
class EditElectionBulletin(LoginRequiredMixin, UpdateView):
    model = HouSyuanRen
    fields = ['first_name', 'name', 'birth', 
    'gender', 'party', 'academy', 'seniority', 'politics']
    success_url = "../"


# 退選
class WithdrawElection(LoginRequiredMixin, DeleteView):
    model = HouSyuanRen
    success_url = "../../"


# 投票
class Vote(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return '../'