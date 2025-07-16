
class IDS:
    def __init__(self, game_state, file_system):
        self.game_state = game_state
        self.file_system = file_system
        self.threshold_critical = 70
        self.threshold_high = 50
        self.threshold_medium = 30

    def increment_anomaly_score(self, amount, reason=""):
        self.game_state.anomaly_score += amount
        if self.game_state.anomaly_score > 100:
            self.game_state.anomaly_score = 100
        print(f"[IDS] Anomaly score increased by {amount} due to: {reason}. Current score: {self.game_state.anomaly_score}")
        self._check_and_trigger_defensive_measures()

    def _check_and_trigger_defensive_measures(self):
        score = self.game_state.anomaly_score
        if score >= self.threshold_critical:
            self._trigger_critical_response()
        elif score >= self.threshold_high:
            self._trigger_high_response()
        elif score >= self.threshold_medium:
            self._trigger_medium_response()

    def _trigger_medium_response(self):
        if not hasattr(self, '_medium_response_triggered'):
            print("[IDS] Warning: System activity is being monitored closely. Reduce suspicious actions.")
            self._medium_response_triggered = True

    def _trigger_high_response(self):
        if not hasattr(self, '_high_response_triggered'):
            print("[IDS] ALERT: Defensive measures initiated! Some files may be temporarily locked.")
            # Example: Lock a random file
            # This is a placeholder, actual implementation would involve more complex FS interaction
            # For now, just a message.
            self._high_response_triggered = True

    def _trigger_critical_response(self):
        if not hasattr(self, '_critical_response_triggered'):
            print("[IDS] CRITICAL: System lockdown! Player access may be revoked or critical files wiped.")
            # Example: Wipe player's code or lock out
            # For now, just a message.
            self._critical_response_triggered = True

    def reset_anomaly_score(self):
        self.game_state.anomaly_score = 0
        print("[IDS] Anomaly score reset.")
