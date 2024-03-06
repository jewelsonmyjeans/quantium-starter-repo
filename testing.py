import dash
from dash.testing.application_runners import import_app
from dash import html, dcc  
import plotly.express as px
import pandas as pd
import pytest

app = import_app('app')  

@pytest.fixture
def dash_app():
    return app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    #ensure the header is present
    assert dash_duo.find_element('h1').text == 'Sales of Pink Morsels'

def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    #ensure the visualization is present
    assert dash_duo.find_element('#Pink Morsel Sales').is_displayed()

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    #ensure the region picker is present
    assert dash_duo.find_element('#region-select').is_displayed()

