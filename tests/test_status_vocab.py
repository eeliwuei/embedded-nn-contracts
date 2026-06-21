from embedded_nn_contracts.status import VALID_STATUSES


def test_required_statuses():
    for status in ["retained", "prebuilt_oracle_only", "dropped_noncompetitive", "infeasible_on_board"]:
        assert status in VALID_STATUSES
