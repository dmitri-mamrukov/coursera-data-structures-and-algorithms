DIRS := $(shell find . -maxdepth 1 -mindepth 1 -type d | sort)

all: build_and_test

build_and_test:
	for dir in $(DIRS); do \
		cd $$dir; \
		make -f Makefile build_and_test; \
		cd ..; \
	done

clean:
	for dir in $(DIRS); do \
		cd $$dir; \
		make -f Makefile clean; \
		cd ..; \
	done
