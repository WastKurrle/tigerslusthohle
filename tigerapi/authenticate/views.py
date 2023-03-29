from rest_framework.views import APIView
from rest_framework.response import Response

password = 'tigerslusthöhle'

class AuthenticateView(APIView):
    def post(self, request):
        passwd = request.data['password']
        if passwd == password:
            return Response(status=200)

        return Response(status=403)
