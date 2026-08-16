from app.services.log_analyzer import LogAnalyzer


def test_log_analyzer_returns_log_response() -> None:
    analyzer = LogAnalyzer()

    result = analyzer.analyze("Connection refused on port 5432")

    assert result.received_log == "Connection refused on port 5432"
    assert result.category == "unknown"
    assert result.severity == "low"
    assert result.reason == "No matching rule found."
    assert result.recommendation == "Manual investigation required."
    assert result.message == "Log analyzed successfully"


def test_log_analyzer_uses_rule_engine_result() -> None:
    analyzer = LogAnalyzer()

    result = analyzer.analyze(
        "Failed password for root from 192.168.1.10"
    )

    assert result.received_log == (
        "Failed password for root from 192.168.1.10"
    )
    assert result.category == "authentication"
    assert result.severity == "medium"
    assert result.reason == "Failed password detected in log."
    assert result.recommendation == (
        "Verify credentials and inspect the source IP."
    )
    assert result.message == "Log analyzed successfully"