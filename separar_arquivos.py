import os
import shutil

# Caminho da pasta onde os arquivos estão localizados
source_folder = r'C:\Users\wesley.teixeira\Desktop\Extratos 05.2024\Extrato_Abril\Extrato_Abril'
# Caminho da pasta de destino
destination_folder = r'C:\Users\wesley.teixeira\Desktop\Extratos 05.2024\EXB - ITAU - 05.2024'

# Certifique-se de que a pasta de destino existe, se não, crie-a
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Itera sobre os arquivos na pasta de origem
for filename in os.listdir(source_folder):
    # Verifica se '31-05-2024' está no nome do arquivo
    if '31-05-2024' in filename:
        # Caminho completo do arquivo de origem
        source_file = os.path.join(source_folder, filename)
        # Caminho completo do arquivo de destino
        destination_file = os.path.join(destination_folder, filename)
        # Move o arquivo para a pasta de destino
        shutil.move(source_file, destination_file)
