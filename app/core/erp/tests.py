# from pathlib import Path
# import sys
# sys.path.append(str(Path(__file__).parent.parent.parent))
# from config.asgi import *
# from core.erp.models import Client

#esto es como hacer un SELECT * FROM TABLA
#los datos se insertaron directamente desde SQLLite
# query = Client.objects.all()
# print(query)

#insertar un nuevo registro a la tabla cliente
# # nombre = Client()
# # nombre.first_name = 'Javier'
# # nombre.last_name = 'Mogrvejo'
# # nombre.save()
# estado = Client.objects.all()
# #t = Client.objects.get(id=18)
# nombre = Client()
# # print(t.first_name)
# #nombre.first_name = 'Javierjihuhy'
# nombre.first_name = 'HolaMundo'
# #nombre.save()
# print(estado)

#eliminar un registro de la tabla cliente
# try:
#     t = Client.objects.get(id=1)
#     t.delete()
# except Exception as e:
#     print("error: ", e)

# t = Client.objects.filter(first_name__icontains='javier')

# print(t)
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from config.asgi import *
from core.erp.models import *


data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
        'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
        'Grasas, aceite y mantequilla']

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado registro N°{}'.format(cat.id))