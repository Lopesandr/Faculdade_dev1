from django.core.validators import MinValueValidator, MaxValueValidator

from .base_model import BaseModel
from django.db import models

class Example(BaseModel): 
    descricao = models.CharField(
        max_length=200, null=False, blank=False,
        help_text= "Descrição de um exemplo",
        verbose_name = "Descrição"
    )

    qualidade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text = "Valor para qualidade do exemplo. Entre 0 e 100.",
        verbose_name = "Qualidade"
    )

    balance = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        max_digits=5,
        decimal_places = 2,
        default = 0.00,
        help_text = "Valor para o balançeamento",
        verbose_name = "Balaço"

    )