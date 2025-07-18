#!/usr/bin/env python3
"""
Script para vincular plantilla de Word con resumen de documentos
"""

import csv
import os
import shutil
from datetime import datetime

class GestorDocumentos:
    def __init__(self, archivo_resumen="resumen_documentos.csv", 
                 plantilla="plantilla_documento.docx"):
        self.archivo_resumen = archivo_resumen
        self.plantilla = plantilla
        self.documentos = []
        self.cargar_resumen()
    
    def cargar_resumen(self):
        """Carga el resumen de documentos desde el archivo CSV"""
        try:
            with open(self.archivo_resumen, 'r', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                self.documentos = list(lector)
            print(f"Cargados {len(self.documentos)} documentos del resumen")
        except FileNotFoundError:
            print(f"Archivo {self.archivo_resumen} no encontrado. Creando nuevo...")
            self.crear_resumen_vacio()
    
    def crear_resumen_vacio(self):
        """Crea un archivo de resumen vacío"""
        cabeceras = [
            'Número Documento', 'Título', 'Autor', 'Fecha Creación', 
            'Estado', 'Prioridad', 'Tipo Documento', 'Ubicación Archivo',
            'Última Modificación', 'Observaciones'
        ]
        
        with open(self.archivo_resumen, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(cabeceras)
        
        self.documentos = []
    
    def generar_numero_documento(self):
        """Genera un nuevo número de documento único"""
        if not self.documentos:
            return "DOC-001"
        
        numeros = []
        for doc in self.documentos:
            num_doc = doc.get('Número Documento', '')
            if num_doc.startswith('DOC-'):
                try:
                    numeros.append(int(num_doc.split('-')[1]))
                except ValueError:
                    continue
        
        if numeros:
            siguiente_num = max(numeros) + 1
        else:
            siguiente_num = 1
        
        return f"DOC-{siguiente_num:03d}"
    
    def crear_documento_desde_plantilla(self, datos):
        """Crea un nuevo documento basado en la plantilla"""
        if not os.path.exists(self.plantilla):
            print(f"Plantilla {self.plantilla} no encontrada")
            return ""
        
        fecha_hoy = datetime.now().strftime("%Y%m%d")
        numero_doc = datos.get('numero_documento', self.generar_numero_documento())
        nombre_archivo = f"{numero_doc}_{datos.get('titulo', 'documento').replace(' ', '_')}_{fecha_hoy}.docx"
        
        try:
            shutil.copy2(self.plantilla, nombre_archivo)
            
            with open(self.plantilla, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            
            reemplazos = {
                '[FECHA_AUTO]': datetime.now().strftime("%d/%m/%Y"),
                '[NUM_DOCUMENTO]': numero_doc,
                '[TITULO_DOCUMENTO]': datos.get('titulo', ''),
                '[AUTOR]': datos.get('autor', ''),
                '[ESTADO]': datos.get('estado', 'Borrador'),
                '[PRIORIDAD]': datos.get('prioridad', 'Media')
            }
            
            for marcador, valor in reemplazos.items():
                contenido = contenido.replace(marcador, valor)
            
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)
            
            print(f"Documento creado: {nombre_archivo}")
            return nombre_archivo
            
        except Exception as e:
            print(f"Error creando documento: {e}")
            return ""
    
    def agregar_al_resumen(self, datos, ubicacion_archivo):
        """Agrega un nuevo documento al resumen"""
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
        nuevo_documento = {
            'Número Documento': datos.get('numero_documento', self.generar_numero_documento()),
            'Título': datos.get('titulo', ''),
            'Autor': datos.get('autor', ''),
            'Fecha Creación': fecha_actual,
            'Estado': datos.get('estado', 'Borrador'),
            'Prioridad': datos.get('prioridad', 'Media'),
            'Tipo Documento': datos.get('tipo', 'Documento'),
            'Ubicación Archivo': ubicacion_archivo,
            'Última Modificación': fecha_actual,
            'Observaciones': datos.get('observaciones', 'Documento creado automáticamente')
        }
        
        self.documentos.append(nuevo_documento)
        self.guardar_resumen()
    
    def guardar_resumen(self):
        """Guarda el resumen actualizado en el archivo CSV"""
        if not self.documentos:
            return
        
        cabeceras = list(self.documentos[0].keys())
        
        with open(self.archivo_resumen, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=cabeceras)
            escritor.writeheader()
            escritor.writerows(self.documentos)
    
    def mostrar_resumen(self):
        """Muestra un resumen de todos los documentos"""
        if not self.documentos:
            print("No hay documentos en el resumen")
            return
        
        print(f"\nRESUMEN DE DOCUMENTOS ({len(self.documentos)} documentos)")
        print("=" * 50)
        
        for doc in self.documentos:
            print(f"{doc['Número Documento']} - {doc['Título']}")
            print(f"   Autor: {doc['Autor']}")
            print(f"   Estado: {doc['Estado']}")
            print(f"   Prioridad: {doc['Prioridad']}")
            print(f"   Archivo: {doc['Ubicación Archivo']}")
            print("-" * 30)

def main():
    """Función principal"""
    gestor = GestorDocumentos()
    
    print("GESTOR DE DOCUMENTOS VINCULADOS")
    print("1. Crear nuevo documento")
    print("2. Mostrar resumen")
    print("3. Salir")
    
    while True:
        opcion = input("\nSelecciona una opción (1-3): ")
        
        if opcion == "1":
            print("\nCREAR NUEVO DOCUMENTO")
            datos = {
                'titulo': input("Título: "),
                'autor': input("Autor: "),
                'estado': input("Estado (Borrador/En Proceso/Aprobado): ") or "Borrador",
                'prioridad': input("Prioridad (Alta/Media/Baja): ") or "Media",
                'tipo': input("Tipo: ") or "Documento"
            }
            
            archivo_creado = gestor.crear_documento_desde_plantilla(datos)
            if archivo_creado:
                datos['numero_documento'] = gestor.generar_numero_documento()
                gestor.agregar_al_resumen(datos, archivo_creado)
        
        elif opcion == "2":
            gestor.mostrar_resumen()
        
        elif opcion == "3":
            break

if __name__ == "__main__":
    main()