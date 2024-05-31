
# Ferramenta de Transcrição de Áudio para Texto

Esta ferramenta foi desenvolvida para transcrever arquivos de áudio em texto utilizando a biblioteca Whisper, da OpenAI. O objetivo é facilitar a transcrição de entrevistas realizadas em áudio para texto, especialmente útil para estudantes que necessitam documentar entrevistas.

## Requisitos

Para utilizar esta ferramenta, você precisa ter o seguinte instalado em seu ambiente:

- Python 3.x
- Biblioteca Whisper da OpenAI
- 
Você pode instalar a biblioteca Whisper utilizando pip:

```bash
pip install openai-whisper
```

## Arquivos

A ferramenta consiste em um único arquivo Python, `transcriber.py`.

## Uso

Para utilizar a ferramenta, você deve executar o script `transcriber.py` passando três parâmetros:
1. O modelo a ser utilizado para a transcrição (e.g., `base`, `small`, `medium`, `large`).
2. O arquivo de áudio que será transcrito.
3. O nome do arquivo de saída que conterá a transcrição em texto.

### Exemplo de Execução

```bash
python transcriber.py base entrevista.mp3 transcricao.txt
```

### Estrutura do Script

O script `transcriber.py` contém o seguinte código:

```python
import sys
import whisper

def transcrever_audio(modelo, arquivo_audio, arquivo_saida):
    model = whisper.load_model(modelo)
    result = model.transcribe(arquivo_audio)
    
    with open(arquivo_saida, 'w') as f:
        f.write(result['text'])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python transcriber.py <modelo> <arquivo_audio> <arquivo_saida>")
        sys.exit(1)
    
    modelo = sys.argv[1]
    arquivo_audio = sys.argv[2]
    arquivo_saida = sys.argv[3]
    
    transcrever_audio(modelo, arquivo_audio, arquivo_saida)
```

### Passos para Executar

1. Certifique-se de que todos os requisitos estão instalados.
2. Coloque o arquivo de áudio que deseja transcrever na mesma pasta do script ou especifique o caminho correto.
3. Execute o script conforme o exemplo acima.

### Modelos Disponíveis

Os modelos disponíveis no Whisper variam em tamanho e precisão. Para a maioria das aplicações, os modelos `base` ou `small` são suficientes, mas você pode optar por modelos maiores como `medium` ou `large` se precisar de maior precisão.

### Contato

Para mais informações ou ajuda, entre em contato com [seu email ou contato preferido].
