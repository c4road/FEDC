from django.db import models
from django.core.validators import FileExtensionValidator

from mixins.models import CreationModificationDateMixin
from conectores.models import Compania
# Create your models here.


# Allowed files by extension
VALID_FILE_EXTENSIONS = ['pdf','jpeg','jpg','png', 'xls', 'xml', 'doc', 'docx']

class Intercambio(CreationModificationDateMixin):
    """
    Clase para el modelo de intercambio
    @author Alberto Rincones (alberto at timg.cl)
    @copyright TIMG
    @date 01-04-19 (dd-mm-YY)
    @version 1.0
    """

    ## codigo_email = models.IntegerField(null=True, default=0)
    receptor = models.ForeignKey(Compania, on_delete=models.CASCADE, blank=True, null=True)
    remisor = models.CharField(max_length=128,blank=True, null=True)
    email_remisor = models.EmailField(blank=True, null=True)
    fecha_de_recepcion = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    cantidad_dte = models.IntegerField(null=True, default=0)
    titulo = models.CharField(max_length=128,blank=True, null=True)
    contenido = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (("fecha_de_recepcion", "receptor", "email_remisor"),)
            

class DteIntercambio(models.Model):
    """
    Clase para el modelo de dte en el intercambio
    @author Alberto Rincones (alberto at timg.cl)
    @copyright TIMG
    @date 01-04-19 (dd-mm-YY)
    @version 1.0
    """
    
    def get_upload_to(self, filename):
        return "intercambio_dte/%s/%s" % (str(self.id_intercambio.receptor.rut), filename)

    id_intercambio = models.ForeignKey(Intercambio, on_delete=models.CASCADE, blank=True, null=True)
    dte_attachment = models.FileField(upload_to=get_upload_to, validators=[FileExtensionValidator(VALID_FILE_EXTENSIONS)])
