export PIPENV_VENV_IN_PROJECT=1

venv: .venv/bin/activate
.venv/bin/activate: Pipfile
	pipenv install --dev
	touch $@

clean:
	git clean -Xdf