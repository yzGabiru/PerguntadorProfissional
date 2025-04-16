import cohere
import pdfplumber
import csv

co = cohere.ClientV2(api_key="BpT9EVupvucDnOJnQm63HNIez29glZ1tu0F25ozx")


texto_curriculo = ""
with pdfplumber.open("Currículo Profissional Teste.pdf") as pdf:
    for page in pdf.pages:
        texto_curriculo += page.extract_text()


response = co.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "system",
            "content": "Você é um recrutador experiente que ajuda candidatos a se prepararem para entrevistas de emprego. Analise o currículo e fazer perguntas relevantes para o candidato.(maximo de 300 caracteres, não coloque palavras em negrito, coloque um titulo, apenas as perguntas.)",
        },{
            "role": "user",
            "content": f"Currículo anexado: \n\n{texto_curriculo}",
        }
    ],
)

nome_arquivo = "perguntas.csv"
texto_gerado = response.message.content[0].text

with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow([texto_gerado])
print(f"Arquivo '{nome_arquivo}' criado com sucesso!")




