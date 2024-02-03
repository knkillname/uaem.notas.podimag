export PIPENV_VENV_IN_PROJECT=1

systemdeps:
	sudo apt-get update && sudo apt-get install --yes ffmpeg libsm6 libxext6

venv: .venv/bin/activate
.venv/bin/activate: Pipfile
	pipenv install --dev
	touch $@

clean:
	git clean -Xdf