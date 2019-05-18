class Util:

    #staticmethod
    def __check_args(data):
        assert(2 <= len(data))
        for i in data:
            assert(0 <= i)

    #staticmethod
    def max_pairwise_product(data):
        Util.__check_args(data)

        if data[0] < data[1]:
            first_largest_index = 1
            second_largest_index = 0
        else:
            first_largest_index = 0
            second_largest_index = 1

        for i in range(2, len(data)):
            if (data[i] > data[first_largest_index]):
                second_largest_index = first_largest_index
                first_largest_index = i
            elif (data[i] > data[second_largest_index]):
                second_largest_index = i

        return data[first_largest_index] * data[second_largest_index]
