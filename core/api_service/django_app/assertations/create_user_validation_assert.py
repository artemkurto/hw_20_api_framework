from assertpy import assert_that


def assert_user_created_validation(response, expected_text, property_name: str):
    assert_that(response, 'Quantity of error').is_length(1)

    key = list(response.keys())[0]
    assert_that(key, 'Error property').is_equal_to(property_name)
    values = response[key]

    assert_that(values, 'Quantity of error for property').is_length(1)
    assert_that(values[0], 'Error property').is_equal_to(expected_text)
