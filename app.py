import os
from flask import Flask, request, jsonify, send_from_directory
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")

SUPABASE_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")

RPCS = {
    "1hr": "energia_inversor_1hr",
    "15min": "energia_inversor_15min",
}

@app.get("/")
def index():
    return send_from_directory(".", "index.html")

@app.get("/api/health")
def health():
    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        return jsonify({
            "ok": False,
            "error": "SUPABASE_URL ou SUPABASE_SERVICE_ROLE_KEY não configurada no arquivo .env."
        }), 500
    return jsonify({"ok": True})

@app.post("/api/consulta")
def consulta():
    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        return jsonify({
            "ok": False,
            "error": "Configure SUPABASE_URL e SUPABASE_SERVICE_ROLE_KEY no arquivo .env."
        }), 500

    body = request.get_json(silent=True) or {}
    data = body.get("data")
    resolucao = body.get("resolucao", "1hr")
    hora_inicio = body.get("hora_inicio")
    hora_fim = body.get("hora_fim")
    limite_ativo = bool(body.get("limite_ativo", False))
    limite = body.get("limite")

    if not data:
        return jsonify({"ok": False, "error": "Informe a data."}), 400

    if resolucao not in RPCS:
        return jsonify({"ok": False, "error": "Resolução inválida."}), 400

    def parse_hour(value, field):
        if value in (None, "", "null"):
            return None, None
        try:
            n = int(value)
        except (TypeError, ValueError):
            return None, f"{field} deve ser uma hora inteira entre 0 e 23."
        if n < 0 or n > 23:
            return None, f"{field} deve estar entre 0 e 23."
        return n, None

    h_ini, err = parse_hour(hora_inicio, "Hora inicial")
    if err:
        return jsonify({"ok": False, "error": err}), 400

    h_fim, err = parse_hour(hora_fim, "Hora final")
    if err:
        return jsonify({"ok": False, "error": err}), 400

    if (h_ini is None) != (h_fim is None):
        return jsonify({
            "ok": False,
            "error": "Informe as duas horas ou deixe as duas em branco para consultar o dia completo."
        }), 400

    if h_ini is not None and h_fim <= h_ini:
        return jsonify({
            "ok": False,
            "error": "A hora final deve ser maior que a hora inicial."
        }), 400

    limite_value = None
    if limite_ativo:
        try:
            limite_value = float(limite)
        except (TypeError, ValueError):
            return jsonify({"ok": False, "error": "A margem deve ser um percentual numérico."}), 400
        if limite_value > 0:
            return jsonify({"ok": False, "error": "A margem de chamada deve ser negativa."}), 400

    payload = {
        "p_data": data,
        "p_hora_inicio": h_ini,
        "p_hora_fim": h_fim,
        "p_limite_chamada": limite_value if limite_ativo else None,
    }

    rpc_url = f"{SUPABASE_URL}/rest/v1/rpc/{RPCS[resolucao]}"
    headers = {
        "apikey": SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(rpc_url, headers=headers, json=payload, timeout=60)
    except requests.RequestException as exc:
        return jsonify({
            "ok": False,
            "error": f"Falha de comunicação com o Supabase: {exc}"
        }), 502

    if not response.ok:
        try:
            detail = response.json()
        except ValueError:
            detail = response.text
        return jsonify({
            "ok": False,
            "status": response.status_code,
            "error": "O Supabase recusou a consulta.",
            "detail": detail
        }), 502

    try:
        rows = response.json()
    except ValueError:
        return jsonify({
            "ok": False,
            "error": "O Supabase retornou uma resposta que não é JSON.",
            "detail": response.text[:1000]
        }), 502

    return jsonify({
        "ok": True,
        "rows": rows,
        "quantidade": len(rows)
    })

if __name__ == "__main__":
    print("=" * 60)
    print("MONITOR DE GERAÇÃO - SERVIDOR LOCAL")
    print("URL: http://127.0.0.1:8080")
    print("=" * 60)
    app.run(host="127.0.0.1", port=8080, debug=False)
