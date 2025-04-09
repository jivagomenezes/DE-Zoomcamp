# Credenciais do Google Cloud Platform

## Localização das Credenciais de Aplicação Padrão

As credenciais de aplicação padrão do Google Cloud Platform (GCP) estão salvas em:

```
/home/jivagomenezes/.config/gcloud/application_default_credentials.json
```

## Como Usar

Para usar essas credenciais em seus aplicativos, você pode configurar a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS` apontando para este arquivo:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/jivagomenezes/.config/gcloud/application_default_credentials.json"
```

## Observações

- Estas credenciais são sensíveis. Não compartilhe este arquivo.
- Para renovar as credenciais, use o comando: `gcloud auth application-default login`
- Data de criação das credenciais: 07/04/2025
