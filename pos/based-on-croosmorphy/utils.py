import pandas as pd

def preprocess(out, lexeme):
    df = pd.DataFrame(list(map(lambda x: x.split(', '), out)))
    df.columns = ['form', 'normal form', 'speech part', 'tags']
    if not lexeme:
        df = df.drop_duplicates(subset='form')
        df = df.reset_index(drop=True)

    df['form'] = df['form'].str.strip('[form: ')
    df['normal form'] = df['normal form'].str.strip('[normal form: ')
    df['speech part'] = df['normal form'].str.strip('[speech part: ')
    df['tags'] = df['tags'].str.strip('tags=(')
    df['tags'] = df['tags'].str.strip(')]')
    return df.to_json(orient='index', force_ascii=False)
