draft:
	python3 -m pkgs.news

.PHONY: draft ready clean

ready:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	deactivate

clean:
	find . -type d -name __pycache__ | xargs rm -rf
