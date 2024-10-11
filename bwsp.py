import os
import pandas as pd

# Definir rutas
input_folder = 'input'
output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)  # Crear la carpeta de salida si no existe

# Buscar archivo en la carpeta input
for filename in os.listdir(input_folder):
    if filename.endswith(".xlsx"):  # Asegurarse de que sea un archivo Excel
        file_path = os.path.join(input_folder, filename)

        # Leer el archivo Excel asegurándose de que pandas no convierta a int los números
        df = pd.read_excel(file_path, dtype=str)

        # Función para eliminar el primer "15" en cada número telefónico
        def remove_first_15(phone):
            phone_str = str(phone)  # Asegurarse de que sea string
            start = phone_str.find('15')
            if start != -1:
                # Eliminar el primer "15" encontrado
                return phone_str[:start] + phone_str[start+2:]
            else:
                return phone_str  # Si no hay "15", devuelve el número tal cual

        # Crear una nueva columna con los números sin "15"
        df['Telefono_sin_15'] = df.iloc[:, 0].apply(remove_first_15)

        # Eliminar la columna original
        df = df.drop(df.columns[0], axis=1)

        # Guardar el resultado en un archivo nuevo en la carpeta de salida
        output_file = os.path.join(output_folder, 'output_without_15.xlsx')
        df.to_excel(output_file, index=False)

        print(f'Archivo procesado y guardado en: {output_file}')
