from django.db import models


class BlockModel(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    user = models.OneToOneField(
        'user.UserModel',  
        on_delete=models.CASCADE,
        related_name='block_user',
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class PostModel(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=140, blank=True)
    created_at = models.DateField(auto_now_add=True)
    block =  models.ForeignKey(
        'block.BlockModel',  
        on_delete=models.CASCADE,
        related_name='post_block',
    )

    def __str__(self):
        return self.title
    

class SubscriptionModel(models.Model):
    user = models.ForeignKey(
        'user.UserModel',  
        on_delete=models.CASCADE,
        related_name='subscription_user',
    )
    block = models.ForeignKey(
        'block.BlockModel',  
        on_delete=models.CASCADE,
        related_name='subscription_block',
    )
    read_status = models.BooleanField(db_default=False)
    