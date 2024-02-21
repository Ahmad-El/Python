.PHONY: ex00 ex00_test

run:
	python3 credentials.py

test:
	curl http://127.0.0.1:8888/?species=Time%20Lord
	curl http://127.0.0.1:8888/dafsdagdasf

clean: kill-port

kill-port:
	@PID=$$(lsof -ti :8888); \
	if [ -n "$$PID" ]; then \
		echo "Killing process with PID $$PID using port 8888"; \
		kill -9 $$PID; \
		else \
		echo "No process found using port 8888"; \
	fi