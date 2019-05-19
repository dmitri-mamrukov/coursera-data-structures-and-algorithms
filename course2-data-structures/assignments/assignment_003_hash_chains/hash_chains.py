#!/usr/bin/python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.index = int(query[1])
        else:
            self.text = query[1]

class HashUtil:

    MULTIPLIER = 263
    PRIME = 1000000007

    @staticmethod
    def hash_function(s, bucket_count):
        result = 0
        for c in reversed(s):
            result = (result * HashUtil.MULTIPLIER + ord(c)) % HashUtil.PRIME

        return result % bucket_count

class QueryProcessor:

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.table = {}

    def process_query(self, query):
        if query.type == 'add':
            key = HashUtil.hash_function(query.text, self.bucket_count)
            if key not in self.table:
                self.table[key] = [ query.text ]
            else:
                if query.text not in self.table[key]:
                    self.table[key].insert(0, query.text)

            return
        elif query.type == 'del':
            key = HashUtil.hash_function(query.text, self.bucket_count)
            if key in self.table:
                if query.text in self.table[key]:
                    self.table[key].remove(query.text)

            return
        elif query.type == 'find':
            key = HashUtil.hash_function(query.text, self.bucket_count)
            if key in self.table:
                if query.text in self.table[key]:
                    return 'yes'

            return 'no'
        elif query.type == 'check':
            if query.index in self.table:
                return ' '.join(self.table[query.index])

            return ''

class QueryProcessorSlow:

    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elements = []

    def _hash_function(self, s):
        answer = 0
        for c in reversed(s):
            answer = (answer * self._multiplier + ord(c)) % self._prime

        return answer % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use the reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elements)
                if self._hash_function(cur) == query.index)
        else:
            try:
                index = self.elements.index(query.text)
            except ValueError:
                index = -1

            if query.type == 'find':
                self.write_search_result(index != -1)
            elif query.type == 'add':
                if index == -1:
                    self.elements.append(query.text)
            else:
                if index != -1:
                    self.elements.pop(index)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

def read_query():
    return Query(input().split())

def process_queries(processor):
    n = int(input())
    for i in range(n):
        result = processor.process_query(read_query())
        if result != None:
            print(result)

if __name__ == '__main__':
    bucket_count = int(input())
    processor = QueryProcessor(bucket_count)
    process_queries(processor)
