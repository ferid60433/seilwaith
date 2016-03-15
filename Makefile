default: run

run : build

	docker run --name htk -i -t techiaith/htk bash

build:
	docker build --rm -t techiaith/htk .

clean: stop
	docker rmi techiaith/htk

stop:
	docker stop htk
	docker rm htk
