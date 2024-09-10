from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
# class MemoView(APIView):
category = {

}


class MemoView(APIView):
    def get(self, request, **kwargs):
        print("")
        data = {"message": "result"}
        return Response(data)


class UserMemoCategoryView(APIView):
    def get(self, request, **kwargs):
        user_categories = ['1', '2', '3', '4', '5', '6']
        return Response({
            "categories" : user_categories
        })
