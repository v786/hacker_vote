from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# Create your views here.

from .models import Candidate, Vote, Expertise

class IndexView(generic.ListView):
    template_name = 'hackers/index.html'
    context_object_name = 'latest_candidate_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Candidate.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Candidate
    template_name = 'hackers/detail.html'


class ResultsView(generic.DetailView):
    model = Candidate
    template_name = 'hackers/results.html'

def vote(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    try:
        selected_choice = candidate.vote_set.get(pk=request.POST['vote'])
    except (KeyError, Vote.DoesNotExist):
        # Redisplay the candidate voting form.
        return render(request, 'hackers/detail.html', {
            'candidate': candidate,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.count += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('hackers:results', args=(candidate.id,)))