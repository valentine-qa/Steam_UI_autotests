import allure
from allure_commons.types import Severity


@allure.title('Fail example')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'valentine-qa')
def test_fail():
    assert False

@allure.title('Pass example')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'valentine-qa')
def test_pass():
    pass