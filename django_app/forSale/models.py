from django.db import models

# standardizing image sizes
from stdimage.models import StdImageField

# Create your models here.
class ItemsForSale(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    # With StdImage: adding a thumbnail, cropping the image
    image = StdImageField(upload_to='items_for_sale_images',
                                    variations={
                                    'thumbnail': {"width":100, "height":100, "crop":True},
                                    'large': (400, 300)
                                    })

    # mutliple ways of doing this, for this template, seems to be the best to have
    # it explicitly defined to enter it in cent format (to ensure entry is thoughtout)
    price = models.IntegerField(help_text="Use the following format: 1000 for $10.00")

    # displaying the price, since it needs to be displayed in dollar.cent format
    def price_displayed(self):
        return "{0:.2f}".format(self.price / 100)
