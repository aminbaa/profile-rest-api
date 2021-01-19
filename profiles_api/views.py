from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "uses HTTP methods as function (get, post, pathc, put, delete)",
            "is similar to a traditional Django View",
            "gives you the most control over yor application logic",
            "is mapped manually to urls"
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request, format=None):
        """Creates A Hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle Updating an object"""
        return Response({'Method': 'Put'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'Method': 'Patch'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'Method': 'Delete'})



