all: build_and_test

TEST = test.py

permission:
	chmod +x $(TEST)

build_and_test:
	./$(TEST)

clean:
	rm -f *~
	rm -rf __pycache__
