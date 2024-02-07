from django.db import models


class BlockModel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(
        "user.UserModel",  
        on_delete=models.CASCADE,
        related_name="block_for_user",
    )
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = "block"
    

class PostModel(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=140, blank=True)
    created_at = models.DateField(auto_now_add=True)
    block =  models.ForeignKey(
        "block.BlockModel",  
        on_delete=models.CASCADE,
        related_name="post_for_block",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "post"
    

class BlockUserModel(models.Model):
    user = models.ForeignKey(
        "user.UserModel",  
        on_delete=models.CASCADE,
        related_name="block_user_for_user",
    )
    block = models.ForeignKey(
        "block.BlockModel",  
        on_delete=models.CASCADE,
        related_name="block_user_for_block",
    )
    
    class Meta:
        db_table = "block_user"
    

class PostUserModel(models.Model):
    post = models.ForeignKey(
        "block.PostModel",  
        on_delete=models.CASCADE,
        related_name="post_user_for_post",
    )
    user = models.ForeignKey(
        "user.UserModel",  
        on_delete=models.CASCADE,
        related_name="post_user_for_user",
    )
    read_status = models.BooleanField(db_default=False)
    
    class Meta:
        db_table = "post_user"   
    