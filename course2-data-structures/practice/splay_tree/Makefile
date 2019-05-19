all: build_and_test

MAIN = splay_tree.py
TEST_MAIN = test.py

permission:
	chmod +x $(TEST_MAIN) $(MAIN)

build_and_test:
	./$(TEST_MAIN)

clean:
	rm -f *~
	rm -rf __pycache__
