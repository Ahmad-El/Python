run0:
	python ex00/main.py


run1:
	python ex01/main.py

cov:
	pytest --cov=ex01 --cov-report=html ex01/tests

test:
	pytest

html1:
	open htmlcov/index.html



run2:
	python ex02/main.py 

docs: docs_init
	cp -r source docs
	cd docs && make html

docs_html: 
	open docs/build/html/index.html

docs_init:
	sphinx-quickstart docs

html2:
	open docs/build/html/index.html
	
docs_build:
	sphinx-build -M html docs/source/ docs/build/




clean:
	@rm -rf htmlcov 
	@rm -rf .coverage
	@rm -rf ex01/__pycache__
	@rm -rf ex01/tests/__pycache__
	@rm -rf ex00/__pycache__
	@rm -rf .pytest_cache
	@rm -rf ex02/__pycache__
	@rm -rf ex02/tests/__pycache__
	@rm -rf docs/build


style:
	black ex00/*.py 
	black ex01/*.py 
	black ex01/tests/*.py 
	black ex02/*.py 
	black ex02/tests/*.py 