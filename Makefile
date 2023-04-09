build:
	python -m build

install:
	make build
	pip install .\dist\node_chatgpt_api-1.0.0.tar.gz