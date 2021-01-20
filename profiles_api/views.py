from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings



from profiles_api import permissions




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



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello Message"""

        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial update)",
            "Automatically maps to urls using routers",
            "provides more functionality with less code",
                      ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a New Hello Message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'name': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an objects by its id"""
        return Response({'Http_Method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'Http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'Http-Method': 'patch'})

    def destroy(self, request, pk=None):
        """Handle deleting of an object"""
        return Response({'HTTP-Method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )

class UserLoginApiView(ObtainAuthToken):
    """Handle creating authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES