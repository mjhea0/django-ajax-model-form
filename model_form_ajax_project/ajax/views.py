from django.shortcuts import HttpResponse, render
from ajax.models import FeedBack
from ajax.forms import FeedBackForm
import json


def feedback(request):
    # if request.method == "POST":
    #     form = FeedBackForm(request.POST)
    #     message = 'Oops!'
    #     if(form.is_valid()):
    #         message = request.POST['title']
    #     return HttpResponse(json.dumps({'message': message}))

    return render(request, 'index.html', {'form': FeedBackForm()})


def create_feedback(request):

    feedback_text = request.POST.get('the_post_text')
    feedback_description = request.POST.get('the_post_description')
    response_data = {}

    print feedback_text
    print feedback_description

    feedback = FeedBack(
        title=feedback_text, description=feedback_description
    )
    feedback.save()

    response_data['result'] = 'Success!'
    response_data['title'] = feedback.title
    response_data['desc'] = feedback.description

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
