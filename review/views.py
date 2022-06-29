from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from review.models import Review
from review.serialize import ReviewSerializer


class ReviewList(APIView):
    def get(self, request):  # 기본 실행
        qs = Review.objects.all()
        serializer = ReviewSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    def get(self, request, pk):  # pk 전달해서 호출하면 실행
        qs = Review.objects.get(id=pk)
        serializer = ReviewSerializer(qs, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        qs = Review.objects.get(id=pk)
        serializer = ReviewSerializer(qs, data=request.data, partial=True)  # 특정 필드(score, contents)만 수정 가능
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        qs = Review.objects.get(id=pk)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

