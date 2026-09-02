# Prática 04 - Integração Contínua (CI)

Projeto acadêmico da disciplina **Práticas Integradas: Full Cycle - DevOps**.

## Objetivos

- Configurar um ambiente de Integração Contínua.
- Automatizar testes unitários em uma aplicação Python + Flask.
- Verificar a cobertura de testes e exigir 100% de cobertura.

## Estrutura

- `app/app.py`: aplicação Flask.
- `tests/appTest.py`: testes unitários com `unittest`.
- `.gitlab-ci.yml`: configuração pedida no roteiro para GitLab CI.
- `.github/workflows/ci.yml`: execução equivalente no GitHub Actions.
- `requirements.txt`: dependências.

## Executar localmente

```bash
pip install -r requirements.txt
python -m unittest -v tests/appTest.py
```

## Verificar cobertura

```bash
python -m coverage run -m unittest -v tests/appTest.py
python -m coverage report --fail-under=100
```
