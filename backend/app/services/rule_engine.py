from app.models.rule_result import RuleResult


class RuleEngine:
    def analyze(self, log: str) -> RuleResult:
        normalized_log = log.lower()

        if "failed password" in normalized_log:
            return RuleResult(
                category="authentication",
                severity="medium",
                reason="Failed password detected in log.",
                recommendation="Verify credentials and inspect the source IP.",
            )

        if "permission denied" in normalized_log:
            return RuleResult(
                category="authorization",
                severity="medium",
                reason="The current user or process does not have sufficient permissions.",
                recommendation="Check file ownership, access rights, and the executing user.",
            )

        if "connection refused" in normalized_log:
            return RuleResult(
                category="network",
                severity="high",
                reason="The target host rejected the connection.",
                recommendation="Check whether the service is running and listening on the expected port.",
            )

        if "no space left on device" in normalized_log:
            return RuleResult(
                category="storage",
                severity="high",
                reason="The system has no available storage space.",
                recommendation="Free disk space and inspect large files or log directories.",
            )

        if "service not found" in normalized_log:
            return RuleResult(
                category="service",
                severity="medium",
                reason="The requested service could not be found.",
                recommendation="Verify the service name and confirm that it is installed.",
            )

        return RuleResult(
            category="unknown",
            severity="low",
            reason="No matching rule found.",
            recommendation="Manual investigation required.",
        )