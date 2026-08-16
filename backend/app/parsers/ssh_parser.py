from app.models.parsed_log import ParsedLog


class SSHParser:
    def parse(self, log: str) -> ParsedLog:
        message = log

        if ":" in log:
            message = log.split(":", 1)[1].strip()

        return ParsedLog(
            raw=log,
            source="ssh",
            message=message,
        )