import random
import string
def generate_code_invoice(model,length=10, prefix='INVOICE-'):
    chars = string.ascii_uppercase + string.digits
    newCodeInvoice = prefix + ''.join(random.choices(chars, k=length))
    while True:
        if not model.objects.filter(invoice_code=newCodeInvoice).exists():
            return newCodeInvoice
