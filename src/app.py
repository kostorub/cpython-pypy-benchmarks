from statistics import correlation

from generate_complex_data import OrdinaryClass, gen_ordinary_models
from utils import average_time_map, timeitit

ITERATIONS = 40
MODELS_LEN = 5000


def check_ordinary_model_correlation() -> None:
    ordinary_models_list = [gen_ordinary_models(MODELS_LEN) for _ in range(ITERATIONS)]
    [check_correlation_iterative(models) for models in ordinary_models_list]


@timeitit
def check_correlation_iterative(models: list[OrdinaryClass]) -> None:
    floats_list_1 = []
    floats_list_2 = []
    floats_list_1.append(models[0].one_data)
    floats_list_2.append(models[0].another_data)
    for model in models[1:]:
        floats_list_1.append(model.one_data)
        floats_list_2.append(model.another_data)
        correlation(floats_list_1, floats_list_2)


def print_stats() -> None:
    for key, value in average_time_map.items():
        print(f"{key}: {sum(value)/len(value)}")
    average_time_map.clear()


if __name__ == "__main__":
    check_ordinary_model_correlation()
    print_stats()
