## API de Consultas Públicas

**API** simples para buscar informações sobre _**estados, empresas (CNPJ) e BIN de cartões**_.

**Rotas** e Exemplos

1. Consultar Estado (IBGE)

## URL:

GET ```http://localhost:5000/ibge/estado?uf=SP```

## Resposta:

``{
  "id": 35,
  "sigla": "SP",
  "nome": "São Paulo",
  "regiao": { "id": 3, "sigla": "SE", "nome": "Sudeste" }
}``


##

2. Consultar Empresa (CNPJ API)

## URL:

GET ```http://localhost:5000/cnpj?cnpj=00000000000191```

## Resposta:

``{
  "cnpj": "00.000.000/0001-91",
  "razao_social": "EMPRESA EXEMPLO LTDA",
  "fantasia": "EXEMPLO",
  "atividade_principal": "Comércio varejista",
  "endereco": "Rua Exemplo, 123, São Paulo - SP"
}``


##

3. Verificar BIN do Cartão

## URL:

GET ```http://localhost:5000/bin?bin=45717360```

## Resposta:
``{
  "scheme": "Visa",
  "type": "Credit",
  "brand": "Classic",
  "bank": { "name": "Banco Exemplo", "country": "BR" }
}``


##
