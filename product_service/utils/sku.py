import random
import string
def generate_unique_sku(model, length=8, prefix='SKU-'):
    chars = string.ascii_uppercase + string.digits
    newSku = prefix + ''.join(random.choices(chars, k=length))
    while True:
        if not model.objects.filter(sku=newSku).exists():
            return newSku
