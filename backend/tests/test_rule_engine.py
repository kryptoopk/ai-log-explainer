from app.services.rule_engine import RuleEngine


def test_detects_failed_password_as_authentication() -> None:
    engine = RuleEngine()

    result = engine.analyze(
        "Failed password for root from 192.168.1.10"
    )

    assert result.category == "authentication"
    assert result.severity == "medium"
    assert result.reason == "Failed password detected in log."
    assert result.recommendation == (
        "Verify credentials and inspect the source IP."
    )


def test_returns_unknown_when_no_rule_matches() -> None:
    engine = RuleEngine()

    result = engine.analyze(
        "Application started successfully"
    )

    assert result.category == "unknown"
    assert result.severity == "low"
    assert result.reason == "No matching rule found."
    assert result.recommendation == "Manual investigation required."