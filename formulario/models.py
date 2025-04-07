from django.db import models

class DadosDiabetes(models.Model):
    id = models.AutoField(primary_key=True)  # ID principal auto-incrementável
    gravidez = models.IntegerField(verbose_name="Número de gestações", null=True, blank=True) # Permitindo valores nulos e em branco
    glicose = models.IntegerField(verbose_name="Nível de glicose")
    pressao = models.IntegerField(verbose_name="Pressão arterial diastólica")
    espessura_pele = models.IntegerField(verbose_name="Espessura da dobra cutânea do tríceps")
    insulina = models.IntegerField(verbose_name="Nível de insulina")
    imc = models.FloatField(verbose_name="Índice de Massa Corporal")
    pedigree = models.FloatField(verbose_name="Histórico familiar (Diabetes Pedigree Function)")
    idade = models.IntegerField(verbose_name="Idade")
    resultado = models.IntegerField(verbose_name="Diagnóstico (0 = não, 1 = sim)", default=0)

    class Meta:
        app_label = 'formulario'
        db_table = 'dados_diabetes'

    def __str__(self):
        return f"Paciente {self.id} - Idade {self.idade}"
