from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import ollama
from pydantic import BaseModel

app = FastAPI()

#Corrigir alguns erros de CORS:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # * para liberar todos os IPs, ou informe um IP especifico no lugar de *, ou você pode colocar mais do que só 1 IP
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Criando um Type para facilitar na hora de receber a resposta na requisição,
class TextRequest(BaseModel):
    text: str

@app.post("/")
def read_root(request: TextRequest):
    if not request.text:
        raise HTTPException(status_code=400,detail="Não enviou nenhuma pergunta!")
    try:
        # essa informação de model e bom colocar em um arquivo de config para conseguir mudar facilmente
        response = ollama.chat(model="tinyllama", messages=[
            # tem varios tipos de role, ver para que serve cada um
            # Poso enviar uma lista de mensagem, cada uma mensagem vai ser um objeto
            # no lugar de content tem outras opções, estudar para ver oque cada uma faz, tem um "imagem"
            {
                "role":"user",
                "content": request.text
            }
        ])

        llm_res = response.get('message', {}).get('content','')
        return {"resposta da LLM: ": llm_res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    