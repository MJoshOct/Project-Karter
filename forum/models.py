from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    tags = models.ManyToManyField(Tag, related_name="questions", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Question.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer by {self.author} on {self.question}"


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    # Generic relation (can comment on Question or Answer)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)

    def __str__(self):
        return f"Comment by {self.author}"


class Vote(models.Model):
    VOTE_TYPES = (
        (1, "Upvote"),
        (-1, "Downvote"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="votes", null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="votes", null=True, blank=True)
    value = models.SmallIntegerField(choices=VOTE_TYPES)

    class Meta:
        unique_together = ("user", "question", "answer")  # prevent double-voting

    def __str__(self):
        target = self.question if self.question else self.answer
        return f"{self.user} voted {self.value} on {target}"
