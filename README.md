
# AI Cloud Project

API de classificação ML com deploy escalável na AWS.

## Arquitetura
```
Usuário → Load Balancer → EC2 (Container FastAPI) → Resposta
                                    ↓
                              S3 (modelo .pkl)
                                    ↓
                            CloudWatch (logs)
```

## Componentes AWS

- **VPC** `10.0.0.0/16` — rede privada isolada
- **Subnet Pública** `10.0.1.0/24` — Load Balancer
- **Subnet Privada** `10.0.2.0/24` — EC2 com container
- **Internet Gateway** — entrada de tráfego externo
- **Route Table** — direciona tráfego público para o IGW
- **Load Balancer** — distribui requisições entre instâncias
- **Auto Scaling** — escala EC2 conforme demanda
- **ECR** — repositório da imagem Docker
- **S3** — armazena o modelo treinado (.pkl)
- **CloudWatch** — logs e alarme de CPU > 70%

## Decisões Técnicas

- Modelo separado da API (S3) para facilitar atualização sem redeploy
- Subnet privada para EC2 — nenhuma instância exposta diretamente à internet
- Load Balancer na subnet pública como único ponto de entrada
- Container Docker para garantir ambiente reproduzível

## Estrutura do Projeto
```
ai-cloud-project/
├── model/
│   └── train.py        # treino do classificador
├── app/
│   ├── main.py         # API FastAPI
│   ├── requirements.txt
│   └── Dockerfile
├── infra/
│   └── architecture-diagram.png
└── README.md
```

## Como Escalar

- Auto Scaling aumenta instâncias EC2 quando CPU > 70%
- Load Balancer distribui tráfego automaticamente entre instâncias
- Modelo no S3 permite atualização sem alterar infraestrutura

## Status do Projeto

- [x] VPC, Subnets, Internet Gateway, Route Table
- [ ] Modelo ML (train.py)
- [ ] API FastAPI + Docker
- [ ] Deploy EC2 + ECR
- [ ] Load Balancer + Auto Scaling
- [ ] CloudWatch + Monitoramento

## Pontos de Melhoria Futura

- Migrar para ECS/Fargate para orquestração de containers
- Adicionar cache com ElastiCache
- CI/CD com GitHub Actions