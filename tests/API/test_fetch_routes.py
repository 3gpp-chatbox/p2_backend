from fastapi.testclient import TestClient
from src.API.main import app

client = TestClient(app)
# used real data for testing
procedures = [
  {
    "id": "b22925be-be43-402f-8646-55143e87b798",
    "name": "Sample Graph"
  },
  {
    "id": "0a3cf55b-5b8a-4f96-ae12-b63d0f8e4c08",
    "name": "Sample Graph"
  },
  {
    "id": "b0c4ae04-5efe-49e5-8f1c-e32ca11fa28a",
    "name": "Initial Registration Procedure"
  }
]
procedure_item = {
  "id": "b0c4ae04-5efe-49e5-8f1c-e32ca11fa28a",
  "name": "Initial Registration Procedure",
  "document_id": "f73687e1-305c-4b97-b2cf-55631ac9bfaa",
  "graph": {
    "graph": {
      "edges": [
        {
          "to": "1",
          "from": "start",
          "type": "sequential",
          "properties": {
            "trigger": "UE sends REGISTRATION REQUEST"
          }
        },
        {
          "to": "2",
          "from": "1",
          "type": "sequential",
          "properties": {
            "trigger": "UE starts timer T3510"
          }
        }
      ],
      "nodes": [
        {
          "id": "start",
          "type": "start",
          "properties": {

          },
          "description": "Procedure starts"
        },
        {
          "id": "1",
          "type": "process",
          "properties": {
            "entity": "UE",
            "messages": [
              "REGISTRATION REQUEST"
            ],
            "state_change": "5GMM-DEREGISTERED"
          },
          "description": "UE sends REGISTRATION REQUEST message to the AMF"
        }
      ]
    }
  },
  "accuracy": 1,
  "created_at": "2025-04-09T09:16:32.301841"
}
def test_get_procedures():
    response = client.get("/procedures/list")
    assert response.status_code == 200
    assert response.json() == procedures


def test_get_procedure():
    response = client.get("/procedures/b0c4ae04-5efe-49e5-8f1c-e32ca11fa28a")
    assert response.status_code == 200
    assert response.json() == procedure_item


def test_get_procedure_not_found():
    response = client.get("/procedures/0a3cf55b-5b8a-4f96-ae12-b63d0f8e4c00")
    assert response.status_code == 404


