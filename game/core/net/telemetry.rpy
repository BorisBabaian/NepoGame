# core/net/telemetry.rpy — episode results & progress telemetry
# (design: docs/TELEMETRY_AND_ADMIN_PANEL.md)
#
# Backend-agnostic ON PURPOSE. The game records results into a local
# offline queue right now; when Supabase exists, only api.rpy learns how
# to ship the queue. Story code never changes.
#
# Story code calls exactly one function:
#     $ record_episode_result("1.1", score=8, max_score=10, artifact={...})

init python:

    TELEMETRY_VERSION = 1

    def _new_event(kind, payload):
        import time
        return {
            "kind": kind,                       # "episode_result" | "progress"
            "client_version": config.version,
            "schema": TELEMETRY_VERSION,
            "client_ts": time.time(),
            "payload": payload,
        }

    def _attempt_number(episode):
        """How many times this episode was already recorded (append-only)."""
        n = 1
        for e in persistent.telemetry_queue or []:
            if e["kind"] == "episode_result" and e["payload"]["episode"] == episode:
                n += 1
        return n

    def record_episode_result(episode, score=None, max_score=None,
        passed=None, artifact=None, duration_sec=None):
        """Append one immutable episode attempt to the outbound queue.

        artifact: what the player actually produced (answers, canvas, choices).
        Storing it makes the score auditable by a human — see design doc §2.
        """
        payload = {
            "episode": episode,
            "attempt": _attempt_number(episode),
            "score": score,
            "max_score": max_score,
            "passed": passed,
            "artifact": artifact or {},
            "duration_sec": duration_sec,
        }

        queue = list(persistent.telemetry_queue or [])
        queue.append(_new_event("episode_result", payload))
        persistent.telemetry_queue = queue

        queue_sync()

    def record_progress():
        """Snapshot of where the player currently is (overwritten server-side)."""
        queue = list(persistent.telemetry_queue or [])
        queue.append(_new_event("progress", player.to_dict()))
        persistent.telemetry_queue = queue

        queue_sync()

    def telemetry_pending_count():
        return len(persistent.telemetry_queue or [])


# Offline buffer. Survives restarts; drained once the backend exists.
default persistent.telemetry_queue = []
