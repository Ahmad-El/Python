proto:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. air_craft.proto


clean:
	rm -rf *_pb2*

server:
	python reporting_server.py

test:
	python reporting_client.py 17 45 40.0409 -29 00 28.118

exe:
	chmod +x reporting_client.py
	chmod +x reporting_server.py