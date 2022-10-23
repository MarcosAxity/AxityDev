import os

import boto3

import json

SAMPLE_FILE = "text_clean.txt"

api = boto3.client("comprehend")
translate = boto3.client('translate')

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
new_textblock = []

for paragraph in text_blocks:
    result = translate.translate_text(
        Text=paragraph,
        SourceLanguageCode='es',
        TargetLanguageCode='en'
    )
    print(result['TranslatedText'])
    new_textblock.append(result['TranslatedText'])

response = None

# LLamada del API
if len(text_blocks) >= 1 and len(text_blocks) <= 25:
    response = api.batch_detect_targeted_sentiment(
        TextList=new_textblock, LanguageCode="en")
else:
    print("No hay bloques de texto")

# Respuesta del API
data = []
if response:
    print("------------------------------")
    for result in response['ResultList']:
        print(result)
        data.append(result)
        json_object = json.dumps(data, indent=4)
        with open("sample4.json", "w") as outfile:
            outfile.write(json_object)
            outfile.write('\n')
else:
    print("No hay respuesta de Amazon Comprehend")
