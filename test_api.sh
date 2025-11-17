#!/bin/bash

# Script de teste da API Oasis
# Execute: bash test_api.sh

echo "🚀 Testando API Oasis Backend"
echo "================================"
echo ""

API_URL="http://localhost:5000"

# Cores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função de teste
test_endpoint() {
    local method=$1
    local endpoint=$2
    local data=$3
    local description=$4
    
    echo -e "${YELLOW}Testing:${NC} $description"
    echo -e "${YELLOW}$method${NC} $endpoint"
    
    if [ -z "$data" ]; then
        response=$(curl -s -w "\n%{http_code}" -X $method "$API_URL$endpoint")
    else
        response=$(curl -s -w "\n%{http_code}" -X $method "$API_URL$endpoint" \
            -H "Content-Type: application/json" \
            -d "$data")
    fi
    
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | sed '$d')
    
    echo "Response ($http_code):"
    echo "$body" | python3 -m json.tool 2>/dev/null || echo "$body"
    echo ""
    
    if [ $http_code -ge 200 ] && [ $http_code -lt 300 ]; then
        echo -e "${GREEN}✓ Success${NC}"
    else
        echo -e "${RED}✗ Failed${NC}"
    fi
    
    echo "================================"
    echo ""
}

# 1. Testar rota raiz
test_endpoint "GET" "/" "" "API Home"

# 2. Testar cadastro de usuário
test_endpoint "POST" "/api/signup" \
    '{"nome":"Teste User","email":"teste@oasis.com","senha":"senha123"}' \
    "Cadastrar novo usuário"

# 3. Testar login
test_endpoint "POST" "/api/login" \
    '{"email":"teste@oasis.com","senha":"senha123"}' \
    "Login do usuário"

# 4. Listar usuários
test_endpoint "GET" "/api/users" "" "Listar todos os usuários"

# 5. Criar hábito
test_endpoint "POST" "/api/habits" \
    '{"titulo":"Meditação","tempo":"15","user_id":1}' \
    "Criar novo hábito"

# 6. Listar hábitos
test_endpoint "GET" "/api/habits" "" "Listar todos os hábitos"

# 7. Buscar hábito específico
test_endpoint "GET" "/api/habits/1" "" "Buscar hábito ID 1"

# 8. Atualizar hábito
test_endpoint "PUT" "/api/habits/1" \
    '{"titulo":"Meditação Matinal","tempo":"20"}' \
    "Atualizar hábito ID 1"

# 9. Excluir hábito
test_endpoint "DELETE" "/api/habits/1" "" "Excluir hábito ID 1"

echo "================================"
echo "🎉 Testes concluídos!"
echo "================================"
