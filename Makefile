TASKS = $(shell ./tasks.sh list)

all:
	chmod 755 ./tasks.sh

$(TASKS):
	./tasks.sh $@
