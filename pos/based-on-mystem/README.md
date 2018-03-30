# Based on MyStem
POS tagging for Russian language for NetCracker Inc. based on MyStem. DEMO is available [here]('http://159.65.201.37:7000/')

## Requirements

Install all dependencies via ```pip3 install -r requirements.txt``` or just use Dockerfile to create Docker image.

## Docker

```bash
docker build -t pos-tagger .
docker run -d -it -p 9000:9000 --rm --name pos pos-tagger
```

## Usage

- Service runs on port 9000. 
- To get POS tag for each word of your sentence, just execute the query `/pos/?text=YOURTEXT`

## Example

```http://0.0.0.0:9000/pos/?text=%D0%9C%D0%B0%D0%BC%D0%B0%20%D0%BC%D1%8B%D0%BB%D0%B0%20%D1%80%D0%B0%D0%BC%D1%83```

```json
{
 "tokens": [
  {
   "analysis": [
    {
     "lex": "мама",
     "gr": "S,жен,од=им,ед"
    }
   ],
   "text": "Мама"
  },
  {
   "text": " "
  },
  {
   "analysis": [
    {
     "lex": "мыть",
     "gr": "V,несов,пе=прош,ед,изъяв,жен"
    }
   ],
   "text": "мыла"
  },
  {
   "text": " "
  },
  {
   "analysis": [
    {
     "lex": "рама",
     "gr": "S,жен,неод=вин,ед"
    }
   ],
   "text": "раму"
  },
  {
   "text": "\n"
  }
 ]
}
```