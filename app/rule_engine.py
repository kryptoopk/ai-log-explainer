from model import AnalyzeResponse

RULES = [
    {
        "keywords": ["failed password", "authentication failure", "invalid password"],
        "response": AnalyzeResponse(
            category="authentication",
            severity="medium",
            summary="Failed SSH login attempt detected",
            recommendation=[
                "Verify credentials",
                "Check source IP",
                "Consider blocking repeated failed attempts"
            ]
        )
    },
    {
        "keywords": ["connection refused", "connection timed out"],
        "response": AnalyzeResponse(
            category="network",
            severity="high",
            summary="Network connectivity issue detected",
            recommendation=[
                "Check if the service is running",
                "Verify firewall rules",
                "Check network configuration"
            ]
        )
    },
    {
        "keywords": ["disk full", "no space left", "out of disk"],
        "response": AnalyzeResponse(
            category="storage",
            severity="critical",
            summary="Disk space exhausted",
            recommendation=[
                "Free up disk space immediately",
                "Check for large log files",
                "Consider adding more storage"
            ]
        )
    },
    {
        "keywords": ["out of memory", "oom killer", "cannot allocate memory"],
        "response": AnalyzeResponse(
            category="memory",
            severity="critical",
            summary="System is running out of memory",
            recommendation=[
                "Restart memory-heavy services",
                "Check for memory leaks",
                "Consider increasing RAM"
            ]
        )
    },
]

DEFAULT_RESPONSE = AnalyzeResponse(
    category="unknown",
    severity="low",
    summary="No matching rule found for this log",
    recommendation=[
        "Review the log manually",
        "Check system documentation"
    ]
)

def analyze(log: str) -> AnalyzeResponse:
    log_lower = log.lower()
    
    for rule in RULES:
        for keyword in rule["keywords"]:
            if keyword in log_lower:
                return rule["response"]
    
    return DEFAULT_RESPONSE