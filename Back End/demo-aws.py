import os

import boto3

import json

SAMPLE_FILE = "text_clean.txt"

api = boto3.client("comprehend")

print("Ingresando amazon comprehend via {}".format(api.meta.endpoint_url))

paragraphs = []


if os.path.exists(SAMPLE_FILE):
    try:
        with open(SAMPLE_FILE, 'r') as fh:
            doc = fh.read()
            paragraphs = doc.split('\n')
    except Exception as err:
        print("Error".format(err))

else:
    print("No se encontro el archivo".format(SAMPLE_FILE))

# Guardando en bloques de texto
text_blocks = [p for p in paragraphs if len(p.strip()) > 0]

response = None

# LLamada del API
if len(text_blocks) >= 1 and len(text_blocks) <= 25:
    response = api.batch_detect_sentiment(
        TextList=text_blocks, LanguageCode="es")
else:
    print("No hay bloques de texto")

# Respuesta del API
data = []
if response:
    print("------------------------------")
    for result in response['ResultList']:
        text_block_snippet = "{}...".format(
            text_blocks[result['Index']][0:101])
        index = result['Index']
        sentiment = result['Sentiment']
        score = result['SentimentScore'][result['Sentiment'].title()]
        data.append(result)
        json_object = json.dumps(data, indent=4)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
            outfile.write('\n')
        print(f"""BLOQUE DE TEXTO {index}
{text_block_snippet}
    {sentiment} {score}""")
else:
    print("No hay respuesta de Amazon Comprehend")
