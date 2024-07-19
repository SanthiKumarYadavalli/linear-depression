from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from complaints.serializer import ComplaintSerializer
from users.serializer import UserSerializer
from users.models import User
from complaints.models import Complaint


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class ComplaintCreate(generics.ListCreateAPIView):
    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        complaints = Complaint.objects.filter(user=user)
        return complaints

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ComplaintDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ComplaintSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Complaint.objects.filter(user=self.request.user)

    # Need check for role is it Admin or Student
    def perform_update(self, serializer):
        serializer.save(status=True)
