VENV_NAME := venv
PYTHON := $(VENV_NAME)/bin/python

venv:
	python3 -m venv $(VENV_NAME)
	$(VENV_NAME)/bin/pip install -r requirements.txt


clean: kill-port
	rm -rf $(VENV_NAME)

kill-port:
	@PID=$$(lsof -ti :8888); \
	if [ -n "$$PID" ]; then \
		echo "Killing process with PID $$PID using port 8888"; \
		kill -9 $$PID; \
		else \
		echo "No process found using port 8888"; \
	fi
