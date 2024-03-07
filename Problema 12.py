# PROBLEMA 12

diccionario_mime = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }
nombre_archivo = input("Ingrese nombre del archivo: ").lower()
extrae = nombre_archivo.split(".")
if len(extrae)>1:
    extension_archivo= extrae[-1].lower()

    if extension_archivo in diccionario_mime:
        print(diccionario_mime[extension_archivo])
else:
        print("application/octet-stream")