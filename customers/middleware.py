from django.http import HttpResponseForbidden
import requests


class CepValidate:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_view(self, request, func, args, kwargs):
        cep = request.POST.get('CEP')
        if cep is not None:
            cep_serializer = cep.replace("-", "").replace(".", "").replace(" ", "")
            if len(cep_serializer) == 8:
                viacep = requests.get(f'https://viacep.com.br/ws/{cep_serializer}/json/')
                cep_info = viacep.json()
                if "erro" in cep_info:
                    return HttpResponseForbidden("CEP doesn't exist")
            if len(cep_serializer) < 8:
                return HttpResponseForbidden("Invalid CEP")

        return None
