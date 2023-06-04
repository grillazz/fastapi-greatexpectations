import pytest
from fastapi import status
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    "response_data, status_code",
    (
            (
                    [
                        "expect_column_distinct_values_to_be_in_set",
                        "expect_column_distinct_values_to_contain_set",
                        "expect_column_distinct_values_to_equal_set",
                        "expect_column_kl_divergence_to_be_less_than",
                        "expect_column_max_to_be_between",
                        "expect_column_mean_to_be_between",
                        "expect_column_median_to_be_between",
                        "expect_column_min_to_be_between",
                        "expect_column_most_common_value_to_be_in_set",
                        "expect_column_pair_values_a_to_be_greater_than_b",
                        "expect_column_pair_values_to_be_equal",
                        "expect_column_pair_values_to_be_in_set",
                        "expect_column_proportion_of_unique_values_to_be_between",
                        "expect_column_quantile_values_to_be_between",
                        "expect_column_stdev_to_be_between",
                        "expect_column_sum_to_be_between",
                        "expect_column_to_exist",
                        "expect_column_unique_value_count_to_be_between",
                        "expect_column_value_lengths_to_be_between",
                        "expect_column_value_lengths_to_equal",
                        "expect_column_value_z_scores_to_be_less_than",
                        "expect_column_values_to_be_between",
                        "expect_column_values_to_be_dateutil_parseable",
                        "expect_column_values_to_be_decreasing",
                        "expect_column_values_to_be_in_set",
                        "expect_column_values_to_be_in_type_list",
                        "expect_column_values_to_be_increasing",
                        "expect_column_values_to_be_json_parseable",
                        "expect_column_values_to_be_null",
                        "expect_column_values_to_be_of_type",
                        "expect_column_values_to_be_unique",
                        "expect_column_values_to_match_json_schema",
                        "expect_column_values_to_match_like_pattern",
                        "expect_column_values_to_match_like_pattern_list",
                        "expect_column_values_to_match_regex",
                        "expect_column_values_to_match_regex_list",
                        "expect_column_values_to_match_strftime_format",
                        "expect_column_values_to_not_be_in_set",
                        "expect_column_values_to_not_be_null",
                        "expect_column_values_to_not_match_like_pattern",
                        "expect_column_values_to_not_match_like_pattern_list",
                        "expect_column_values_to_not_match_regex",
                        "expect_column_values_to_not_match_regex_list",
                        "expect_compound_columns_to_be_unique",
                        "expect_multicolumn_sum_to_equal",
                        "expect_select_column_values_to_be_unique_within_record",
                        "expect_table_column_count_to_be_between",
                        "expect_table_column_count_to_equal",
                        "expect_table_columns_to_match_ordered_list",
                        "expect_table_columns_to_match_set",
                        "expect_table_row_count_to_be_between",
                        "expect_table_row_count_to_equal",
                        "expect_table_row_count_to_equal_other_table"
                    ],
                    status.HTTP_200_OK,
            ),
    ),
)
def test_get_expectation_types(client: TestClient, response_data: dict, status_code: int):
    response = client.get("/v1/expectation/list_available_expectation_types/chapter")
    assert response.status_code == status_code
    assert response.json() == response_data
