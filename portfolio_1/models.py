from django.db import models

class About(models.Model):
    """
    Informations générales sur la personne.
    Il ne devrait y avoir qu'une seule instance (singleton).
    """
    name = models.CharField(max_length=100, verbose_name="Nom complet")
    title = models.CharField(max_length=150, verbose_name="Titre (ex: Développeur web)")
    description = models.TextField(verbose_name="Description à propos de vous")
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True, verbose_name="Lien LinkedIn")
    github_url = models.URLField(blank=True, verbose_name="Lien GitHub")

    def __str__(self):
        return f"À propos de {self.name}"

    class Meta:
        verbose_name = "À propos"
        verbose_name_plural = "À propos"


class Project(models.Model):
    """
    Un projet dans la section 'Mes projets'.
    """
    title = models.CharField(max_length=200, verbose_name="Titre du projet")
    description = models.TextField(verbose_name="Description du projet")
    created_at = models.DateField(auto_now_add=True, verbose_name="Date d'ajout")
    link = models.URLField(blank=True, verbose_name="Lien vers le projet (optionnel)")
    techno = models.TextField(verbose_name= "Technologie utiliser",default="Non spécifié")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-created_at']