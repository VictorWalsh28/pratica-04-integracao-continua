# Prática 06 - Segurança em DevOps (DevSecOps)

Exemplo didático para demonstrar SQL Injection em ambiente local e a correção por meio de consultas parametrizadas.

## Preparação local

```bash
pip install flask
python devsecops_demo/init_db.py
flask --app devsecops_demo.app run
```

Abra:

http://127.0.0.1:5000/

### Usuários do banco

- teste@teste.com / 1234
- teste2@teste.com / 1234
- teste3@teste.com / supersenha
- teste4@teste.com / souhacker

### Demonstração da vulnerabilidade (somente no commit da Ação 1)

No ambiente local controlado, o roteiro propõe testar entradas como:

```text
' or 1=1; --
```

e também:

```text
' OR 'a'='a' --
```

A versão final do projeto corrige a falha usando consulta parametrizada.
