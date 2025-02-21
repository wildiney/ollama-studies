# Customize Ollama Model

## Creating the custom model

```shell
ollama create sky -f ./Sky.Modelfile
```

### Create inside a ollama docker

```shell
docker cp Sky.ModelFile ollama:/Sky.ModelFile
docker exec -it ollama bash
ollama create sky -f /Sky.ModelFile
```

## API

```shell
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "give me a tip for today",
  "stream": false
  }'
```

```shell
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [{"role": "user","content":"tell me something fun" }],
  "format": "json",
  "stream": false
  }'
```
