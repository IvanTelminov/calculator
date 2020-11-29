from django.http import HttpResponse


def index(request, *args, **kwargs):
    html = 'Hello world'
    html += 'Ыщо одын'
    response = HttpResponse(html)
    return response


def test(request, *args, **kwargs):
    return HttpResponse('teeeeeeeest')

