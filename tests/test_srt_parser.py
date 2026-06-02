#from std_to_text_convertors.srt_to_text import std_srt_to_text_line

import srt

if __name__ == '__main__':
    example_fn = './projects/research/test_data/srts/Iron1and8.srt'

    with open(example_fn, 'r', encoding='utf-8') as f:
        srt_data = f.read()

    subtitles = list(srt.parse(srt_data))

    for s in subtitles:
        print(s.content)