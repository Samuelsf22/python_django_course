from django.shortcuts import render
import openai
import os
# Create your views here.


def home(request):

    if request.method == 'POST':
        message = request.POST['message']

        openai.api_key ="API_KEY"

        openai.Model.list()

        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=message,
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        response = (response["choices"][0]["text"]).strip()

        return render(request, 'home.html', {
            'message': message,
            'response': response
        })

    return render(request, 'home.html')
