from Django_projects.forms import OfficeForm


def post_form(request):
    return {
        'office_form': OfficeForm(data={'office': request.session.get('office_id')})
    }