from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from ware.models import Ware
from ware.serialize import WareSerializer


class WareViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Ware.objects.all()
    serializer_class = WareSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(seller=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 오버라이딩
    def get_queryset(self):
        qs = super().get_queryset()

        search_name = self.request.query_params.get('name',)

        if search_name:
            qs = qs.filter(name__icontains=search_name)
            # name : 정확히 일치
            # name__contains : 포함되는 글자, 대소문자 구분o
            # name__icontains : 포함되는 글자, 대소문자 구분x

        return qs

    @action(detail=False, methods=['get'], url_path="search/(?P<name>[^/.]+)")  # 정규표현식
    def search(self, request, name=None):
        qs = self.get_queryset().filter(name__icontains=name)
        serializer = self.get_serializer(qs, many=True)

        return Response(serializer.data)
