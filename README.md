MONITOR DE GERACAO - V7
==========================

Esta versao usa:
- SUPABASE_URL
- SUPABASE_SERVICE_ROLE_KEY
- RPC energia_inversor_1hr
- RPC energia_inversor_15min

Nao usa PGHOST, PGPORT, PGUSER ou PGPASSWORD.

INSTALACAO
1. Copie .env.example para .env
2. Abra .env
3. Preencha SUPABASE_SERVICE_ROLE_KEY com a sua chave.
4. Nao coloque a service_role no index.html.
5. Execute "Iniciar Monitor de Geracao.bat".
6. Abra http://127.0.0.1:8080

INTERFACE
- 1 hora ou 15 minutos
- Uma unica data
- Horas inicial/final opcionais
- Horas vazias = dia completo
- Hoje e Ontem executam a consulta imediatamente
- Limite de chamada opcional
- Tabela compacta para exibir um dia completo

RPCS NECESSARIAS
public.energia_inversor_1hr
public.energia_inversor_15min

As RPCs devem existir no Supabase antes de usar o monitor.
