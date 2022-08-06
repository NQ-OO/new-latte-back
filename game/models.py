from django.db import models

# Create your models here.

class Scene(models.Model):
    id=models.IntegerField(default=0,primary_key=True,help_text="장면 고유 번호")
    Name=models.CharField(max_length=255,null=True,blank=True, help_text="장면 이름")
    NextScenes=models.ManyToManyField('self',null=True,blank=True,symmetrical=False, help_text="다음 장면들")
    # 서로를 가리키게 되고, 반대 방향으로 참조할 수 있다.
    #History=models.OneToOneField('self',null=True,blank=True,on_delete=models.SET_NULL,help_text="이전 장면")
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Name)

class Scene_picture(models.Model):
    Scene = models.ForeignKey(Scene, on_delete=models.CASCADE, help_text="장면")
    Pictures=models.ImageField(upload_to="",null=True,blank=True, help_text="삽화")
    Name=models.CharField(max_length=255,default="씬 번호", help_text="이미지 이름")
    Comment=models.CharField(max_length=255,null=True,blank=True,  help_text="코멘트")
    pub_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.Name)

class Scene_text(models.Model):
    Scene = models.ForeignKey(Scene, on_delete=models.CASCADE, help_text="장면")
    Title = models.CharField(max_length=255,default="제목", help_text="제목")
    Narrative=models.CharField(max_length=4096,null=True,blank=True, help_text="내용")
    pub_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.Title)

class Turning_point(models.Model):
    Scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    Name=models.CharField(max_length=255,default="씬 번호",help_text="제목")
    Question=models.CharField(max_length=1024, help_text="질문")

    Player_Answer=models.CharField(max_length=1024,null=True,blank=True, help_text="플레이어 응답")
    Story_Option=models.IntegerField(default=0,help_text="선택지 번호",null=True,blank=True)
    
    pub_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.Name)

