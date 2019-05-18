all: build_and_test

MAIN = main.py
MAIN_TEST = main_test.py

permission:
	chmod +x $(MAIN_TEST) $(MAIN)

build_and_test:
	./$(MAIN_TEST)

demo:
	./$(MAIN) < input1.txt
	./$(MAIN) < input2.txt
	./$(MAIN) < input3.txt
	./$(MAIN) < input4.txt

clean:
	rm -f *~
	rm -rf __pycache__
