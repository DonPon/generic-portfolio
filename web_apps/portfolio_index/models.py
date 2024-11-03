# index/models.py
import uuid
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon_file = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class PersonalDetails(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    linkedin_url = models.URLField(verbose_name='Linkedin url', blank=True)
    github_url = models.URLField(verbose_name='github url', blank=True)
    skills_tools = models.ManyToManyField(Skill, blank=True)

    class Meta:
        verbose_name = "Personal Details"
        verbose_name_plural = "Personal Details"


class PortfolioItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Short description")
    image = models.ImageField(upload_to='', blank=True)
    url = models.URLField(blank=True)
    details = models.TextField(verbose_name="Extensive details", blank=True)

    class Meta:
        verbose_name = "Portfolio projects"
        verbose_name_plural = "Portfolio projects"

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    user_agent = models.TextField()
    visit_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Website visit"
        verbose_name_plural = "Website visits"

    def __str__(self):
        return f"IP: {self.ip_address} ({self.region} - {self.city}) at {self.visit_time}"

