from vosk import Model, KaldiRecognizer
import json
import wave


class SoundRecognizer:
    def recognize(path):
        model = Model("lang_models/vosk-model-small-ru-0.22")
        wf = wave.open(path, 'rb')
        rcgn_fr = wf.getframerate() * wf.getnchannels()
        rec = KaldiRecognizer(model, rcgn_fr)

        text_res = ''
        last_n = False

        read_block_size = wf.getnframes()
        while True:
            data = wf.readframes(read_block_size)
            if len(data) == 0:
                break

            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())

                if res['text'] != '':
                    text_res += f" {res['text']}"
                    if read_block_size < 200000:
                        print(res['text'] + " \n")

                        last_n = False
                    elif not last_n:
                        text_res += '\n'
                        last_n = True
        res = json.loads(rec.FinalResult())

        text_res += f" {res['text']}"

        return text_res


