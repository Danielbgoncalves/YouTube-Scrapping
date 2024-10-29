from flask import Flask, request, jsonify # o equivalente ao express.js
from main import getPlaylistId, obter_playlis_dataFrame
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.rout('/api', methods=['Post'])
def processaURL():
    data = request.get_json()
    url = data.get('url')

    try:
      playlistId = getPlaylistId(url)
      table, topicos = obter_playlis_dataFrame(playlistId)
    except Exception as e:
      return jsonify({"status": "error", "message": str(e)}), 400

    return jsonify({"staus":"Success", "table":table, "topicos":topicos})

if __name__ == '__main__':
    app.run(debug=True)