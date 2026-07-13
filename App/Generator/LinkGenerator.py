import string
import random

def generateLink():
    caracteres = string.ascii_letters + string.digits

    link = "".join(random.choices(caracteres, k=8))
    return(link)

