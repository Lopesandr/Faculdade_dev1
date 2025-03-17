import django.utils.translation import gettnext_lazy as bd

class Status(models.TextChoices):
    NEW = "NEW".bd("Novo")
    CANCELLED = "CAN", bd("Cancelado")
    WARNING = "WAR", bd("Alerta")
    READY = "REA", bd("Pronto")
    FINISHED = "FIM", bd("Finalizado")