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
