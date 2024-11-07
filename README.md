Comandos utilizados:

Atualizar o pip
python.exe -m pip install --upgrade pip

Instalar o fastapi e o uvicorn
pip install fastapi uvicorn

Exportar todas as dependencias instaladas:
pip freeze > requeriments.txt

Executar a api:
uvicorn main:app --reload


requisição via curl:
curl -X GET http://127.0.0.1:8000


site para baixar os modelos de IA treinados:
https://huggingface.co/


Ferramenta para servir o modelo da IA, baixar ferramenta
https://ollama.com/

Repositorio do ollama no github:
https://github.com/ollama/ollama


Modelos para depois analisar:
https://huggingface.co/microsoft/OmniParser

https://huggingface.co/openai/whisper-large-v3-turbo

https://huggingface.co/meta-llama/Llama-3.2-1B


Vou usar um modelo do proprio ollama: 
ollama pull tinyllama

servir modelo com ollama:
ollama serve

instalando biblioteca ollama no python:
pip install ollama

Nova requisição curl:
curl -X POST http://127.0.0.1:8000 -H "Content-Type: application/json" -d "{\"text\":\"what's 6 + 3 ?\"}"

Nova requisição curl calculando o tempo de resposta:
curl -w "Tempo Total: %{time_total} segundos\n" -X POST http://127.0.0.1:8000 -H "Content-Type: application/json" -d "{\"text\":\"what's 6 + 3 ?\"}"

Comando para verificar oque a GPU está executando:
nvidia-smi 



Procurar como usar os modelos do hugging face no ollama:
'como usar os modelos do huggingface no ollama ?'

https://medium.com/fretebras-tech/mistralai-gemma-importando-llms-do-huggingface-com-ollama-49a7729baef1



Procurar saber como usar as venv com python

Oque é o termo MVP no desenvolvimento?