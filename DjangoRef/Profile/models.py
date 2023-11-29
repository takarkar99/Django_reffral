from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True, related_name='ref_code')
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user}, {self.code}"
    

    def get_recommended_profiles(self):

        obj = Profile.objects.all()

        li = [ p for p in obj if p.recommended_by == self.user]

        return li

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
        super().save( *args, **kwargs)