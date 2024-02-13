import json
import sys
from random import randint

# Carrega o estado salvo do arquivo JSON
document_id = sys.argv[1] if len(sys.argv) > 1 else ""

if document_id.strip() == "":
    document_id = f"doc_{randint(0, 1000)}"

print("Document ID:", document_id)

file_path = f'./workflows/saved_data_{document_id}.json'

try:
    with open(file_path, 'r') as file:
        print("Carregando o estado salvo")
        saved_data = json.load(file)
except FileNotFoundError:
    print("Nenhum estado salvo encontrado, começando do zero")
    saved_data = {
        'completed_step': False,
        'random_number': -1
    }
    with open(file_path, 'w') as file:
        print("Salvando o estado inicial")
        json.dump(saved_data, file)

print("Estado salvo:", saved_data)

# Verifica se a etapa já foi concluída antes de executá-la novamente
if not saved_data.get('completed_step'):
    # Executa a etapa que ainda não foi concluída
    print("Executando a etapa que ainda não foi concluída")

    saved_data['completed_step'] = True
    # gerar um numero aleatorio com python
    saved_data['document_id'] = document_id
    with open(file_path, 'w') as file:
        json.dump(saved_data, file)

else:
    print(f"A etapa para o documento {document_id} já foi concluída")
