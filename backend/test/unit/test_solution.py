import sys
import os
# Adjust PYTHONPATH to include the project's root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import pytest
from unittest.mock import MagicMock
from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet

@pytest.fixture(autouse=True)
def mock_load_recipes(mocker):
    mocker.patch.object(RecipeController, 'load_recipes', return_value=[
        {'name': 'vegan_recipe_1', 'diets': ['vegan']},
        {'name': 'vegan_recipe_2', 'diets': ['vegan']},
        {'name': 'normal_recipe_1', 'diets': ['normal']},
        {'name': 'normal_recipe_2', 'diets': ['normal']},
        {'name': 'vegetarian_recipe_1', 'diets': ['vegetarian']},
        {'name': 'vegetarian_recipe_2', 'diets': ['vegetarian']}
    ])

@pytest.mark.unit
def test_vegan_take_best(mocker):
    controller = RecipeController(None)
    controller.recipes = [
        {'name': 'vegan_recipe_1', 'diets': ['vegan']},
        {'name': 'vegan_recipe_2', 'diets': ['vegan']}
    ]
    mocker.patch.object(controller, 'get_readiness_of_recipes', return_value={
        'vegan_recipe_1': 0.5,
        'vegan_recipe_2': 0.8
    })

    recipe = controller.get_recipe(Diet.VEGAN, True)
    assert recipe == 'vegan_recipe_2'

@pytest.mark.unit
def test_vegan_random(mocker):
    controller = RecipeController(None)
    controller.recipes = [
        {'name': 'vegan_recipe_1', 'diets': ['vegan']},
        {'name': 'vegan_recipe_2', 'diets': ['vegan']}
    ]
    mocker.patch.object(controller, 'get_readiness_of_recipes', return_value={
        'vegan_recipe_1': 0.5,
        'vegan_recipe_2': 0.8
    })

    recipe = controller.get_recipe(Diet.VEGAN, False)
    assert recipe in ['vegan_recipe_1', 'vegan_recipe_2']

@pytest.mark.unit
def test_normal_take_best(mocker):
    controller = RecipeController(None)
    controller.recipes = [
        {'name': 'normal_recipe_1', 'diets': ['normal']},
        {'name': 'normal_recipe_2', 'diets': ['normal']}
    ]
    mocker.patch.object(controller, 'get_readiness_of_recipes', return_value={
        'normal_recipe_1': 0.3,
        'normal_recipe_2': 0.9
    })

    recipe = controller.get_recipe(Diet.NORMAL, True)
    assert recipe == 'normal_recipe_2'

@pytest.mark.unit
def test_normal_random(mocker):
    controller = RecipeController(None)
    controller.recipes = [
        {'name': 'normal_recipe_1', 'diets': ['normal']},
        {'name': 'normal_recipe_2', 'diets': ['normal']}
    ]
    mocker.patch.object(controller, 'get_readiness_of_recipes', return_value={
        'normal_recipe_1': 0.3,
        'normal_recipe_2': 0.9
    })

    recipe = controller.get_recipe(Diet.NORMAL, False)
    assert recipe in ['normal_recipe_1', 'normal_recipe_2']

@pytest.mark.unit
def test_vegetarian_take_best(mocker):
    controller = RecipeController(None)
    controller.recipes = [
        {'name': 'vegetarian_recipe_1', 'diets': ['vegetarian']},
        {'name': 'vegetarian_recipe_2', 'diets': ['vegetarian']}
    ]
    mocker.patch.object(controller, 'get_readiness_of_recipes', return_value={
        'vegetarian_recipe_1': 0.4,
        'vegetarian_recipe_2': 0.7
    })

    recipe = controller.get_recipe(Diet.VEGETARIAN, True)
    assert recipe == 'vegetarian_recipe_2'

@pytest.mark.unit
def test_vegetarian_random(mocker):
    controller = RecipeController(None)
    controller.recipes = [
        {'name': 'vegetarian_recipe_1', 'diets': ['vegetarian']},
        {'name': 'vegetarian_recipe_2', 'diets': ['vegetarian']}]
    mocker.patch.object(controller, 'get_readiness_of_recipes', return_value={
        'vegetarian_recipe_1': 0.4,
        'vegetarian_recipe_2': 0.7
    })

    recipe = controller.get_recipe(Diet.VEGETARIAN, False)
    assert recipe in ['vegetarian_recipe_1', 'vegetarian_recipe_2']

@pytest.mark.unit
def test_no_recipes_take_best(mocker):
    controller = RecipeController(None)
    controller.recipes = []
    mocker.patch.object(controller, 'get_readiness_of_recipes', return_value={})

    recipe = controller.get_recipe(Diet.NORMAL, True)
    assert recipe is None

@pytest.mark.unit
def test_no_recipes_random(mocker):
    controller = RecipeController(None)
    controller.recipes = []
    mocker.patch.object(controller, 'get_readiness_of_recipes', return_value={})

    recipe = controller.get_recipe(Diet.NORMAL, False)
    assert recipe is None
