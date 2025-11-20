import requests
from behave import given, when, then
from utils.api_helpers import get_candlestick_data
import os
import json

@given('the instrument name is "{instrument_name}"')
def step_impl(context, instrument_name):
    context.instrument_name = instrument_name

@given('the timeframe is "{timeframe}"')
def step_impl(context, timeframe):
    context.timeframe = timeframe

@when('I call the public/get-candlestick endpoint')
def step_impl(context):
    context.response = get_candlestick_data(
        instrument_name=context.instrument_name,
        timeframe=context.timeframe,
        context=context
    )
    context.api_response = context.response

@then('the response code should be 0')
def step_impl(context):
    assert context.response["code"] == 0, f"Expected code 0, got {context.response['code']}"
    print("yes")

@then('the response should contain candlestick data')
def step_impl(context):
    data = context.response.get("result", {}).get("data", [])
    assert isinstance(data, list) and len(data) > 0, "No candlestick data found"

@then('the response code should not be 0')
def step_impl(context):
    assert context.response["code"] != 0, "Expected non-zero error code"
