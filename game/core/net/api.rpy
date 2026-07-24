# core/net/api.rpy — network layer STUB (TECHNICAL_PLAN.md §7)
#
# The real backend arrives later (Stage 5), but the interface is laid down
# NOW so story/mechanics code already calls queue_sync() in the right places.
# When the server exists, only this folder changes — nothing else.

default persistent.pending_sync = False

# Account (future mandatory registration — TECHNICAL_PLAN.md §7).
# The token is issued by the server after sign-in; never store passwords.
default persistent.account_id = None
default persistent.auth_token = None

init python:

    def queue_sync():
        """Mark that there is unsynced progress. Offline-first: never blocks."""
        persistent.pending_sync = True

    def try_flush_sync():
        """Drain the telemetry queue to the server. No-op until backend exists.

        This is the ONLY place that will learn HTTP. Planned shape once the
        Supabase project exists (docs/TELEMETRY_AND_ADMIN_PANEL.md §6):

            for event in list(persistent.telemetry_queue):
                renpy.fetch(SUPABASE_URL + "/rest/v1/episode_results",
                            method="POST", json=row_from(event),
                            headers={"Authorization": "Bearer " + persistent.auth_token,
                                     "apikey": SUPABASE_ANON_KEY},
                            timeout=5)
                # drop from queue only on success — offline-first

        NOTE: only the public anon key ever ships in the build. The key that
        can read every student's rows never leaves the admin side.
        """
        if not persistent.pending_sync:
            return
        if persistent.auth_token is None:
            return  # not signed in yet — keep buffering, never block play
        return
