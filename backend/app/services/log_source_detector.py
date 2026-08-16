class LogSourceDetector:
    def detect(self, log: str) -> str:
        normalized_log = log.lower()

        if "sshd" in normalized_log or "failed password" in normalized_log:
            return "ssh"

        if "docker" in normalized_log or "container" in normalized_log:
            return "docker"

        if "nginx" in normalized_log:
            return "nginx"

        if "systemd" in normalized_log or "systemctl" in normalized_log:
            return "systemd"

        if "event id" in normalized_log:
            return "windows-event-log"

        return "unknown"