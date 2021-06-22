from django.db import models

class baterias (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	modelo = models.CharField(default = "",null=True,max_length = 200)
	precio = models.CharField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	marca = models.CharField(default = "",null=True,max_length = 200)
	imagen = models.ImageField(upload_to = "imagen" , null="True")

	def __str__ (self):
		return self.nombre

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)


class filtros (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	modelo = models.CharField(default = "",null=True,max_length = 200)
	precio = models.CharField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	marca = models.CharField(default = "",null=True,max_length = 200)
	imagen = models.ImageField(upload_to = "imagen" , null="True")

	def __str__ (self):
		return self.nombre

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)


class aceites (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	modelo = models.CharField(default = "",null=True,max_length = 200)
	precio = models.CharField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	marca = models.CharField(default = "",null=True,max_length = 200)
	imagen = models.ImageField(upload_to = "imagen"  , null="True")

	def __str__ (self):
		return self.nombre
	
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('aceites', related_name='comments', on_delete=models.CASCADE) 
    author = models.CharField(max_length=200)
    text = models.TextField()

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text