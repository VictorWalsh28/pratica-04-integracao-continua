# Prática 08 - Infraestrutura como Código e Gestão de Configuração

Projeto Terraform simples usando o provider `local`.

## Estrutura

- `terraform/provider.tf`: configuração do provider `local`.
- `terraform/variables.tf`: variáveis `file_name` e `file_content`.
- `terraform/main.tf`: recurso `local_file`.
- `.gitlab-ci.yml`: pipeline `validate -> plan -> apply`.
- `.github/workflows/iac-terraform.yml`: pipeline equivalente no GitHub Actions.

## Execução local

```bash
cd terraform
terraform init
terraform fmt -check
terraform validate
terraform plan -out=plan.out
terraform apply plan.out
```

Ao final, o Terraform cria:

```text
exemplo.txt
```

com o conteúdo:

```text
Aqui teremos o conteúdo do arquivo de texto
```
