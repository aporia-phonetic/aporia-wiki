# Engine bridge (find ↔ heterodyne)

find's own roadmap section marks this explicitly as unfinished:

> "Engine bridge polish — bidirectional sync with `the-heterodyne` is
> sketched but minimal. Production-grade telemetry feeding finance +
> customer-success is future work."

Intent: heterodyne production events (episodes shipped, costs incurred)
and audience/customer signals should flow into find's
[Decision Queue](decision-queue.md) — e.g. royalty tracking, customer-
success signals tied to specific episodes/worlds. As of this writing
that bridge is not built out; treat any current integration as
provisional. Check `find/connectors/` for the current state of this
adapter before relying on it.
