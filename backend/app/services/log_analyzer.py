from app.models.log_response import LogResponse
from app.parsers.ssh_parser import SSHParser
from app.services.log_source_detector import LogSourceDetector
from app.services.rule_engine import RuleEngine


class LogAnalyzer:
    def __init__(self) -> None:
        self.rule_engine = RuleEngine()
        self.source_detector = LogSourceDetector()
        self.ssh_parser = SSHParser()

    def analyze(self, log: str) -> LogResponse:
        source = self.source_detector.detect(log)

        if source == "ssh":
            parsed_log = self.ssh_parser.parse(log)
        else:
            parsed_log = None

        if parsed_log is not None:
            rule_input = parsed_log.message
        else:
            rule_input = log

        rule_result = self.rule_engine.analyze(rule_input)

        return LogResponse(
            received_log=log,
            source=source,
            category=rule_result.category,
            severity=rule_result.severity,
            reason=rule_result.reason,
            recommendation=rule_result.recommendation,
            message="Log analyzed successfully",
        )