cadena = "mi cadena de texto"
print(cadena[0],cadena[-1])
#cadena[0]="M"   error al no poder inmutar strings

otra_cadena=""
for caracter in cadena:
    otra_cadena+=caracter
print(otra_cadena)

#caracteres especiales \", \', \n, \t, \\

#dir(str): list of attributes

s="esto programandoy"

print("abn".isalpha())
print("t/".isalpha())
print("34".isdigit())

print(s.startswith("st"))
print(s.endswith("do"))

#print(s.find("y"))
#print(s.find("y p"))

#print(s.index("y",4,11))
#print(s.index("p",5,10))

s2=s.split(" ")
print(s2)
s3="#".join(s2) #join, une elemento con elemento de str (s) o lista (s2)
print(s3)
print(s.replace(" ","**"))
print(s) #no actualiza variable original

nombre = "Juan Perez"
nota = 4.5
if nota >= 4.0:
    resultado="aprobado"
else:
    resultado="reprobado"

print(f"Hola {nombre}, estas {resultado}. Tu nota fue un {nota}.") #print f - funciones desde un print

class EMail:
    def __init__(self, from_addr, to_addr, subject,message):
        self.from_addr=from_addr
        self.to_addr=to_addr
        self.subject=subject
        self.message=message

email=EMail("a@ejemplo.com","b@ejemplo.com","Tienes un correo", "\nEl mensaje es inutil\n\nSaludos")

print(f"""
From: <{email.from_addr}>
To: <{email.to_addr}>
Subject: {email.subject}
{email.message}""")

print("s"+email.from_addr)

#str.format() permit trabajar con funciones
correo_1="a@ejemplo.com"
correo_2="b@ejemplo.com"

saludos_entre_usuarios = "Hola {saludado}, te saluda el usuario {saludador}"
print(saludos_entre_usuarios.format(saludado=correo_1,saludador=correo_2))

compra =[('leche',2,120),('pan',3.5,800),('arroz',1.75,960)]
print("PRODUCTO CANTIDAD PRECIO SUBTOTAL")
for producto,precio,cantidad in compra:
    subtotal=precio*cantidad
    #print (f"{producto}  {cantidad} ${precio} ${subtotal}") #f" va junto
    print (f"{producto:8.8s} {cantidad:^9d} ${precio:<8.2f}  ${subtotal:>7.2f}") #f" va junto
#8s: 8 caracteres maximo
#^9d: 9 caracters, se rellenan con espacio o 0
#8.2f: 8 caracteres con 2 floats
#^centrado, <,> alineado