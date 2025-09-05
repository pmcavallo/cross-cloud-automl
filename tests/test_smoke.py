import os

def test_generated_files_exist():
    for fn in ['data/train.csv','data/valid.csv','data/test.csv','data/schema.yaml']:
        assert os.path.exists(fn), f'Missing {fn}'
