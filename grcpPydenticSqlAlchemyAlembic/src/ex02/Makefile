proto:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. air_craft.proto


clean:
	rm -rf *_pb2*

server:
	python reporting_server.py

test:
	python reporting_client_v3.py 17 45 40.0409 -29 00 28.118

traitor:
	python reporting_client_v3.py list_traitors

exe:
	chmod +x reporting_server.py
	chmod +x reporting_client_v3.py


alem:
	alembic init alembic

alem_migrate:
	alembic revision -m "add speed column to spaceship"

alem_upgrade:
	alembic upgrade head
