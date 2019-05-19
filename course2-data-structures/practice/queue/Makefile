all: build_and_test

MAIN_TEST = test.py

permission:
	chmod +x $(MAIN_TEST)

build_and_test:
	./$(MAIN_TEST)

clean:
	rm -f *~
	rm -rf __pycache__
