all: build_and_test

TEST_HEAP = test_heap.py
TEST_UNION_FIND = test_union_find.py
TEST_GRAPH = test_graph.py

permission:
	chmod +x $(TEST_HEAP) $(TEST_UNION_FIND) $(TEST_GRAPH)

build_and_test:
	./$(TEST_HEAP)
	./$(TEST_UNION_FIND)
	./$(TEST_GRAPH)

clean:
	rm -f *~
	rm -rf __pycache__
