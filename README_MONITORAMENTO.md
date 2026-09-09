# Prática 07 - Monitoramento em DevOps

O projeto expõe métricas da aplicação Flask em `/metrics`, coleta essas métricas com Prometheus e disponibiliza um dashboard no Grafana.

## Executar

```bash
docker-compose up --build
```

Acessos:

- Aplicação: http://localhost:5000/
- Métricas: http://localhost:5000/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

Login padrão do Grafana: `admin` / `admin`.

## Gerar tráfego para o dashboard

```bash
curl http://localhost:5000/health-check
curl "http://localhost:5000/hello?name=Victor"
curl http://localhost:5000/hello
```

O dashboard provisionado possui três painéis:
- Requisições GET;
- Tempo médio de resposta;
- Erros HTTP.
