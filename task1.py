def get_number_stats(numbers: list) -> dict:
    result_dict = {}
    in_interval_count = 0
    positive_count = 0
    negative_count = 0
    zero_count = 0
    positive_sum = 0
    negative_sum = 0
    for i in range(0, len(numbers)):
        if 0 <= numbers[i] <= 10:
            in_interval_count += 1
        if numbers[i] < 0:
            negative_count += 1
        if numbers[i] > 0:
            positive_count += 1
        if numbers[i] == 0:
            zero_count += 1
        if numbers[i] > 0:
            positive_sum += numbers[i]
        if numbers[i] < 0:
            negative_sum += numbers[i]
    result_dict["max"] = result_dict.get("max", max(numbers))
    result_dict["min"] = result_dict.get("min", min(numbers))
    result_dict["average"] = result_dict.get("average", sum(numbers) / len(numbers))
    result_dict["in_interval_count"] = result_dict.get("in_interval_count", in_interval_count)
    result_dict["positive_count"] = result_dict.get("positive_count", positive_count)
    result_dict["negative_count"] = result_dict.get("negative_count", negative_count)
    result_dict["zero_count"] = result_dict.get("zero_count", zero_count)
    result_dict["positive_sum"] = result_dict.get("positive_sum", positive_sum)
    result_dict["negative_sum"] = result_dict.get("negative_sum", negative_sum)
    return result_dict


my_list = [0, 0, -1, -6, 2, 3, 10, 9]
print(get_number_stats(my_list))
