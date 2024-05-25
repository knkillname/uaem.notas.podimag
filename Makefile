export PIPENV_VENV_IN_PROJECT=1

systemdeps:
	sudo apt-get update && sudo apt-get install --yes ffmpeg libsm6 libxext6 libopencv-dev libgl1-mesa-glx
	sudo chmod 744 /dev/video*

venv: .venv/bin/activate
.venv/bin/activate: Pipfile
	pipenv sync --dev
	touch $@

clean:
	git clean -Xdf