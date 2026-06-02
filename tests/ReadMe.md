
1. Env
```
python3.8 -m venv venv_v3.8

pip install -r tests/requirements.txt
```

2. Run
```
. ./venv_v3.8/bin/activate

PYTHONPATH=projects/shadow/kmap-builder-jython27/spiders_processors:projects/research/models/src:projects/shadow/kmap-builder-jython27/ \
python tests/test_srt_parser.py
```