# Prática 09 - Automação de Build

Exemplo de aplicação Flask empacotada em Docker para demonstrar:

- pipeline de build;
- versionamento por hash do commit;
- tag `latest`;
- push da imagem para Container Registry;
- cache de camadas para reduzir o tempo dos builds seguintes.

## Teste local

```bash
docker build -t pratica09 .
docker run --rm -p 5000:5000 pratica09
```

Acesse: http://localhost:5000/
