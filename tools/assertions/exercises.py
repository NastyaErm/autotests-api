from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_internal_error_response


def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на создание заданий соответствует данным из запроса.

    :param request: Запрос на создание заданий.
    :param response: Ответ API с данными заданий.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


def assert_exercise(
        expected: ExerciseSchema,
        actual: ExerciseSchema
):
    """
    Проверяет, что данные задания соответствуют ожидаемым значениям.

    :param expected: Ожидаемые данные задания.
    :param actual: Фактические данные задания из ответа API.
    :raises AssertionError: Если хотя бы одно поле задания не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(
        expected: CreateExerciseResponseSchema,
        actual: GetExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение задания соответствует ожидаемым значениям.

    :param expected: Ожидаемый ответ на создание задания.
    :param actual: Фактический ответ на получение задания.
    :return: Если данные задания не совпадают.
    """
    assert_exercise(
        expected.exercise,
        actual.exercise
    )

def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema
):
    """
    Проверяет, что ответ на обновление задания соответствует данным из запроса.

    :param request: Запрос на обновление задания.
    :param response: Ответ API с данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

def assert_exercise_not_found_response(
        actual: InternalErrorResponseSchema
):
    """
    Проверяет, что тело ответа на запрос получения задания содержит внутреннюю ошибку

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)