import pytest
from markupsafe import Markup


@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = 'Relatório de Testes Unitários'


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    ambiente = Markup('<p><strong>Ambiente:</strong> Desenvolvimento</p>')
    executor = Markup('<p><strong>Executor:</strong> Alexandre P. Santos</p>')
    prefix.extend([ambiente])
    prefix.extend([executor])
