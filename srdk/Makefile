default: run

run : build

	mkdir -p $(PWD)/srdk_projects
	docker run --name srdk -it \
	-v $(PWD)/cy/:/usr/local/srdk/cy/ \
	-v $(PWD)/htk/:/usr/local/srdk/htk/ \
	-v $(PWD)/lm/:/usr/local/srdk/lm/ \
	-v $(PWD)/srdk_projects/:/srdk_projects/ \
	techiaith/srdk bash

build:
	docker build --rm -t techiaith/srdk .

clean: stop
	docker rmi techiaith/srdk

stop:
	docker stop srdk
	docker rm srdk
