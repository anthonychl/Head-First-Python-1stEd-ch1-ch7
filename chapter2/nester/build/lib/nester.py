"""
print_lol() prints lists that may or may not include nested lists

the_list  la lista q queremos imprimir
indent    True o False si queremos q indente o no
level     nivel de indentacion, cuantos tabs de indentacion queremos
fh        archivo en donde queremos guardar los datos, si no se especifica el archivo, el valor por defecto es sys.stdout para q siga imprimiendo en pantalla
"""
import sys
def print_lol(the_list,indent=False,level=0,fh=sys.stdout): # valores por defecto en caso de q no introduzcan ninguno en esos argumentos
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            if indent:
                print('\t'*level,end='',file=fh)
            print(each_item,file=fh)
            

