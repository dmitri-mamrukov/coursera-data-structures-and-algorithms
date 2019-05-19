all: build_and_test

MAIN_DEMO = demo.py
MAIN_TEST = test.py

permission:
	chmod +x $(MAIN_TEST) $(MAIN_DEMO)

build_and_test:
	./$(MAIN_TEST)

demo:
	./$(MAIN_DEMO)

clean:
	rm -f *~
	rm -rf __pycache__
