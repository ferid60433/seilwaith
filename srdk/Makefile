default: run

run : build

	mkdir -p $(HOME)/srdk_projects
	docker run --name srdk -i -t -v $(HOME)/src/seilwaith/srdk/cy/:/usr/local/srdk/cy/ -v $(HOME)/src/seilwaith/srdk/htk/:/usr/local/srdk/htk/ -v $(HOME)/src/seilwaith/srdk/lm/:/usr/local/srdk/lm/ -v $(HOME)/srdk_projects/:/srdk_projects/  techiaith/srdk bash

build:
	docker build --rm -t techiaith/srdk .

clean: stop
	docker rmi techiaith/srdk

stop:
	docker stop srdk
	docker rm srdk
