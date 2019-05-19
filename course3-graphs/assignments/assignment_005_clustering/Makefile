INPUT_FILES := $(shell find . \
	-maxdepth 1 -mindepth 1	-type f -name 'input*.txt' | sort)

all: build_and_test

MAIN = clustering.py
MAIN_TEST = test.py

permission:
	chmod +x $(MAIN_TEST) $(MAIN)

build_and_test:
	./$(MAIN_TEST)

demo:
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN) < $$file; \
	done

clean:
	rm -f *~
	rm -rf __pycache__
